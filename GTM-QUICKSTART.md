# CitraChem GTM Toolkit — Quickstart

## What this is
A set of Claude Code subagents for CitraChem's go-to-market, tuned for the current motion: **technical/relationship sales to pharma, nutraceutical, and research buyers, quote-based pricing (no self-serve checkout)**, buyer persona is the R&D/chemistry lead or procurement/sourcing lead — not a self-serve retail buyer.

This is a port of the same agent architecture built for Shredly.io (an MCP-hosting SaaS), adapted for CitraChem's actual business: a life-sciences ingredient/API manufacturer selling phytocannabinoids, terpenes, and custom synthesis to regulated, technical buyers instead of self-serve SaaS to developers. Same shape (positioning doc → specialist subagents → local CRM → playbooks), different motion throughout — see `CLAUDE.md` for what changed and why.

`CLAUDE.md` is the shared source of truth every agent reads automatically — positioning, ICP, pricing model, differentiators. Change it there, not per-agent, when positioning changes.

## Fastest way to use it: slash commands
| Command | Does |
|---|---|
| `/outreach <company or signal>` | Draft first-touch outbound (outbound-sdr) |
| `/rfq <pasted inbound message>` | Qualify + reply to an inbound sample/quote request (inbound-rfq) |
| `/onboard <customer + situation>` | Onboarding, expansion, or save message (customer-success) |
| `/content <topic or "compare us to X">` | Blog/comparison/SEO content (content-seo) |
| `/community <thread URL or announcement topic>` | Scientific/industry community reply or post (scientific-community) |
| `/battlecard <competitor or route>` | Build/refresh a competitive battlecard (competitive-intel) |
| `/partner <company or category>` | Research/profile a confirmed or prospective partner (partner-intel) |
| `/research <company, indication, or institution>` | Dig into a specific pharma/biotech opportunity before anyone drafts outreach (pharma-research) |
| `/pipeline [filter]` | Summarize the current pipeline |
| `/dashboard` | Regenerate (and, once published, republish) the visual pipeline dashboard |

You can also just ask naturally ("draft a cold email to...") — Claude delegates to the matching agent automatically.

## Where things live
- `CLAUDE.md` — positioning, ICP, pricing model, differentiators (edit this first when the business changes)
- `playbooks/RFQ-PLAYBOOK.md` — default technical-sales sequences, tone, and objection handling
- `playbooks/agent-discoverable-content.md` — checklist for content that AI agents can parse/cite accurately
- `content/llms.txt` — canonical machine-readable summary of CitraChem, meant to be published at citrachem.com/llms.txt
- `pipeline/contacts.csv` — the CRM's actual data (one row per company); `pipeline/crm.py` is the tool that reads/writes it; `pipeline/PIPELINE.md` is an auto-generated human-readable snapshot of the same data — edit the CSV via `crm.py`, not the snapshot
- `research/OPPORTUNITY-MAP.md` — the pharma-research agent's seed reference, distilled from CitraChem's Series A deck: disease-target matrix, named big-pharma targets with patent-cliff data, academic institution pool, and existing client/MOU relationships that must never be treated as cold outbound prospects; `research/briefs/` holds its per-target opportunity briefs
- `content/`, `outreach/`, `leads/`, `customer-comms/`, `community/`, `battlecards/`, `partners/` — each agent's isolated output folder
- `.claude/agents/` — the subagent definitions themselves
- `.claude/commands/` — the slash commands above

## The local CRM (`pipeline/crm.py`)
A small, dependency-free Python script — no network access, no email sending, just structured record-keeping so outbound/inbound/customer-success stay in sync instead of drifting across separate Markdown drafts. Stages are tuned for a sample/quote-based motion instead of SaaS demo/trial: `Prospecting → Contacted → Replied → Sample Sent / Quote Sent → Customer` (or `Churned` / `Closed-lost`).

```
python3 pipeline/crm.py find "acme"      # look up a company (also checks for dupes before adding)
python3 pipeline/crm.py add --company "Acme Biotech" --contact "Jane Doe" --email jane@acmebiotech.com \
  --role "Director of R&D" --stage Prospecting --source outbound --owner outbound-sdr \
  --draft outreach/2026-09-16-acme-biotech.md --touch      # upsert; --touch advances the cadence automatically
python3 pipeline/crm.py due               # who's overdue for a follow-up, oldest first
python3 pipeline/crm.py stats             # counts by stage, anything missing a next action
python3 pipeline/crm.py snapshot          # regenerate pipeline/PIPELINE.md from the CSV
```

`outbound-sdr`, `inbound-rfq`, and `customer-success` all call this automatically as part of drafting — you generally don't need to run it by hand, but `/pipeline` and the commands above are there when you want to check status directly or fix a record.

## Viewing it: the dashboard
There's a visual frontend — a published page you can open from any device: **https://claude.ai/artifact/9fWJD7P5ie35Gn6iRQ3mbf**

It's a snapshot, not a live feed: it shows stat tiles per stage, an overdue-follow-up list, and a searchable/sortable contacts table, generated from `pipeline/contacts.csv` at the moment it's built. Run `/dashboard` any time to regenerate it from the latest data and republish it to that same link (the URL is also saved in `pipeline/dashboard_url.txt`). It's private to this Claude account by default (share the link yourself if you want someone else to see it) — worth keeping in mind once the pipeline has real prospect names/emails in it.

## Automated outbound lead sourcing
A Routine ("CitraChem Daily Outbound Lead Sourcing", trigger `trig_019HJMA7FBx1BqBSCuUxES43`) fires weekdays at 14:00 UTC into this same Claude Code session. Each run:
- Sources 5 new, real, independently-verified prospect companies worldwide matching the ICP in `CLAUDE.md` (ECS-targeted pharma/biotech, nutraceutical/cannabis-infused consumer product companies, CROs, academic/government research labs), rotating sourcing signals across runs (publications, patent filings, press releases, conference programs, hiring posts) so it doesn't keep re-hitting the same result set. As of 2026-09-30, `CLAUDE.md`'s Research arm section also points it at `research/OPPORTUNITY-MAP.md`'s academic-institution pool and open disease-target-matrix gaps as an additional rotation signal — the Routine's own stored prompt wasn't editable directly this session (`list_triggers`/`get_trigger`/`update_trigger` all returned "not found" for this trigger despite it actively firing into this session, likely a session/account scoping gap in that tool), so this was wired in via `CLAUDE.md` instead, which every run already reads. If you have access to edit the Routine's prompt directly via the claude.ai Routines UI, folding this instruction into the prompt text itself would be more robust than relying on the indirect link.
- Checks `pipeline/crm.py find "<company>"` first to skip anything already tracked.
- Delegates drafting to the `outbound-sdr` agent per company (LinkedIn DM unless a verified email actually exists — never a guessed email address), which logs the touch to the CRM itself.
- Refreshes `pipeline/PIPELINE.md` and commits + pushes everything to this branch.
- **Drafts and commits only — it never sends anything or opens a PR.** Review `outreach/` and the pipeline before actually sending any of it.

To pause or stop it: ask Claude to disable/delete trigger `trig_019HJMA7FBx1BqBSCuUxES43`, or use the claude.ai Routines UI.

## Keeping it current
- Pricing or positioning changed → edit `CLAUDE.md` (and `content/llms.txt` if it affects the public summary), everything downstream picks it up automatically.
- A competitor's or alternative route's pricing/capabilities changed → `/battlecard <name>` to refresh; other agents defer to that file rather than re-researching.
- Run `/pipeline` (or `python3 pipeline/crm.py due`) periodically for overdue follow-ups on existing contacts.

## Known gaps / next steps if you want more automation
- **No real email sending or external CRM sync.** This repo has no Gmail/Outlook/HubSpot/Salesforce connector wired in. Everything here produces Markdown drafts you copy-paste and send yourself, and `pipeline/contacts.csv` is local to this repo, not synced anywhere. If you connect an email or CRM connector later, ask to wire actual sending/syncing in — that should still confirm with you before each real send, since sending is visible to the recipient and hard to undo.
- Follow-up timing (touch 2/3 of a sequence on companies already in the pipeline) is tracked (`crm.py due` will tell you it's time) but not auto-triggered — you still run `/outreach` yourself for a follow-up touch.
- `content/llms.txt` publishing to the live site is a manual step for whoever has citrachem.com access — this repo only keeps the source copy current.
- `battlecards/` starts empty — run `/battlecard <competitor or route>` (e.g. "agricultural extraction", "Purisys", "de novo synthesis") to build the first ones before `content-seo` or `outbound-sdr` need to make a competitive claim.
