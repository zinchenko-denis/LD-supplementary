# Changelog

All notable changes to the LD-supplementary repository are recorded
here. Historical release notes for the v8 → v1728 transition are
kept in `CHANGELOG_v1728.md` for reference.

---

## [v9 supplementary stale-ref cleanup — round 2] — 2026-05-17 (S635d)

**Status.** Two-source adversarial review (Cloud Code + GPT-5.5)
of the remaining stale references in LD-supplementary public files
beyond the FAQ. 16 file patches across 5 files + 3 retroactive
CHANGELOG entries.

### Changes

**README.md (6 edits)**
- L7–11: DOI ordering flipped — v9 first as current paper,
  v1728 second as previous baseline.
- L53: section heading "Verification Suite (Python, v1728-era)"
  → "Verification Suite (Python, v1728 baseline carried into v9)".
- L70–76: scope paragraph reworded to clarify the suite covers
  the shared v1728 numerical baseline (architecture-lock values)
  and that the v9-only benchmark additions (LHCb-CONF-2025-003,
  NuFIT 6.1 IC23 NO, JUNO 2025) are deferred to a future
  verification update.
- L105 (negative-space catch from Cloud Code): Sage notebook
  description "paper v8 baseline" → "v1728 baseline carried into
  v9" to align with the FAQ header framing.
- L114–117: FAQ description corrected ("23 entries" → "33 entries";
  removed false "carried into v9 unchanged"); pointer to the
  S635c CHANGELOG entry added.
- L128–131: LD-explorer description "(v1728-era; v9 update planned)"
  → "(synchronised to paper v9)" (LD-explorer was already deployed
  with v9 DOI in S635 batch).

**verify/run_all.py (1 edit)**
- L36–38: startup banner — removed stale "S295+" session ID and
  "v1728_draft_S295" string; replaced with two-line DOI block
  (v9 current + v1728 baseline). Print-only change; test logic
  untouched.

**verify/ARCHITECTURE.md (2 edits)**
- L265: section heading "## Метрики (v1728)" → "## Метрики
  (v1728 baseline, carried into v9)".
- L286: footer provenance "290 v8 + 87 v1728 + 131 S300"
  (mixed paper-version / session-ID scheme) → "290 (paper v8)
  + 87 (v1728 additions) + 131 (v1728 tower/CRT additions)"
  (Option A from review; matches per-row markers in rows 269–285).

**verify/ tier docstrings (7 edits)**
- t10_weinberg.py: "Paper v1728: §XIV" → "Paper v9 / v1728:
  §14 (Electroweak Mixing), Theorem 14.1 (Weinberg angle)".
- t11_cp_phase.py: "Paper v1728: §XIII" → "Paper v9 / v1728:
  §13 (CP Violation)".
- t12_cr_master.py (negative-space catch from Cloud Code):
  "Paper v1728: §XII (PMNS — Cross-Ratio)" → "Paper v9: §12.5
  (Gap 9 reframing: CR = master, M = scaffolding). Paper v1728:
  §XII." (verified v9 §12.5 at PDF line 3687).
- t13_tower.py: "Paper v1728: §XVI (Tower Structure)" → "Paper
  v9: §6 (NLO, Tower, and Response). Paper v1728: §XVI."
  (per FAQ Q23: tower content was moved to §6 in v9; §16 in v9
  is "Arithmetic Geometry of X₀(6)").
- t14_directed.py: paper ref expanded to cite Schur eigenvalues
  {3, 6/5, 8/11} shared content at §12.5/§16.5 (referenced
  there as X.336).
- t15_golden_bridge.py: companion-only flag added (X.263, X.267
  zero occurrences in v9 paper PDF; X.272 and X.275 not in v9
  paper either, but the qualified wording avoids overclaiming
  for the latter two).
- t16_crt_unification.py: X.280 (CRT framing, companion-only,
  0 occurrences) disambiguated from X.281 (Schur complement,
  paper-side, 4 occurrences at §12.5 + §16.5).

**verify/t4_ckm.py (1 edit)**
- L126: inline comment "per S295" cleaned (parallel symmetry
  with Block 6's removal of "S295+" from the run_all.py banner;
  session IDs do not belong in public-facing code comments).

**CHANGELOG.md**
- Retroactive entry for S635b (stale-ref cleanup in FAQ +
  derivation chain) — landed on main as commits 8a87a0d / d568f3e
  but no CHANGELOG entry was added at that time.
- Retroactive entry for S635c (FAQ three-way audit closure) —
  landed on main as commits 4bf2159 / 43d1186 but no CHANGELOG
  entry was added at that time.
- This S635d entry.

### Verification

- 0 architecture-lock baseline mutations.
- 0 changes to verification logic (banners, docstrings, and
  one inline comment only).
- 508/508 Python + 91/91 Sage check counts unchanged
  (re-verified post-patch).
- 0 new session IDs introduced into FAQ Q-bodies or anywhere
  in the public docs.

### Two-source adversarial review chain

- Round 1 (Cloud Code + GPT-5.5): 11 patches proposed initially;
  GPT-5.5 contributed Block 3 "shared baseline" wording precision
  and Block 9d explicit X.336 reference; Cloud Code contributed
  Block 5b negative-space catch (README L105 Sage v8 baseline)
  and Block 9f X.280 vs X.281 disambiguation.
- Round 2 (Cloud Code): CHANGELOG factual cross-check confirmed
  commit hashes and dates; flagged that the round-1 draft missed
  verify/t12_cr_master.py (Block 9g) and verify/t4_ckm.py L126
  S295 inline comment (Block 9h). Both added.
- Block 8 (ARCHITECTURE.md footer) final pick: Option A,
  agreeing with Cloud Code's lower-redundancy reasoning
  (the section heading already says "carried into v9", so a
  suffix on the footer line would repeat that three lines below).

### Commit

To be assigned at merge; see commits on `doc-cleanup/v9-stale-refs-S635d`.

---

## [v9 FAQ three-way audit closure] — 2026-05-17 (S635c)

**Status.** Three-way adversarial audit of LD_reviewer_FAQ.md
against paper v9 (Zenodo DOI 10.5281/zenodo.20257066). Audit
sources: this assistant (Logos), Cloud Code, and GPT-5.5.

### Patches applied (31 total)

- 30 round-1 patches (Q1–Q30 corrections, plus 3 new Q31/Q32/Q33,
  plus summary table re-references).
- 1 round-2 fix on Q18 (LHCb-direct vs CKMfitter-indirect χ²/dof
  inversion: paper L3426–3428 says LHCb direct yields 0.65 as the
  headline; CKMfitter indirect is the alternative yielding 0.15).

### Critical factual corrections

- Q1: "weight-2 newform" → "weight-10 newform" (LMFDB 6.10.a.a
  convention; the most cite-checkable single error in the previous
  FAQ).
- Q5: theorem references Thms 4.2/4.3/4.4 → Thms 2.1/2.2/2.3
  (paper v9 §2 carries primary filters).
- Q9: "Anchor Lemma 5.5" → "Anchor Lemma 3.5" (paper §3.4).
- Q10: "R² → 0 with pole masses" → R² = 0.61 with m_t(MS̄) = 162.5
  GeV per paper L1635.
- Q11: "three routes" → "two structural + two auxiliary" (paper
  §8.2 Theorem 8.2 literal wording); NLO residual 0.009 ppm
  (not <0.001 ppm).
- Q15: "δ ≠ 270° ± 20°" kill rule → "|sin δ| ≠ 1 at > 5σ" (the
  "± 20°" band has zero occurrences in v9).
- Q24: "MDL axiom" → NCG-based selection ("MDL" has zero
  occurrences in v9 paper).
- Q30: tier breakdown 93+56+81+83+131 = 444 ≠ 508 → corrected
  144+56+91+86+131 = 508 from single-process run.

### Honesty fixes

- Q3, Q4, Q12, Q19, Q20, Q22, Q29: status-layer overclaims softened
  to preserve [CONJ]/[OBS]/[DER cond.] markers.
- Section VII (Q26/Q27/Q28) re-labeled as "Companion-only
  structural extensions": X.263, X.267, X.276, X.280 verified to
  have zero occurrences in paper v9 PDF.

### New entries

- Q31 (Prior Art): Tatitscheff–He–McKay, Bao–He–Zahabi,
  Bao–Foda–He et al., Ashok–Cachazo–Dell'Aquila, He–McKay,
  Feruglio modular flavour line — what LD genuinely adds per §17.
- Q32 (v9 audit closure): three-source audit metadata.
- Q33 (v1728 → v9 diff): LHCb-CONF-2025-003 integration, NuFIT
  6.1 IC23, JUNO 2025, DESI DR2, expanded prior art, audit closure.

### Verification

- 0 architecture-lock baseline mutations.
- 0 paper, companion, DB, or verify/ touches.
- File diff: 239 → 284 lines (+45 from new entries and expanded
  formulations).

### Commits

- 4bf2159 S635c: FAQ three-way audit closure (feature branch)
- 43d1186 Merge S635c into main

---

## [v9 supplementary stale-ref cleanup] — 2026-05-17 (S635b)

**Status.** Stale-ref cleanup in public-facing documents that
survived the S635 DOI substitution batch. No content rewording,
only metadata updates.

### Changes

- LD_reviewer_FAQ.md (6 edits): v1728 DOI demoted to historical
  pointer; companion description corrected (was "post-S291,
  1244 theorem headers, 117+ dead directions"; numbers verified
  by grep — replaced with "v9 snapshot, ~19800 lines, 70+ dead
  directions"); audit lineage line de-referenced (S283/S284/S287/
  S297 removed); §VII title cleaned of session IDs; Q29 GPT-review
  lineage reworded; footer updated to v9 release with current DOI
  and verified numbers.
- LD_derivation_chain.md (2 edits): GPT triple audit reference
  de-referenced; footer fully updated to v9 release line.

### Verification

- Companion blocks grepped: 955 (not 1244 as previous footer
  claimed).
- DEAD entries: 78 "DEAD #N" + 8 "## [DEAD]" + namespace ≈ 86;
  previous "117+" overstated, "70+" conservative.
- 508/508 Python and 91/91 Sage check counts unchanged.

### Commits

- 8a87a0d S635b: stale-ref cleanup in FAQ + derivation chain
- d568f3e Merge S635b into main

---

## [v9 published] — 2026-05-17 (S635)

**Status.** Paper v9 deposited on Zenodo with assigned DOI
[10.5281/zenodo.20257066](https://doi.org/10.5281/zenodo.20257066).

### Changes

- DOI placeholders substituted with the assigned v9 DOI:
  - `LD_proof_companion.md` header (L7).
  - `README.md` (paper-v9 line + BibTeX citation block).
  - `CHANGELOG.md` (this entry).
- Repository visibility switched from private to public.
- Companion content unchanged from the v9 snapshot (S631);
  body checksum preserved.

### Companion ↔ paper correspondence

- Paper PDF: `LD_v9_FINAL.pdf`, 1.28 MB, 121 pp.
- File MD5: `2fdc4b14b97828310713eda94faa1c8e`.
- Architecture-lock baselines preserved exactly relative to the
  S634 three-way audit close: α⁻¹ = 137.035999202, μ = 6π⁵,
  R = 33.48, sin²θ_W = 3/13, sin²θ₁₂ = 4/13, sin²θ₁₃ = 2/91,
  sin²θ₂₃ ∈ {81/145, 64/145}, γ_CKM = 66.04°, δ_CP = 270°,
  m_e = 0.51099895 MeV.

---

## [v9 snapshot] — 2026-05-16 (S631)

**Status.** Snapshot prepared on a feature branch ahead of the v9
paper deposit. Visibility set to private until the paper is published.

### Companion

- `LD_proof_companion.md` rebuilt from the live working companion
  post-S618 (Phase 5 sync, 49/49 atomic edits closed).
- Preamble (L1–L73 in the source) replaced by a short release header.
- Body L74+ carried verbatim, including:
  - Internal session markers (`Source: SNNN`, `post-SNNN`) preserved
    as a provenance trail.
  - Closed (DEAD) directions retained as part of the falsification
    record.
  - Footer marker `post-S618` retained (already release-ready).
- Size: 19840 lines (vs 11690 in the v1728 snapshot).

### Headline preservation

- **X.247c [CONJ ★2 HEADLINE]** preserved as conjecture.
  Discharge framework now ADDITIVELY supplemented by four conditional /
  no-go patches: X.247c.cond [DER ★3], X.247c.no-go [THM-arith ★4],
  X.247c.A-prime [DER ★3], X.247c.EC1a [THM-arith ★4]. None promote
  X.247c to [DER].
- **I.1 [DER ★5 HEADLINE]** (ratchet-conditional) preserved.

### New content added in companion vs v1728 (selected highlights)

Sessions S282 through S618 added approximately 8 150 lines of
new derivation material to the companion. Notable additions:

- Generator dynamics, channel decomposition, commutator spectral
  theory (S351–S355: X.335–X.341c).
- All-LD PMNS eigensystem; θ₂₃ octant promoted [DER] → [THM-arith]
  via Catalan-Octant chain (X.340b/d/e).
- Lie algebra Lie(C_eff, L_eff) = sl(2,ℝ) ⊕ ℝ; Cartan-Weyl basis;
  rotation quadratic 3t² − 168t − 14 = 0; splitting field ℚ(√42)
  (X.346 series).
- Universal asymmetry ratio d₁L = 14 (X.343a_PMNS).
- Multi-route uniqueness of (d₁, d₂) = (2, 3): Catalan, NCG/Connes,
  Ihara d₁³ = N + 2, Mihailescu d₂² − d₁³ = 1
  (X.358a–c series, S389–S391).
- Cuspal Arithmetic Identity (j + N)/(j + L) = 1 − 1/(j + L);
  fourth characterisation of L = 7 via anchor Fricke-pair residue
  sum −L (X.353a, X.354).
- AL-universality of bad-Euler formula and h-vector non-universality
  (X.353, S368).
- Aut(dessin, O.1) = {e} rigidity (X.355b).
- Eisenstein a_p ≡ 1 + p⁹ (mod 1056), exhaustive at good primes
  ≤ 10⁴ (X.357).
- Anchor-Pair Demarcation X.423 [THM-arith ★4] (Form A doubly
  determined; subsequently TRIPLY determined post-S541 by anchor
  + Grothendieck whole-eigensummand + Fricke-pair log-residue G.10C).
- Phase 5 companion-sync 49/49 atomic edits (S614–S618): structural
  alignment of companion with paper post-cycle-4 v9 finalisation.

### DEAD directions

70+ closed branches recorded (canonical `## [DEAD] …` and numbered
`DEAD #1…` entries), each carrying the session reference and the
falsification argument that closed it. None removed.

### Auxiliary files

- `README.md` rewritten for v9 snapshot context.
- `CHANGELOG_v1728.md` retained as historical release notes for the
  v8 → v1728 transition.
- `LD_verification.sage`, `verify/`, `LD_reviewer_FAQ.md`, and
  `LD_derivation_chain.md` kept unchanged at v1728-era state. The
  Python verify suite (508 checks, 17 tiers) remains the
  authoritative cross-check for all v1728 numerical results carried
  unchanged into v9. A dedicated v9 verification update is planned.

### Not in this snapshot

- Working database (`LD_db_current.json`): private SSoT, not mirrored.
- Working notes, session logs, lessons learned: private.
- Paper PDF: published on Zenodo, not duplicated here.

### Visibility

Repository switched to private on 2026-05-16 ahead of paper deposit.
Public access restored after the v9 paper is deposited on Zenodo.

---

## [v1728] — 2026-04-12

Initial public release alongside paper v1728
(DOI 10.5281/zenodo.19520240). See `CHANGELOG_v1728.md` for the
v8 → v1728 transition record.
