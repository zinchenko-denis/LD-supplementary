# Changelog

All notable changes to the LD-supplementary repository are recorded
here. Historical release notes for the v8 → v1728 transition are
kept in `CHANGELOG_v1728.md` for reference.

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
