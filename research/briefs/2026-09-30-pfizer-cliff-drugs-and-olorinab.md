# Opportunity Brief: Pfizer — Eliquis/Xtandi Patent Cliffs, Reframed Around Existing CB2 Program

**Date:** 2026-09-30
**Researcher:** pharma-research agent
**Status: The strongest existing-ECS-activity signal found in this entire sweep — but it is disconnected from both named patent-cliff drugs. Flagging honestly rather than forcing a cliff-drug narrative that doesn't hold up.**

---

## 1. Target & angle

Pfizer appears twice in the patent-cliff table: Eliquis (apixaban, co-marketed with Bristol Myers Squibb, 2026 cliff, ~$12B at risk) and Xtandi (enzalutamide, co-developed/co-promoted with Astellas via the Medivation acquisition, 2027 cliff, ~$6.3B at risk). Neither drug's own indication maps to CitraChem's disease-target matrix (anticoagulation; prostate cancer, which is not one of the matrix's listed cancer types). So this brief tested a different angle: does Pfizer, as a company, have any real existing cannabinoid/ECS activity at all that would make it a credible "Intel Inside" target independent of these two specific drugs? It does — via a 2022 acquisition, not via either cliff drug.

## 2. Verified findings

**Eliquis patent timing (confirmed):** EU exclusivity lost May 19, 2026 (~15.2% global sales decline projected for 2026); US patent expiry expected 2028, extended via a supplementary protection certificate that added an estimated $29.5B in revenue beyond the original 2022 expiry. Sales forecast to peak near $14.2B in 2025 then decline as much as ~92% by 2030. BMS/Pfizer have already responded with a direct-to-patient discount program (Sept 2025), not a pipeline/indication pivot. [drug-dev.com, GlobalData, Pharmaceutical Technology via WebSearch]

**Xtandi patent timing and ownership structure (confirmed):** Composition-of-matter patent expires August 13, 2027, though later-filed formulation patents extend to 2033/2037; generics are litigating the 2027 patent specifically. Xtandi is owned by Astellas, with Pfizer holding a co-development/co-promotion economic interest via its 2016 acquisition of Medivation — so Pfizer's exposure here is a royalty/co-promote stream, not a wholly-owned asset, which matters for whether Pfizer itself would be the right BD target at all for this specific drug. [GreyB Pharsight, Scrip/Informa via WebSearch]

**Pfizer's real, confirmed cannabinoid-receptor drug development activity — via the 2022 Arena Pharmaceuticals acquisition ($6.7B, all-cash):** Arena's pipeline included **olorinab (APD371)**, an orally available, highly selective CB2 (cannabinoid receptor 2) full agonist — confirmed as a synthetic new chemical entity (C18H23N5O3, CAS 1268881-20-4, EC50 6.2 nM at hCB2), developed for visceral/abdominal pain in **irritable bowel syndrome and Crohn's disease**. [Wikipedia, MedChemExpress, InvivoChem, BioSpace, ClinicalTrials.gov protocol PDF via WebSearch] **Crohn's disease is a form of Inflammatory Bowel Disease — an exact match to CitraChem's disease-target matrix, and the same indication as CitraChem's own confirmed Waystone Pharmaceuticals LOI** (an existing precedent deal for a preclinical company developing ECS-targeted small molecules for IBD, per `CLAUDE.md`).

**Current status of olorinab — unconfirmed, flag clearly:** The Phase 2b CAPTIVATE trial (IBS-associated pain) reportedly missed its primary endpoint in the overall population, with a positive signal only in a moderate-to-severe pain subgroup at the highest dose. It is unclear from available search-snippet sources whether olorinab is still an active Pfizer program post-acquisition, was deprioritized after that setback, or has been discontinued — no 2024-2026 pipeline update specifically naming olorinab/APD371 was found, and Pfizer's own pipeline page (pfizer.com) returned `EGRESS_BLOCKED` on direct fetch, so this could not be page-verified. **Treat "Pfizer has an active CB2 program" as unconfirmed for its current status, though the acquisition and the underlying science are confirmed historical fact.**

**Chemistry note — same calibration as other CRM entries in this sweep:** Like Synendos' SYT-510, NeuroTherapia's NTRX-07, and Skye Bioscience's pipeline (all flagged in `pipeline/contacts.csv`), olorinab is a fully synthetic NCE, not a phytocannabinoid — so even if active, it would not be a drug CitraChem could directly supply raw material into. The realistic angle is the same "reference-standard/comparator material for CB2 pharmacology" positioning `outbound-sdr` has used elsewhere, not bulk API supply.

## 3. Fit assessment

**Weak fit on both named cliff drugs themselves; a real but disconnected and unconfirmed-status signal on Pfizer as a company.** Be honest about the shape of this: this is not "Pfizer has an opening in Eliquis or Xtandi that cannabinoids could fill" — neither drug's indication has any ECS plausibility. What this research actually found is that Pfizer, independent of either cliff drug, is the only company in this entire 11-target sweep with a **confirmed, named, indication-matched (IBD) cannabinoid-receptor drug development program** — which is a materially stronger signal than the purely speculative indication-overlap reasoning behind the Lilly and Amgen briefs. The catch is status uncertainty (is olorinab even still running?) and that it's a synthetic-NCE comparator angle, not an ingredient-supply angle.

## 4. Existing-relationship check

Checked `research/OPPORTUNITY-MAP.md`'s "Existing relationships" table — Pfizer is **not listed**. Checked `python3 pipeline/crm.py find "Pfizer"`: **no match**. Confirmed fresh, untouched target (Arena Pharmaceuticals itself, the originating company, is also not in the CRM or Opportunity Map — it no longer exists as an independent entity post-acquisition).

## 5. Recommended next step & owner

**Verify before anything else moves forward:** the single highest-value next step is simply confirming whether olorinab/APD371 is still an active Pfizer program in 2026 — a person with access to Pfizer's pipeline page, a paid pipeline database (e.g. GlobalData, Evaluate), or Pfizer's Q3/Q4 2026 earnings materials could resolve this in minutes; this agent could not due to the egress block. If confirmed active: hand to **`partner-intel`** to scope this as a reference-standard/comparator-material relationship (same shape as the Synendos/NeuroTherapia/Skye precedents `outbound-sdr` has already used), explicitly pitched around CB2 pharmacology and IBD relevance, not around Eliquis or Xtandi. If confirmed discontinued or unconfirmed after a real attempt to check: **not actionable — Pfizer stays on the "Intel Inside" list in principle, but this specific opening closes**, and a future brief would need a different Pfizer signal (a different pipeline asset or drug) to reopen the company as a target.
