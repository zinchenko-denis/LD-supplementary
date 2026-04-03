# LD Framework — Reviewer FAQ

**Companion document to:** D.D. Zinchenko, "Discrete Scale Invariance and the Standard Model Mass Spectrum: A Number-Theoretic Framework from X₀(6)" (2026).  
**Paper:** [DOI 10.5281/zenodo.19393365](https://doi.org/10.5281/zenodo.19393365)  
**Code:** [github.com/zinchenko-denis/LD-supplementary](https://github.com/zinchenko-denis/LD-supplementary) (290/290 Python + 91/91 Sage tests)

This document anticipates questions that arise on first reading and provides concise answers with precise references to the paper. It is intended for reviewers, endorsers, and anyone evaluating the framework for the first time.

---

## I. Foundations (§§1–4)

### Q1. Why Γ₀(N) and not Γ₁(N), Γ(N), or Γ₀(N)⁺?

Γ₁(6) = Γ₀(6) since φ(6) = 2 (the only Dirichlet character is trivial). Γ(6) has genus 1 and 12 cusps all of width 6 — it fails genus 0 and cusp-width matching simultaneously. Γ₀(6)⁺ (Atkin–Lehner normaliser) has index 6, giving only 6 edges — insufficient for 12 particles. Among all congruence subgroups at level 6, Γ₀(6) is the unique one with genus 0, exactly 4 cusps, and cusp widths = Div(N) = {1, 2, 3, 6}. See Lemma 4.1 and §15.3 ("Regarding L0").

### Q2. Why N = 6 and not some other level?

Three independent filters, each selecting N = 6 uniquely from all positive integers:

- **Theorem 4.2** (cusp–representation correspondence): index = 12, exactly 4 cusps, widths = Div(N). Unique among N = 1…100 (Sage verified).
- **Theorem 4.3** (index = 2N): the condition (p−1)(q−1) = 2 for N = pq has the unique solution (2, 3).
- **Theorem 4.4** (Path A — analytic closure): genus 0 ∧ ν₂ = ν₃ = 0 for squarefree N. Unique among all 85 squarefree genus-0 levels.

No other N passes even one of these filters.

### Q3. The algebraic input A_F = ℂ ⊕ ℍ ⊕ M₃(ℂ) comes from NCG. What if NCG is wrong?

The only information extracted from A_F is two integers: dim(fund SU(2)) = 2 and dim(fund SU(3)) = 3. These are experimental facts of the Standard Model — they do not require the NCG spectral action, the Λ-cutoff, or any other NCG-specific machinery. NCG provides one of 44 paths to (d₁, d₂) = (2, 3); the other 43 paths (§13) are independent of NCG.

### Q4. The MDL axiom is not falsifiable.

Agreed. "Axiom" is a misnomer; "selection criterion" or "heuristic principle" is more accurate. MDL selects the generator pair ⟨2, 3⟩ from 36 tested pairs (Theorem 3.2). After this single use, B₁ follows from the Hecke orbit of K = 1 at diameter 3 (Theorem 4.6) — pure mathematics, no further appeal to MDL. The framework does not stand or fall with MDL: it is one of many paths to ⟨2, 3⟩.

### Q5. "Zero free parameters" — but Table 4 lists 12 inputs.

Zero *continuous* free parameters. The 12 items in Table 4 are: one dimensionful scale (mₑ), one algebraic classification (A_F), one family postulate (Γ₀), one external coupling (αₛ), three discrete selections from finite sets, and five physical identifications (postulated bridges). Every item is enumerated explicitly; no hidden inputs exist. The claim is that no continuous dial is turned to fit data — not that the framework has no structural content.

---

## II. The Dessin (§§5–6)

### Q6. Why are edges identified with particles, rather than vertices?

The dessin has 10 vertices (4 BV + 6 WV) and 12 edges. Vertices cannot carry full particle identity: each black vertex hosts 3 particles that it cannot distinguish (the σ₀-orbit). Edges are the minimal objects carrying a unique triple (BV, WV, Face) with zero collisions (Theorem 5.13, dessin-address theorem). The complete derivation chain σ∞ → face → ε, η → n, ℓ, K (§6.8, Figure 3) exists only for edges. No analogous chain exists for vertices.

### Q7. The SM has 17 particles (12 fermions + 4 gauge bosons + Higgs). The dessin has 12 edges. Where are the gluons, Z, and γ?

The dessin encodes the pre-EWSB gauge–Higgs content. The 2-face contains exactly 2 edges, identified with W and H. The photon γ and Z boson arise from W₃–B mixing after electroweak symmetry breaking and do not appear as independent edges. The 8 gluons are gauge degrees of freedom, not matter fields; the dessin encodes the Yukawa (matter + Higgs) spectrum. A constructive derivation of the 4 post-EWSB electroweak bosons from 2 dessin edges is acknowledged as open (Gap 10, Remark 5.2).

### Q8. The proton is a composite particle. Why does it serve as the anchor of a fundamental structure?

The proton is the unique stable baryon and the unique σ∞-fixed point of the dessin (Anchor Lemma 5.5). Its mass enters through μ = mₚ/mₑ, which requires QCD (αₛ is an external input, Table 4 #4). The hierarchy is explicit: L1 precision (α, μ) is closed within Γ₀(6); L1b (G) requires nuclear data. The proton's compositeness is not hidden — it is the mechanism by which QCD data enters the framework. Mesons and other baryons lie outside the scope: the dessin encodes the 12-particle Yukawa spectrum, not the full hadron spectrum.

---

## III. The Mass Formula (§§7–8)

### Q9. R² = 0.89 with 10 data points is fragile. How sensitive is it to αₛ?

Remark 7.5 addresses this directly. Substituting pole masses (which absorb αₛ running differently) for c and b quarks destroys the correlation: R² → 0. This scheme-specificity is a prediction: the dessin encodes Lagrangian-level Yukawa couplings, not QCD-dressed propagators. MS̄ current masses at μ_MS = 2 GeV — the fundamental parameters of the QCD Lagrangian — are the correct comparison. Varying all quark masses within ±1σ gives R² ∈ [0.63, 0.77] (NLO), confirming robustness against experimental uncertainties.

### Q10. Is μ₀ = 6π⁵ a numerical coincidence?

Each factor has a modular origin: 6 = N (uniquely selected by Theorems 4.2–4.4); 5 = N − 1 = index/2 − 1 (degree of the Hauptmodul minus 1); π enters from the SL₂(ℝ)-invariant hyperbolic metric (vol(Γ₀(6)\H) = 4π by Gauss–Bonnet). The neutron β-decay phase space factor f(Q/mₑ) = 1.636 ≠ 6π⁵ — this is not the Lenz derivation from beta decay, but a structural embedding in modular arithmetic. NLO coefficient C = 10/9 is derived from three independent routes (Theorem 8.1). NNLO series from Riemann–Roch dimension formulas (Theorem 8.2). Combined residual: < 0.001 ppm. Status: [DER].

### Q11. Why MS̄ at μ = 2 GeV? Is the renormalisation scale derivable?

No — the renormalisation scale is not derivable from the dessin. This is a genuine limitation. The dessin encodes the Yukawa structure at the Lagrangian level; QCD running is external physics. However, μ_MS = 2 GeV is the standard PDG convention for light quark masses, not a choice made by the model. The model is *compatible* with this convention; it does not select it.

---

## IV. Fundamental Constants (§§9, 12)

### Q12. The cos²(1/(Nπ)) factor: is ϕ(w) = 1/(πw) unique?

The QTC chain (§9.3, Theorem 9.3) derives cos²(1/(Nπ)) in 5 steps. The intensive phase ϕ(w) = 1/(πw) is called "Fricke-canonical" — the unique assignment giving integer phase differences mᵢⱼ ∈ {0, …, N−1} with minimal range. A strict uniqueness proof ruling out all alternatives (e.g., ϕ = c/(πw) for c ∈ ℤ) is not provided. The paper marks this: "two physics inputs enter" (Step 4 phase assignment, Step 5 Born rule). Status: [DER] with two standard physics inputs, not [THM].

### Q13. The W₆-odd selection in the α formula is 1 bit of empirical input.

Correct. The Grothendieck splitting (Theorem 9.4) produces exactly two candidates: W₆-odd (α⁻¹ = 137.035999202, pull −1.2σ) and W₆-even (α⁻¹ = 137.035948904, excluded at ~2400σ). The mathematical derivation of both candidates is [THM]. The selection of odd over even is confirmed empirically at ~2400σ but not derived from a principle. The paper states this explicitly: "one binary empirical input (1 bit)."

### Q14. G is conditional on nuclear data — not a closed derivation.

Correct. The formula G = e²/(ε₀ m²ₑ α⁻²ᑫ) with q = 1/(α²μ_G) requires μ_G, which depends on the neutron mass mₙ and deuteron binding energy B_d — nuclear data external to Γ₀(6). The ring is closed at L1 (α, μ: derived from Γ₀(6) alone) but open at L1b (G: requires nuclear physics). §12.4 states this explicitly. G is a forward prediction given nuclear data, not a self-contained derivation.

---

## V. Mixing Parameters (§§10–11)

### Q15. Are all 4 CKM Wolfenstein parameters derived?

Yes. All four arise from the uniform spanning tree (UST) ensemble of the dessin's bipartite graph (§10):

| Parameter | LD value | Pull | Source |
|-----------|----------|------|--------|
| λ | 9/40 = 0.22500 | −0.04σ | Residual Tree Theorem 10.1 |
| A | 3/√13 = 0.83205 | +0.63σ | √(P_triple / (ΔP + P_triple)) |
| γ | arctan(9/4) = 66.04° | −1.25σ | arctan(P_triple / ΔP) |
| R_b | √(3/20) = 0.38730 | +0.17σ | √(N/K) |

χ²/dof = 0.66 (p = 0.58). The physical bridge is the transfer current theorem (Burton–Pemantle 1993): P(edge ∈ UST) = effective resistance. Status: [DER] — every graph quantity is [THM]; the sole non-mathematical ingredient is the identification of UST probabilities with CKM parameters.

### Q16. PMNS angles are [DER], but neutrino masses are [CONJ]. Is this clear enough?

The three PMNS angles are derived from projective invariants of the Hauptmodul with Σ|pull| = 0.27 (§11.3–11.5). Neutrino masses use 6 discrete inputs to predict 3 observables — formally overfit (§11.9 honest caveat: "conjecture with plausible inputs, not prediction"). Table 3 marks angles as [DER] and masses are discussed separately in §11.9 with [CONJ] status.

### Q17. The PMNS matrix is real (δ_CP = 0 or π). What if CP violation is confirmed?

T2K and NOvA have hints of δ_CP ~ −π/2. If nonzero δ_CP is confirmed at > 5σ, the model requires extension (a complex phase from the dessin). This would be an extension, not a kill — the paper does not predict δ_CP = 0 as a structural kill condition. The three mixing angles and the five structural kills (§14.3) are independent of δ_CP.

### Q18. The θ₂₃ octant prediction depends on the dataset.

LD predicts sin²θ₂₃ = 81/145 (upper octant), a consequence of d₂² > d₁³ (Catalan/Mihailescu: 9 > 8). NuFIT 6.0 IC19: +0.16σ. IC24+SK prefers lower octant at some tension. The experimental situation is unsettled — NuFIT has changed the preferred octant three times in five years. The LD prediction is fixed; the decisive experiments are DUNE and Hyper-Kamiokande.

---

## VI. Falsifiability and Honest Assessment (§§14–15)

### Q19. The Koide formula (Q = 2/3) for charged leptons is more precise (0.58%) than LD (Q = 0.671, deviation 0.73%). Why does LD perform worse on this specific test?

LD does not use or target the Koide relation. The two frameworks give different numbers for the charged-lepton mass ratio; one of them is incorrect. Koide applies to 3 leptons with 1 parameter; LD covers 12 particles with 0 continuous parameters. This is a trade-off between precision on one observable and coverage across the full spectrum.

### Q20. JUNO +0.17σ is not a "confirmation."

Correct. The accurate statement is: "consistent at +0.17σ" and "the most precise existing prediction for the solar mixing angle." The word "confirmed" at current precision (σ = 0.014) is premature. JUNO's final measurement (expected ~2027–28, σ ~ 0.005) will be decisive: it will separate 4/13 = 0.30769 from the tribimaximal value 1/3 = 0.33333 at > 5σ.

### Q21. There is no discussion of RG evolution. Is the lattice compatible with running?

This is an open question. The lattice is defined at fixed scales. SM running modifies masses and couplings, but lattice positions n are integers — they are topological (graph-theoretic) quantities, not energy-dependent. The mass residuals δK may acquire scale dependence, but n, ℓ, and K are discrete and do not run. A full RG compatibility analysis has not been performed and would be valuable future work.

### Q22. How many of the 44 paths are truly independent?

§13.2 gives a conservative count of ~11 independent clusters. Within each cluster, paths share mathematical infrastructure. Between clusters, failure modes are independent: a flaw in spanning-tree combinatorics (cluster 2) would not affect the moonshine identity (cluster 6) or the scattering matrix values (cluster 7). The abstract states "44 converging paths... clustering into 11 independent groups." The next-best candidate ⟨3, 13⟩ passes at most 4 of 44 tests.

### Q23. Is this numerology?

Three criteria distinguish the framework from number-fitting (§15.3):

1. **Out-of-sample prediction.** sin²θ₁₂ = 4/13 was computed before the first JUNO measurement and is consistent at +0.17σ, while the tribimaximal value 1/3 is disfavoured at −2.8σ.
2. **Falsifiability.** Five structural kills are catalogued in §14.3, each a genuine risk. The author specifies how to destroy the framework.
3. **Internal consistency.** The 12 identification steps feed a directed acyclic graph of 54 theorems with no circular dependencies and no adjustable couplings. Every ingredient of the δK formula is derived (§7.6, [DER]).

What is missing is not a derivation but an action principle — dynamics, not predictions. The framework is in the position of Balmer's formula (1885): fully predictive but awaiting its Schrödinger equation.

---

## Summary Table

| # | Question | Short answer | Paper reference |
|---|----------|-------------|-----------------|
| 1 | Why Γ₀? | Unique: genus 0, widths = Div(N) | Lemma 4.1, §15.3 |
| 2 | Why N = 6? | 3 independent filters, each unique | Thms 4.2–4.4 |
| 3 | NCG dependence? | Only (2,3) used; 43 other paths exist | §4.1, §13 |
| 4 | MDL falsifiable? | Heuristic, not axiom; used once | §3.1 |
| 5 | "Zero parameters"? | Zero continuous; 12 structural listed | Table 4 |
| 6 | Why edges? | Unique carrier of full identity | Thm 5.13 |
| 7 | Missing particles? | Pre-EWSB; Gap 10 open | Remark 5.2 |
| 8 | Proton composite? | Unique stable baryon = anchor | Lemma 5.5, §12.4 |
| 9 | R² fragile? | Scheme = prediction; robust ±1σ | Remark 7.5 |
| 10 | 6π⁵ coincidence? | Structural embedding; [DER] | §8.1–8.3 |
| 11 | Why μ_MS = 2 GeV? | PDG convention; not derivable | §7, Remark 7.5 |
| 12 | cos² unique? | [DER] with 2 physics inputs | §9.3 |
| 13 | W₆-odd = 1 bit? | Confirmed ~2400σ, not derived | §9.4 |
| 14 | G conditional? | L1 closed; L1b needs nuclear | §12.4 |
| 15 | CKM all [DER]? | Yes, 4/4 from UST, χ²/dof = 0.66 | §10 |
| 16 | ν masses overfit? | Angles [DER]; masses [CONJ] | §11.9 |
| 17 | δ_CP = 0? | Extension, not kill | §11 |
| 18 | θ₂₃ octant? | Upper; Catalan theorem; DUNE decisive | §11.4 |
| 19 | Koide better? | Different scope: 3 vs 12 particles | §3 |
| 20 | JUNO "confirmed"? | Consistent; final ~2027 decisive | §11.8 |
| 21 | RG compatible? | Open; n discrete, doesn't run | future work |
| 22 | 44 paths independent? | ~11 clusters; conservative | §13.2 |
| 23 | Numerology? | Out-of-sample + falsifiable + derived | §14–15 |

---

*Document version: S218 (April 2026). Based on paper v8 (DOI 10.5281/zenodo.19393365) and proof companion S217.*
