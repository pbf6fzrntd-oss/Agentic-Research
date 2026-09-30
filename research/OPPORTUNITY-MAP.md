# CitraChem Opportunity Map

Distilled from `CitraChem_Series_A_10_UA_5-22-26.pdf` (the company's own Series A deck, dated May 22, 2026 — internal/investor material, not a public source). This is the seed reference for the `pharma-research` agent and anyone sourcing pharma/biotech targets. Update it if a newer deck or cap-table/BD update supersedes it; note the source date whenever you do.

**Read this file — specifically the "Existing relationships" section below — before sourcing or touching any of these company names as a cold outbound prospect.** Several of them are already CitraChem clients or warm/monitoring accounts per the company's own materials, not new leads.

---

## Existing relationships — NOT cold-outbound targets

These have a confirmed MOU or are named by CitraChem itself as actively monitoring the company. Treat any of these as **existing account / warm relationship handling** (customer-success or a direct BD-led conversation), never as a fresh cold first-touch. If `outbound-sdr` or the daily sourcing routine would otherwise touch one of these, stop and flag it instead of drafting.

| Company | Relationship | Therapeutic target | Molecule | Status |
|---|---|---|---|---|
| GreenWay Herbal Products, LLC | Confirmed client (MOU) | Autism | CBD / CBDA | MOU: YES |
| Bessor Pharma | Confirmed client (MOU) | Fungal pathogen | TBD | MOU: YES |
| Neuropathix | Confirmed client (MOU) | Neurodegenerative | Custom | MOU: YES |
| Waystone Pharmaceuticals | Confirmed client (MOU/LOI) | Inflammatory Bowel Disease | Custom | MOU: YES (April 2025 LOI — see `partners/waystone-pharmaceuticals.md`) |
| Carmen's Biopharma | Confirmed client (MOU) | Metabolic Diseases | CBD / CBG | MOU: YES |
| Jazz Pharmaceuticals | Warm — actively following CitraChem per deck | — | — | Monitoring, not yet engaged; Jazz acquired GW Pharma (Epidiolex) for $7.2B, so this is a live strategic-fit signal, not a cold name |
| Roche | Warm — actively following CitraChem per deck | — | — | Monitoring, not yet engaged |

**Talking point for a future Jazz conversation (not a new lead, just context to have ready):** the ARISTOCRAT Phase II trial (UK multi-center) combining nabiximols/Sativex — a Jazz/GW product — with temozolomide for glioblastoma shows a positive early survival signal. Glioblastoma is on CitraChem's disease-target matrix; this is the strongest science found for that indication in the 2026-09-30 disease-area triage, and it already sits inside the Jazz relationship rather than opening a new one. Found via `research/briefs/` disease-area sweep; no standalone brief written since Jazz is already warm, not cold.

**Known CRM conflict (flagged 2026-09-30, needs human review):** `pipeline/contacts.csv` had GreenWay Herbal Products logged as a cold `outbound` Prospecting lead (touched 2026-09-16, LinkedIn DM, follow-up cadence running). Its auto-follow-up has been neutralized (`next_action_date` cleared, a note added) so the daily sourcing routine won't push a touch-2 to an existing client, but the record's `stage` and `source` still need a human decision — likely reclassify to `Customer`/hand off to `customer-success`, and decide whether the sent touch-1 needs any follow-up message of its own. Bessor Pharma, Neuropathix, and Carmen's Biopharma are not in the CRM at all yet; add them as `Customer`-stage records (not via a fresh outbound touch) once confirmed.

---

## Research programs with active derivative interest (not yet commercial MOUs)

Per the deck, CitraChem is pursuing a derivative in each of these — a warmer research-collaboration signal than a cold outbound lead, but not yet a paying client. Worth a relationship-nurture pass, and useful precedent/case-study material for outbound to *other* academic labs.

| Research area | Starting molecule | Partner | Pursue derivative |
|---|---|---|---|
| Acute Kidney Disease | THCV | Hebrew University | YES |
| Obesity / Type 2 Diabetes | THCV | Hebrew University | YES |
| Chronic Pain | CBC | Penn State | YES |
| Traumatic Brain Injury | CBD / CBG | St. Michael's College | YES |

Hebrew University is already tracked in the CRM as "Multidisciplinary Center for Cannabinoid Research (MCCR), Hebrew University" (Prof. Joseph Tam) — cross-check before treating the THCV programs above as a separate contact; they may be the same lab/PI or a different group at the same institution (verify, don't assume). Penn State and St. Michael's College are not yet in the CRM — check which department/PI runs the CBC and CBD/CBG work above before sourcing them as a fresh academic lead, since CitraChem may already have the relationship through a different contact.

---

## Disease-target matrix

The deck frames CitraChem as "disease agnostic" — the platform can in principle support a derivative program in any of these. Use this list to scope a `pharma-research` brief ("find real, current drug-development activity by a specific company or lab in this indication that a cannabinoid/terpene derivative could plausibly support") rather than treating it as a claim CitraChem already has traction in all of them — only the five in the "Existing relationships" table above and the four research programs above are confirmed engagements as of the deck's date.

Obesity, Breast Cancer, Leukemia, Pancreatic Cancer, Glioblastoma Cancer, Neuroblastoma Cancer, Alzheimer's Disease, Diabetes, Lymphoma, Chronic Pain, Osteoporosis, Antiemetic, Traumatic Brain Injury, Neurodegenerative disease, Migraine, Dermatitis, Inflammatory Bowel Disease, Metabolic disease, Fungal pathogen, Autism.

---

## Named big-pharma targets ("Intel Inside" framing) + patent-cliff urgency data

The deck's core BD thesis: CitraChem's ingredients can power drug discovery/development the way Intel's chips power PC/device makers — i.e. the real prize is a small-molecule/IP relationship with a major pharmaceutical company, not just smaller biotech/academic accounts. It names these companies explicitly as the target class:

Eli Lilly, Pfizer, Novo Nordisk, Novartis, Roche, Merck, Johnson & Johnson, Sanofi, GSK, AstraZeneca, Amgen, AbbVie, Bristol Myers Squibb.

These sit well outside CLAUDE.md's default ICP (which centers on pre-clinical/clinical-stage biotech, CROs, and academic labs) — a named big-pharma target needs a different motion: BD-led, likely through a specific R&D/business-development division or a named executive, and the opening is almost always a **patent-cliff revenue gap** in an indication cannabinoids/terpenes could plausibly address, not a generic "we sell pure cannabinoids" pitch. The deck's own patent-cliff table is the starting data set for finding that opening:

| Year | Drug | Company | Annual revenue at risk |
|---|---|---|---|
| 2025 | Xarelto | Johnson & Johnson | $6.8B |
| 2025 | Entresto | Novartis | $6.0B |
| 2025 | Farxiga | AstraZeneca | $6.0B |
| 2025 | Prolia | Amgen | $4.0B |
| 2026 | Eliquis | Bristol Myers Squibb / Pfizer | $12B |
| 2027 | Trulicity | Eli Lilly | $7.1B |
| 2027 | Ocrevus | Roche | $7.1B |
| 2027 | Xtandi | Pfizer | $6.3B |
| 2027 | Imbruvica | AbbVie / Johnson & Johnson | $4.9B |
| 2028 | Keytruda | Merck | $25B |
| 2028 | Opdivo | Bristol Myers Squibb | $9B |
| 2028 | Gardasil 9 | Merck | $8.9B |

(Citation in the deck: BioPharma APAC / Genetic Engineering and Biotech News. Treat these as directionally correct but re-verify current figures — patent-cliff dates and revenue-at-risk estimates get revised — before using a specific number in outward-facing material.) Broader context cited: ~$230B–$300B in annual drug sales industry-wide at risk from patent expirations between 2025 and 2030, with generic/biosimilar competition typically cutting sales up to 80%.

**Verified corrections (as of 2026-09-30, from `pharma-research` briefs in `research/briefs/`) — the table above is left as the deck originally stated it for provenance; use these corrected figures instead when citing a specific date/number:**
- **Prolia / Amgen:** the deck frames this as a 2025 cliff still approaching. Current reporting: the US patent already **expired Feb 19, 2025**, and Sandoz and Fresenius Kabi biosimilars are already FDA-approved with launch pending litigation — this has already happened, not an upcoming event. See `research/briefs/2026-09-30-amgen-prolia-cliff.md`.
- **Farxiga / AstraZeneca:** the deck's "2025 / $6.0B" framing doesn't match current reporting, which puts **US loss-of-exclusivity at April 2026** (not 2025), **US 2025 revenue at $1.7B** (21% of ~$8.1B *global* revenue — the deck's $6.0B appears to be a global, not US, figure), with **EU patent protection extending to 2028**. See `research/briefs/2026-09-30-astrazeneca-farxiga-cliff.md`. This brief also found the fit itself doesn't work (SGLT2 inhibitor, no ECS mechanism) independent of the date correction.
- **Imbruvica / AbbVie-J&J:** the deck's "2027 / $4.9B" framing implies near-term urgency; current reporting puts realistic generic entry (via formulation patents, not just the composition-of-matter date) at **2032–2036**, materially later. See `research/briefs/2026-09-30-pfizer-cliff-drugs-and-olorinab.md` (covered as a disqualified candidate inside that brief).
- **Migraine / CGRP-inhibitor class (Aimovig, Emgality, Ajovy, Nurtec ODT, Zavzpret, Qulipta) — not in the deck's table, but tested and found NOT to qualify as a cliff:** every drug in this class has protection running well past 2029 (formulation/use patents to 2039–2043, BPCIA biologic exclusivity to ~2030), and several have growing, not shrinking, revenue. Do not add this class to the table as a cliff entry. See `research/briefs/2026-09-30-migraine-cgrp-cliff.md` — though that brief surfaced a strong *non-cliff* academic-research angle instead (see the institution-pool note below).
- A broader 2026-09-30 sweep for additional 2025–2029 blockbuster cliffs in pain, oncology-supportive-care, and neurodegenerative disease beyond this table's 12 entries found none that clear the bar (real cliff + real revenue + plausible ECS mechanism + named target company) — see the "no new opportunity brief written" trail preserved in that day's session notes if this needs re-walking.

**Open threads flagged, not yet resolved (worth a follow-up `pharma-research` pass before acting on either):**
- **Pfizer / olorinab (APD371):** a CB2 agonist for Crohn's/IBS pain, acquired via the 2022 Arena Pharmaceuticals deal — same indication class as CitraChem's own Waystone Pharmaceuticals precedent, the strongest indication-level ECS signal found in the whole 2026-09-30 sweep. But its current program status is unconfirmed (a Phase 2b readout reportedly missed its primary endpoint; no 2024–2026 pipeline mention found; Pfizer's own pipeline page was egress-blocked). Confirm active/dead before anything else proceeds. See `research/briefs/2026-09-30-pfizer-cliff-drugs-and-olorinab.md`.
- **Bristol Myers Squibb / FAAH-MAGL — resolved, still disqualified (2026-09-30):** the garbled snippet was BMS-986368 (irafamdastat), a dual FAAH/MAGL inhibitor BMS holds via its 2019 Celgene acquisition (originally in-licensed by Celgene from Abide Therapeutics in 2018). Active Phase 2 trials in Alzheimer's-associated agitation (NCT06808984) and MS spasticity (NCT06782490) — Alzheimer's and neurodegenerative disease are both on CitraChem's own disease-target matrix, but irafamdastat is a synthetic serine-hydrolase-inhibitor small molecule, not a phytocannabinoid/terpene, so no ingredient-supply or custom-synthesis fit was found. See `research/briefs/2026-09-30-bms-faah-magl.md`. BMS remains disqualified as a cold "Intel Inside" target (Eliquis, Opdivo, and now this) unless a future signal surfaces an actual exogenous-cannabinoid sourcing need tied to this program.

**How to use this table:** a `pharma-research` brief on a named big-pharma target should identify (a) which of its patent-cliff drugs sits in an indication overlapping the disease-target matrix above (pain, oncology, metabolic/diabetes-obesity, neurodegenerative are the most plausible cannabinoid/terpene fits), (b) whether that company has any existing cannabinoid/ECS pipeline activity or public statements, and (c) a real, current point of contact or BD channel — not just "email a generic corporate address."

---

## M&A / valuation comps (context, not a target list)

Useful as market-sizing and urgency talking points in a pitch, not as sourcing targets themselves:

- Jazz Pharmaceuticals acquired GW Pharmaceuticals (Epidiolex, a cannabinoid drug) for **$7.2B**.
- Recursion Pharmaceuticals acquired Exscientia (automated molecular design/chemistry synthesis platform) — all-stock, ~**$1.3B** pro forma — Aug 7, 2024.
- Novartis acquired MorphoSys (computational antibody/therapeutic molecule discovery platform) — ~€2.7B (~**$3.0B**) — mid-2024.

---

## Active-cannabinoid-research academic institutions (deck-sourced target pool)

The deck lists these as institutions with active cannabinoid research, positioned as either direct research-sample customers or credibility/referral sources. Cross-check each against `pipeline/crm.py find` before sourcing — several are likely already touched by the daily outbound routine (e.g. UCLA, Hebrew University, Mississippi, Dalhousie is not on this list but similar ones are); many are not yet tracked and are a ready-made pool for future `pharma-research` → `outbound-sdr` handoffs:

Johns Hopkins University, Harvard University, Penn State, UC San Diego, Universitat de Barcelona, University of Sydney, University of Amsterdam, University of Alberta, NIH National Center for Complementary and Integrative Health (NCCIH), Yale, Columbia University, Temple University, University of Illinois Urbana-Champaign, University of Utah, Indiana University, Hebrew University of Jerusalem, Oregon State University, Washington State University, UCLA, University of Minnesota, UNLV, University of Colorado Denver, University of Toronto, Drexel University, MUSC Health, University of Mississippi, Saint Michael's College.

**Additions found through `pharma-research` briefs, not in the original deck list:**
- **University of Iowa** (Andrew F. Russo lab) and **Leiden University Medical Center** (van den Maagdenberg / Tolner) — added 2026-09-30, via the migraine brief. Two 2025 *Cephalalgia* papers from this collaboration show CBD:THC combinations directly rescue CGRP-induced migraine symptoms in mouse models — a concrete, current, published signal, not general literature. Not yet researched deeply enough for an outbound touch; see "Other next steps" below.
- **UC San Diego** was already on the list above, now has a concrete hook: Dr. Nathaniel Schuster's Center for Pain Medicine, AHS-award-winning THC:CBD migraine RCT (NCT04360044) — already touched by `outbound-sdr`, 2026-09-30 (see `outreach/2026-09-30-ucsd-schuster-migraine-lab.md`).
- **MUSC Health** was already on the list above, now has a concrete hook: Dr. Nancy DeMore's Hollings Cancer Center breast-cancer CBD trial (NCT06148038) — already touched by `outbound-sdr`, 2026-09-30 (see `outreach/2026-09-30-musc-demore-breast-cancer.md`).

**Note on Hebrew University — two distinct programs, don't conflate them:** the CRM's existing "Multidisciplinary Center for Cannabinoid Research (MCCR)" touch is Prof. Joseph Tam. The osteoporosis/bone-metabolism cannabinoid research at Hebrew University (CB2 receptor/HU-308) traces to a *different* PI, Prof. Itai Bab — real foundational science but largely 2005–2021-era with no current active commercial program tied to it (found during the 2026-09-30 disease-area triage). If ever pursued, it runs through a different contact at an institution CitraChem is already prospecting, not a new account.

---

## Other deck data points worth reusing in outreach/content (verify currency before reuse)

- **Natural-compound success rate:** FDA-approved active ingredients inspired by a natural compound have a **45%** clinical-trial success rate vs. **10%** for fully synthetic active ingredients (cited source: "Natural Products Have Increased Rates of Clinical Trial Success throughout the Drug Development Process," *Journal of Natural Products*, July 6, 2024). Strong, citable "Facts" block material per `playbooks/agent-discoverable-content.md` — verify the citation directly before using it in published content, don't take the deck's citation on faith.
- **Production economics framing:** ~500 million pills/year is the rough scale the deck cites for "capital intensive" natural-material production — useful color for a differentiation narrative, not a CitraChem-specific claim.
- **Regulatory tailwind:** April 2026 rescheduling move (per the deck's CNN/Dr. Sanjay Gupta clip and the Inc. article on marijuana rescheduling) is cited as a catalyst for cannabinoid drug-discovery investment. Re-verify current federal scheduling status before citing this as fact in any outward-facing material — it moves fast and the deck is a point-in-time snapshot.
