# LD Framework — Reviewer FAQ

**Companion document to:** D.D. Zinchenko, "1728: The Standard Model from X₀(6)" (2026).
**Paper v9 (current):** [DOI 10.5281/zenodo.20257066](https://doi.org/10.5281/zenodo.20257066)
**Paper v1728 (April 2026):** [DOI 10.5281/zenodo.19520240](https://doi.org/10.5281/zenodo.19520240)
**Code:** [github.com/zinchenko-denis/LD-supplementary](https://github.com/zinchenko-denis/LD-supplementary) — 508/508 Python checks (17 tiers) + 91/91 Sage (v1728 baseline carried unchanged into v9)
**Companion:** LD_proof_companion (v9 snapshot, ~19800 lines, 70+ dead directions)

This document anticipates questions that arise on first reading and provides concise answers with precise references. Questions are ranked by frequency from 15+ independent audits during paper preparation (physics/math/experimentalist reviews, adversarial audits, cross-verifications, full paper audits, three-way audit prior to the v9 release).

---

## I. The Big Question

### Q1. Where is the Lagrangian? Where are the equations of motion?

This is the most common criticism. The honest answer: there is no Lagrangian. The framework is at the Balmer stage (1885), not the Schrödinger stage (1926).

What exists instead is an arithmetic-geometric scaffold: monodromy, the Belyi map, cusp and tower data, and exact rational identities organise the observed quantities. The L-function L(6.10.a.a, s), evaluated at the four cusps of X₀(6), generates all coupling scales through its values at divisors of N. The tower structure (X.197, X.202) shows that a single modular object — the unique **weight-10** newform 6.10.a.a on the unique genus-0 curve with cusp widths = Div(6) — determines all observables.

The monodromy relation σ₁·σ₀·σ∞ = id is the constraint. The Belyi map β: X₀(6) → ℙ¹ is the solution. The spectrum L(f, s) at cusps yields the physics. This is not yet an action principle in the QFT sense. The paper explicitly leaves the Balmer → Schrödinger action-principle problem open (§19.4).

Balmer's formula was not wrong for 40 years — it was incomplete. We claim to be at the Balmer stage. The review implicitly demands the Schrödinger stage as an entry ticket. We believe this sets the bar at the wrong height for the specific claims we make: zero-parameter numerical predictions that can be falsified.

### Q2. This is numerology. How is it different from number-fitting?

Three criteria distinguish the framework from number-fitting in the v9 framing:

1. **Out-of-sample check.** sin²θ₁₂ = 4/13 is consistent with JUNO 2025 at +0.17σ, while TBM (1/3) is disfavoured at −2.8σ.
2. **Falsifiability.** Structural kills are catalogued in §18.4 (Table 7), each a genuine risk: failure of sin²θ₁₂ = 4/13, the pair {81/145, 64/145}, |sinδ| = 1, sin²θ₁₃ = 2/91, and the 12-particle dictionary.
3. **Status-labelled derivations.** v9 separates [THM], [DER], [DER cond.], [OBS], and [CONJ] layers. The mass-formula trace-formula chain has theorem-level arithmetic pieces (§5.3–§5.4), but the action-principle origin of the mass law remains open (§19.4).

Statistical argument: the figure p < 10⁻²⁶ from 18 rational predictions matching experiment is a reductio-style [EMP/STAT] plausibility argument (§12.11), not a theorem-level probability for the framework.

### Q3. "Zero free parameters" — but Table 2 lists inputs. Is this honest?

Zero *continuous* free parameters. The structural inputs are:

- One dimensionful scale (mₑ)
- One algebraic classification (A_F → (d₁, d₂) = (2, 3))
- Physical identifications (bridges between mathematics and observables)

No parameter is adjusted, fitted, or optimised to match data. Every headline number is either a theorem (exact rational from the dessin), a derived quantity, or explicitly marked as conditional ([DER cond.]), observational ([OBS]), or conjectural ([CONJ]) — see status markers in v9 §1.4. Table 2 enumerates all inputs explicitly — nothing is hidden.

### Q4. "18 predictions" vs "58+ observables" — what's the real count?

18 Tier A: arithmetic outputs with experimentally distinct correspondences. They have no continuous fit parameters, but internal derivational dependencies are explicitly displayed in v9 §1.2 (independence-block decomposition). These are the headline number.

58+ includes downstream quantities (e.g. mass ratios from individual masses), structurally constrained items (e.g. det M_lep = 13 from spectrum), and reformulations (same result from different angles). The independence ledger is in the companion.

---

## II. Why This Curve (§§1–4)

### Q5. Why N = 6?

v9 §2 uses three scoped primary filters within the Γ₀(N) / squarefree-genus-zero framework:

- **Theorem 2.1** (cusp–representation correspondence): index = 12, exactly 4 cusps, widths = Div(N).
- **Theorem 2.2** (index = 2N characterisation): rad(N) = 6 selects N = 6 uniquely among squarefree levels.
- **Theorem 2.3** (analytic closure): genus 0 ∧ ν₂ = ν₃ = 0 for squarefree N uniquely selects N = 6.
- **Theorem 2.6** (maximality): N = 6 = max{genus 0 ∩ φ(N) ≤ 2}.

Theorems 2.4–2.8 give further corroborating characterisations (Picard–Fuchs triple, etc.). The uniqueness claim is scoped to the stated families — squarefree genus-zero levels — not stated as an unqualified all-positive-integers theorem.

### Q6. Why Γ₀(N) and not Γ₁(N), Γ(N), or Γ₀(N)⁺?

Γ₁(6) = Γ₀(6) since φ(6) = 2. Γ(6) has genus 1 and 12 cusps all of width 6 — fails both genus 0 and cusp-width matching. Γ₀(6)⁺ has index 6 — only 6 edges, insufficient for 12 particles. Complete classification of the relevant index-12 subgroups, recorded as companion block X.217, shows Γ₀(6) is unique with genus 0, 4 cusps, and widths = Div(N) in the stated subgroup family. (Block IDs of the form X.NNN, I.NN, etc. reference the companion database, not paper sections — see v9 §1.4.)

### Q7. The input A_F = ℂ ⊕ ℍ ⊕ M₃(ℂ) comes from NCG. What if NCG is wrong?

Only two integers are used: dim(fund SU(2)) = 2 and dim(fund SU(3)) = 3. These are experimental facts. NCG is one of multiple independent paths to (d₁, d₂) = (2, 3); v9 §2 catalogues three primary filters + three corroborating characterisations (§2.7 Summary), and the companion records additional structural identities (Catalan d₂² − d₁³ = 1, Ihara d₁³ = N + 2, K-theory routes) converging on the same point.

---

## III. The Dessin and Particles (§§5–6)

### Q8. The SM has 17 particles. The dessin has 12 edges. Where are the gluons, Z, and γ?

The 2-face of the dessin contains W and H (v9 §4.9 + Table 3). Photon γ and Z arise from W₃–B mixing after EWSB — not independent dessin edges. Gluons are gauge degrees of freedom, realised through colour ramification (d₂ = 3 black-vertex valency, §3.1). Note: Gap 10 in v9 (§19.3) is the neutrino-mass Universality conditional layer, **not** post-EWSB boson content.

### Q9. The proton is composite. Why is it fundamental here?

The proton is not elementary in QFT. In the LD dictionary it is the unique stable baryon and the unique σ∞-fixed point (Anchor Lemma 3.5, §3.4). Its mass enters through μ = mₚ/mₑ. The compositeness is the structural mechanism by which QCD data enters the framework — not hidden, but a structural dictionary role rather than a claim of fundamentality.

---

## IV. Mass Formula and Constants (§§7–9, 12)

### Q10. R² = 0.89 with 10 data points is fragile.

The mass comparison is scheme-sensitive and v9 §5.5 states the scheme explicitly: light quarks use MS̄(2 GeV), charm and bottom use MS̄(m_c) and MS̄(m_b), and the top uses the pole mass. With m_t(MS̄) = 162.5 GeV, R² drops from 0.89 to 0.61; excluding the top, R² ≈ 0.90 in either scheme. The robust claims are the stated scheme, 10/10 NLO signs correct, and zero continuous fit parameters.

### Q11. Is μ₀ = 6π⁵ a coincidence?

Each factor has modular origin: 6 = N; 5 = N−1; π from SL₂(ℝ) hyperbolic metric. v9 §8.2 Theorem 8.2 derives NLO C = 10/9 from **two structurally dual presentations** (B₁ cardinality ratio |B₁|/(|B₁|−1) = 10/9, and index–ramification ratio (index − d₁)/(index − d₂) = 10/9) plus two auxiliary confirmations (empirical best-fit selector below 0.01 ppm; Catalan EC observational match). NLO residual: 0.009 ppm; sub-ppm closure uses the NNLO/Riemann–Roch series and conditional T⊥ corrections. Arithmetic pieces are theorem/derived; the physical μ bridge is layered: H.2a remains a [CONJ] bridge (μ_LO = Z_μ,LO identification), full status [THM/DER cond.; H.2a bridge [CONJ]].

### Q12. The W₆-odd selection in α is 1 bit of empirical input.

The bit is now physically replaced. v9 §7.6 catalogues four routes to the W₆-odd selection: empirical at ~2400σ (W₆-even gives α⁻¹ = 137.035948904 at +2394σ, dead); β₀·vol(X₀(6)) = L under the Nf = N physical condition; w₆ = w₂·w₃ = −1 trace formula [THM, X.97]; Ihara bipartite-graph identity. The W₆-odd α-IR fluctuation sector inherits the X.247c [CONJ HEADLINE] Costello/BV one-loop axiom (§19.2). Arithmetic Fricke parity is theorem-level; the physical identification of the fluctuation sector is conditional.

### Q13. G is conditional on nuclear data.

L1 (α, μ) closed within Γ₀(6). L1b (G) requires neutron mass and deuteron binding energy — nuclear physics external to the dessin.

### Q14. Why MS̄ at μ = 2 GeV? Is the scale derivable?

No. The renormalisation scale is not derivable from the dessin — genuine limitation. But μ = 2 GeV is the PDG convention, not a model choice.

---

## V. Mixing Parameters (§§10–14)

### Q15. Does the framework predict CP violation?

Yes, conditionally. |sinδ| = 1 is [THM-arith, X.218] conditional on CP-field minimality (cos δ ∈ ℚ); sinδ = −1, i.e. δ_CP = 270°, is [DER, 1 identification; cond. CP-field minimality + canonical ℍ/F₂ orientation X.224]. v9 §13.1: DUNE and Hyper-K will measure δ to ~15° precision by ~2030. Current global fit (NuFIT 6.1): δ = 207°₋₂₀⁺²³, 2.7σ from 270°. The framework's structural kill criterion is |sinδ| ≠ 1 at > 5σ (v9 §18.1 Tier 1), not a hard '270° ± 20°' band.

### Q16. The θ₂₃ octant depends on the dataset.

v9 §12.3 derives the **orbit pair** {81/145, 64/145} as [THM-arith] from the four-cusp cross-ratio. X.130 channel rule + X.340b Schur magnitude indicator give the structural upper representative 81/145 [DER]. Under current NuFIT 6.1 IC23 NO empirical convention combined with the I.1 NO branch, the lower 64/145 is the active comparison branch [EMP/STAT cond. I.1]. NuFIT has changed the preferred octant three times in five years; DUNE and Hyper-K will decide. Framework is falsified only if **both** 81/145 and 64/145 are excluded at > 5σ (§12.11, §18.1).

### Q17. JUNO +0.17σ is not a "confirmation."

Correct: "consistent at +0.17σ." JUNO final (σ ~ 0.005) will separate 4/13 from TBM at > 5σ.

### Q18. All 4 CKM parameters derived?

Yes, conditionally through the UST bridge. v9 §11.5: χ²/dof = 0.65 with dof = 3, R_b² excluded as constraint, p = 0.58 (Rb² = 0.405 carried as observational consistency check, not a fit constraint). The graph/UST quantities are theorem-level; the physical identification with CKM parameters is [DER], motivated by the Burton–Pemantle transfer-current theorem. With the LHCb-CONF-2025-003 direct γ = 62.8 ± 2.6° benchmark (paper headline), v9 gives χ²/dof = 0.65. If the CKMfitter indirect value γ = 66.3° is used instead, γ drops to +0.1σ and χ²/dof = 0.15.

### Q19. Three angles share denominator 13 — coincidence?

Structural: 13 = Φ₃(d₂) = det M_lep. The denominator enters PMNS/tower/electroweak through the X₀(6) arithmetic. Note: in v9 the lepton operator M itself is scaffolding and Gap 9 (§19.1) remains open — do not attribute the 13 to a derived operator.

### Q20. sin²θ_W = 3/13 — tree or MS-bar?

Tree: sin²θ_W = 3/13 = 0.23077, status [DER, 1 identification] via the electroweak generator-counting bridge (v9 §14, Theorem 14.1). NLO: (3/13)(1 + (5/3)α/(2π)) = 0.23122, pull +1.9σ, status [OBS, X.192].

---

## VI. Structure and Falsification (§§14–18)

### Q21. Is there RG evolution?

Open. Lattice positions n are integers — topological, don't run. Valuable future work.

### Q22. How many independent paths exist to (d₁, d₂) = (2, 3)?

v9 §2 catalogues three primary filters + three corroborating characterisations. Appendix E reports "40+ structural theorem families and robustness checks." The companion records additional independent route clusters (ramification, Hecke, K-theory, etc.); a ≥9-cluster scaffold is documented in companion B.4. Between clusters, failure modes are independent.

### Q23. What is the tower and why does it halt?

Tower L(6.10.a.a, k/2+n) for n = 0,1,2,3 (mass, CKM, PMNS, HALT). HALT from Fermat filtration: W₂ = +1 → 3 sectors.

### Q24. How is (d₁, d₂) = (2, 3) selected?

In v9, (d₁, d₂) = (2, 3) is fixed by the NCG algebra A_F = ℂ ⊕ ℍ ⊕ M₃(ℂ) (§1, §2): dim(fund SU(2)) = 2 and dim(fund SU(3)) = 3 are experimental facts. This is a single structural identification; after it, the framework is pure dessin combinatorics. MDL was companion-only language from earlier versions and is not part of v9's framing. The companion records additional independent paths to the same (2, 3) point (Catalan d₂² − d₁³ = 1, Ihara d₁³ = N + 2, K-theory routes); see Q7.

### Q25. Koide is more precise for leptons.

Different scope: 3 particles / 1 parameter vs 12 particles / 0 continuous parameters.

---

## VII. Companion-only structural extensions (Directed Operators and CRT)

### Q26. What is the golden bridge? *(companion-only)*

In the companion (block X.263, [THM-arith]), the directed adjacency A_dir on the bipartite dessin has characteristic polynomial factoring through the golden quadratic q_φ = x² − x − 1, with q₅ = q_φ·q₃ − d₂. The orientation operator Ω₃ on the level-3 exact subspace (companion X.267) has eigenvalues {0, −φ, 1/φ}. This material is recorded in the companion only; X.263 and X.267 have zero occurrences in the v9 paper PDF. It documents algebraic specificity of the X₀(6) framework but is not on the path to the 18 Tier A outputs.

### Q27. What does CRT Grand Unification mean? *(companion-only framing)*

In the companion (X.280), the Laplacian restricted to the exact-level subspace V₆^{ex} decomposes as L|_{V₆^{ex}} = 3I − A_dir − σ₀⁻¹, where A_dir is the directed adjacency containing the golden-bridge subspace (Q26). The 'CRT Grand Unification' framing is companion-only (X.280 has zero occurrences in the v9 paper PDF). The Schur eigenvalues themselves do appear in v9: the L_eff spectrum {c₁ = d₂ = 3, c₂ = 6/5, c₃ = 8/11} is given at §12.5 (L_eff eigenvalues) and §16.5 (W₃ tower derivation), referenced as X.336 in v9 §12.5.

### Q28. Why is N = 6 unique for the golden bridge? *(companion-only)*

In the companion (X.276), the functional F(A, Ω) = det(A)² + Tr([A, Ω]²)² evaluates to zero uniquely at N = 6 among tested semiprimes: p = 2 supplies ker(Ω), q = 3 supplies deg(q_φ) = q − 1. The selection is algebraic rigidity, not variational. X.276 is companion-only (zero occurrences in v9 paper PDF). The v9 paper's own uniqueness arguments for N = 6 live in §2 (Theorems 2.1–2.3, 2.6); see Q5.

---

## VIIIa. Prior Art and Originality

### Q31. What is the prior art on dessins in physics, and what is genuinely new in LD?

Dessins d'enfants on modular curves, including Γ₀(6) specifically, have been studied for decades in mathematics (Grothendieck, Belyi, Lando–Zvonkin, Schneps, Wolfart) and connected to gauge theories and Seiberg–Witten curves (Ashok–Cachazo–Dell'Aquila, He–McKay, Bao–He–Zahabi, Bao–Foda–He et al.). Modular flavour symmetry — modular forms as Yukawa couplings — is an active programme (Altarelli–Feruglio, Feruglio, Li–Liu–Ding). The dessin of X₀(6) with passport {3⁴, 2⁶, 6+3+2+1} has been independently tabulated by Tatitscheff–He–McKay (arXiv:1812.11752) and Bao–He–Zahabi (arXiv:2111.03655); see v9 §3.7 and §17.

**What is NOT new in LD** (acknowledged in v9 §17):
- Dessins in physics generally; X₀(6) dessin combinatorics specifically.
- Modular flavour mixing schemes producing rational angles (Feruglio line).
- The leading μ ≈ 6π⁵ relation (Lenz 1951).

**What IS genuinely new** (per v9 §17, "no precedent in the dessin literature"):
- The simultaneous identification X₀(6) dessin → 12 SM particles → {α, μ, 10 masses, 4 CKM, 3 PMNS + δ_CP, sin²θ_W} from a single combinatorial object, with zero continuous parameters.
- CKM Wolfenstein parameters from uniform-spanning-tree probabilities on the bipartite dessin (transfer-current bridge, §11).
- PMNS mixing angles from cross-ratios of the Γ₀(6) Hauptmodul (§12.1–§12.3).
- Use of the weight-10 newform 6.10.a.a as the generator of the perturbative tower L(f, k/2 + n) controlling NLO corrections across mass, response, and mixing sectors (§5.3, §6).

This is the divisive claim. The paper's own framing (v9 §1.7) is "speculative mathematical physics with sharp phenomenological claims," not a derivation of the Standard Model.

---

## VIII. External Audits

### Q29. GPT-physicist gave "reject." Do you agree?

LLM-assisted pre-publication QA, not peer review. Three independent GPT-class reviews during v1728 preparation flagged overclaims, structural gaps, and statistical packaging issues — addressed in the v1728 → v9 transition. The v9 release additionally underwent a three-source adversarial pre-deposit audit (Logos + Cloud Code + GPT-5.5) closing 9 Tier-2 findings (8 paper-side + 1 DB-side) with zero architecture-lock baseline mutations; see CHANGELOG. These are internal QA artefacts, not substitutes for peer review.

### Q30. 508 verification checks — what do they test?

17 tiers from monodromy to observables (counts from a single-process run of `verify/run_all.py`):

| Tiers | Content | Checks |
|-------|---------|--------|
| t0–t3 | Foundation, monodromy, quantum numbers, spectrum | 144 |
| t4–t5 | CKM, PMNS | 56 |
| t6–t9 | Mass formula, α/μ/G, Gap 3, information | 91 |
| t10–t13 | Weinberg, CP, CR master, tower | 86 |
| t14–t16 | Directed operators, golden bridge, CRT unification | 131 |
| **Total** |  | **508** |

Every check starts from O.1 monodromy — no precomputed results. Fraction arithmetic + numpy cross-validation.

### Q32. What is the v9 audit closure?

Pre-deposit, v9 underwent a three-source adversarial audit (Logos + Cloud Code + GPT-5.5) reading the paper, the DB (1000 blocks), and the companion (~19800 lines) under identical inputs. The audit identified 9 Tier-2 findings (zero Tier-1 blockers): a missing LHCb-CONF-2025-003 bibliography entry for the direct γ measurement, a CODATA-2018 reference fix, a §12.5 wording clarification for X.221 Layer A vs full-block status, two D.8b namespace clarifications, a §15 status-box split between individual-mass [CONJ] and block-level [DER cond.] ratchet-conditional, a §7.6 footnote on six-selector treatment, a Figure 3 caption neutral-relabel, an authorship/title fix for Esteban et al. (arXiv:2601.09791), and a stale CKM-pulls entry in DB block V.4. All 9 closed via 8 atomic paper commits + 1 DB commit + PDF rebuild. Architecture-lock baselines (α⁻¹ = 137.035999202, μ = 1836.15267343, R = 33.48, all mixing angles, γ_CKM, sin²θ_W, m_e) preserved bit-exactly. Companion drift across X.221 / I.1 / D.8b loci: zero.

### Q33. What changed v1728 → v9?

v9 (May 2026) is incremental over v1728 (Apr 2026, DOI: 10.5281/zenodo.19520240). Substantive paper-side changes:

- LHCb-CONF-2025-003 direct γ = 62.8 ± 2.6° measurement integrated (§11.5, App C.2).
- NuFIT 6.1 IC23 NO benchmark adopted for atmospheric/solar pulls (§12.10).
- JUNO 2025 first reactor measurement of θ₁₂ folded into §12.9 / §15; pull = +0.17σ.
- DESI DR2 cosmological Σm_ν bound flagged in §15.
- α Form A triply determined: anchor Fricke-pair + Grothendieck whole-eigensummand + Fricke-pair log-residue (§7.5, §7.6, §19.2).
- Expanded prior-art coverage (§3.7, §17): Tatitscheff–He–McKay, Bao–He–Zahabi, Bao–Foda–He et al., Ashok–Cachazo–Dell'Aquila, He–McKay.
- §15 status box: individual neutrino masses [CONJ]; block-level I.1 architecture [DER cond.] ratchet-conditional via T.10 Universality candidate.
- Three-source pre-deposit audit closure (see Q32).
- Architecture-lock baselines unchanged. 121 pages (was 120 in v1728; +1 from LHCb bibitem block float).

Full diff: CHANGELOG.md (v1728 → v9 section).

---

## Summary Table

| # | Question | Short answer | Ref |
|---|----------|-------------|-----|
| 1 | Lagrangian? | Balmer stage; action principle open | §19.4 |
| 2 | Numerology? | Out-of-sample + falsifiable + status-labelled | §18.4 |
| 3 | "0 parameters"? | Zero continuous; inputs in Table 2 | Tab 2 |
| 4 | 18 vs 58+? | 18 distinct Tier A; internal deps shown | §1.2 |
| 5 | Why N = 6? | Three primary filters + three corroborating | Thms 2.1–2.3, 2.6 |
| 6 | Why Γ₀? | Unique genus-0 with Div(N) widths | companion X.217 |
| 7 | NCG? | (2,3) from NCG; multiple independent paths | §2.7 + companion |
| 8 | Missing particles? | 2-face = W, H; gluons via colour ramification | §4.9, Tab 3 |
| 9 | Proton? | Unique σ∞-fixed point | Lem 3.5, §3.4 |
| 10 | R²? | Mass scheme stated; R²=0.61 with top-MS̄ | §5.5 |
| 11 | 6π⁵? | Two structural + two auxiliary; H.2a [CONJ] | §8.2 |
| 12 | W₆-odd? | Four routes; X.247c [CONJ HEADLINE] | §7.6 |
| 13 | G? | L1 closed; L1b nuclear input | §9 |
| 14 | ν masses? | Indiv. [CONJ]; block-level [DER cond. ratchet] | §15 |
| 15 | δ_CP? | sin δ = −1 [DER cond.]; kill at \|sinδ\|≠1, >5σ | §13.1, §18.1 |
| 16 | θ₂₃? | Orbit pair {81/145, 64/145}; kill if both >5σ | §12.3, §18.1 |
| 17 | JUNO? | +0.17σ; final σ ~ 0.005 ~2027 | §12.9 |
| 18 | CKM? | 4/4 UST; χ²/dof = 0.65 (dof=3, Rb² excluded) | §11.5 |
| 19 | Denom 13? | Φ₃(d₂) = det M_lep; operator open per Gap 9 | §14, §19.1 |
| 20 | sin²θ_W? | Tree 3/13 [DER]; NLO +1.9σ [OBS] | §14 |
| 21 | RG? | Open; n discrete | — |
| 22 | Paths? | 40+ structural; ≥9 companion clusters | §2.7 + companion |
| 23 | Tower? | Fermat filtration | §6 |
| 24 | (d₁,d₂) selection? | NCG A_F = ℂ⊕ℍ⊕M₃(ℂ); MDL deprecated | §1, §2 |
| 25 | Koide? | 3 vs 12 particles | §17 |
| 26 | Golden bridge? *(companion)* | q₅ = q_φ·q₃ − d₂ | companion X.263 |
| 27 | CRT? *(companion framing)* | Schur eigenvalues in paper | companion X.280 + §12.5 |
| 28 | N=6 golden? *(companion)* | F = 0 unique | companion X.276 |
| 29 | GPT reject? | LLM-assisted QA, not peer review | — |
| 30 | 508 checks? | 17 tiers, 144+56+91+86+131 = 508 | verify/ |
| 31 | Prior art? | Dessins known; LD-new = simultaneous map | §3.7, §17 |
| 32 | v9 audit closure? | 9 Tier-2 closed; baselines preserved | CHANGELOG |
| 33 | v1728→v9 diff? | LHCb, JUNO2025, NuFIT 6.1, audit closure | CHANGELOG |

---

*Version: v9 release (May 2026), updated 17 May 2026 (three-way audit closure of FAQ accuracy/honesty). Based on paper v9 (DOI 10.5281/zenodo.20257066) and companion v9 snapshot. 508/508 Python (17 tiers) + 91/91 Sage carried unchanged from v1728 baseline. 70+ documented dead directions.*
