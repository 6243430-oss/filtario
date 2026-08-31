# Outbound Email Sequences — English Market
# Target: HR Directors, Talent Acquisition Managers, COOs
# Companies: 100-2000 employees, retail/logistics/hospitality/manufacturing

---

## EMAIL 1 — Initial outreach (Day 1)

**Subject:** {{company_name}}'s hiring pace

Hi {{first_name}},

Noticed {{company_name}} has {{open_roles_count}} open roles right now — including {{specific_role}}. At that volume, your team is probably spending more time screening and scheduling than actually hiring.

We built Filtario for exactly this: AI screens every resume, conducts first-round interviews automatically, and hands your team a ranked shortlist. Companies like yours cut hiring time from 30 days to 7.

Worth a 20-minute call to see if it fits your process?

{{sender_name}}

---

## EMAIL 2 — Follow-up (Day 4)

**Subject:** Re: {{company_name}}'s hiring pace

Hi {{first_name}},

Just following up on my note from earlier this week.

One thing that stands out about {{company_name}}: you're hiring in {{industry}} where turnover tends to be high and speed matters. Every week a role stays open costs you roughly $500-1,500 in lost productivity.

Filtario typically pays for itself within the first hire. Happy to show you a quick demo — no commitment.

{{sender_name}}

---

## EMAIL 3 — Final follow-up (Day 10)

**Subject:** Last note — Filtario for {{company_name}}

Hi {{first_name}},

Last follow-up from me.

If speeding up your hiring process isn't a priority right now, no worries at all. If it is — I'd love to show you what Filtario does in 20 minutes.

Either way, you can explore it yourself at filtario.com — there's a free 14-day trial, no card required.

{{sender_name}}

---

## CLAUDE API PROMPT — Personalization

```
SYSTEM:
You are a B2B SaaS sales expert writing cold emails for Filtario — an AI hiring automation platform.
Write emails that sound human, direct, and relevant. Max 5 sentences.
Never use: synergy, innovative, excited to share, hope this finds you well.

USER:
Company: {{company_name}}
Website summary: {{website_summary}}
Recipient: {{first_name}}, {{job_title}}
Current open jobs at this company: {{open_jobs}}
Industry: {{industry}}
Company size: {{company_size}} employees
Sender: {{sender_name}}

Take EMAIL 1 template above and rewrite the first sentence to reference something specific
about this company (their industry, a recent job posting, or their growth stage).
Keep everything else the same. Return only the final email, plain text.
```
