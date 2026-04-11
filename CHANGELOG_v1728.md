# LD-supplementary: v8 → v1728 Changelog

Prepared: 2026-04-08 (S269). NOT deployed — awaiting v1728 publication on Zenodo.

## Summary
- Verification suite: 290 → **376** checks (+86 new, 0 broken)
- Companion: S217 → **S269** (9110 → 11246 lines)
- New sections: Weinberg angle, CP violation, CR master equation, tower structure
- FAQ: 23 → **27** questions (Q17 critical fix: δ_CP prediction)

## New files (4)
- `verify/t10_weinberg.py` — sin²θ_W = 3/13 (X.219), 15 checks
- `verify/t11_cp_phase.py` — |sinδ|=1, J², |U|² matrix (X.218/X.224), 25 checks
- `verify/t12_cr_master.py` — CR = master equation (X.225/X.226), 15 checks
- `verify/t13_tower.py` — tower n=0..3, JUNO, X.228 (X.183/X.202), 31 checks

## Modified files (6)
- `verify/framework.py` — added: C_tower dict, alien_89, EXP_JUNO, EXP_EW, EXP_PMNS.delta
- `verify/run_all.py` — added t10–t13 tiers, updated header to v1728/S269
- `verify/ARCHITECTURE.md` — added t10–t13 descriptions, updated metrics table
- `README.md` — rewritten for v1728 (376 checks, 14 tiers, updated citation)
- `LD_reviewer_FAQ.md` — CRITICAL: Q17 rewritten (was: "δ=0, extension needed";
  now: "sinδ=−1, falsifiable prediction"). New Q24–Q27. Updated header/footer/table.
- `LD_proof_companion.md` — replaced with S269 (11246 lines)

## Unchanged files (12)
- `verify/t0_foundation.py` through `verify/t9_information.py` (10 tier modules)
- `verify/__init__.py`
- `verify/requirements.txt`
- `LD_verification.sage` (legacy, 87 Sage checks — separate update if needed)
- `LICENSE`

## Bug found in v1728 draft
§XIV: "pull = −1.1σ (without radiative corrections)" for sin²θ_W is WRONG.
At σ_exp = 0.00004, tree-level pull = +11.3σ. NLO pull = +0.10σ is correct.
The "−1.1σ" likely uses σ ≈ 0.0004 (10× too large). Fix needed in draft.

## Deploy checklist (when ready)
1. [ ] v1728 published on Zenodo
2. [ ] git checkout main in LD-supplementary
3. [ ] Copy all changed/new files from this archive
4. [ ] Verify: `cd verify && python run_all.py` → 376/376
5. [ ] git add -A && git commit -m "v1728: +86 verification checks (376 total)"
6. [ ] git push
7. [ ] Update Zenodo DOI if new version published
