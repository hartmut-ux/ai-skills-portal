# Stripe Integration Reference

Patterns for payment integration in production apps deployed on Railway.

**Critical rule:** Stripe Secret Key and Webhook Secret belong ONLY on the Railway server. Never in frontend, never in Edge Functions (unless you have no Railway server — in that case, Edge Functions with service role are acceptable).

---

## Architecture

```
User clicks "Pay" → Frontend creates checkout session via API
                  → Railway server calls Stripe API
                  → Stripe redirects user to hosted checkout page
                  → User pays
                  → Stripe sends webhook to Railway server
                  → Server updates DB (payment status)
                  → Frontend polls or listens for status change
```

---

## Setup

### 1. Install Stripe on Railway server
```bash
cd server
npm install stripe
```

### 2. Environment variables (Railway)
```
STRIPE_SECRET_KEY=sk_live_...       # or sk_test_... for testing
STRIPE_WEBHOOK_SECRET=whsec_...     # from Stripe webhook config
SUPABASE_URL=https://[ref].supabase.co
SUPABASE_SERVICE_ROLE_KEY=eyJ...
```

### 3. Stripe Dashboard setup
- Create webhook endpoint: `https://[railway-url]/api/webhooks/stripe`
- Listen for events: `checkout.session.completed`, `payment_intent.succeeded`, `payment_intent.failed`

---

## Stripe Checkout (one-time payment)

### Create checkout session (server)
```typescript
// server/src/webhooks/stripe.ts
import Stripe from 'stripe'
import { Router } from 'express'

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!)
const router = Router()

router.post('/create-checkout', async (req, res) => {
  const { amount, currency, description, metadata } = req.body

  const session = await stripe.checkout.sessions.create({
    payment_method_types: ['card'],
    line_items: [{
      price_data: {
        currency: currency || 'chf',
        product_data: { name: description },
        unit_amount: Math.round(amount * 100), // Stripe uses cents
      },
      quantity: 1,
    }],
    mode: 'payment',
    success_url: `${process.env.FRONTEND_URL}/payment/success?session_id={CHECKOUT_SESSION_ID}`,
    cancel_url: `${process.env.FRONTEND_URL}/payment/cancel`,
    metadata, // e.g., { placement_id: '...', arbeitgeber_id: '...' }
  })

  res.json({ url: session.url })
})

export default router
```

### Webhook handler (server)
```typescript
router.post('/webhooks/stripe',
  express.raw({ type: 'application/json' }),
  async (req, res) => {
    const sig = req.headers['stripe-signature']!
    let event: Stripe.Event

    try {
      event = stripe.webhooks.constructEvent(
        req.body,
        sig,
        process.env.STRIPE_WEBHOOK_SECRET!
      )
    } catch (err) {
      return res.status(400).send(`Webhook Error: ${err.message}`)
    }

    switch (event.type) {
      case 'checkout.session.completed': {
        const session = event.data.object as Stripe.Checkout.Session
        // Update payment status in Supabase
        await supabase
          .from('placements')
          .update({ payment_status: 'bezahlt', stripe_session_id: session.id })
          .eq('id', session.metadata?.placement_id)
        break
      }
      case 'payment_intent.failed': {
        // Handle failed payment
        break
      }
    }

    res.json({ received: true })
  }
)
```

### Frontend: redirect to checkout
```typescript
const handlePayment = async (placementId: string, amount: number) => {
  const response = await fetch(`${API_URL}/api/create-checkout`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      amount,
      currency: 'chf',
      description: 'Vermittlungsgebühr SkillBridge',
      metadata: { placement_id: placementId }
    })
  })
  const { url } = await response.json()
  window.location.href = url  // Redirect to Stripe Checkout
}
```

---

## Stripe Connect (payouts to users)

For apps where users receive money (e.g., sign-on bonus for candidates):

### Onboarding a connected account
```typescript
const account = await stripe.accounts.create({
  type: 'express',
  country: 'CH', // or 'LI'
  capabilities: {
    transfers: { requested: true },
  },
})

const accountLink = await stripe.accountLinks.create({
  account: account.id,
  refresh_url: `${FRONTEND_URL}/stripe/refresh`,
  return_url: `${FRONTEND_URL}/stripe/success`,
  type: 'account_onboarding',
})

// Redirect user to accountLink.url
```

### Creating a payout
```typescript
const transfer = await stripe.transfers.create({
  amount: bonusAmount * 100, // in cents
  currency: 'chf',
  destination: connectedAccountId,
  description: 'Sign-on Bonus — SkillBridge',
  metadata: { placement_id: placementId }
})
```

### Refund (e.g., failed probation period)
```typescript
const refund = await stripe.refunds.create({
  payment_intent: originalPaymentIntentId,
  amount: Math.round(originalAmount * 0.80 * 100), // 80% refund
  reason: 'requested_by_customer',
})
```

---

## Testing

Use Stripe test mode (`sk_test_...`) during development.

### Test card numbers
- Success: `4242 4242 4242 4242`
- Declined: `4000 0000 0000 0002`
- 3D Secure: `4000 0025 0000 3155`

### Webhook testing
```bash
# Install Stripe CLI
stripe listen --forward-to localhost:3001/api/webhooks/stripe
```

---

## v1 vs. v2 approach

**v1 (simpler):**
- Stripe Checkout for one-time payments (hosted page)
- Manual bank transfer for payouts (no Connect)
- Track payment status in DB

**v2 (full automation):**
- Stripe Connect for payouts
- Automatic refund calculation
- Recurring billing if needed
- Payment dashboard with analytics

Build for v1, but structure the code so Connect can be added later without rewriting.
