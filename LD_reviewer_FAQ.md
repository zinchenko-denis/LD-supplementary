# LD Framework — Reviewer FAQ

**Companion document to:** D.D. Zinchenko, "1728: The Standard Model from X₀(6)" (2026).
**Paper:** [DOI 10.5281/zenodo.19520240](https://doi.org/10.5281/zenodo.19520240)
**Code:** [github.com/zinchenko-denis/LD-supplementary](https://github.com/zinchenko-denis/LD-supplementary) — 508/508 Python checks (17 tiers) + 91/91 Sage
**Companion:** LD_proof_companion (post-S291, 1244 theorem headers, 117+ dead directions)

This document anticipates questions that arise on first reading and provides concise answers with precise references. Questions are ranked by frequency from 15+ independent audits (GPT physics/math/experimentalist reviews, adversarial audits S283–S284, cross-verification S287, paper audit S297).

---

## I. The Big Question

### Q1. Where is the Lagrangian? Where are the equations of motion?

This is the most common criticism. The honest answer: there is no Lagrangian. The framework is at the Balmer stage (1885), not the Schrödinger stage (1926).

What exists instead is an *arithmetic* action principle. The L-function L(6.10.a.a, s), evaluated at the four cusps of X₀(6), generates all coupling scales through its values at divisors of N. The tower structure (X.197, X.202) shows that a single modular object — the unique weight-2 newform on the unique genus-0 curve with cusp widths = Div(6) — determines all observables.

The monodromy relation σ₁·σ₀·σ∞ = id is the constraint. The Belyi map β: X₀(6) → ℙ¹ is the solution. The spectrum L(f, s) at cusps yields the physics. This replaces δS/δφ = 0 with arithmetic rigidity.

Balmer's formula was not wrong for 40 years — it was incomplete. We claim to be at the Balmer stage. The review implicitly demands the Schrödinger stage as an entry ticket. We believe this sets the bar at the wrong height for the specific claims we make: zero-parameter numerical predictions that can be falsified.

### Q2. This is numerology. How is it different from number-fitting?

Three criteria distinguish the framework from numerology (§15.3):

1. **Out-of-sample prediction.** sin²θ₁₂ = 4/13 was computed before JUNO's first measurement and is consistent at +0.17σ, while TBM (1/3) is disfavoured at −2.8σ.
2. **Falsifiability.** Five structural kills are catalogued in §14.3, each a genuine risk. The author specifies how to destroy the framework.
3. **Derivation, not fitting.** The 12 identification steps feed a directed acyclic graph of 54+ theorems with no circular dependencies and no adjustable parameters. Every ingredient of the mass formula is derived (§7.6).

Statistical argument: 18 independent rational predictions matching experiment at Σ|pull| < 15σ from 0 continuous parameters has a chance probability p < 10⁻²⁶ (companion B.4).

### Q3. "Zero free parameters" — but Table 2 lists inputs. Is this honest?

Zero *continuous* free parameters. The structural inputs are:

- One dimensionful scale (mₑ)
- One algebraic classification (A_F → (d₁, d₂) = (2, 3))
- Physical identifications (bridges between mathematics and observables)

No parameter is adjusted, fitted, or optimised to match data. Every number is either a theorem (exact rational from the dessin) or a derived quantity. Table 2 enumerates all inputs explicitly — nothing is hidden.

### Q4. "18 predictions" vs "58+ observables" — what's the real count?

18 Tier A: independently derived outputs with distinct derivation chains and no shared free parameters. These are the headline number.

58+ includes downstream quantities (e.g. mass ratios from individual masses), structurally constrained items (e.g. det M_lep = 13 from spectrum), and reformulations (same result from different angles). The independence ledger is in the companion (S267).

---

## II. Why This Curve (§§1–4)

### Q5. Why N = 6?

Three independent filters, each selecting N = 6 uniquely from all positive integers:

- **Theorem 4.2** (cusp–representation): index = 12, exactly 4 cusps, widths = Div(N). Unique among N = 1…100.
- **Theorem 4.3** (index = 2N for squarefree N): (p−1)(q−1) = 2 has unique solution (2, 3).
- **Theorem 4.4** (analytic closure): genus 0 ∧ ν₂ = ν₃ = 0 for squarefree N. Unique among all 85 squarefree genus-0 levels.
- **X.228** (maximality): N = 6 = max{genus 0 ∩ φ(N) ≤ 2}.

No other N passes even one of these filters.

### Q6. Why Γ₀(N) and not Γ₁(N), Γ(N), or Γ₀(N)⁺?

Γ₁(6) = Γ₀(6) since φ(6) = 2. Γ(6) has genus 1 and 12 cusps all of width 6 — fails both genus 0 and cusp-width matching. Γ₀(6)⁺ has index 6 — only 6 edges, insufficient for 12 particles. Complete classification of 19 subgroups at order 12 (X.217) shows Γ₀(6) is unique with genus 0, 4 cusps, widths = Div(N).

### Q7. The input A_F = ℂ ⊕ ℍ ⊕ M₃(ℂ) comes from NCG. What if NCG is wrong?

Only two integers are used: dim(fund SU(2)) = 2 and dim(fund SU(3)) = 3. These are experimental facts. NCG provides one of 44 paths to (d₁, d₂) = (2, 3); the other 43 are independent.

---

## III. The Dessin and Particles (§§5–6)

### Q8. The SM has 17 particles. The dessin has 12 edges. Where are the gluons, Z, and γ?

The dessin encodes pre-EWSB gauge–Higgs content. The 2-face contains W and H. Photon γ and Z arise from W₃–B mixing after EWSB — not independent edges. Gluons are gauge degrees of freedom. Gap 10 (post-EWSB bosons) is open.

### Q9. The proton is composite. Why is it fundamental here?

The proton is the unique stable baryon and the unique σ∞-fixed point (Anchor Lemma 5.5). Its mass enters through μ = mₚ/mₑ. The compositeness is the mechanism by which QCD data enters the framework — not hidden, structural.

---

## IV. Mass Formula and Constants (§§7–9, 12)

### Q10. R² = 0.89 with 10 data points is fragile.

Scheme-specificity is a prediction: pole masses destroy the correlation (R² → 0). MS̄ at μ = 2 GeV are the correct comparison (PDG convention, not a model choice).

### Q11. Is μ₀ = 6π⁵ a coincidence?

Each factor has modular origin: 6 = N; 5 = N−1; π from SL₂(ℝ) hyperbolic metric. NLO C = 10/9 from three routes. Residual < 0.001 ppm. Status: [DER].

### Q12. The W₆-odd selection in α is 1 bit of empirical input.

Correct. W₆-odd gives α⁻¹ = 137.035999202 (−1.2σ); W₆-even excluded at ~2400σ. Both derivations [THM]; selection empirical.

### Q13. G is conditional on nuclear data.

L1 (α, μ) closed within Γ₀(6). L1b (G) requires neutron mass and deuteron binding energy — nuclear physics external to the dessin.

### Q14. Why MS̄ at μ = 2 GeV? Is the scale derivable?

No. The renormalisation scale is not derivable from the dessin — genuine limitation. But μ = 2 GeV is the PDG convention, not a model choice.

---

## V. Mixing Parameters (§§10–14)

### Q15. Does the framework predict CP violation?

Yes. |sinδ| = 1 [THM-arith, X.218]: rationality of |U|² forces cos δ = 0. sinδ = −1 [DER, X.224] from ℍ orientation. DUNE/Hyper-K will test: δ ≠ 270° ± 20° → framework killed.

### Q16. The θ₂₃ octant depends on the dataset.

LD predicts upper octant (sin²θ₂₃ = 81/145) from Catalan's theorem: d₂² > d₁³ (9 > 8). NuFIT has changed the preferred octant three times in five years. DUNE will decide.

### Q17. JUNO +0.17σ is not a "confirmation."

Correct: "consistent at +0.17σ." JUNO final (σ ~ 0.005) will separate 4/13 from TBM at > 5σ.

### Q18. All 4 CKM parameters derived?

Yes, from UST ensemble. χ²/dof = 0.65 (p = 0.58). Bridge: Burton–Pemantle transfer current theorem.

### Q19. Three angles share denominator 13 — coincidence?

Structural: 13 = Φ₃(d₂) = det M_lep. The lepton operator produces this prime.

### Q20. sin²θ_W = 3/13 — tree or MS-bar?

Tree: 3/13 = 0.23077. NLO: (3/13)(1 + (5/3)α/(2π)) = 0.23122, pull +1.9σ.

---

## VI. Structure and Falsification (§§14–18)

### Q21. Is there RG evolution?

Open. Lattice positions n are integers — topological, don't run. Valuable future work.

### Q22. How many of the 44 paths are truly independent?

~12 independent clusters. Between clusters, failure modes are independent.

### Q23. What is the tower and why does it halt?

Tower L(6.10.a.a, k/2+n) for n = 0,1,2,3 (mass, CKM, PMNS, HALT). HALT from Fermat filtration: W₂ = +1 → 3 sectors.

### Q24. MDL axiom — falsifiable?

"Selection criterion" not "axiom." Used once to select ⟨2, 3⟩. After that, pure dessin combinatorics.

### Q25. Koide is more precise for leptons.

Different scope: 3 particles / 1 parameter vs 12 particles / 0 continuous parameters.

---

## VII. New in v1728: Directed Operators and CRT (S288–S291)

### Q26. What is the golden bridge?

q₅ = q_φ·q₃ − d₂ (X.263): the quintic from χ(A_dir) factors through the golden ratio polynomial q_φ = x²−x−1. The golden ratio enters through the orientation operator Ω₃ on the level-3 exact subspace (X.267), with eigenvalues {0, −φ, 1/φ}.

### Q27. What does CRT Grand Unification mean?

L|_{V₆^{ex}} = 3I − A_dir − σ₀⁻¹ (X.280): the Laplacian on the exact-level subspace decomposes into the directed adjacency (containing the golden bridge) and the inverse generator. The Schur complement has eigenvalues {3, 6/5, 8/11} — all LD monomials, det = 144/55 = index²/f₁⁻¹ (X.281).

### Q28. Why is N = 6 unique for the golden bridge?

p = 2 (for ker) AND q = 3 (for deg q_φ = q−1). F(A,Ω) = 0 selects N = 6 among all tested semiprimes (X.276). No variational principle — algebraic rigidity.

---

## VIII. External Audits

### Q29. GPT-physicist gave "reject." Do you agree?

Three independent GPT reviews (S270): physicist (reject on overclaims), mathematician (pass), experimentalist (premature — needs better statistical packaging). All overclaims fixed. Mathematical core passed clean.

### Q30. 508 verification checks — what do they test?

17 tiers from monodromy to observables:

| Tiers | Content | Checks |
|-------|---------|--------|
| t0–t3 | Foundation, monodromy, quantum numbers, spectrum | 93 |
| t4–t5 | CKM, PMNS | 56 |
| t6–t9 | Mass formula, α/μ/G, Gap 3, information | 81 |
| t10–t13 | Weinberg, CP, CR master, tower | 83 |
| t14–t16 | Directed operators, golden bridge, CRT unification | 131 |

Every check starts from O.1 monodromy — no precomputed results. Fraction arithmetic + numpy cross-validation.

---

## Summary Table

| # | Question | Short answer | Ref |
|---|----------|-------------|-----|
| 1 | Lagrangian? | Balmer stage; arithmetic principle | §15.4 |
| 2 | Numerology? | Out-of-sample + falsifiable + derived | §15.3 |
| 3 | "0 parameters"? | Zero continuous; inputs in Table 2 | Tab 2 |
| 4 | 18 vs 58+? | 18 Tier A independent | §1.2 |
| 5 | Why N = 6? | 3+ unique filters | Thms 4.2–4.4 |
| 6 | Why Γ₀? | Unique genus-0 with Div(N) widths | X.217 |
| 7 | NCG? | Only (2,3); 43 other paths | §4 |
| 8 | Missing particles? | Pre-EWSB; Gap 10 | Rem 5.2 |
| 9 | Proton? | Unique anchor | Lem 5.5 |
| 10 | R²? | Scheme = prediction | §7 |
| 11 | 6π⁵? | Structural [DER] | §8 |
| 12 | W₆-odd? | ~2400σ, not derived | §9 |
| 13 | G? | L1 closed; L1b nuclear | §12 |
| 14 | ν masses? | Angles [DER]; masses [CONJ] | §11 |
| 15 | δ_CP? | sinδ = −1; DUNE kills if wrong | §13 |
| 16 | θ₂₃? | Upper; DUNE decisive | §12 |
| 17 | JUNO? | +0.17σ; 2027 decisive | §12 |
| 18 | CKM? | 4/4 UST; χ²/dof = 0.65 | §10 |
| 19 | Denom 13? | Φ₃(d₂) = det M | §14 |
| 20 | sin²θ_W? | Tree 3/13; NLO +1.9σ | §14 |
| 21 | RG? | Open; n discrete | — |
| 22 | 44 paths? | ~12 clusters | §18 |
| 23 | Tower? | Fermat filtration | §16 |
| 24 | MDL? | Used once | §3 |
| 25 | Koide? | 3 vs 12 particles | §3 |
| 26 | Golden bridge? | q₅ = q_φ·q₃ − d₂ | DIR |
| 27 | CRT? | L = 3I − A_dir − σ₀⁻¹ | X.280 |
| 28 | N=6 golden? | F = 0 unique | X.276 |
| 29 | GPT reject? | Overclaims fixed; math clean | S270 |
| 30 | 508 checks? | 17 tiers, O.1 → observables | verify/ |

---

*Version: S300 (April 2026). Based on paper v1728 and companion S291. 508/508 Python (17 tiers) + 91/91 Sage. 117+ dead directions.*
