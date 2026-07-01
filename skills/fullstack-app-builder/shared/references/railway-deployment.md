# Railway Deployment Reference

Patterns and solutions for deploying React + Vite apps on Railway.

---

## How Railway works

Railway detects your framework from `package.json` and builds automatically:
1. You push to `main` on GitHub
2. Railway pulls the code, runs `npm install` + `npm run build`
3. Railway serves the built files via Caddy webserver
4. Custom domain SSL is provisioned automatically (takes 10-60 min after DNS setup)

## Required files for successful deployment

### package.json (minimal)
```json
{
  "name": "app-name",
  "private": true,
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "lint": "eslint .",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "react-router-dom": "^6.28.0",
    "@supabase/supabase-js": "^2.46.0"
  },
  "devDependencies": {
    "@types/react": "^18.3.12",
    "@types/react-dom": "^18.3.1",
    "@vitejs/plugin-react": "^4.3.4",
    "typescript": "^5.6.3",
    "vite": "^5.4.11"
  }
}
```

### vite.config.ts
```typescript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0',
    port: 5173
  }
})
```

### tsconfig.json
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "isolatedModules": true,
    "moduleDetection": "force",
    "noEmit": true,
    "jsx": "react-jsx",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "include": ["src"]
}
```

### index.html (in repo root)
```html
<!DOCTYPE html>
<html lang="de">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>App Name</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
```

### src/main.tsx (minimal entry)
```tsx
import React from 'react'
import ReactDOM from 'react-dom/client'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', height: '100vh' }}>
      <h1>App Name — wird gebaut...</h1>
    </div>
  </React.StrictMode>
)
```

---

## Custom Domain Setup

### Step 1: Add domain in Railway
Railway Dashboard → Service → Settings → Custom Domain → add `app.[domain.tld]`

Railway provides a target like `2umzzpqa.up.railway.app`

### Step 2: DNS records at domain registrar

| Type | Host | Value | TTL |
|------|------|-------|-----|
| CNAME | `app` | `[railway-target].up.railway.app` | 3600 |

Some registrars also need a verification TXT record:

| Type | Host | Value |
|------|------|-------|
| TXT | `_railway-verify.app` | `[verification-code]` |

### Step 3: Wait for SSL
Railway auto-provisions SSL certificates via Let's Encrypt. Takes 10-60 minutes after DNS propagation. During this time, browsers will show a security warning — this is expected and resolves itself.

---

## Environment Variables

Set these in Railway Dashboard → Service → Variables:

| Variable | Value | Required |
|----------|-------|----------|
| `VITE_SUPABASE_URL` | `https://[ref].supabase.co` | Yes |
| `VITE_SUPABASE_ANON_KEY` | `eyJ...` | Yes |
| `PORT` | (auto-set by Railway) | No |

Railway automatically sets `PORT`. Vite builds a static site that Caddy serves on port 8080.

---

## Common deployment issues

### "tsc: command not found" or tsc prints help text
**Cause:** TypeScript not installed or no tsconfig.json
**Fix:** Ensure `typescript` is in devDependencies and tsconfig.json exists in repo root

### Build succeeds but page shows blank
**Cause:** Routes not configured for SPA
**Fix:** Railway's Caddy serves index.html for all routes by default with Vite — should work automatically. If not, check that React Router is set up correctly.

### First deploy fails, second works
**Cause:** Railway sometimes picks up the initial empty commit
**Fix:** Push a second commit, Railway redeploys automatically

### Environment variables not available
**Cause:** Variables added after deployment
**Fix:** Redeploy after adding variables (Railway usually does this automatically)

---

## Railway + Express Server (for server-side features)

When the app needs a backend server (web scraping, cron, webhooks), add a `server/` directory with its own `package.json`. Deploy as a separate Railway service:

1. Create a second Railway service in the same project
2. Set root directory to `/server`
3. Add server-specific env vars (DATABASE_URL, STRIPE_SECRET_KEY, etc.)
4. Custom domain not needed — use Railway's internal networking or the generated URL

### Express health check (required)
```typescript
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'ok', timestamp: new Date().toISOString() })
})
```
