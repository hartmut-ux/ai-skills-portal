# Supabase Patterns Reference

Common patterns for Auth, RLS, Edge Functions, and Storage in production apps.

---

## Auth: Magic Link

### Frontend: Sign in
```typescript
const { error } = await supabase.auth.signInWithOtp({
  email: userEmail,
  options: {
    emailRedirectTo: `${window.location.origin}/auth/callback`
  }
})
```

### Frontend: Auth callback page
```typescript
// src/pages/AuthCallback.tsx
import { useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { supabase } from '@/lib/supabase'

export default function AuthCallback() {
  const navigate = useNavigate()

  useEffect(() => {
    supabase.auth.onAuthStateChange(async (event, session) => {
      if (event === 'SIGNED_IN' && session) {
        // Check if user profile exists
        const { data: profile } = await supabase
          .from('user_profiles')
          .select('rolle')
          .eq('user_id', session.user.id)
          .single()

        if (!profile) {
          // New user — create profile (role from URL param or default)
          const params = new URLSearchParams(window.location.search)
          const rolle = params.get('role') || 'user'
          await supabase.from('user_profiles').insert({
            user_id: session.user.id,
            rolle
          })
          navigate(`/dashboard/${rolle}`)
        } else {
          navigate(`/dashboard/${profile.rolle}`)
        }
      }
    })
  }, [navigate])

  return <div>Anmeldung wird verarbeitet...</div>
}
```

### Auth context hook
```typescript
// src/hooks/useAuth.ts
import { createContext, useContext, useEffect, useState } from 'react'
import { supabase } from '@/lib/supabase'
import type { User, Session } from '@supabase/supabase-js'

interface AuthContext {
  user: User | null
  profile: { rolle: string; [key: string]: any } | null
  loading: boolean
  signOut: () => Promise<void>
}

const AuthContext = createContext<AuthContext>({
  user: null, profile: null, loading: true, signOut: async () => {}
})

export function useAuth() { return useContext(AuthContext) }
```

---

## RLS Patterns

### User sees only own data
```sql
CREATE POLICY "user_own_data" ON table_name
  FOR ALL USING (auth.uid() = user_id);
```

### Admin sees everything
```sql
CREATE POLICY "admin_full_access" ON table_name
  FOR ALL USING (
    EXISTS (
      SELECT 1 FROM public.user_profiles
      WHERE user_id = auth.uid() AND rolle = 'admin'
    )
  );
```

### Role-based access (e.g., employer sees candidate profiles)
```sql
CREATE POLICY "employers_see_active_profiles" ON candidate_profiles
  FOR SELECT USING (
    status = 'aktiv'
    AND EXISTS (
      SELECT 1 FROM public.user_profiles
      WHERE user_id = auth.uid() AND rolle = 'arbeitgeber'
    )
  );
```

### Blacklist filter (hide data from blocked users)
```sql
CREATE POLICY "respect_blacklist" ON candidate_profiles
  FOR SELECT USING (
    NOT EXISTS (
      SELECT 1 FROM public.blacklist
      WHERE kandidat_id = candidate_profiles.kandidat_id
      AND arbeitgeber_id = (
        SELECT id FROM public.employers WHERE user_id = auth.uid()
      )
    )
  );
```

### Important RLS rules
- Always enable RLS: `ALTER TABLE table_name ENABLE ROW LEVEL SECURITY;`
- Always create at least one policy (otherwise no one can access the table)
- Test policies in Supabase SQL Editor before relying on them
- Service role key bypasses RLS — never use in frontend

---

## Edge Functions

### Basic structure
```typescript
// supabase/functions/function-name/index.ts
import { serve } from "https://deno.land/std/http/server.ts"
import { createClient } from "https://esm.sh/@supabase/supabase-js@2"

const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
}

serve(async (req) => {
  // Handle CORS preflight
  if (req.method === 'OPTIONS') {
    return new Response('ok', { headers: corsHeaders })
  }

  try {
    const { param1, param2 } = await req.json()

    // Create Supabase client with service role for server-side operations
    const supabase = createClient(
      Deno.env.get('SUPABASE_URL')!,
      Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!
    )

    // Your logic here...

    return new Response(
      JSON.stringify({ success: true, data: result }),
      { headers: { ...corsHeaders, 'Content-Type': 'application/json' } }
    )
  } catch (error) {
    return new Response(
      JSON.stringify({ error: error.message }),
      { status: 400, headers: { ...corsHeaders, 'Content-Type': 'application/json' } }
    )
  }
})
```

### Claude API call from Edge Function
```typescript
const response = await fetch('https://api.anthropic.com/v1/messages', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'x-api-key': Deno.env.get('ANTHROPIC_API_KEY')!,
    'anthropic-version': '2023-06-01'
  },
  body: JSON.stringify({
    model: 'claude-sonnet-4-20250514',
    max_tokens: 2000,
    system: 'Your system prompt here',
    messages: [{ role: 'user', content: userMessage }]
  })
})

const result = await response.json()
const aiResponse = result.content[0].text
```

### AI usage logging (EU AI Act compliance)
```typescript
await supabase.from('ai_usage_log').insert({
  user_id: userId,
  endpoint: 'chat-kandidat',
  model: 'claude-sonnet-4-20250514',
  input_tokens: result.usage.input_tokens,
  output_tokens: result.usage.output_tokens,
  kosten: calculateCost(result.usage),
})
```

### Rate limiting
```typescript
const { count } = await supabase
  .from('ai_usage_log')
  .select('*', { count: 'exact', head: true })
  .eq('user_id', userId)
  .gte('created_at', new Date(Date.now() - 24*60*60*1000).toISOString())

const { data: limits } = await supabase
  .from('ai_usage_limits')
  .select('max_calls_pro_tag')
  .eq('rolle', userRole)
  .single()

if (count >= limits.max_calls_pro_tag) {
  return new Response(
    JSON.stringify({ error: 'Tägliches Limit erreicht' }),
    { status: 429, headers: corsHeaders }
  )
}
```

### Calling Edge Functions from frontend
```typescript
const { data, error } = await supabase.functions.invoke('function-name', {
  body: { param1: 'value1', param2: 'value2' }
})
```

---

## Storage

### Upload file
```typescript
const { data, error } = await supabase.storage
  .from('documents')
  .upload(`${userId}/${file.name}`, file, {
    cacheControl: '3600',
    upsert: false
  })
```

### Get public URL
```typescript
const { data } = supabase.storage
  .from('documents')
  .getPublicUrl('path/to/file.pdf')
```

### Storage bucket creation (in migration)
```sql
INSERT INTO storage.buckets (id, name, public)
VALUES ('documents', 'documents', false);

CREATE POLICY "Users upload own docs" ON storage.objects
  FOR INSERT WITH CHECK (
    bucket_id = 'documents'
    AND auth.uid()::text = (storage.foldername(name))[1]
  );

CREATE POLICY "Users read own docs" ON storage.objects
  FOR SELECT USING (
    bucket_id = 'documents'
    AND auth.uid()::text = (storage.foldername(name))[1]
  );
```

---

## Database migration patterns

### updated_at trigger (include once, reuse for all tables)
```sql
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = now();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Apply to each table:
CREATE TRIGGER set_updated_at
  BEFORE UPDATE ON table_name
  FOR EACH ROW EXECUTE FUNCTION update_updated_at();
```

### Safe migration order
Tables must be created in dependency order. If Table B references Table A, create A first. This is especially important for RLS policies that query other tables — the referenced table must exist before the policy is created.

Common dependency chain:
1. user_profiles (references auth.users)
2. Domain tables without cross-references
3. Tables with foreign keys to domain tables
4. Tables with RLS policies that query other tables
