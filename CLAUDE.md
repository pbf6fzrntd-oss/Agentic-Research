# CitraChem — Biomimetic Phytocannabinoid & Terpene Manufacturing

This file loads automatically for every subagent in this project (unless a subagent sets `omitClaudeMd: true`), so it's the shared source of truth for positioning. Keep it current — every agent below reads it.

## What we do
CitraChem manufactures botanically-identical phytocannabinoids, terpenes, and custom terpenophenolic derivatives through a patent-pending **biomimetic semi-synthesis process** — starting from plant-based essential oil precursors, not cannabis cultivation or agricultural extraction. The platform delivers active pharmaceutical ingredients (APIs) and research/consumer-product ingredients that are >98% pure and free of agricultural impurities (pesticides, heavy metals, batch-to-batch variability), at volumes and prices competitive with extraction. The **PhytoCules** product line is the catalog of ready-to-ship phytocannabinoids; the **custom synthesis** service produces novel/rare cannabinoids and terpenophenolic derivatives to a client's own specification (candidate molecules can be submitted directly via citrachem.com/custom/).

Tagline: "Advancing the Science of Nature."

## Ideal customer profile
- **Company types:** pre-clinical/clinical-stage pharmaceutical and biotech companies developing endocannabinoid-system (ECS)-targeted therapeutics; nutraceutical and cannabis-infused consumer product companies; contract research organizations (CROs) and academic/government research labs; specialty ingredient distributors.
- **Buyer personas:** Director/VP of R&D or Chemistry, Head of Formulation/Product Development, a procurement/sourcing lead, a Principal Investigator at an academic lab or CRO, or a BD lead at a partner pharma company evaluating a supply relationship (see the Waystone Pharmaceuticals LOI, April 2025, as a precedent deal shape — a preclinical company developing ECS-targeted small molecules for IBD).
- **Signal:** needs a specific phytocannabinoid, rare cannabinoid, or terpenophenolic derivative for research, formulation, or drug development, and their current source is agricultural-extract batch variability, a slow/costly de novo total-synthesis house, or a supplier that doesn't carry the specific molecule/stereochemistry needed; or they're publishing/patenting in the ECS space and need a dependable API supply partner.
- **Current alternative:** agricultural (plant) extraction; fully synthetic (de novo) multi-step chemical routes; other semi-synthesis or fermentation/biosynthesis suppliers (e.g. Purisys, Noramco, Willow Biosciences-style platforms) that may not offer the specific rare cannabinoid or bespoke derivative work.
- **Buying motion is technical/relationship sales, not self-serve.** CitraChem is a life-sciences ingredient manufacturer selling into regulated, multi-stakeholder buying processes (a scientist plus procurement, sometimes regulatory) — default every touch to "request a sample" or "submit a custom synthesis inquiry," never "sign up" or "buy now." See `playbooks/RFQ-PLAYBOOK.md` for the default sequence and tone.

## Value proposition (one sentence)
Botanically-identical, >98%-pure phytocannabinoids, terpenes, and custom terpenophenolic derivatives — produced by a patent-pending biomimetic semi-synthesis process, without cannabis cultivation, at research and commercial scale.

## GTM motion: agent-discoverable marketing
Alongside marketing to the human R&D/procurement buyer above, we also want AI agents doing vendor or literature research on a scientist's behalf (e.g. "what's a reliable supplier for pharmaceutical-grade CBG") to find and cite CitraChem accurately. Concretely:
- Keep `content/llms.txt` current — the canonical machine-readable summary of what CitraChem does, its platform, and how it compares, meant to be published at `citrachem.com/llms.txt`.
- Every comparison/battlecard should include a clearly-labeled, terse "Facts" block (plain claims, no adjectives, sourced) that an LLM can lift and cite directly, separate from the narrative prose around it.
- See `playbooks/agent-discoverable-content.md` for the full checklist.
- This is a supplement to, not a replacement for, marketing to the human buyer persona above — content should serve both a scientist skimming it and an agent parsing it, and every claim needs to survive a scientist checking it against a COA or patent.

## Pricing
No public price list — CitraChem is quote-based, priced per project:
- **Sample quantities** (research-scale) — for evaluation, assay work, early formulation.
- **Commercial/bulk quantities** — priced per volume once a molecule and spec are confirmed.
- **Custom synthesis** — scoped and quoted per candidate molecule/derivative (submit via citrachem.com/custom/ or info@citrachem.com).

> Agents: never invent a price, discount, minimum order quantity, or lead time. If asked for a number, say pricing is quote-based and route to a sample/custom-synthesis request — verify anything more specific at citrachem.com/custom/ or with a human before it goes into a live deal.

## Key differentiators vs. alternatives
- **vs. agricultural (plant) extraction:** no crop variability, no pesticide/heavy-metal/agricultural impurity carryover, consistent stereoisomeric purity batch to batch — CitraChem starts from plant-based essential oils in a controlled lab process, not cannabis cultivation.
- **vs. fully synthetic (de novo) chemical routes:** the biomimetic route follows the plant's own biosynthetic logic from readily available essential-oil precursors — fewer steps, lower cost, and faster scale-up than total synthesis from scratch.
- **vs. other semi-synthesis / fermentation-biosynthesis suppliers:** platform generality extends past the common majors (CBD, CBG) to rare/unusual cannabinoids and bespoke terpenophenolic derivatives, with an in-house custom synthesis service for a client's own candidate molecule.

## Voice & tone
- Scientific, precise, evidence-led. Cite purity/COA figures, process facts, and patent status — not adjectives.
- This audience is technical and regulated (pharma, pharma-adjacent, academic) and will check claims against a Certificate of Analysis or a patent filing. Never state a claim that isn't backed by `CLAUDE.md`, a COA, or a `battlecards/` file.
- Never claim something isn't true to close a sale.

## Team of agents in this project
This project has specialist subagents in `.claude/agents/` for sales and marketing tasks: `content-seo`, `outbound-sdr`, `scientific-community`, `inbound-rfq`, `customer-success`, `competitive-intel`, `partner-intel`. Delegate to the matching one when a task fits its description rather than doing the work in the main conversation — each keeps its output type isolated and consistent with this positioning doc. Slash commands in `.claude/commands/` wrap the common ones — see `GTM-QUICKSTART.md`.

## Ecosystem: competitors and partners
`battlecards/` (via `competitive-intel`) and `partners/` (via `partner-intel`) hold the detailed per-company profiles — see those agents' definitions for format. Competitor/partner profiles across both are independent files, so unlike outreach (which serializes through the shared CRM), researching multiple competitors or partners is safe to parallelize across several agent instances at once. `pipeline/ecosystem.csv` is a compact rollup of both (type, name, category, status, one-line summary, path to the full profile) that feeds the dashboard's "Partners & Competitors" section — update it (by hand or script, not through `crm.py`, which only owns `contacts.csv`) whenever a battlecard or partner profile is added or its status changes, then regenerate the dashboard.

## Pipeline tracking (local CRM)
`pipeline/contacts.csv` is the single structured record of every prospect/customer, driven through `pipeline/crm.py` (stdlib-only Python, no network access — it does not send anything). Any agent that touches a named prospect or customer (`outbound-sdr`, `inbound-rfq`, `customer-success`) logs/updates that company's record via `python3 pipeline/crm.py add ...` in the same turn it writes its draft, and checks `python3 pipeline/crm.py find "<company>"` first to avoid duplicate records. `pipeline/PIPELINE.md` is a generated human-readable snapshot (`crm.py snapshot`) — don't hand-edit it. Use `/pipeline` (or `python3 pipeline/crm.py stats` / `due`) to see overall status and what's due for follow-up.

This is a local record-keeping tool only — there is no connected email/CRM provider in this workspace, so nothing here sends email or syncs to an external CRM. Drafts remain Markdown files you send yourself; see `GTM-QUICKSTART.md` if you want to wire in an actual send/sync integration later.

There is also a visual dashboard (`pipeline/dashboard_template.html` → generated `pipeline/dashboard.html`, publishable as an Artifact) — see `GTM-QUICKSTART.md` / run `/dashboard`.

## Playbooks
`playbooks/RFQ-PLAYBOOK.md` and `playbooks/agent-discoverable-content.md` contain the default sequences, tone, and checklists for the technical-sales motion and the agent-discoverable content initiative described above. Agents producing outreach, content, or lead replies should follow them by default rather than improvising a generic self-serve SaaS motion.
