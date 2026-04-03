# LD PROOF COMPANION
# Version: post-S217 (2026-04-02, S207–S217: Gap 9(γ₂) attack. X.103 28-dim family [THM-comp]. X.104 NO-GO ℤ[Mon] [THM-arith]. X.107–X.110c face-cyclotomic results [THM-arith]. X.111–X.113a irreps blind to PMNS [THM-comp]. X.115–X.117 circulant obstruction + rationality theorem [THM-arith/comp]. X.118a–X.119d operator M exists, two families, symbolic Schur [THM-comp]. X.120–X.126 seesaw anatomy: Gram identity, anchor invisibility, mediator triangle, UST [THM-arith/comp]. X.128 unified face-pair construction [THM-comp]. X.129 index formula sin²θ₁₃=index/(N·∏Φ₃) [THM-arith]. X.129a–d GN↔PMNS + cyclotomic unification [THM-arith/OBS]. I.4 [CONJ→DER] (X.129+X.130). Gap 3 CLOSED (was incorrectly listed open). ERRATUM: v=U_CR^T·(1,1,1) basic S215 false. 90+ dead. Audited S217 with errata E1–E4.)
# Previous: post-S205 (S204–S205: X.99–X.102, CR→PMNS [DER], two-scale structure. S202–S203: periods, QTC. S195–S201: Gap 3 [OBS]→[DER] via X.97. S190–S194: spectral bridge, t [DER]. S189: DESSIN PRIMACY)
# Author: Denis D. Zinchenko
# Assembled by: Claude (from session logs S42–S100, S125–S153, paper v5.5, context files)
# Purpose: Self-contained reference for all LD theorems, derivations, observations
# License: CC BY 4.0 (same as paper)

---

# NOTATION AND CONVENTIONS

| Symbol | Value | Meaning |
|--------|-------|---------|
| N | 6 | Level of Γ₀(N) |
| d₁ | 2 | dim fund SU(2) |
| d₂ | 3 | dim fund SU(3) |
| index | 12 = 2N | [SL₂(ℤ) : Γ₀(6)] |
| ∏wᵢ | 36 = 1·2·3·6 | Product of cusp widths |
| j(i) | 1728 = (2N)³ | j-invariant at τ = i |
| dim M_k | dim M_k(Γ₀(6)) | Space of weight-k modular forms |
| dim S_k | dim S_k(Γ₀(6)) | Space of weight-k cusp forms |
| L | 7 = N+1 | Lattice boundary |
| |B₁| | 10 | Cardinality of multiplier set |
| C | 10/9 | NLO coefficient |
| mₑ | 0.51099895 MeV | Electron mass (CODATA 2018) |
| μ | 1836.15267343 | Proton-to-electron mass ratio |
| g | μ^{1/4} = 6.5460180326 | Lattice base |
| α⁻¹ | 137.035999177(21) | Fine structure constant (CODATA 2022) |

**Convention:** All σ-pulls quoted as **(exp − theory)/σ** throughout this document.

Epistemic markers:
- **[THM]** = Sage/analytically verified theorem
  - **[THM-arith]** = arithmetic/algebraic identity verified by substitution (subset of [THM])
  - **[THM-comb]** = combinatorial fact on finite graph, verified by exhaustive search (subset of [THM])
  - **[THM-math]** = general mathematical theorem (not specific to N=6 graph)
  - **[THM-cond]** = theorem conditional on physical identification step
- **[DER]** = Derived with ≤1 selection criterion
- **[DER cond.]** = Conditionally derived (depends on δK formula or empirical masses)
- **[OBS]** = Motivated pattern, not proven
- **[CONJ]** = Conjecture with empirical support
- **[DEAD]** = Closed direction
- **[FITTED]** = Fitted with structural coefficients

Dual markers (e.g. **[THM-arith / CONJ]**): the numerical content is [THM], the physical identification is [CONJ]. See §I.25 for the precise logic frame.

---

# O. MONODROMY — SINGLE SOURCE OF TRUTH

## [THM-comb] O.1: Unique Monodromy of X₀(6) Dessin
Source: S112
Status: [THM-comb] (exhaustive search: 1/480 candidates)
Dependencies: C.1 (dessin structure), F.7 (face triples)
Verified: Python (MCT 12/12, |Mon|=72, spectrum=I.6, face triples=F.7)

### Statement

The monodromy triple of the X₀(6) dessin, with particle labels fixed by F.7 face triples, is **unique**:

```
σ∞ = (c u b s d t)(e τ μ)(W H)(p)     type (6,3,2,1)
σ₁ = (u t)(c p)(b μ)(d e)(s W)(τ H)   type (2⁶)
σ₀ = (c u p)(b t e)(s μ H)(d W τ)     type (3⁴)
```

### Verification (MCT = Monodromy Closure Test)

σ₁·σ₀·σ∞ = id verified for all 12 edges:
c→u→p→c ✓, u→b→t→u ✓, p→p→c→p ✓, b→s→μ→b ✓, t→c→u→t ✓, e→τ→d→e ✓,
s→d→W→s ✓, μ→e→b→μ ✓, H→W→τ→H ✓, d→t→e→d ✓, W→H→s→W ✓, τ→μ→H→τ ✓.

### σ₀-orbits (BV labels)

| BV | σ₀-orbit | Label | Composition | Σn | Σℓ |
|----|----------|-------|-------------|:--:|:--:|
| BV₀ | (c → u → p) | **anchor** | 2Q + A | 9 = d₂² | 6 = N |
| BV₁ | (b → t → e) | **index** | 2Q + 1L | 12 = index | 13 = d₁²+d₂² |
| BV₂ | (s → μ → H) | **star** | 1Q + 1L + 1B | 12 = index | 11 = dim M₁₀ |
| BV₃ | (d → W → τ) | **other** | 1Q + 1B + 1L | 11 = dim M₁₀ | 16 = d₁⁴ |

### σ₁-pairs (WV labels)

| WV | σ₁-pair | BV—BV | Role | n+n' | ℓ+ℓ' |
|----|---------|-------|------|:----:|:----:|
| A | {u, t} | anc—idx | **Bridge** (FORCED in all spanning trees) | 8 = d₁³ | 6 = N |
| B | {c, p} | anc—anc | **Multi-edge** (one per spanning tree) | 8 = d₁³ | 3 = d₂ |
| C | {b, μ} | idx—star | Interior | 8 = d₁³ | 10 = |B₁| |
| D | {d, e} | idx—oth | Interior (contains √2 anomaly) | 1 | 10 = |B₁| |
| E | {s, W} | star—oth | **Far-end** (competing pair) | 9 = d₂² | 9 = d₂² |
| F | {τ, H} | star—oth | **Far-end** (competing pair) | 10 = |B₁| | 8 = d₁³ |

### Key derived quantities

| Quantity | Definition | Value |
|----------|-----------|-------|
| anchor | unique σ∞-fixed point | **p** |
| pre_anchor | σ₀⁻¹(anchor) | **u** |
| σ₁(anchor) | | **c** |
| T³(σ₁(anchor)) | half-rotation of c in 6-cycle | **s** → BV_star = BV₂ |
| Aut(G) | undirected Cayley graph automorphisms | **⟨(c↔p)⟩**, |Aut| = 2 |

### Proof of uniqueness

480 candidates = 240 σ∞-orderings of the 6-cycle × 2 options for the ambiguous lepton-quark pair. Requirements: (a) σ₁·σ₀·σ∞ = id; (b) σ₀ cycle type (3,3,3,3); (c) F.7 face-triple consistency (12/12). Exactly 1 candidate survives. [S112]

### Automorphism proof

Only c and p have non-distinct neighbor multisets: nbrs(c) = {u, p, p}, nbrs(p) = {c, c, u}. All other 10 vertices have 3 distinct neighbors. The swap (c↔p) preserves all adjacencies. |Aut(G)| = 2. Undirected operator rank = 11 (not 12).

### RULE: MCT (Monodromy Closure Test)

Any companion section using σ₁-partner NAMES (not just Fσ₁) must cite §O.1 and be verifiable against the permutations above. Fσ₁ (face size of partner) is preferred over partner names when possible (immune to label errors).


---

# A. FOUNDATION: N = 6 AND (d₁, d₂) = (2, 3)

## A.0: DESSIN PRIMACY (S189)
Status: Methodological principle (BARRIER-level)

### Statement
All physical quantities of the LD model (masses, mixing angles, coupling constants) are encoded in the combinatorial and spectral data of the dessin d'enfant of X₀(6). The work of the model is decipherment, not derivation from external principles.

### Operational consequence
The starting point of any investigation is the dessin X₀(6). External ideas are admissible, but the first step is reformulation in the language of the dessin (σ₁/σ₀/σ∞, spectrum of L, Cayley graph, UST, modular forms of Γ₀(6)). If reformulation is impossible in principle — do not invest. If reformulation is possible — compute from the dessin.

The criterion is not "is the connection visible in advance" (it often isn't — spanning trees → CKM was not obvious before S138), but "where does the construction start": from dessin data, or from an imported external framework?"

### Empirical basis
194 sessions, 67+ dead external directions, 0 dead internal decipherments. Every breakthrough of the model came from the structure of the dessin: masses from σ∞-cycles (F.3), mixing from Cayley spectrum (I.6), coupling from Eisenstein values (H.1), CKM from spanning trees (E.8), PMNS from Schur complement (I.11) and heat kernel (I.17), NLO corrections from σ₁-face function h (G.0b).

### Scope
DESSIN PRIMACY is an empirical generalization, not a mathematical theorem. It can be falsified if a non-dessin construction proves necessary. Current evidence strongly favors it.


## [THM] A.1: Uniqueness of N = 6 (three filters)
Source: Paper §4, Thm 4.2–4.6
Status: [THM]
Dependencies: A_F = ℂ⊕ℍ⊕M₃(ℂ) (fixes d₁=2, d₂=3 → N=6); **choice of Γ₀(N) family** (L0 postulate)
Verified: Sage (exhaustive scan N = 1..100)

### Scope caveat
All three filters below prove uniqueness **within** the Γ₀(N) family. The choice of Γ₀ over Γ₁ or Γ(N) is motivated by Lemma 4.1 of the paper (Γ₀ is unique with genus 0 and cusp widths = Div(N) at level 6) but not derived from first principles. This is part of the L0 postulate (see §H.5).

### Statement
N = 6 is the unique positive integer satisfying any ONE of the following:
1. **Cusp-representation correspondence:** Cusp widths of Γ₀(N) = {1, d₁, d₂, N} = Div(N), AND index = 12, AND 4 cusps.
2. **Index = 2N:** [SL₂(ℤ) : Γ₀(N)] = 2N. Equivalently, (p−1)(q−1) = 2 for N = pq with p < q prime.
3. **Path A (analytic closure):** N squarefree, genus 0, ν₂ = ν₃ = 0.

### Proof of Filter 2
For N = pq (p < q primes): index = (p+1)(q+1). Condition (p+1)(q+1) = 2pq gives pq − p − q + 1 = pq, hence (p−1)(q−1) = 2. Factor 2 = 1·2: p−1 = 1, q−1 = 2 → (p,q) = (2,3). ∎

### Proof of Filter 3
For Γ₀(N) squarefree: g = 1 + index/12 − ν₂/4 − ν₃/3 − #cusps/2. With g = 0, ν₂ = ν₃ = 0: index = 6(#cusps − 2). For N = pq: #cusps = 4, so index = 12 = 2N → N = 6. ν₂ = ∏_{p|N}(1+(−4/p)) = (1+0)(1+(−1)) = 0 ✓. ν₃ = ∏_{p|N}(1+(−3/p)) = (1+(−1))(1+0) = 0 ✓. Sage: unique among squarefree N ≤ 100. ∎

### Key numbers
index = 12, #cusps = 4, genus = 0, ν₂ = ν₃ = 0, widths = {1,2,3,6}

### Connection to paper
Paper §4, Theorems 4.2–4.6.


### [THM-analytic] A.1a: Bootstrap invariant — ring selects N=6 with 10⁴³ separation (S107)

Define B(N) := ι(N)·δ(N)/π · cos²(1/(Nπ)), M(N) := N·π^{N−1}, F(N) := B(N)²·ln B(N)/M(N), where ι = index, δ = ∏_{d|N} d. Physical target: ξ := ½ ln(C₀/G_N) = 50.33. The ring equation G(N) = G_Newton is equivalent to F(N) = ξ, with amplification lg(G/G_N) = (2ξ/ln 10)·(1 − F/ξ), A = 43.72.

**Uniqueness.** For all N ∈ ℤ₊: |F(N)/ξ − 1| < 0.023 ⟺ N = 6. Proof: finite check N=2..500, asymptotic bound N≥30 via τ(N)=O(N^ε) (Hardy-Wright Thm 315). F(6)/ξ = 1.0012; nearest competitor N=24 with F/ξ=1.207 (gap 177×, corresponding to 10⁹ in G).

| N | B(N) | M(N) | F/ξ | lg(G/G_obs) |
|---|------|------|-----|-------------|
| 5 | 9.51 | 487 | 0.008 | +43.4 |
| **6** | **137.12** | **1836** | **1.001** | **−0.05** |
| 7 | 17.79 | 6730 | 0.003 | +43.6 |
| 24 | 5.07M | 6.5T | 1.207 | −9.1 |

**Family comparison.** Among {Γ₀, Γ₁, Γ, Γ₀⁺}: only Γ₀(N) has a bootstrap fixed point. Γ(N) fails: all cusp widths = N, ∏w ~ exp(N²·ln N) overwhelms M ~ exp(N·ln π). Γ₀(N)+: index/2^{ω(N)} too small (B=34.3 at N=6). Γ₁(6) = Γ₀(6) trivially (φ(6)=2). [THM-computational, S107]

**Scope.** ABD applies ONLY to level selection. Internal scan: signs, BVP, loop dimension, PMNS, IR coefficients, c_n series — none benefit from ring amplification.

**Caveat.** The amplification identity is algebraically exact but tautological: F(N)=ξ restates G(N)=G_N in log-form. The value lies in the uniqueness scan, not in the identity itself. Ring convergence is by Newton's method, NOT Banach contraction (see H.3a, X.15).


## [THM] A.2: (p−1)(q−1) = 2
Source: Paper §4, Thm 4.4

### Proof
Factor 2 = 1·2 with p−1 ≥ 1: p = 2, q = 3. Both prime. ∎


## [OBS/DER] A.3: ≥44 paths to (d₁, d₂) = (2, 3)
Source: Compiled S73 §11, updated S99–S132

| # | Test | Status |
|---|------|--------|
| 1 | (p−1)(q−1) = 2 | [THM] |
| 2 | Genus 0 + ν₂=ν₃=0 squarefree | [THM] |
| 3 | 10/10 δK signs (Sign Window) | [THM] |
| 4 | C₂f·C₂f = 1 (unit Casimir) | [THM] |
| 5 | φ(N) = 2 | [THM] |
| 6 | BIC minimum at ⟨2,3⟩ | [THM] |
| 7 | Isospin universality r = 3 | [THM] |
| 8a | d₁+d₂ = 5 (BVP D⁴ well-posedness) | [THM] |
| 8b | 1+d₂ = d₁² (Residual Tree identity) | [THM] |
| 9 | L(fᵢ)/L(fⱼ) = d₁ˢ, d₂ˢ | [THM] |
| 10 | σ²(B) = {N,N−1,d₁,1} | [THM] |
| 11 | Σℓ Diophantine: 39 = d₂(d₁²+d₂²) | [DER] |
| 12 | C identity ONLY (2,3) | [DER] |
| 13 | col_sums ∩ B₁ → unique | [DER cond.] |
| 14 | ℓ-equipartition 13 = d₁²+d₂² | [OBS] |
| 15 | Φ(d₁²) = j(i)/(d₂²L); d₁^{2d₁−1}=8 | [THM] |
| 16 | b₀(n_f=d₂) = d₂² (QCD) | [THM] |
| 17 | D₀ unique 10/10 twist | [DER cond.] |
| 18 | Kirchhoff = |B₁|·d₁² ∧ residual = d₂² | [THM] |
| 19 | λ_CKM = d₂²/[2d₁²(d₁+d₂)] at −0.04σ | [DER] |
| 20 | Catalan: |d₂²−d₁³|=1 ⟺ (2,3) (Mihailescu) | [THM] |
| 21 | Moonshine: T_{6E} = t₆+5 (Monster class 6E) | [THM] |
| 22 | Cross-duality: p²−p+1|_{d₁} = d₂ (scattering) | [THM] |
| 23 | Schur discriminant = 26² = (d₁·det M_lep)² | [THM] |
| 24 | Schur eigenvectors = LD monomials (−L, d₁, N−1) | [THM] |
| 25 | Irrep localization: P₂ = N−1 (moment theorem) | [THM] |
| 26 | S₃ polarization: Σλ·w₊ = |B₁|, Σλ·w₋ = d₁³ | [THM-arith] |
| 27 | E₂* variational: E₂*(τ)=0 ∧ j≠0 → τ=i unique on X₀(6) | [THM] |
| 28 | j(i)+N factorization: j/N+1 = (index+d₁+d₂)² iff d₁=2 | [THM] |
| 29 | 137 = index·Σ(1/K): factors as d₁·(d₁−2)·(...) = 0 | [THM] |
| 30 | |d₁−d₂| = 1 iff d₁=2 (lemma from Catalan, not independent) | [THM] |
| 31 | d₁+(N−1)² = d₂³ (commutator mixing formula, I.29) | [THM-arith] |
| 32 | Cuspal regulators: ∫η = −2π ln(w_c), mechanism via K₂-theory (R.1–R.3) | [THM] |
| 33 | Cayley–Hecke trace: Tr(A·T_p) = (p+1)−2χ₋₃(p), unique N=6 (Q.1) | [THM-comb] |
| 34 | Reciprocal cusp: ε(w) cubic root 1/d₂ iff d₂=d₁+1 (S.1) | [THM-arith] |
| 35 | V₂ cipher det = −(N²−N+1) = −31, cross-duality chain (S.7) | [THM-arith] |
| 36 | Palindromic UST edge probabilities ΔP = {1/5, 1/10, 1/5} (V.2) | [THM-comb] |
| 37 | CKM-PMNS complementarity A² + sin²θ₁₂ = 1 from UST (V.6) | [THM-arith] |
| 38 | η-quotient R = 0 at t₆ ∈ {−d₂², −d₁³}, Catalan via modular function (W.1) | [THM-arith] (#20 alt) |
| 39 | Tutte polynomial T(d₁,d₂) = index² = 144 for face graph (X.68) | [THM-arith] |
| 40 | Bipartite-Cayley spectral bridge: 4 identities (L²+d₂=d₁²·det_M, L²+d₁·det_M=d₂·(N−1)², det_M=(Δ₁+Δ₂)/2, det(M^{μτ})=disc_φ), common root d₁=2 (S192/S193) | [THM-arith] |
| 41 | Φ₃ cyclotomic recurrence: d₁·Φ₃(d₁)−1 = Φ₃(d₂) ⟺ d₁=2 (X.99, S204) | [THM-arith] (#30 alt) |
| 42 | Cross-ratio characterization: CR(j=0,q,l,b) = d₁/d₂ on Hauptmodul ℙ¹ (X.100, S204) | [THM-arith] |
| 43 | d₂⁴+d₁⁶ = index²+1 ⟺ d₁=2 (X.101a, S204) | [THM-arith] |
| 44 | Cross-exponent: d₂^{d₁}−d₁^{d₂} = 1 ⟺ Catalan + CRT duality (X.102a, S205) | [THM-arith] (#20 alt) |

No other pair survives more than 4 tests. ≥44 paths in 11 clusters (paths #38, #41, #44 = reformulations, not independent).

### Independence analysis (11 clusters)
Not all paths are fully independent. They cluster into ~11 groups sharing common inputs:

| Cluster | Paths | Shared input |
|---------|-------|-------------|
| **Pure number theory** | 1, 2, 5, 20, 30, 41 | Properties of N=6 as integer, consecutive, Catalan, Φ₃ |
| **Ramification/j-geometry** | 3, 8, 10, 15, 16, 17, 18, 27, 28, 32, 34, 36, 37, 42, 43 | j-map structure, ν₂=ν₃=0, UST, Hauptmodul |
| **B₁ algebra** | 4, 6, 7, 11, 12, 29 | Generator lattice ⟨2,3⟩, K-cipher |
| **L-functions** | 9 | η-product Hecke relations |
| **Physical data** | 13, 14, 19 | Empirical masses or CKM |
| **Sporadic groups** | 21 | Monster representation theory |
| **Automorphic (scattering)** | 22, 35 | Scattering matrix / cross-duality p²−p+1 |
| **Effective Laplacian** | 23, 24, 25, 26, 31 | Schur complement / Cayley graph |
| **Cayley×Hecke** | 33 | Monodromy-Hecke interaction on P¹(ℤ/6ℤ) |
| **Graph polynomials** | 39 | Tutte polynomial of face graph (S178) |
| **Bipartite-Cayley bridge** | 40 | Spectral bridge identity BB^T+ΠLΠ^T=2d₂I (S192/S193) |

Within each cluster, paths share assumptions and could fail together. Between clusters, failure modes are independent. Conservative count: **~11 independent lines of evidence**.

Path 32 arrives at the same uniqueness condition (ν₂ = ν₃ = 0, R.7) through K₂-regulators and Bloch–Wigner theory — a different mathematical domain from dimension formulas, but the same discriminating filter.


---

# B. THE SET B₁

## [DER] B.1: MDL → ⟨2,3⟩ generators (Thm 3.2)
Source: Paper §3
Dependencies: MDL axiom (defined below)
Verified: Sage (36 pairs)

### MDL axiom
**Minimum Description Length** (Rissanen 1978, Grünwald 2007): Nature minimises the algorithmic complexity of the mass spectrum. This is a **philosophical selection principle**, not a theorem. It serves as the sole non-geometric axiom of LD. Operationally: generators ⟨p,q⟩ are ranked by BIC (Bayesian Information Criterion) over all 10 non-anchor particle fits.

### Statement
Among 36 generator pairs ⟨p,q⟩ (p,q prime ≤ 23), ⟨2,3⟩ uniquely matches 10/10 particles within 6%. BIC = −49.3 vs second-best −26.2 (23-bit gap).

## [THM] B.2: R = 3 sharp (Thm 3.3)
Source: Paper §3

### Statement
BIC uniquely minimised at R = 3 in ⟨2,3⟩ lattice.

## [THM] B.3: Hecke orbit = B₁\{√2} (Thm 4.7)
Source: Paper §4
Verified: Sage

### Statement
B₁\{√2} = orbit of K = 1 under ⟨T₂,T₃⟩ at distance ≤ 3 in [1/3, 3].

### Proof
Distance 0: {1}. Distance 1: {1/2, 2, 1/3, 3}. Distance 2: {2/3, 3/2}. Distance 3: {4/3, 3/4}. Total = 9 elements = B₁\{√2}. ∎

MDL ⟨2,3⟩ ≡ Hecke ⟨T₂,T₃⟩: one metric ‖(a,b)‖₁, two names.

## [DER] B.4: |B₁| = 2(d₁+d₂) from ramification
Source: S73 §6
Status: [DER] (preimage count [THM]; equality with |B₁| [OBS])

### Statement
Non-cuspal ramified preimages of j: X₀(6)→ℙ¹ number index/d₁ + index/d₂ = 2(d₁+d₂) = 10.
|B₁| = 10 by construction. Cardinalities match.

### Proof (preimage count)
ν₂ = ν₃ = 0 → uniform ramification: e = d₁ at j=1728 (#preimages = 2d₂ = 6), e = d₂ at j=0 (#preimages = 2d₁ = 4). Total = 10. ∎

### Honesty caveat
No constructive bijection B₁ ↔ {ramified preimages} exists. The equality |B₁| = 10 = #{preimages} is a coincidence of cardinalities [OBS], not a proven isomorphism.

## [OBS] B.5: √2 triple anomaly
Source: Paper §3.4, S40

1. Hecke: √2 ∉ orbit (irrational)
2. W₆: 6/√2 ∉ B₁
3. p-adic: |√2|₂ ∉ ℤ

Physical: K_d = √d₁ from EWSB (Higgs VEV v/√2).


---

# C. DESSIN D'ENFANT

## [THM] C.1: Dessin structure
Source: Paper §4.5, S54

4 black (val d₂=3) + 6 white (val d₁=2) + 12 edges + 4 faces {6,3,2,1}. Euler = 2 (g=0). Mon = PSL₂(ℤ/6ℤ), |Mon|=72, |Aut|=1.

**Convention (S90):** σ₁·σ₀·σ∞ = id, i.e. σ∞ = (σ₁∘σ₀)⁻¹.

Biadjacency:
```
B0 [2 1 0 0 0 0]   B1 [0 1 1 0 1 0]   B2 [0 0 1 1 0 1]   B3 [0 0 0 1 1 1]
```

## [THM] C.2: Ramification table
Source: Paper §4.5

| j-fibre | e | #preimages | Σ(e−1) |
|---------|---|-----------|--------|
| 0 | d₂=3 uniform | 4 | 8 |
| 1728 | d₁=2 uniform | 6 | 6 |
| ∞ | {6,3,2,1} | 4 | 8 |
| **Total** | | | **22** ✓ RH |

## [THM] C.3: Dessin uniqueness (36/36)
Source: S71 §3
Verified: Sage (full enumeration)

ALL 36 connected dessins with (3⁴,2⁶,6+3+2+1) isomorphic: same |Mon|=72, |Aut|=1, Schreier spectrum, σ². 36 = 6·3·2·1 internal relabelings. X₀(6) dessin is unique.

## [THM] C.4: BV-structure universality (36/36)
Source: S71 §2
Verified: Sage

For ALL 36 dessins: BV_index = unique uniform-ecc orbit (ecc=d₂=3, composition 2Q+1L). BV_anchor = (2Q+A). BV_star = BV_other = (Q+L+B). pre_anchor ∈ quarks. Doublet Δ=3 universal. ecc ∈ {3,4,5}.

All definitions label-free:
- **anchor** = unique σ∞-fixed point (exists by Anchor Lemma, §D.1)
- **BV_anchor** = σ₀-orbit containing anchor
- **BV_index** = unique σ₀-orbit with uniform eccentricity (all members ecc = d₂ = 3)
- **BV_star** = σ₀-orbit of T³(σ₁(anchor)), where **T = σ∞ restricted to the 6-cycle** (rotation by 1 position), so **T³ = half-rotation** (diametrically opposite element in 6-cycle)
- **pre_anchor** = σ₀⁻¹(anchor) = unique edge mapping to anchor under σ₀

## [THM] C.5: ECC theorem (face-opposite shortcut)
Source: S70, verified 36/36

### Theorem (pure combinatorics)
Among the four σ₀-orbits (3-cycles), EXACTLY ONE contains a pair of diametrically opposite elements of the 6-cycle of σ∞. Verified 36/36.

### Corollary (ecc trichotomy)
This gives three eccentricity classes: ecc ∈ {d₂, d₁², N−1} = {3, 4, 5}.

| ecc | Value | Generation |
|-----|-------|-----------|
| Shortcut pair | d₂=3 | g=3 (t,b) |
| Indirect | d₁²=4 | g=2 (c,s) |
| No shortcut | N−1=5 | g=1 (u,d) |

### Interpretation (depends on §F.3)
The identification ecc → generation number g = N − ecc, and hence "three generations from one face-opposite shortcut", requires the n-formulas of §F.3. The ECC theorem itself is pure combinatorics (36/36, not X₀(6)-specific); the physical interpretation uses the quark n-formula.

## [THM] C.6: Dessin-address theorem (12/12)
Source: S68

Triple (B,W,F) uniquely identifies all 12 edges, 0 collisions.


## [THM] C.7: CRT-биекция (36/36, unique)
Source: S82–S83
Status: [THM] (computational, 36/36)
Dependencies: C.1 (dessin structure), C.3 (36 dessins isomorphic)
Verified: Python (full enumeration of 246400 σ₀-candidates → 36 valid dessins; each tested)

### Statement
There exists a **unique** bijection

φ: {12 edges of dessin} → P¹(ℤ/6ℤ)

compatible with all three monodromy permutations:
- σ₀ ↔ ST (black vertices, 3-cycles)
- σ₁ ↔ S  (white vertices, 2-cycles)
- σ∞ ↔ T⁻¹ (faces, 6+3+2+1)

For EVERY one of the 36 dessins, exactly 1 bijection exists, and all 36 yield the **same** 3×4 CRT grid.

### CRT decomposition
P¹(ℤ/6ℤ) ≅ P¹(𝔽₂) × P¹(𝔽₃) via CRT. Each edge e gets coordinates (x₂(e), x₃(e)).

### CRT grid

```
x₂\x₃:    (0,1)       (1,0)       (1,1)       (1,2)
────────────────────────────────────────────────────────
(0,1):   u(n=1,2/3)  H(n=6,3)   b(n=5,2/3)  s(n=3,2/3)
(1,0):   τ(n=4,2)    p(n=4,1)   e(n=0,1)    μ(n=3,3/4)
(1,1):   d(n=1,√2)   W(n=6,2)   t(n=7,2/3)  c(n=4,4/3)
```

### [THM] Face type = active primes
F(e) = ∏{p ∈ {2,3} : x_p(e) ≠ ∞}

| Type | x₂ | x₃ | F |
|------|----|----|---|
| Quarks | finite | finite | 2·3 = 6 |
| Leptons | ∞ | finite | 3 |
| Bosons | finite | ∞ | 2 |
| Anchor | ∞ | ∞ | 1 |

12/12, 36/36 dessins. Arithmetic origin of particle types from CRT.

### [THM] Latin square
Each BV contains exactly one edge from each x₂ ∈ {(0,1), (1,0), (1,1)}.

### CRT column/row sums [OBS]

| Row | Σn | = |
|-----|-----|---|
| x₂=(0,1) | 15 | d₂(d₁+d₂) |
| x₂=(1,0) | 11 | dim M₁₀ |
| x₂=(1,1) | 18 | d₂·N |

| Column | Σn | = |
|--------|-----|---|
| x₃=(0,1) | 6 | N |
| x₃=(1,0) | 16 | d₁⁴ |
| x₃=(1,1) | 12 | index |
| x₃=(1,2) | 10 | |B₁| |

### [THM] (n, ℓ, K, face) multiset invariance (36/36)
Source: S83
All 36 dessins produce the **identical** multiset of 12 quadruples (n, ℓ, K, face). The K-cipher F.5 is a dessin-invariant. 36/36 verified computationally.

### [THM] K-cipher CRT-irreducibility (36/36)
Source: S83
v₃(K) is NOT a pure function of x₃. All 4 CRT columns give MIXED v₃ values:

| x₃ | v₃ values | Status |
|----|-----------|--------|
| (0,1) | {0, −1} | MIXED |
| (1,0) | {0, +1} | MIXED |
| (1,1) | {0, −1} | MIXED |
| (1,2) | {+1, −1} | MIXED |

The branching of F.5 (face/BV_star/pre_anchor) is irreducible to CRT coordinates. Unified K(x₂, x₃) without branching: **DEAD**.


## [THM-arith/THM-comb] C.7b: Irrep decomposition of particle quantum numbers (S144)
Source: S144
Status: [THM-arith] (ℓ factorization), [THM-comb] (K non-factorization)
Dependencies: C.7, O.1, F.7e, G.8

### Statement

Under the irrep decomposition V_perm = V₁ ⊕ V₃ ⊕ V₂ ⊕ V₆ of the S₃ × A₄ ≅ Mon action (cf. S.6):

**ℓ-factorization [THM-arith]:** The V₆ component of ℓ has **rank 1**. The EW operator factorizes completely as (S₃-part) ⊗ (A₄-part). This is a CRT-reformulation of the DFT result G.8/F.7e: ℓ depends on ε-η bits which split across the CRT factors.

**K non-factorization [THM-comb]:** The V₆ components of v₂ and v₃ (hence ln K) have **rank 2**. The K-cipher is structurally CRT-irreducible (cf. C.7). No additional decomposition beyond F.7b-K exists.

### √2 localization

The P¹(𝔽₃)-fiber containing the d-quark (sole particle with K = √2) is the unique fiber with irrational K-product. All other three fibers have ∏K ∈ ℚ. The √2-anomaly (B.5) is localized in CRT coordinates.

Verified: explicit computation in companion CRT grid (C.7). Fiber x₃ = (0,1): {u, τ, d} with ∏K = 4√2/3 (irrational). Remaining fibers: ∏K ∈ {6, 4/9, 2/3} (rational).


## [THM-comp / OBS] C.7c: Canonical CRT from normal subgroups (S148)
Source: S148 §2
Status: [THM-comp] (normal subgroup orbits, face block-diagonal), [OBS] (comparison)
Dependencies: C.7, O.1

### Construction [THM-comp]

Mon ≅ S₃ × A₄ has a unique normal subgroup of order 6 (≅ S₃) and a unique of order 12 (≅ A₄). Their orbits define a canonical CRT:

**S₃-orbits (columns):** {c,s,τ}, {u,d,μ}, {b,t,e}, {W,H,p}.
**A₄-orbits (rows):** {c,d,b,H}, {s,u,t,W}, {τ,μ,e,p}.

Verified computationally: unique normal S₃ (1/1), unique normal A₄ (1/1).

### Face type block-diagonal [THM-comp]

F(e) = (d₁ if x₂ finite) × (d₂ if x₃ finite). 12/12. Irrep decomposition reads from coordinates.

### Comparison with companion CRT (C.7) [OBS]

**Columns:** 2/4 identical ({b,t,e}, {W,H,p}). Remaining two differ by τ ↔ μ: canonical {c,s,τ},{u,d,μ} vs companion {c,s,μ},{u,d,τ}.

**Rows:** Completely different partitions. Canonical rows (A₄-orbits) ≠ companion rows. Only {τ,μ,e,p} shared. NOT reducible to τ ↔ μ.

### n-sums

| | Canonical | Companion (C.7) |
|---|---|---|
| Row Σn | {16, 17, 11} | {15, 11, 18} = {d₂(d₁+d₂), dim M₁₀, d₂N} |
| Col Σn | {11, 5, 12, 16} = {dim M₁₀, N−1, index, d₁⁴} | {N, d₁⁴, index, |B₁|} |

All companion sums are LD monomials. Canonical row sum 17 is not.

### Marking ambiguity

2!×3! = 12 valid orderings within block partition. Both canonical and companion CRT live in this space. Neither dominates overall: canonical has block-diagonal face type, companion has monomial n-sums.


## [THM-arith] C.8: Information Geometry of the Dessin (S176, verified S177)
Source: S176, verified S177 (independent recomputation from O.1)
Status: [THM-arith]
Dependencies: C.6 (dessin-address), O.1 (monodromy), G.0b (h values)

### C.8.1: Shannon optimality and information cascade [THM-arith]

The face-size triple (face(e), face(σ₁(e)), face(σ₀(e))) achieves maximum Shannon entropy:

H(face, face(σ₁), face(σ₀)) = log₂(12) = 3.585 bits

All 12 triples distinct (= C.6 dessin-address theorem). Deficit = 0.

**Information cascade:**

| Contribution | Bits | Cumulative |
|---|---|---|
| σ∞: H(face) | 1.730 | 1.730 |
| σ₁: H(face(σ₁)\|face) | 1.355 | 3.085 |
| σ₀: H(face(σ₀)\|face, face(σ₁)) | 0.500 | 3.585 = log₂(12) |

Mutual information: I(face; face(σ₁)) = 0.374 bits.

**Physical reading:** σ∞ encodes particle type (1.730 bits), σ₁ adds generation/partner info (1.355 bits), σ₀ provides final disambiguation (0.500 bits = 1 effective binary choice).

Note: the 12-triple uniqueness is C.6; the new content is the cascade decomposition.

### C.8.2: Face equicorrelation [THM-arith]

The 3×3 Gram matrix of face vectors (face(e), face(σ₁(e)), face(σ₀(e))) over the 12 edges is:

G = 252·I₃ + 192·(J₃ − I₃)

where J₃ = all-ones matrix. Explicitly:
- Diagonal: Σ face(e)² = Σ face(σ₁(e))² = Σ face(σ₀(e))² = 252 (trivial: σ₁, σ₀ are bijections)
- **All three off-diagonal entries = 192 = d₁⁶d₂:**
  - Σ face(e)·face(σ₁(e)) = 192
  - Σ face(e)·face(σ₀(e)) = 192
  - Σ face(σ₁(e))·face(σ₀(e)) = 192

Correlation coefficient: 192/252 = 16/21.

Note: σ∞ trivially preserves face(e)² (identity on faces), so the content is that both face-SCRAMBLING operators (σ₁ and σ₀) produce the same quadratic sum, and their cross-product also equals 192.

### C.8.3: Spectral sum rule Σf²h = Σn [THM-arith]

Σ_{f|N} f²·h(f) = Σ_{e} n(e) = 44 = d₁²·dim M₁₀

Explicit: 1²·2 + 2²·(9/4) + 3²·1 + 6²·(2/3) = 2 + 9 + 9 + 24 = 44.

Uses count(face=f) = f for all f|N (verified 12/12).

**Connection to X.54b:** d₁·f·h(f) ∈ {d₁², d₂², N, d₁³}. Weighted sum with face-multiplicity recovers Σn.

Deps: G.0b (h), F.7 (Σn = 44), X.54b.

### C.8.4: h-uniqueness from cubic (3c−2)(45c²−29c−2) = 0 [THM-arith]

The four constraints:
1. h(2) = d₂²/d₁² = 9/4  [DER, V.4]
2. ∏h(f) = d₂ = 3  [OBS]
3. Σf²h(f) = Σn = 44  [THM-arith, C.8.3]
4. ⟨π,h⟩ = d₂²/d₁³ = 9/8  [OBS, X.50]

determine h(6) as unique positive LD-monomial root of:

**135c³ − 177c² + 52c + 4 = (3c − 2)(45c² − 29c − 2) = 0**

Three roots:

| c = h(6) | h(1) | h(3) | All > 0? | LD monomials? |
|---|---|---|---|---|
| **2/3 = d₁/d₂** | **2 = d₁** | **1** | **yes** | **yes** |
| (29+√1201)/90 ≈ 0.707 | ≈ 2.37 | ≈ 0.80 | yes | no |
| (29−√1201)/90 ≈ −0.063 | ≈ −4.57 | ≈ 4.65 | **no** | no |

With LD-monomial constraint: **unique** h = (d₁, d₂²/d₁², 1, d₁/d₂).

**Note on second root:** c₂ ≈ 0.7073 ≈ 1/√2 but NOT exact (disc = 1201 prime; c₂ = (29+√1201)/90 ∉ ℚ(√2)).

**Comparison with G.0c (S169–S171):**
G.0c uses 4 LINEAR constraints (1)+(1')+(⊥)+(2), two of which are [OBS].
C.8.4 uses (1)+(2)+(3)+(4), replacing (1') and (⊥) with C.8.3 [THM-arith] and ∏h=d₂ [OBS].
Advantage: C.8.3 has clear physical meaning ("face-weighted NLO = total n-sum").
Remaining for full derivation: derive any two of {(2), (4), ∏h=d₂} from dessin.

Deps: V.4, G.0b, X.50, C.8.3. Verified: sympy symbolic factorization + Fraction arithmetic.

### C.8.5: T₁ = T₀ for ANY dessin [THM-math, L8.14]

The face Markov chains of σ₁ and σ₀ are IDENTICAL:
T₁(f→f') = T₀(f→f') for all face sizes f, f'.

**Proof:** σ₀ = σ₁⁻¹·σ∞⁻¹. Since face is constant on σ∞-orbits,
σ∞⁻¹ permutes within faces. Substituting e' = σ∞⁻¹(e):
T₀(f→f') = #{e: face(e)=f, face(σ₁(σ∞⁻¹(e)))=f'} = #{e': face(e')=f, face(σ₁(e'))=f'} = T₁(f→f'). ∎

**Scope:** General for ALL dessins (uses only monodromy relation + face definition).
**Consequence:** σ₁/σ₀ asymmetry is INVISIBLE at face-statistics level.
Both have same eigenvalues μ(d)/d, same eigenvectors, same stationary distribution π(f) = f/12.

**Edge-level check (X₀(6)):** face(σ₁(e)) ≠ face(σ₀(e)) for 10/12 edges (only e, p coincide). The T₁=T₀ identity is nontrivial: it holds at the AGGREGATE level despite pervasive edge-level disagreement.

Deps: monodromy axiom σ₁·σ₀·σ∞=id. Verified S178 (all 16 T-matrix entries match).

### C.8.6: w = h·f spectral decomposition [THM-arith, L8.15]

w(f) = h(f)·f: {1→2, 2→9/2, 3→3, 6→4}.

In T-eigenbasis (π-orthogonal, ‖v_d‖²_π = d):

| Mode | Eigenvalue | c_d(w) | LD identification |
|------|-----------|--------|-------------------|
| v₁ (trivial) | 1 | 11/3 | dim M₁₀/d₂ |
| v₂ (p-mode) | −1/d₁ | 11/24 | dim M₁₀/(d₁³d₂) |
| v₃ (q-mode) | −1/d₂ | **0** | ← **(⊥)** |
| v₆ (pq-coupled) | 1/N | −1/8 | −1/d₁³ |

dim M₁₀ = 11 appears in BOTH nonzero non-coupled coefficients.
Relation c₁(w)·c₆(w) = −c₂(w) [THM-arith, L8.18].
Ratio c₁/c₂ = d₁³ = 8.

Deps: G.0b (h), X.48 (T eigenbasis), X.57 (tensor factorization).

### C.8.7: h spectral decomposition — all coefficients LD monomials [THM-arith, L8.16]

| Mode | c_d(h) | LD monomial |
|------|--------|-------------|
| v₁ | 9/8 | d₂²/d₁³ |
| v₂ | −1/16 | −1/d₁⁴ |
| v₃ | −25/72 | −(N−1)²/|Mon| |
| v₆ | −7/144 | −L/index² |

Note: c₃(h) ≠ 0. The (⊥) constraint is about h·f, NOT h alone (C.8.8).
Ratio c₂(h)/c₆(h) = 9/7 = d₂²/L.

Confirms and extends X.49: "all 4 coefficients LD monomials" now fully tabulated.

Deps: X.49 (original observation), G.0b, X.48.

### C.8.8: Precise statement of (⊥) [THM-arith, L8.17]

**(⊥) = c₃(h·f) = 0**, equivalently Σ f²·h(f)·v₃(f) = 0.

This means w = h·f has zero projection onto v₁^(2)⊗v₃^(3) (the "pure-q" tensor mode, X.57). The q-divisibility mode v₃ enters the NLO correction h·f ONLY through the (p,q)-coupled channel v₆ = v₂^(2)⊗v₃^(3), never alone.

**Clarification:** c₃(h) = −25/72 ≠ 0 (C.8.7). The (⊥) constraint acts on h·f, not h. Previous shorthand "h·f ⊥ v_{d₂}" (X.49, G.0c) is correct but the subscript refers to the projection of h·f, not of h.

Deps: C.8.6, C.8.7, X.57 (tensor interpretation).

### C.8.9: σ₁ sufficient statistic, σ₀ not [THM-comp, L8.19]

face(σ₁) groups particles into sets where h is constant:
- face(σ₁)=1: {c}, h=2
- face(σ₁)=2: {s,τ}, h=9/4
- face(σ₁)=3: {b,d,H}, h=1
- face(σ₁)=6: {u,t,e,μ,W,p}, h=2/3

face(σ₀) groups have VARYING h: e.g. face(σ₀)=6 contains {c,b,e,τ,H,p} with h ∈ {2, 1, 2/3, 9/4, 1, 2/3} (spread 3.375×).

σ₁ is a sufficient statistic for h; σ₀ is not.
YET T₁ = T₀ (C.8.5). The asymmetry is purely correlational, invisible to face-transition statistics.

Deps: G.0b, O.1, C.8.5.

### C.8.10: Cycle h-products [THM-arith, L8.20]

h-product over σ∞-cycles (each particle contributes h(face(σ₁(e)))):

| Cycle | Product | LD |
|---|---|---|
| 6-cycle (quarks) | h(1)¹h(2)¹h(3)²h(6)² | d₁ = 2 |
| 3-cycle (leptons) | h(2)¹h(6)² | 1 |
| 2-cycle (bosons) | h(3)¹h(6)¹ | d₁/d₂ = 2/3 |
| 1-cycle (anchor) | h(6)¹ | d₁/d₂ = 2/3 |

All LD monomials. Exponents = T₁ transition counts (= T₀ counts by C.8.5).

**Note:** 3-cycle = 1 follows from constraint (1): h(2)·h(6)² = (9/4)·(4/9) = 1. NOT independent.
6-cycle = d₁ does NOT discriminate physical vs alternative h: h_alt also gives ∏=2 for 6-cycle. All cycle products reduce to ∏h = d₂ (not independent of G.0b).

Deps: O.1, G.0b, X.48.

### C.8.11: (⊥) as q-balance condition [THM-arith, L8.21]

**(⊥) ⟺ per-edge average of f·h(f) is constant across d₂-divisibility classes.**

Σ_{3|f} f²h / Σ_{3|f} f = 33/9 = **11/3 = dim M₁₀/d₂**
Σ_{3∤f} f²h / Σ_{3∤f} f = 11/3 = **11/3 = dim M₁₀/d₂**

Interpretation: 3-divisibility of face is INDEPENDENT of f·h in the edge measure.
E[f·h | 3|f] = E[f·h | 3∤f] = E[f·h] = dim M₁₀/d₂.

NOT symmetric under d₁↔d₂: for 2-divisibility partition, averages are 33/8 ≠ 11/4 (ratio d₂/d₁ = 3/2).

**Gap 3 significance:** This is the cleanest combinatorial formulation of (⊥) — a conditional-independence statement about the dessin that might follow from the passport structure.

Deps: C.8.6, C.8.3.

### C.8.12: Constraint landscape for h [THM-arith, S178 synthesis]

Given (1): h(2) = d₂²/d₁² and (1'): h(1) = d₁, two unknowns remain: h(3), h(6).

Three [OBS] constraints (any two determine uniquely):
- **(⊥):** h(3) + 4h(6) = 11/3
- **(2):** h(3) + 2h(6) = 7/3
- **∏h:** h(3)·h(6) = d₁/d₂ = 2/3

Pairwise analysis:
- **(⊥) + (2) → UNIQUE:** h(3) = 1, h(6) = 2/3. No ambiguity, no Z₂.
- **∏h + (2) → Z₂:** h(6) ∈ {2/3, 1/2}. [G.0c Z₂ ambiguity]
- **∏h + (⊥) → Z₂:** h(6) ∈ {2/3, 1/4}. Different spurious root!

**Any ONE [OBS] + (1)+(1') → 1-parameter family.**
**Any TWO [OBS] → unique.** Gap 3 = derive 2 of 3.

Deps: G.0c, C.8.6, C.8.11.


---

# D. SPECTRUM AND KIRCHHOFF

## [THM] D.1: Anchor Lemma
Source: S73 §1.1

### Statement
#{internal σ₁-pairs} = #{fixed points of σ∞}. For (6,3,2,1): m=1.

### Proof
**Forward:** x fixed by σ∞ ⟹ σ₀⁻¹(σ₁(x))=x ⟹ σ₁(x)=σ₀(x) ∈ same σ₀-orbit.

**Reverse:** {x,y} internal, y=σ₁(x)=σ₀(x) ⟹ σ∞(x)=σ₀⁻¹(σ₁(x))=σ₀⁻¹(σ₀(x))=x.

**Injectivity:** Is partner y also fixed? σ∞(y)=σ₀(σ₁(y))=σ₀(x)≠y (σ₀ has no fixed points). Each internal pair has exactly 1 fixed point. Bijection. ∎

## [THM] D.2: BB^T uniqueness
Source: S73 §1.2–1.5

### Proof
**Diagonal:** Anchor BV row = (2,1,0,0,0,0) → (BB^T)₀₀ = 5 = d₁²+1. Others: row = (1,1,1,0,0,0) → diagonal = 3 = d₂.

**Row sums:** (BB^T)𝟏 = B(B^T𝟏) = B(d₁𝟏) = d₁d₂𝟏 = 6𝟏.

**Off-diagonal:** BV₀: off-diag sum = 1 → a₀₁=1, a₀₂=a₀₃=0. System for remaining: a₁₂+a₁₃=2, a₁₂+a₂₃=3, a₁₃+a₂₃=3. Unique: a₁₂=1, a₁₃=1, a₂₃=2. ∎

$$BB^T = \begin{pmatrix} 5&1&0&0 \\ 1&3&1&1 \\ 0&1&3&2 \\ 0&1&2&3 \end{pmatrix}$$

## [THM] D.3: σ²(B) = {N, N−1, d₁, 1} = {6, 5, 2, 1}
Source: S73 §1.6–1.7
Replaces: S55 [OBS]

### Proof
3×3 minor (rows 1,2,3): M₃ has char poly (λ−1)(λ²−8λ+13).

Cofactor C₃ = −(λ−1)(λ−5).

Full: det(λI−BB^T) = (λ−5)·M₃ − C₃ = (λ−1)(λ−5)[(λ²−8λ+13)−1] = **(λ−1)(λ−2)(λ−5)(λ−6)**. ∎

### Structural insight
Without anchor: σ² = {N, d₁, d₁, d₁} (degenerate). Anchor splits: {d₁,d₁,d₁} → {N−1, d₁, 1}. One bit → Kirchhoff → Cabibbo.

## [THM] D.4: Kirchhoff = 40
Source: S73 §2
Dependencies: D.3
Verified: Sage (cofactor det over ℚ, 36/36)

### Graph and Laplacian definition
The **bipartite graph** G_bip has n_b = 4 black vertices (BVs) and n_w = 6 white vertices (WVs), with adjacency given by the biadjacency matrix B (4×6). The **bipartite Laplacian** is the (n_b+n_w) × (n_b+n_w) matrix:

L_bip = [[d₂·I_{n_b}, −B], [−B^T, d₁·I_{n_w}]]

where d₂ = 3 = black vertex degree, d₁ = 2 = white vertex degree (biregular).

### From σ²(B) to Laplacian spectrum
The nonzero eigenvalues of L_bip come in pairs (λ₊, λ₋) for each singular value σᵢ of B, satisfying:

λ₊ + λ₋ = d₁ + d₂ = 5,  λ₊·λ₋ = d₁d₂ − σᵢ²

| σᵢ² | d₁d₂ − σᵢ² = λ₊λ₋ | Eigenvalues | Note |
|------|---------------------|-------------|------|
| N = 6 | 0 | {5, 0} | Zero mode (connected graph) |
| N−1 = 5 | 1 | {(5+√21)/2, (5−√21)/2} | |
| d₁ = 2 | 4 | {4, 1} | |
| 1 | 5 | {(5+√5)/2, (5−√5)/2} | |

Additionally: L_bip has eigenvalue d₁ = 2 with multiplicity n_w − n_b = 6 − 4 = **2** (from ker B^T, which has dimension n_w − rank(B) = 6 − 4 = 2, since BB^T is nonsingular). Mechanism: vectors (0, v) with v ∈ ker B^T satisfy L_bip·(0,v) = (−Bv, d₁v) = (0, d₁v), giving eigenvalue d₁.

### Kirchhoff number (Matrix Tree Theorem)
For a bipartite graph, the number of spanning trees is:

K = (1/n) · ∏(nonzero eigenvalues of L_bip)

where n = n_b + n_w = 10.

Product of nonzero eigenvalues:
∏ = (d₁+d₂) · (1) · (4) · (5) · d₁² = 5 · 1 · 4 · 5 · 4 = **400**

(Here: from σ² = 6: contributes λ₊ = 5; from σ² = 5: contributes λ₊λ₋ = 1; from σ² = 2: contributes λ₊λ₋ = 4; from σ² = 1: contributes λ₊λ₋ = 5; from ker: contributes d₁² = 4.)

K = 400/10 = **40**. ∎

### General formula
K = d₁³(d₂−1)(N−1)/2. At (2,3): 8·2·5/2 = 40. ✓

### Identity
K = |B₁|·d₁² = 2(d₁+d₂)·d₁² = 10·4 = 40.

This uses |B₁| = 2(d₁+d₂) from §B.4 (preimage count [THM]; identification [OBS]).

### Cayley graph coincidence Tr(A²) = K [THM-arith, unique to X₀(6), S176/S177]

On the Cayley (Schreier) graph with generators {σ₁, σ₀, σ₀⁻¹}:

Tr(A²) = 40 = K(bipartite)

**Mechanism:** Tr(A²) = Σ_{ij} A²_{ij} = 32·1 + 2·4 = 40, where 32 entries have A_{ij}=1 (simple edges) and 2 entries have A_{ij}=2 (multi-edge c↔p from Anchor Lemma D.1). Equivalently: 3·index + 2·(Anchor multi-edge count) = 36 + 4 = 40.

**Uniqueness (S177):** Tested on 6 squarefree levels N ∈ {6, 10, 14, 15, 21, 35}. Tr(A²) = K holds ONLY for N=6. All other levels fail. Three contributing factors unique to N=6:
1. σ₁ fixed-point-free on P¹(ℤ/6ℤ) (ν₂ = 0) → Tr(A¹) = 0
2. ν₃ = 0 → no order-3 elliptic contributions
3. Exactly 1 multi-edge (Anchor Lemma) → exactly 2 generator collisions

For N=10: σ₁ has 2 fixed points → Tr(A¹) = 2, Tr(A²) = 58 ≠ K = 72.

Higher traces also LD-monomial and unique: Tr(A³) = 30 = N(N−1), Tr(A⁴) = 224 = d₁⁵L. See X.67.

Deps: I.6 (Cayley spectrum), D.1 (Anchor Lemma).


## [THM] D.5: Leptonic block M_lep
Source: S73 §4

M_lep = 3×3 non-anchor submatrix of BB^T. Eigenvalues: 4+√3, 4−√3, 1.

**det(M_lep) = 13 = d₁²+d₂² = Φ₃(d₂).** ← PMNS denominator. Cyclotomic chain (X.99, S204): Φ₃(1,d₁,d₂) = (d₂,L,det M_lep).

**Pell relation (X.99a):** d₂²−2d₁²=1. M_lep eigenvalue center = (d₂²−1)/2 = d₁² exactly.

**Characteristic polynomial (X.99b):** char(M_lep) = x³−d₂²x²+d₂Lx−Φ₃(d₂). All coefficients LD monomials. Quadratic factor disc = 4d₂.

**μ-τ symmetry [THM]:** PMP = M (P swaps rows 2,3). Proof: (BB^T)₁₂ = (BB^T)₁₃ = 1, (BB^T)₂₂ = (BB^T)₃₃ = 3. ∎

Tree level: sin²θ₁₃ = 0, sin²θ₂₃ = 1/2.

Leptonic Kirchhoff = N−1 = 5. Full/leptonic = d₁³ = 8.

**Cross-reference (S148):** BV-quotient 3×3 block (D.8) has spec = {d₁ ± √d₂, N−1}, same √d₂ and trace d₂² = 9, but different center (d₁ vs d₁²) and det (5 vs 13). Two independent √d₂ channels.


---


## [THM] D.6: φ-Zero Theorem
Source: S90
Status: [THM]
Dependencies: I.6 (Cayley Laplacian spectrum), C.6 (dessin-address)
Verified: Python/numpy (12/12 edges, machine precision)

### Statement
The two eigenvectors of L with eigenvalues (5±√5)/2 (the φ-pair, disc = d₁²+1 = 5) vanish identically on exactly the 4-element set:

**Z_φ = BV_anc ∪ σ₁(BV_anc) = {p, c, u, t}**

### Proof sketch
σ₁(BV_anc) = {c, p, t}, so Z_φ = {p, c, u, t}. All neighbours of p, c, u lie in Z_φ → eigenequation trivially satisfied. For t: nbrs = {u, b, e} requires v(b) = −v(e), which the restricted 8×8 system satisfies for both φ-eigenvalues. ∎

### Structural meaning
Z_φ = BFS ball of radius 2 around anchor. Also: Z_φ = set of 4 edges forced or multi-edge in ALL 40 spanning trees (E.8).


## [THM] D.7: Golden Hierarchy
Source: S90
Status: [THM]
Dependencies: D.6
Verified: Python/numpy (machine precision)

### Statement
The φ-eigenvector components take exactly 3 nonzero absolute values in the ratio **1 : φ : φ²**:

| |v(e)| | Edges | Count |
|:------:|:-----:|:-----:|
| 0 | p, c, u, t | 4 |
| 1/(φ√10) | b, e | 2 |
| 1/√10 | s, τ, W, H | 4 |
| φ/√10 | d, μ | 2 |

Normalization: √10 = √|B₁|. Ratios verified to machine precision.

### Key pairing
d (K=√2, EWSB anomaly) and μ (K=3/4) carry maximal φ-amplitude φ/√10.

### Interference theorem [CONFIRMED S90]
Neither integer-spectrum nor irrational-spectrum part of exp(−L/d₁) alone gives |U_e|² = 4/13. Integer part: 0.540. Irrational: 0.170. φ-pair alone: 0.152. The 4/13 result emerges ONLY from full superposition = **quantum interference** between discrete (ℤ-spectrum) and irrational (φ, √21) sectors.


## [THM-arith / THM-comp] D.8: BV-projection of Cayley Laplacian (S148, updated S193/S194)
Source: S148 §3, spectral bridge S193 (verified S194)
Status: [THM-arith] (erasure, quotient matrix, char poly, containment, spectral bridge), [THM-comp] (orthogonality, 3×3 block)
Dependencies: O.1, I.6, D.2, D.5

### σ₀-erasure identity [THM-arith]

Π·L = Π·(I₁₂ − σ₁)

where Π is the 4×12 BV-indicator matrix (Π_{i,j} = 1 if particle j ∈ BVᵢ).

**Proof.** σ₀-orbits = BVs ⟹ Π·σ₀ = Π, Π·σ₀⁻¹ = Π. Therefore Π·L = Π·(3I − σ₁ − σ₀ − σ₀⁻¹) = 3Π − Π·σ₁ − Π − Π = Π·(I − σ₁). ∎

**Consequence:** BV-quotient physics depends on σ₁ ONLY. σ₀ (generation) and σ∞ (face) are invisible.

Verified: exact integer arithmetic, entry-by-entry.

### Quotient Laplacian [THM-arith]

Π·L·Πᵀ = 3I₄ − Π·σ₁·Πᵀ (from erasure).

Rows/columns: BV₀(anc), BV₁(idx), BV₂(star), BV₃(oth).

```
         ⎡ 1  -1   0   0 ⎤
ΠLΠᵀ =  ⎢-1   3  -1  -1 ⎥
         ⎢ 0  -1   3  -2 ⎥
         ⎣ 0  -1  -2   3 ⎦
```

det(λI₄ − ΠLΠᵀ) = λ(λ − 1)(λ − d₁²)(λ − (N−1)) = λ(λ−1)(λ−4)(λ−5)

All eigenvalues LD monomials. Trace = |B₁| = 10. Det = 0.

### Eigenvalue containment [THM-arith] (upgraded S193, verified S194)

spec(ΠLΠᵀ) = {0, 1, 4, 5} ⊂ spec(L).

BV partition is NOT equitable (neighbor profiles differ within every BV). For equitable partitions, containment is guaranteed; here non-trivial. **Proved analytically via spectral bridge (D.8b):** the bipartite quadratic factors x²−5x+μ for each μ ∈ spec(ΠLΠᵀ) all divide char(L). See D.8b for full proof.

### Spectral Bridge Identity [THM-arith] (S193, verified S194) {#D.8b}

**Statement.** BB^T + ΠLΠᵀ = 2d₂I₄.

Equivalently: BB^T = d₂I₄ + Πσ₁Πᵀ and ΠLΠᵀ = d₂I₄ − Πσ₁Πᵀ.

**Proof.**

*Step 1.* BB^T = d₂I₄ + Πσ₁Πᵀ.

Off-diagonal (b≠b'): (BB^T)[b,b'] = Σ_w B[b,w]·B[b',w]. Each WV w = {j,σ₁(j)} contributes 1 iff one element in BV_b, the other in BV_b'. This equals (Πσ₁Πᵀ)[b,b'] (counting σ₁-edges from BV_b to BV_b'). Diagonal: (BB^T)[b,b] = d₂ + 2·n_int(b) = d₂ + (Πσ₁Πᵀ)[b,b], where n_int(b) = #{internal σ₁-pairs in BV_b}. ∎

*Step 2.* ΠLΠᵀ = d₂I₄ − Πσ₁Πᵀ (from σ₀-erasure: Π(3I−σ₁−σ₀−σ₀⁻¹)Πᵀ = 3d₂I − Πσ₁Πᵀ − d₂I − d₂I). ∎

*Step 3.* Sum: (d₂I + Πσ₁Πᵀ) + (d₂I − Πσ₁Πᵀ) = 2d₂I₄. ∎

Verified: Fraction arithmetic (3 independent methods, S194).

**Corollary: Eigenvalue pairing.** For paired eigenvalues: σ²(BB^T) + μ(ΠLΠᵀ) = 2d₂.

| μ(ΠLΠᵀ) | σ²(BB^T) = 2d₂−μ | Bipartite quadratic x²−5x+μ |
|-----------|-------------------|------------------------------|
| 0 | 6 = N | x(x−5) |
| 1 | 5 = N−1 | x²−5x+1 [√21-pair] |
| 4 = d₁² | 2 = d₁ | (x−1)(x−4) |
| 5 = N−1 | 1 | x²−5x+5 [φ-pair] |

**Spectral containment proof.** Each bipartite quadratic x²−5x+μ divides char(L):

(a) Integer factors: x(x−5) and (x−1)(x−4) divide char(L) by inspection of known spectrum I.6. ✓

(b) φ-pair: (x²−5x+5) | char(L). By D.6, φ-eigenvectors vanish on Z_φ = {p,c,u,t}. The restricted 8×8 adjacency A₈ on the complement has char(A₈) = λ(λ+2)²(λ²−λ−1)(λ³−3λ²−λ+4). The factor λ²−λ−1 maps to x²−5x+5 via x = 3−λ. ✓

(c) √21-pair: (x²−5x+1) | char(L) directly from the factored characteristic polynomial I.6. A structural proof avoiding the 12×12 char poly remains OPEN. ✓

(d) ker B^T exclusion: L_bip has eigenvalue d₁=2 (mult 2). char(L) mod (x−2) = 540 ≠ 0 → d₁ ∉ spec(L_Cayley). ✓

**Conclusion:** spec(L_bip) \ {d₁} ⊂ spec(L_Cayley). ∎

Dependencies: D.2, D.6, I.6.

### Eigenspace orthogonality [THM-comp]

| λ | mult in L | BV-rank | ⊥ BV? |
|---|-----------|---------|-------|
| 0 | 1 | 1 | no |
| (5−√21)/2 | 1 | 1 | no |
| 1 | 1 | 1 | no |
| (5−√5)/2 | 1 | 1 | no |
| **3** | **2** | **0** | **yes** |
| (5+√5)/2 | 1 | 1 | no |
| **4** | 1 | 1 | no |
| (5+√21)/2 | 1 | 1 | no |
| **5** | **3** | **0** | **yes** |

dim(ker Π ∩ L-eigenspaces) = 2 + 3 = N−1 = 5. Non-⊥: 7 eigenspaces, each rank 1 in 4D BV-space. Check: 5 + 7 = 12 ✓.

Verified: BV-sums < 10⁻¹⁵. Analytical proof: OPEN.

**Perturbative explanation (not proof):** σ₀-DFT decomposes L into BV sector (k=0, eigenvalues ∈ [0, 5/3]) and ω/ω̄ sector (∈ [10/3, 14/3]). Spectral gap 5/3. λ=3 and λ=5 originate in ω-sector and inherit no BV component (coupling < gap). λ=4 mixes (favorable ratio).

### Non-anchor 3×3 block [THM-comp]

spec(ΠLΠᵀ|_{BV₁,BV₂,BV₃}) = {d₁ − √d₂, d₁ + √d₂, N−1} = {2−√3, 2+√3, 5}

Trace = d₂² = 9. Det = N−1 = 5.

**Comparison with M_lep (D.5):**

| | M_lep (D.5) | BV-quotient 3×3 |
|---|---|---|
| Irrational pair | d₁² ± √d₂ | d₁ ± √d₂ |
| Integer eigenvalue | 1 | N−1 = 5 |
| Trace | d₂² = 9 | d₂² = 9 |
| Det | d₁² + d₂² = 13 | N−1 = 5 |
| √d₂ origin | bipartite graph (disc = 4d₂) | σ₁-quotient |

Same √d₂, same trace. Different center (d₁² vs d₁) and det (13 vs 5). Two independent √d₂ channels. Does NOT close Gap 9. See I.9g.5.


# E. CKM

## [DEAD] E.1: 10 dead graph approaches (S72 §1)
All give inverted hierarchy. Key insight: relevant variable is |Δg|, not graph distance.

## [OBS → DER via V.4] E.2: λ = d₂²/Kirchhoff = 9/40 = 0.22500
Source: S72 §3. PDG: 0.22497±0.00070, δ = **−0.04σ**.

Compact: λ = d₂²/[2d₁²(d₁+d₂)].

## [OBS → DER via V.4] E.3: A = d₂/√(d₁²+d₂²) = 3/√13 = 0.83205
Source: S72 §4. PDG: 0.839±0.011, δ = **+0.63σ**.

A = cos θ₁₂(PMNS). CKM-PMNS link.

## [OBS → DER via V.4] E.4: γ = arctan(d₂²/d₁²) = arctan(9/4) = 66.04°
Source: S72 §5. Exp: (62.8 ± 2.6)° (LHCb combination, Nov 2025), δ = **−1.25σ**. Previous: 65.98°±4.0° (−0.015σ). Now max-pull CKM parameter.

## [OBS → DER via V.4] E.5: R_b² = N/Kirchhoff = 3/20 = 0.15
Source: S72 §6. Exp: 0.15088±0.007, δ = **+0.13σ**.

Identity: R_b² = λ·d₁/d₂ (only 3 independent parameters).

## [OBS → DER via V.4] E.6: Full CKM (9 elements, Sage-verified)
Source: S72 §7. Max deviation: |V_td| at 1.11%. J = 3.095×10⁻⁵ (**−0.12σ**).

| Parameter | LD | Exp | σ-pull |
|-----------|-----|-----|--------|
| λ | 9/40 | 0.22497±0.00070 | −0.04 |
| A | 3/√13 | 0.839±0.011 | +0.63 |
| γ | arctan(9/4) | (62.8±2.6)° (LHCb 2025) | **−1.25** |
| R_b² | 3/20 | 0.15088±0.007 | +0.13 |
| J | 3.095×10⁻⁵ | (3.08±0.13)×10⁻⁵ | −0.12 |

### Degree-of-freedom count
All 4 Wolfenstein parameters are functions of (d₁, d₂) only (K = |B₁|·d₁² follows from d₁, d₂). R_b² = λ·d₁/d₂ is a **constraint**, not an independent prediction → 3 independent measurements. (d₁, d₂) = (2, 3) are **model constants** fixed by the LD framework (§A.1), not fitted to CKM data → **0 fit parameters, dof = 3**. χ²/dof = (0.04² + 0.63² + 1.25² + 0.13²)/3 = **0.66** (p = 0.58). γ dominates at 1.25σ. If CKMfitter indirect (66.3°) preferred over LHCb direct, γ pull drops to +0.1σ.

**Erratum (S142):** Previous version had dof = 1 by subtracting (d₁, d₂) as "inputs". This double-counts model constants as fit parameters.

**S138 UST derivation (§V.4):** All 4 parameters derived from 2 UST quantities: P_triple = d₂²/K = 9/40, ΔP = d₁²/K = 1/10. Physical bridge: transfer current theorem (Burton–Pemantle 1993) identifies P(edge ∈ UST) = tree-level lattice propagator. No postulate beyond L0. Status upgrade: **[OBS]×4 → [DER]**. With corrected R_b error propagation: χ²/dof = **0.66** (p = 0.58). CKM-PMNS complementarity: A² + sin²θ₁₂ = 1 [exact].

## [THM→DER] E.7: Chain anchor → Cabibbo
```
σ∞ 1-cycle → Anchor Lemma [THM] → m=1 → BB^T unique [THM]
→ σ²={N,N−1,d₁,1} [THM] → Kirchhoff=40 [THM] → λ=d₂²/K [THM graph]
→ UST edge probabilities [THM-comb] → P_triple, ΔP → {λ,A,γ,R_b} [DER via V.4]
```
Every step except the physical identification (dessin = lattice at tree level, §V.5) is proven. Status: [THM→DER] (was [THM→OBS]).


## [THM] E.8: Residual Tree Theorem (λ = d₂²/K)
Source: S75
Status: [THM] (graph identity); physical identification λ_CKM = d₂²/K remains [OBS]
Dependencies: D.1 (Anchor Lemma), D.2 (BB^T uniqueness), D.4 (Kirchhoff)
Verified: Sage (40 trees, exhaustive; all 8 triples; 9/9 interior codes)
Replaces: S74 [OBS with mechanism]

### Three-layer decomposition of spanning trees

| Layer | Edges | Size | Role |
|-------|-------|------|------|
| FORCED | {u, t} | 2 | In ALL 40 trees. Bridge WV₁ deterministic. |
| BOUNDARY | {c⊕p} × {s⊕W} × {τ⊕H} | 3 binary choices | 8 configurations |
| RESIDUAL | {b, μ, d, e, W*, s*} | 6 = N | Completion register |

(*W and s appear in both BOUNDARY and RESIDUAL; role depends on boundary configuration.)

**Proof that {u, t} are forced.** From BB^T uniqueness (D.2): (BB^T)₀₁ = 1, (BB^T)₀₂ = (BB^T)₀₃ = 0. BV₀ connects to the rest ONLY through WV₁. Edges BV₀–WV₁ (= u) and BV₁–WV₁ (= t) are the unique path from BV₀ to BV₁. Removing either disconnects BV₀. Therefore u ∈ T and t ∈ T for every spanning tree T. ∎

**Proof of 3 competing pairs.**
(i) Multi-edge {c, p}: both connect BV₀–WV₀. Including both creates cycle. Exactly one per tree. 2 choices.
(ii) Far-end pair {s, W}: both at WV_E (BV₂–BV₃, degree d₁ = 2). Including both creates cycle; excluding both disconnects WV_E. Exactly one per tree. 2 choices.
(iii) Far-end pair {τ, H}: both at WV_F (BV₃–BV₂, degree d₁ = 2). Same argument. 2 choices.
Total boundary configurations: 2³ = 8. ∎

### Residual completion theorem

**Setup.** Fix a boundary triple plus forced edges {u, t}. This fixes 5 edges covering 7 vertices. Three vertices remain: BV₃, WV₂, WV₄. Six residual edges available.

**Decomposition of residual edges:**
- INTERIOR register: {b, μ, d, e} — size d₁² = 4 (edges at WV_C and WV_D, NOT incident to any far-end vertex)
- COMPENSATOR pair: non-chosen edges from WV_E and WV_F (e.g., boundary = {s, τ} → compensators = {W, H}) — size d₂ − 1 = 2

Verify: d₁² + (d₂ − 1) = 4 + 2 = 6 = N. ✓

**Theorem (Residual = d₂²).** For any boundary triple, the number of valid residual completions is exactly d₂² = 9.

**Proof.** A spanning tree on 10 vertices has 9 edges. With 5 fixed, choose 4 from 6 residual, equivalently exclude 2 from 6. Total pairs: C(6,2) = 15.

**Sole constraint:** the two compensator edges connect BV₂ and BV₃ to vertices already in core via the boundary edges. Excluding BOTH compensators disconnects a vertex. Therefore at least one compensator must be included; both cannot be excluded.

Invalid pairs = those drawn entirely from the 4-element interior register: C(d₁², 2) = C(4, 2) = 6.

Valid completions: C(N, 2) − C(d₁², 2) = 15 − 6 = **9 = d₂²**. ∎

Sage verification: all 15 pairs enumerated, 6 invalid = {b,μ}, {b,d}, {b,e}, {μ,d}, {μ,e}, {d,e} — exactly C(4,2) = 6 pairs from interior. All 8 boundary triples give 9. Total: 8 × 9 = 72 tree-triple incidences; actual trees = 40. ✓

### Ground-excitation decomposition

**Ground state (1 tree):** All 4 interior edges present, no compensator. Interior code = 1111 (Hamming weight d₁²). Connectivity through interior path b→BV₁→e and d→BV₃→μ (via σ₀-orbits).

**Excitations (8 trees):** Drop 1 of d₁² interior bits, include 1 of (d₂−1) compensators. Count: d₁² × (d₂−1) = 4 × 2 = 8.

$$d_2^2 = 1 + d_1^2(d_2 - 1)$$

Sage: interior codes for triple (c,s,τ): {1111}×1, {0111,1011,1101,1110}×2 each. Total: 1 + 4·2 = 9. ✓

### Algebraic identity

**Lemma.** The following are equivalent for d₁ ≥ 2, d₂ ≥ 2:
(a) 1 + d₁²(d₂−1) = d₂² (residual tree count)
(b) C(N,2) − C(d₁²,2) = d₂² (pair exclusion)
(c) 1 + d₂ = d₁² (Residual Tree identity; NOT G.2 which gives d₁+d₂=5 separately)

**Proof.** (a) ⟺ (c): d₁²(d₂−1) = d₂²−1 = (d₂−1)(d₂+1). Since d₂ > 1, divide: d₁² = d₂+1. ∎

(c) → d₁ = 2 uniquely: from 1+d₂ = d₁², d₂ = d₁²−1, N = d₁(d₁²−1). Residual size = N requires d₁²+(d₂−1) = d₁d₂, giving 2d₂ = d₁d₂, hence **d₁ = 2**, d₂ = 3. ∎

### The ratio

λ = d₂²/K = 9/40 = 0.22500. PDG: 0.22497 ± 0.00070, pull = **−0.04σ**.

### Structural meaning

The identity 1+d₂ = d₁² controls THREE independent structures:

| Structure | Role |
|-----------|------|
| BVP (G.2) | Vanishing orders of Φ at boundaries |
| Residual trees (E.8) | Completion count d₂² = 1+d₁²(d₂−1) |
| Uniqueness | N = d₁d₂ forces d₁ = 2 |

### Derivation chain (complete)
```
σ∞ 1-cycle [THM]
  → Anchor Lemma (m=1) [THM, D.1]
    → BB^T unique [THM, D.2]
      → σ² = {N,N−1,d₁,1} [THM, D.3]
        → Kirchhoff K = 40 [THM, D.4]
      → backbone {u,t} forced [THM, E.8]
        → 3 competing pairs [THM, E.8]
          → 6 residual = d₁²+(d₂−1) [THM, E.8]
            → valid = C(6,2)−C(4,2) = d₂² [THM, E.8]
              → λ = d₂²/K = 9/40 [THM, graph]
                → λ_CKM = 9/40 [OBS, physics gap]
```

Steps 1–10: pure mathematics. Step 11: physical identification.

### Remaining gap
The graph identity λ = d₂²/K is **proven**. The identification λ_Wolfenstein = d₂²/K remains [OBS]. Bridge from spanning-tree fraction to sin θ_C is physical, not established.


## [THM] E.9: Classification matrix of spanning trees
Source: S75
Status: [THM]
Dependencies: E.8
Verified: Sage (40/40)

### Statement
For each multi-edge choice (c or p), the 20 spanning trees classify by boundary state into a symmetric matrix:

| | W only | both(W,τ) | τ only | sum |
|---|--------|-----------|--------|-----|
| d only | 1 | 4 | 1 | 6 |
| both(d,H) | 4 | 0 | 4 | 8 |
| H only | 1 | 4 | 1 | 6 |
| **sum** | **6** | **8** | **6** | **20** |

### Key features
- Corner entries = 1 (ground state of each triple)
- Off-diagonal entries = d₁² = 4 (excitations)
- Central entry = 0 (both H and τ present = cycle, forbidden)
- Row/column sums: {6, 8, 6} = {N, d₁³, N}
- Trace = 1 + 0 + 1 = 2 = d₁
- Total per multi-edge: 20 = K/2
- Grand total: 2 × 20 = 40 = K ✓


---

# F. MASS FORMULA

## [DEF] F.1: Central formula
$$m_n = m_e \cdot \mu^{n/4} \cdot K(n) \cdot (1 + \frac{\alpha}{2\pi}[\Phi(n) - L\ell])$$

Table 1: see §A3 of context files (12 particles, 10/10 signs, RMS=1.45%).

Post-S70: Table 1 = OUTPUT of dessin (n from ecc, K from cipher).

## [THM] F.2: (n,K)-uniqueness (Thm 3.5, CORRECTED S68)
Source: Paper Thm 3.5 + erratum S68
Status: [THM]
Dependencies: δK formula (§G); **EMP_masses** (empirical particle masses → sign(δK_obs))
Verified: Sage

### Statement
The LD assignment is the unique complete (n,K)-assignment satisfying:
(A) sign(δK_obs) = sign(δK_pred) for all 10 non-anchor particles
(B') |δK_pred/δK_obs| > 1/4 for every particle with |δK_obs| > 1%

### Proof
At g = μ^{1/4} and tolerance ε = 6%, three particles admit dual options within B₁:
- d-quark: K = √2 (LD) vs K = 4/3
- charm: K = 4/3 (LD) vs K = √2
- Higgs: (n=6, K=3) (LD) vs (n=7, K=1/2)

This gives 2³ = 8 variants V1–V8.

**Step 1 (sign kills, 6/8 eliminated):**
δK_pred(c, n=4) = (α/2π)[Φ(4) − 7·3] = (α/2π)[27.43 − 21] = +0.75%.
For charm with K = √2: K_true = m_c/(m_e·g⁴) = 1270/(0.511·1838.8) = 1.352, and K_LD = √2 = 1.414 → δK_obs = (1.352−1.414)/1.414 = −4.29%. Wrong sign vs +0.75%. Kills V1, V2, V5, V6.

δK_pred(d, n=1) = (α/2π)[Φ(1) − 7·3] = (α/2π)[0.857 − 21] = −2.34%.
For d with K = 4/3: K_true = m_d/(m_e·g) = 4.67/(0.511·6.546) = 1.396, K_LD = 4/3 = 1.333 → δK_obs = +4.71%. Wrong sign vs −2.34%. Kills V5, V6, V7, V8.

Survivors after Step 1: **V3 and V4** (10/10 signs). Differ only in Higgs.

**Step 2 (capture ratio, V4 eliminated):**

**CRITICAL CORRECTION (S68):** T₃(H) = −1/2, NOT 0. The physical Higgs h arises from the neutral component H⁰ of the SU(2) doublet H = (H⁺, H⁰)^T, carrying T₃ = −1/2. After EWSB, |Q| = 0 but T₃ retained.

V4 places H at n = 7 = L (boundary). Φ(7) = 7³(1−7/7) = 0.
EW: ℓ = −2(T₃ − d₂|Q|) = −2(−1/2 − 0) = 1.
δK_pred(H, n=7) = (α/2π)[0 − 7·1] = −0.81%.

For V4 Higgs at n=7, K=1/2: K_true = m_H/(m_e·g⁷) = 125100/(0.511·6.546⁷) ≈ 0.476. δK_obs = (0.476−0.500)/0.500 = −4.9%. (Erratum value: −4.93% with exact CODATA constants.)

Capture ratio = |δK_pred|/|δK_obs| = 0.81/4.93 = **0.164 < 1/4**. Condition (B') violated.

For V3 (H at n=6, K=3): δK_pred = +2.77%, δK_obs = +3.72%, capture = 0.74 > 1/4 ✓.

**V4 ruled out. V3 (LD) is the unique survivor.** ∎

### Robustness
- RMS(V3) = 1.45% vs RMS(V4) = 1.92%. Higgs dominates: 4.12² vs 0.95².
- Proximity: V3 leads V4 by 5.2 bits on Higgs alone.
- Threshold stability: any η_min ∈ (0.164, 0.744) separates V4 from V3 (4.5× window).
- Motivation for 1/4: one cusp's worth = 1/|Div(N)| = 1/4.


## [THM] F.3: n-formulas from dessin
Source: S69–S70
Status: [THM] (quarks 6/6 exact, leptons 3/3 exact)
Dependencies: C.5 (ECC theorem)
Verified: Sage

### Quark n-formula [S69, THM: 6/6 EXACT]

**Definition:** ecc_q(e) = max{d(e, q) : q ∈ quarks, q ≠ e} in BFS metric of bipartite Cayley graph of (σ₀, σ₁).

The ECC theorem (§C.5) guarantees ecc_q ∈ {d₂, d₁², N−1} = {3, 4, 5}.

**Generation:** g = N − ecc_q ∈ {1, 2, 3}.

**n-assignment:**
n_up(g) = d₂·g − d₁ = 3g − 2   (T₃ = +1/2)
n_down(g) = d₁·g − 1 = 2g − 1  (T₃ = −1/2)

| ecc | g | up (n) | down (n) | Particles |
|-----|---|--------|----------|-----------|
| N−1 = 5 | 1 | 3·1−2 = 1 | 2·1−1 = 1 | u, d |
| d₁² = 4 | 2 | 3·2−2 = 4 | 2·2−1 = 3 | c, s |
| d₂ = 3 | 3 | 3·3−2 = 7 | 2·3−1 = 5 | t, b |

All 6 values exact. Zero parameters.

**T₃ discrimination:** Within each doublet, the quark with lower s_q (quark-quark distance sum) is the up-type (T₃ = +1/2). Verified for all 3 generations.

**Key observation [OBS, not proven]:** Coefficients in n-formulas = ramification indices: d₂ = e(j=0) for up-type, d₁ = e(j=1728) for down-type. Why d₂ controls up and d₁ controls down is OPEN.

**36/36 universality:** For all 36 dessins, the ecc→g map gives the same three ecc-classes {3,4,5} and the same n-values when the formulas are applied. The quark n-values are dessin-invariants [THM, Sage-verified].

**Parameter count caveat:** The formulas n_up = d₂g−d₁ and n_down = d₁g−1 contain 4 coefficients {d₂, d₁, d₁, 1}. These are NOT free parameters — they are fixed by Γ₀(6) (ramification indices and unit). The formulas have 0 adjustable constants. What is [OBS] is the **identification** of these coefficients with ramification indices; the formulas themselves are exact tautologies once the identification is granted.

### Lepton n-formula [S70, THM: 3/3 EXACT]

**Definition:** ecc_full(e) = max{d(e, v) : v ∈ all 12 edges} in BFS metric of full Cayley graph.

g_lep = ecc_full − d₂ + 1

n_lep(g) = (g − 1)(N − 1 − g)

| ecc_full | g | n | Particle |
|----------|---|---|----------|
| d₂ = 3 | 1 | 0·4 = 0 | e |
| d₁² = 4 | 2 | 1·3 = 3 | μ |
| N−1 = 5 | 3 | 2·2 = 4 | τ |

Quarks: linear in g (isospin doublet). Leptons: quadratic in g (singlet). This doublet/singlet distinction emerges from the graph, not imposed.

### Bosons [S69]
W and H are fully degenerate across ALL 19+ scalar graph invariants (ecc, BFS distances, BV position, quark neighbors, etc.). Both n = 6 = N. Distinguished only by EW operator ℓ (W: T₃=0, |Q|=1 → ℓ=6; H: T₃=−1/2, |Q|=0 → ℓ=1).

### Face n-sums [S70, OBS: 14/14 Γ₀(6) invariants]

| Face | Σn | = Γ₀(6) invariant |
|------|-----|-------------------|
| Quarks (6-face) | 21 | d₂·L = 3·7 |
| Leptons (3-face) | 7 | L = N+1 |
| Bosons (2-face) | 12 | index = 2N |
| Anchor (1-face) | 4 | d₁² |

All 6 WV-pair sums, all 4 BV-triple sums, all 4 face sums = Γ₀(6) invariants [DER+OBS].


## [THM] F.3a: σ₁-sector dichotomy (Isospin Theorem)
Source: S74
Status: [THM] (36/36 Sage-verified + analytical proof)
Dependencies: D.1 (Anchor Lemma), D.2 (BB^T uniqueness), C.4 (BV compositions)
Replaces: F.3 [OBS] on "coefficients = ramification indices"

### Definitions
For a quark edge e (in the 6-face of σ∞), define:
- **σ₁-sector(e)** = face size of σ₁(e)
- **hadronic** if σ₁-sector(e) ∈ {N, 1} = {6-face, 1-face} (quark or anchor)
- **electroweak (EW)** if σ₁-sector(e) ∈ {d₂, d₁} = {3-face, 2-face} (lepton or boson)

### Statement
(i) Within each generation doublet, **exactly one quark is hadronic and one is EW**. (3-3 split.)

(ii) The hadronic quark has lower s_q → T₃ = +1/2 (up-type). The EW quark has higher s_q → T₃ = −1/2 (down-type). [Verified 36/36; analytical proof OPEN.]

(iii) Doublet members are **diametrically opposite** in the 6-cycle: T³(up) = down.

### Consequence for n-formula slopes
- UP (hadronic): slope = d₂ = |σ₀-orbit| (period of black-vertex rotation)
- DOWN (EW): slope = d₁ = |σ₁-orbit| (period of white-vertex involution)

This gives: **n_up = d₂·g − d₁, n_down = d₁·g − 1.**

σ₁-hadronic quarks are "closed" within the strong sector under σ₁; their mass hierarchy is governed by σ₀ (period d₂). σ₁-EW quarks "leak" into the electroweak sector; their hierarchy is governed by σ₁ (period d₁).

### Proof of (i): 3-3 split

**Lemma (Lepton Cycle Constraint).** For a lepton edge L_a in the 3-cycle, σ₁(L_a) is in the same BV as the next lepton σ∞(L_a).

*Proof:* σ∞(L_a) = σ₀(σ₁(L_a)) = L_b. Therefore σ₁(L_a) = σ₀⁻¹(L_b) ∈ same σ₀-orbit as L_b. ∎

**Main argument:**

From BB^T uniqueness (D.2): (BB^T)₀₁ = 1, (BB^T)₀₂ = (BB^T)₀₃ = 0. BV₀ connects to BV₁ only, via exactly 1 white vertex W₁.

*Step 1 (BV₀ routing):* BV₀ = BV_anchor = {anchor, pre_anchor, quark_b} (C.4: 2Q+A). Anchor and pre_anchor share W₀ (multi-edge, Anchor Lemma D.1). Therefore quark_b is in W₁.

*Step 2 (BV₁ lepton excluded from W₁):* BV₁ = BV_index = {quark_c, quark_d, lepton_e} (C.4: 2Q+1L). By Lepton Cycle Constraint, σ₁(lepton_e) ∈ BV₂ ∪ BV₃, so lepton_e is in W₂ or W₃ — **not W₁**.

*Step 3:* The BV₁ edge in W₁ is a quark. W₁ connects quark_b (BV₀) to a quark (BV₁) = unique quark-quark σ₁-pair.

*Step 4 (3-3 count):* Hadronic quarks: pre_anchor (σ₁→anchor) + quark_b (σ₁→quark from BV₁) + that BV₁ quark (σ₁→quark_b) = **3**. EW quarks: remaining 3, σ₁-partners in {leptons, bosons} = **3**. One per generation within each doublet (verified 36/36). ∎

### Proof of (iii): doublets are diametrically opposite
Follows from ECC theorem (C.5): three doublet pairs = three ecc_q classes, each pair diametrically opposite in 6-cycle. Verified 36/36. ∎

### Offsets
n_up(g) = d₂g − d₁: offset −d₁ [OBS, not derived].
n_down(g) = d₁g − 1: offset −1 [OBS, not derived].

### Upgrade summary

| Component | Was | Now |
|-----------|-----|-----|
| d₂ → up, d₁ → down | [OBS] | **[THM]** (σ₁-sector dichotomy) |
| Slopes = permutation periods | [OBS] | **[DER]** |
| Offsets = −d₁, −1 | [OBS] | [OBS] |
| s_q → T₃ | verified 36/36 | verified 36/36, proof OPEN |
| Doublets = diametrically opposite | implicit | **[THM]**, 36/36 |


## [DER] F.4: Σn = 44 = d₁²·dim M₁₀
Source: S71 §4
Status: [DER] from n-formulas at (2,3)
Replaces: S55 [OBS]
Dependencies: F.3
Verified: Sage

### Derivation

**Quarks:** Σn_q = Σ_{g=1}^{d₂} [n_up(g) + n_down(g)] = Σ_{g=1}^{3} [(3g−2)+(2g−1)]
= Σ_{g=1}^{3} [5g−3] = (5·1−3)+(5·2−3)+(5·3−3) = 2+7+12 = 21

General: Σ = (d₁+d₂)·d₂(d₂+1)/2 − d₂(d₁+1) = 5·6 − 9 = 21 = d₂·L.

**Leptons:** Σn_l = Σ_{g=1}^{3} (g−1)(N−1−g) = 0+3+4 = 7 = L.

**Bosons:** 2·N = 12 = index.

**Anchor:** n_p = d₁² = 4.

**Total:** 21 + 7 + 12 + 4 = **44 = d₁²·dim M₁₀ = 4·11**.

Universality: checked at (d₁,d₂) ∈ {(2,3),(3,2),(2,5),(3,5),(2,7)}. Face sums d₂L and L hold ONLY at (2,3). Factorisation 44 = d₁²·(2N−1) matches only (2,3). Status: [DER] at (2,3), identification 4·11 is [OBS].


## [THM] F.5: K-cipher (11/11 label-free)
Source: S71 §1
Status: [THM] (subsumed by F.7b-K constructive derivation; was [OBS] pre-S116)
Dependencies: C.4 (BV structure)
Verified: Sage (11/11)

### Statement
For the 11 rational-K particles, K = 2^{a₂} · 3^{a₃} where:

**a₃ (3-adic valuation, 3 branches):**
- a₃ = −1 if face(e) = quark (6-face) → K contains factor 1/3
- a₃ = +1 if BV(e) = BV_star AND face ≠ quark → K contains factor 3
- a₃ = 0 otherwise → K is pure power of 2

**a₂ (2-adic valuation, 3 branches by sector):**
- Quarks (a₃ = −1): a₂ = 1 + δ(σ₁(e), anchor). All quarks get a₂ = 1 (K = 2/3) EXCEPT c (= σ₁(anchor), with σ₁(c) = p) which gets a₂ = 2 (K = 4/3). See §O.1.
- Neutral (a₃ = 0): a₂ = δ(BV(σ₁(e)), BV_star). Edge gets a₂ = 1 if its S-partner's BV is BV_star, else a₂ = 0.
- BV_star non-quark (a₃ = +1): a₂ = −2·δ(BV(σ₁(e)), BV_index). μ gets a₂ = −2 (K = 3/4); H gets a₂ = 0 (K = 3).

**d-quark:** K = √d₁ = √2 (EWSB), unique irrational. Not covered by formula.

### Verification table
| Particle | face | BV | a₃ | a₂ | K = 2^a₂·3^a₃ | K_LD |
|----------|------|----|----|----|---------------|------|
| u | Q | BV0 | −1 | 1 | 2/3 | 2/3 ✓ |
| t | Q | BV1 | −1 | 1 | 2/3 | 2/3 ✓ |
| s | Q | BV3 | −1 | 1 | 2/3 | 2/3 ✓ |
| b | Q | BV1 | −1 | 1 | 2/3 | 2/3 ✓ |
| c | Q | BV0 | −1 | 2 | 4/3 | 4/3 ✓ |
| p | A | BV0 | 0 | 0 | 1 | 1 ✓ |
| e | L | BV1 | 0 | 0 | 1 | 1 ✓ |
| τ | L | BV3 | 0 | 1 | 2 | 2 ✓ |
| μ | L | BV2 | 1 | −2 | 3/4 | 3/4 ✓ |
| W | B | BV3 | 0 | 1 | 2 | 2 ✓ |
| H | B | BV2 | 1 | 0 | 3 | 3 ✓ |

**Sage-verified: 11/11.** All label-free: anchor, BV_index, BV_star, pre_anchor defined purely graph-theoretically (§C.4).

No linear formula for a₂ exists (exhaustive search over 171 invariant pairs, S71). No polynomial degree ≤ 2 either. Mirror symmetry: K(c)·K(μ) = (4/3)·(3/4) = 1.

### Dessin-invariance [THM, 36/36, S83]
The (n, ℓ, K, face) multiset is identical across all 36 dessins. K-cipher F.5 is a dessin-invariant. See §C.7.

### CRT-irreducibility [THM, 36/36, S83]
v₃(K) is NOT a pure function of x₃ in CRT coordinates. All 4 CRT columns give mixed v₃. Unified formula K(x₂, x₃) without branching: **DEAD**. See §C.7.

### Reformulation (S84)
Three equivalent encodings found in S84 (F.5a, F.5b, F.5d). Primary variable is σ₁-partnership (BV(σ₁)), not face type. Face-pair (F, F(σ₁)) determines K for 8/12 particles; remaining 2 conflicts resolved by single BV-parity bit.


## [THM] F.5a: K-uniqueness via minimal triple (F, F(σ₁), sp)
Source: S84 (corrected after σ₁-map verification)
Status: [THM] (computational, 8/8 = 36/36 by C.3)
Dependencies: C.4 (BV structure), D.1 (Anchor Lemma)
Verified: Python (8 valid σ₀-orientations); analytical recheck against verified edge table

### Definitions

For an edge e of the dessin:
- **F(e)** = size of σ∞-face containing e. Values: {6, 3, 2, 1}.
- **F(σ₁(e))** = size of σ∞-face containing the σ₁-partner of e.
- **sp(e)** = δ(BV(e) ∈ {BV_star, BV_oth}), i.e. sp = 1 iff e is NOT in BV_anchor or BV_index.

All three quantities are label-free dessin invariants.

### Statement

The triple (F(e), F(σ₁(e)), sp(e)) uniquely determines K(e) for all 12 edges. The lookup table has 11 cells, 0 conflicts:

| F | F(σ₁) | sp | K | Particles |
|---|--------|----|---|-----------|
| 6 | 1 | 0 | 4/3 | c |
| 6 | 2 | 1 | 2/3 | s |
| 6 | 3 | 0 | 2/3 | b |
| 6 | 3 | 1 | √2 | d (EWSB) |
| 6 | 6 | 0 | 2/3 | u, t |
| 3 | 2 | 1 | 2 | τ |
| 3 | 6 | 0 | 1 | e |
| 3 | 6 | 1 | 3/4 | μ |
| 2 | 3 | 1 | 3 | H |
| 2 | 6 | 1 | 2 | W |
| 1 | 6 | 0 | 1 | p |

### Proof

**Step 1 (face pair almost suffices).**
The pair (F(e), F(σ₁(e))) takes 9 distinct values among 12 edges. Two conflicts:
- (6, 3): b (K=2/3, BV=idx) vs d (K=√2, BV=oth).
- (3, 6): e (K=1, BV=idx) vs μ (K=3/4, BV=star).
All other 8 particles have K uniquely determined by face pair alone.

**Step 2 (one bit resolves both conflicts).**
Both conflicts have one edge in BV ∈ {anc, idx} (sp=0) and one in BV ∈ {star, oth} (sp=1). The bit sp = δ(BV ∉ {anc, idx}) resolves both simultaneously.

**Step 3 (verification).**
All 11 cells checked for 8 valid dessins. By C.3, extends to 36/36. ∎

### Minimality
The sp bit must satisfy: bit(idx) ≠ bit(oth) and bit(idx) ≠ bit(star). There are exactly 2 non-complementary BV-based bits with this property: sp = BV ∉ {anc, idx} (chosen, gives 11 cells) and sp = BV ≠ idx (gives 12 cells, splits u from t unnecessarily). No 2-variable encoding without BV information achieves 0 conflicts.

### Correction note
Original S84 transfer had u ↔ c swapped in σ₁-column (σ₁(u) was listed as p instead of t). Corrected using code-verified edge table. Conflicts changed from {(6,6), (3,6)} to {(6,3), (3,6)}; sp bit changed from δ(pre_anchor) ∨ δ(BV_star) to δ(BV ∉ {anc, idx}).


## [THM] F.5b: a₂-formula via BV(σ₁)-stratification
Source: S84 (corrected after σ₁-map verification)
Status: [THM] (analytical, 11/11; verified against code-checked edge table)
Dependencies: C.4, F.5
Verified: All 11 rational-K cases checked individually

### Statement

Let S = BV_label(σ₁(e)), F = face(e), BV = BV_label(e). For the 11 rational-K particles (excluding d-quark with K = √2):

**3-adic valuation** (unchanged from F.5):
$$a_3(e) = -\delta(F, 6) + \delta(\text{BV}, \text{star}) \cdot (1 - \delta(F, 6))$$

**2-adic valuation:**
$$a_2(e) = \delta(S, \text{star}) + \delta(S, \text{anc}) \cdot [\delta(F, 6) + \delta(\sigma_1(e), \text{anchor})] + \delta(S, \text{idx}) \cdot [1 - d_2 \cdot \delta(\text{BV}, \text{star})] + \delta(S, \text{oth}) \cdot \delta(F, 6)$$

Then K(e) = 2^{a₂} · 3^{a₃}.

### Proof (stratification by S = BV(σ₁))

**Case S = star** (edges: b, W, τ).
a₂ = 1. K(b) = 2/3 ✓, K(W) = 2 ✓, K(τ) = 2 ✓.

**Case S = anc** (edges: c, t, p).
a₂ = δ(F,6) + δ(σ₁(e), anchor).
- c (F=6, σ₁(c)=p=anchor): a₂ = 1+1 = 2 → K = 4/3 ✓
- t (F=6, σ₁(t)=u≠anchor): a₂ = 1+0 = 1 → K = 2/3 ✓
- p (F=1, σ₁(p)=c≠anchor): a₂ = 0+0 = 0 → K = 1 ✓

**Case S = idx** (edges: u, μ; d excluded as EWSB).
a₂ = 1 − d₂·δ(BV, star).
- u (BV=anc): a₂ = 1−0 = 1 → K = 2/3 ✓
- μ (BV=star): a₂ = 1−3 = −2 → K = 3/4 ✓

**Case S = oth** (edges: e, s, H).
a₂ = δ(F, 6).
- e (F=3): a₂ = 0 → K = 1 ✓
- s (F=6): a₂ = 1 → K = 2/3 ✓
- H (F=2): a₂ = 0 → K = 3 ✓

All 11/11 match. ∎

### Key structural features

1. **S=star and S=oth are trivial:** a₂ = 1 (S=star) or a₂ = δ(F,6) (S=oth). No BV information needed for 6 edges.

2. **The coefficient −d₂ = −3** appears uniquely for μ (BV=star within S=idx), producing K(μ) = 3/4 as the mirror of K(c) = 4/3.

3. **σ₁(e)=anchor term** appears in S=anc: c is the unique edge with σ₁(c) = p = anchor. Note: c = σ₁(anchor), while pre_anchor = σ₀⁻¹(p) = u (which is in S=idx, not S=anc). See §O.1.

4. **Comparison with F.5 (original cipher).** F.5 branches by face type as primary variable; F.5b branches by BV(σ₁). Both give 11/11. F.5b reveals that σ₁-partnership organizes K-values into 4 columns of 3 edges each.

### Correction note
Original S84 transfer had S-strat {S=anc: u,t,p; S=idx: c,s,μ}. Corrected to {S=anc: c,t,p; S=idx: u,μ} after σ₁-map fix. Formula restructured accordingly.


## [DEAD] F.5c: Mon-irreps and stabilisers
Source: S84
Status: [DEAD]

Mon = ⟨σ₀, σ₁⟩ acts **transitively** on the 12 edges. Every edge has |Stab_Mon(e)| = 72/12 = 6. K is NOT a class function of Mon. Irreducible representations and stabiliser subgroups do not distinguish edges. Closes directions B (character theory) and C (stabiliser analysis) from S83 transfer.


## [THM] F.5d: K-uniqueness via full BV triple (F, BV, BV(σ₁))
Source: S84 (corrected after σ₁-map verification)
Status: [THM] (computational, 8/8 = 36/36 by C.3)
Dependencies: C.4

### Statement

The triple (face(e), BV_label(e), BV_label(σ₁(e))) uniquely determines K(e) for all 12 edges. Of 4×4×4 = 64 abstract cells, exactly 12 are occupied, 0 collisions.

### Occupied cells

| face | BV | BV(σ₁) | K | Particle |
|------|----|--------|---|----------|
| 6 | anc | anc | 4/3 | c |
| 6 | anc | idx | 2/3 | u |
| 6 | idx | anc | 2/3 | t |
| 6 | idx | star | 2/3 | b |
| 6 | star | oth | 2/3 | s |
| 6 | oth | idx | √2 | d |
| 3 | idx | oth | 1 | e |
| 3 | star | idx | 3/4 | μ |
| 3 | oth | star | 2 | τ |
| 2 | star | oth | 3 | H |
| 2 | oth | star | 2 | W |
| 1 | anc | anc | 1 | p |

### Relation to F.5a
F.5d uses full BV labels (16 possibilities for (BV, BV(σ₁))), while F.5a collapses this to a single bit. The 12 occupied cells of F.5d map to the 11 cells of F.5a (u and t merge since both sp=0, same K).

### Correction note
Original S84 had u↔c and s↔d swapped in BV/BV(σ₁) columns. Corrected from verified edge table.


## [THM-arith] F.5e: Mirror symmetries of K
Source: S84
Status: [THM-arith] (arithmetic on K values derived by F.7b-K; was [OBS] pre-S116)

| Pair | Mechanism | Product |
|------|-----------|---------|
| K(c)·K(μ) = 4/3 · 3/4 | a₂(c)=+2, a₂(μ)=−2 (exact negatives) | 1 |
| K(H)·K(W) = 3 · 2 | H(star,oth) ↔ W(oth,star): BV↔BV(σ₁) swap | N = 6 |
| K(τ)·K(e) = 2 · 1 | τ(oth,star) ↔ e(idx,oth): gen 3↔1 leptonic | d₁ = 2 |

The c-μ mirror (product = 1) connects S=anc (c) with S=idx (μ). The coefficient −d₂ creating K(μ)=3/4 is the exact inverse of the σ₁(c)=anchor +1 creating K(c)=4/3: both are anchor-proximity effects amplified by d₂.


## Updated K-cipher derivation chain

```
σ∞ 1-cycle [THM]
  → Anchor Lemma (m=1) [THM, D.1]
    → pre_anchor = σ₀⁻¹(anchor) [DEF, label-free]
    → BV_star = BV(T³(σ₁(anchor))) [DEF, label-free]
      → sp(e) = δ(BV ∉ {anc, idx}) [DEF]

σ∞ cycle type (6,3,2,1) [THM]
  → F(e) for all 12 edges [THM]
σ₁ involution [THM]
  → F(σ₁(e)) for all 12 edges [THM]
σ₀ rotation [THM]
  → F(σ₀(e)) for all 12 edges [THM]

K-cipher encodings (all equivalent, all 36/36):
  (F, F(σ₁), sp) → K unique (11 cells)              [THM, F.5a]
  (F, BV, BV(σ₁)) → K unique (12 cells)              [THM, F.5d]
  (F, F(σ₁), F(σ₀)) → K unique (12 cells)            [THM, F.6]  ← LABEL-FREE
  ε, η → (g, v₂, v₃) → (n, K) constructive           [THM, F.7/F.7b/F.7b-K]  ← CONSTRUCTIVE

Dead directions:
  Mon-irreps, |Stab| → K not class function [DEAD, F.5c]
  CRT-coordinates → K CRT-irreducible       [DEAD, S83]
  Linear/polynomial a₂ → empty              [DEAD, S71]
  Unified K(x₂, x₃) → DEAD                 [DEAD, S83]
```


## [THM] F.6: Three-Cusp Cipher (12/12, 36/36)
Source: S86
Status: [THM]
Dependencies: C.1 (dessin), C.3 (uniqueness 36/36)
Verified: Python (12/12 edges, 8/8 orientations = 36/36 by C.3)

### Statement
The triple (F(e), F(σ₁(e)), F(σ₀(e))) uniquely determines K(e) for all 12 edges. Zero collisions among 12 of 4³ = 64 cells in Div(N)³.

| (F, Fσ₁, Fσ₀) | Particle | n | K | v₂ | v₃ |
|:---------------:|:--------:|:-:|:-:|:--:|:--:|
| (6, 1, 6) | c | 4 | 4/3 | 2 | −1 |
| (6, 6, 1) | u | 1 | 2/3 | 1 | −1 |
| (6, 6, 3) | t | 7 | 2/3 | 1 | −1 |
| (6, 3, 6) | b | 5 | 2/3 | 1 | −1 |
| (6, 2, 3) | s | 3 | 2/3 | 1 | −1 |
| (6, 3, 2) | d | 1 | √2 | 1/2 | 0 |
| (3, 6, 6) | e | 0 | 1 | 0 | 0 |
| (3, 6, 2) | μ | 3 | 3/4 | −2 | 1 |
| (3, 2, 6) | τ | 4 | 2 | 1 | 0 |
| (2, 3, 6) | H | 6 | 3 | 0 | 1 |
| (2, 6, 3) | W | 6 | 2 | 1 | 0 |
| (1, 6, 6) | p | 4 | 1 | 0 | 0 |

### Proof of uniqueness
Within each face sector F ∈ {6,3,2,1}, the (Fσ₁, Fσ₀) pairs are all distinct. ∎

### Relation to F.5a
F.6 supersedes F.5a: it uses (F, Fσ₁, Fσ₀) instead of (F, Fσ₁, sp), removing the BV-parity bit entirely. Both σ₀ and σ₁ channels now enter directly.

### Cipher hierarchy
Three equivalent layers:
- F.5a: (F, Fσ₁, sp) — σ₀-free, needs BV-parity bit
- **F.6: (F, Fσ₁, Fσ₀) — label-free, needs σ₀ [THM]**
- F.7: same data → ε, η → (g, v₂, v₃) → (n, K) — **constructive** [THM]


## [THM] F.6.2: v₃ from Triple (12/12)
Source: S86
Status: [THM]
Dependencies: F.6
Verified: Python (12/12)

### Statement

| Sector | v₃ formula | Verification |
|--------|-----------|-------------|
| Quarks (F=N, K≠√2) | v₃ = −1 | c,u,t,b,s: all −1 ✓ |
| **d-quark (EWSB)** | **v₃ = 0** | K = √2 = 2^{1/2}·3⁰ ✓ |
| Leptons (F=d₂) | v₃ = δ(Fσ₀ = d₁) | μ:1 ✓, e:0 ✓, τ:0 ✓ |
| Bosons (F=d₁) | v₃ = δ(Fσ₁ = d₂) | H:1 ✓, W:0 ✓ |
| Anchor (F=1) | v₃ = 0 | p:0 ✓ |

Cross-channel duality: leptons query σ₀ for d₁; bosons query σ₁ for d₂.


## [THM] F.7c: Product Constraint (12/12)
Source: S87
Status: [THM]
Dependencies: F.6
Verified: Python (exhaustive Div(N)³ enumeration)

### Statement
For every edge e of the X₀(6) dessin:

$$F(e) \cdot F(\sigma_1(e)) \cdot F(\sigma_0(e)) \in \{N^2,\; d_2 N^2\} = \{36, 108\}$$

Selects exactly 12 cells from Div(N)³ = 64 total. These 12 are precisely the occupied cells of F.6.

Product = d₂N² = 108 for exactly 3 edges {t, b, e} = BV\_idx.
Product = N² = 36 for the remaining 9 edges.

### Proof
Exhaustive enumeration: Div(N)³ contains exactly 9 triples with product 36 and 3 with product 108. Face-conditional count matches edge counts per sector (6+3+2+1). ∎


## [THM] F.7: Generation from Triple (12/12)
Source: S87
Status: [THM]
Dependencies: F.6
Verified: Python (12/12)

### ε-η indicator functions on Div(N) = {1, 2, 3, 6}

**ε(w) = δ(gcd(w, d₂) = 1)** — "SU(3)-invisible" indicator

| w | 1 | d₁=2 | d₂=3 | N=6 |
|---|:-:|:----:|:----:|:---:|
| ε | 1 | 1 | 0 | 0 |

**η(w) = δ(w ∈ {1, N})** — "non-gauge" indicator

| w | 1 | d₁=2 | d₂=3 | N=6 |
|---|:-:|:----:|:----:|:---:|
| η | 1 | 0 | 0 | 1 |

The pair (ε, η) is a complete coordinate system on Div(N): w=1↔(1,1), w=d₁↔(1,0), w=d₂↔(0,0), w=N↔(0,1).

### Shorthand
ε₀ = ε(Fσ₀(e)), ε₁ = ε(Fσ₁(e)), η₁ = η(Fσ₁(e)).

### Quarks (F = N), 6/6

$$g(e) = d_2 - d_1 \varepsilon_0 - \varepsilon_1$$

isUp(e) = η(Fσ₁) (isospin indicator)

$$n(e) = \text{isUp} \cdot (d_2 g - d_1) + (1 - \text{isUp}) \cdot (d_1 g - 1)$$

| Particle | (F, Fσ₁, Fσ₀) | ε₁ | ε₀ | g | isUp | n |
|----------|:--------------:|:--:|:--:|:-:|:----:|:-:|
| c | (6, 1, 6) | 1 | 0 | 2 | 1 | 4 |
| u | (6, 6, 1) | 0 | 1 | 1 | 1 | 1 |
| t | (6, 6, 3) | 0 | 0 | 3 | 1 | 7 |
| b | (6, 3, 6) | 0 | 0 | 3 | 0 | 5 |
| s | (6, 2, 3) | 1 | 0 | 2 | 0 | 3 |
| d | (6, 3, 2) | 0 | 1 | 1 | 0 | 1 |

### Leptons (F = d₂), 3/3

$$g(e) = 1 + \varepsilon_0 + d_1 \varepsilon_1$$

$$n(e) = (g - 1)(N - 1 - g)$$

| Particle | (F, Fσ₁, Fσ₀) | ε₁ | ε₀ | g | n |
|----------|:--------------:|:--:|:--:|:-:|:-:|
| e | (3, 6, 6) | 0 | 0 | 1 | 0 |
| μ | (3, 6, 2) | 0 | 1 | 2 | 3 |
| τ | (3, 2, 6) | 1 | 0 | 3 | 4 |

### Bosons (F = d₁), 2/2
n = N = 6 (constant).

### Anchor (F = 1), 1/1
n = d₁² = 4 (constant).

### Channel-weight duality [THM]

| Sector | g formula | σ₀ weight | σ₁ weight |
|--------|-----------|:---------:|:---------:|
| Quarks | d₂ − d₁ε₀ − ε₁ | **d₁** | 1 |
| Leptons | 1 + ε₀ + d₁ε₁ | 1 | **d₁** |

Quarks: colour channel (σ₀) dominates. Leptons: isospin channel (σ₁) dominates. ∎

### Relation to F.3
F.7 subsumes the n-formulas of F.3: same results, but derived from face-size triples via ε, η instead of graph eccentricities. The ECC theorem (C.5) remains the topological backbone; F.7 shows how ε-η encodes the same information constructively.

### Relation to F.3a
F.7 absorbs the σ₁-sector dichotomy: isUp = η₁ = δ(Fσ₁ ∈ {1,N}) reads isospin directly from the face triple. The slope d₂ (up) vs d₁ (down) follows from the quark n-formula structure.


## [THM] F.7b: v₂ from Triple (12/12)
Source: S87
Status: [THM]
Dependencies: F.6, F.7
Verified: Python (12/12)

### Statement

| Sector | v₂ formula |
|--------|-----------|
| Quarks (F=N, K rational) | v₂ = 1 + ε₁·η₁ |
| d-quark (EWSB) | v₂ = 1/d₁ = 1/2 |
| Leptons (F=d₂) | v₂ = ε₁ − d₁·ε₀ |
| Bosons (F=d₁) | v₂ = (1−ε₁)·η₁ |
| Anchor (F=1) | v₂ = 0 |

### Verification table

| Particle | (F, Fσ₁, Fσ₀) | ε₁ | ε₀ | η₁ | v₂ | ✓ |
|----------|:--------------:|:--:|:--:|:--:|:--:|:-:|
| c | (6, 1, 6) | 1 | 0 | 1 | 2 | ✓ |
| u | (6, 6, 1) | 0 | 1 | 1 | 1 | ✓ |
| t | (6, 6, 3) | 0 | 0 | 1 | 1 | ✓ |
| b | (6, 3, 6) | 0 | 0 | 0 | 1 | ✓ |
| s | (6, 2, 3) | 1 | 0 | 0 | 1 | ✓ |
| d | (6, 3, 2) | — | — | — | 1/2 | ✓ (EWSB) |
| e | (3, 6, 6) | 0 | 0 | — | 0 | ✓ |
| μ | (3, 6, 2) | 0 | 1 | — | −2 | ✓ |
| τ | (3, 2, 6) | 1 | 0 | — | 1 | ✓ |
| H | (2, 3, 6) | 0 | 0 | 0 | 0 | ✓ |
| W | (2, 6, 3) | 0 | 0 | 1 | 1 | ✓ |
| p | (1, 6, 6) | — | — | — | 0 | ✓ |

### Key insight [S87]
μ is NOT anomalous. v₂(μ) = ε(6) − 2·ε(2) = 0 − 2 = −2 follows from the regular leptonic formula. Only d-quark (K = √2, EWSB) is structurally exceptional.


## [THM] F.7b-K: K-Reconstruction (11/11 + 1 EWSB)
Source: S87
Status: [THM]
Dependencies: F.6.2 (v₃), F.7b (v₂)
Verified: Python (12/12)

### Statement
For all 11 rational-K particles:

$$K(e) = 2^{v_2(e)} \cdot 3^{v_3(e)}$$

The d-quark has K = √d₁ = √2 (B.5 triple anomaly: v₂ = 1/d₁, v₃ = 0, K ∉ ⟨2,3⟩∩ℚ).

| Particle | v₂ | v₃ | K = 2^v₂ · 3^v₃ | ✓ |
|----------|:--:|:--:|:---------------:|:-:|
| c | 2 | −1 | 4/3 | ✓ |
| u | 1 | −1 | 2/3 | ✓ |
| t | 1 | −1 | 2/3 | ✓ |
| b | 1 | −1 | 2/3 | ✓ |
| s | 1 | −1 | 2/3 | ✓ |
| e | 0 | 0 | 1 | ✓ |
| μ | −2 | 1 | 3/4 | ✓ |
| τ | 1 | 0 | 2 | ✓ |
| H | 0 | 1 | 3 | ✓ |
| W | 1 | 0 | 2 | ✓ |
| p | 0 | 0 | 1 | ✓ |
| d | 1/2 | 0 | √2 | ✓ (EWSB) |

### Complete derivation chain

```
INPUT: Dessin d'enfant of X₀(6), monodromy (σ₀, σ₁, σ∞ = σ₁∘σ₀)
  │
  ▼
STEP 1: F(e) ∈ Div(N) = {1,2,3,6}  [from σ∞]
  → 4 sectors: quarks(6), leptons(3), bosons(2), anchor(1)
  │
  ▼
STEP 2: Triple (F, Fσ₁, Fσ₀) ∈ Div(N)³
  Product constraint: F·Fσ₁·Fσ₀ ∈ {N², d₂N²}  [THM F.7c]
  → selects 12 of 64 cells
  │
  ▼
STEP 3: ε(w) = δ(gcd(w,d₂)=1), η(w) = δ(w∈{1,N})  [DEF]
  │
  ▼
STEP 4: g from ε₀,ε₁  [THM F.7]
  │
  ▼
STEP 5: n from g  [THM F.7]
  │
  ▼
STEP 6: v₃ from sector + triple  [THM F.6.2]
  │
  ▼
STEP 7: v₂ from sector + ε,η  [THM F.7b]
  │
  ▼
STEP 8: K = 2^v₂ · 3^v₃  [THM F.7b-K]
  │
  ▼
OUTPUT: Complete particle identity (n, K) from pure cusp arithmetic
```


## [THM-arith] F.7d: Global n-polynomial (10 terms, 12/12)
Source: S127 (DFT §1.1)
Status: [THM-arith] (unique minimal; exhaustive search over C(16,k) subsets, k=7..10)
Dependencies: F.7 (ε-η bits)
Verified: Python (12/12)

### Statement

A single polynomial over all 12 particles:

n = N·εF + (N−1)·ηF + (N−1)·ε₀ + d₁²·ε₁
    − d₂²·ηF·εF − d₂²·ηF·ε₀ − N·ηF·ε₁
    + d₁·ηF·η₁ − d₁·ε₀·η₁ − ε₁·η₁

ALL 10 coefficients ∈ {±1, ±d₁, ±d₁², ±d₂², ±N, ±(N−1)} = LD monomials.

**Minimality:** exhaustive search shows no polynomial with fewer than 10 terms and integer coefficients reproduces n for all 12 particles. The 5 bits (εF, ηF, ε₀, ε₁, η₁) with pairwise products span rank 12 (= full diagonal space, §F.7f), so degree ≤ 2 suffices.

### Relation to F.7

F.7 gives sector-specific formulas (3 terms for quarks, 4 for leptons, constants for bosons/anchor). F.7d is the unified global version — one formula for all particles, no branching.


## [THM-arith] F.7e: Global ℓ-polynomial (5 terms, 12/12)
Source: S127 (DFT §1.2)
Status: [THM-arith]
Dependencies: F.7 (ε-η bits)
Verified: Python (12/12)

### Statement

ℓ = L − N·εF − d₁²·ηF − d₁·εF·ηF + (N−1)·εF·η₁

Coefficients: {L, −N, −d₁², −d₁, N−1}. All LD monomials. 5 terms only.

### Consequence for G.8

This polynomial derives ℓ for ALL 12 particles (including bosons W and H) from ε-η bits alone — **no SM quantum numbers needed**. The η₁ = η(Fσ₁) bit distinguishes W (η₁=1, Fσ₁=N) from H (η₁=0, Fσ₁=d₂), giving ℓ(W)=6 and ℓ(H)=1 purely from dessin data. Supersedes the G.8 dependency note on SM_QN for bosons.


## [THM-comb] F.7f: ε-η algebra completeness
Source: S125 (DFT §1.4)
Status: [THM-comb]
Dependencies: F.7 (ε-η bits)

### Statement

The 5 indicator bits (εF, ηF, ε₀, ε₁, η₁) and their pairwise products span a rank-12 space — the FULL diagonal space on the 12-particle set. Any function f: {12 particles} → ℝ is a polynomial of degree ≤ 2 in the 5 bits.

### Consequence

The ε-η architecture is algebraically complete: it does not miss any particle-distinguishing information that monodromy provides. The n-formula (F.7d) and ℓ-formula (F.7e) are not ad hoc — they are the UNIQUE low-degree polynomials for n and ℓ in this complete basis.


## [THM-arith/OBS] F.8: BV-level sums
Source: S87
Status: [THM-arith/OBS] (Σn from F.3 [THM]; Σℓ fully from ε-η [THM, F.7e]; was [OBS] pre-S116, Σℓ upgraded S127)

| BV | Edges | Σℓ | = | Σn | = |
|----|-------|:---:|:-:|:---:|:-:|
| anc | c, u, p | 6 | N | 9 | d₂² |
| idx | b, t, e | 13 | d₁²+d₂² | 12 | index |
| star | s, μ, H | 11 | dim M₁₀ | 12 | index |
| oth | d, W, τ | 16 | d₁⁴ | 11 | dim M₁₀ |

Totals: Σℓ = 46, Σn = 44 = d₁²·dim M₁₀.

F.7c product dichotomy: product = d₂N² ⟺ BV\_idx = {b, t, e}. Status: [OBS].


## [THM-comb] F.9: Minimal identifying set from F.1 ingredients (S146)
Source: S146
Status: [THM-comb]
Dependencies: F.1 (mass formula), F.3 (n), F.7e (ℓ), F.5 (K)
Verified: exhaustive enumeration of 66 particle pairs

### Statement

Φ(n)−Lℓ distinguishes 65 of 66 particle pairs. The sole collision is (u, d): both have (n, ℓ) = (1, 3). Resolved by K(u) = 2/3 ≠ K(d) = √2.

Consequence: **{n, K}** is a minimal complete identifier of all 12 particles among F.1 ingredients {n, ℓ, K}. K is necessary: u and d are identical in (n, ℓ), hence in any f(n, ℓ). The √2 anomaly (B.5) is the sole obstruction to (n, ℓ)-completeness.

Note: Φ−Lℓ has exactly the same resolving power as the pair (n, ℓ) on the 12-particle set (both collide only at (u, d)). The nonlinearity of Φ(n) = n³(1−n/L) does not add information beyond what (n, ℓ) already provides.


## Channel Duality Summary

```
  ┌────────────┬───────────────────┬───────────────────┐
  │            │   σ₀ (colour)     │   σ₁ (isospin)    │
  ├────────────┼───────────────────┼───────────────────┤
  │ Quarks g   │  weight = d₁      │  weight = 1       │
  │ Leptons g  │  weight = 1       │  weight = d₁      │
  ├────────────┼───────────────────┼───────────────────┤
  │ Leptons v₃ │  queries d₁       │       —           │
  │ Bosons v₃  │       —           │  queries d₂       │
  ├────────────┼───────────────────┼───────────────────┤
  │ Leptons v₂ │  weight = −d₁     │  weight = +1      │
  │ Quarks v₂  │       —           │  ε₁·η₁ bonus      │
  │ Bosons v₂  │       —           │  (1−ε₁)·η₁       │
  └────────────┴───────────────────┴───────────────────┘
```

Each sector reads its K-content from the OTHER channel. This is the ε-η architecture: a single pair of indicator functions on Div(N) replaces all BV-label branching of F.5.


---

# G. δK FORMULA

## [DEF] G.0: The unified δK formula
Source: Paper §6, eq. (7)

### Statement
$$\frac{\delta K}{K} = \frac{\alpha}{2\pi}\left[\Phi(n) - L \cdot \ell\right]$$

where:
- Φ(n) = n^{d₂}(1 − n/L)^{d₁−1} = n³(1 − n/7) is the polynomial part
- L = N + 1 = 7 is the lattice boundary
- ℓ = −2(T₃ − d₂|Q|) is the electroweak operator
- α/(2π) is the 1-loop coupling

### Full prediction table (0 free parameters)

| Particle | n | ℓ | Φ(n) | L·ℓ | δK_pred (%) | δK_obs (%) | sign |
|----------|---|---|------|-----|------------|------------|------|
| u | 1 | 3 | 0.857 | 21 | −2.34 | −3.14 | ✓ |
| d | 1 | 3 | 0.857 | 21 | −2.34 | −1.28 | ✓ |
| μ | 3 | 7 | 15.43 | 49 | −3.90 | −1.71 | ✓ |
| s | 3 | 3 | 15.43 | 21 | −0.65 | −2.26 | ✓ |
| c | 4 | 3 | 27.43 | 21 | +0.75 | +1.52 | ✓ |
| τ | 4 | 7 | 27.43 | 49 | −2.51 | −5.31 | ✓ |
| b | 5 | 3 | 35.71 | 21 | +1.71 | +2.09 | ✓ |
| W | 6 | 6 | 30.86 | 42 | −1.29 | −0.04 | ✓ |
| H | 6 | 1 | 30.86 | 7 | +2.77 | +3.72 | ✓ |
| t | 7 | 3 | 0.00 | 21 | −2.44 | −1.58 | ✓ |

Signs: **10/10**. RMS = 1.45%. Zero **continuous** adjustable parameters.

### Parameter honesty
- **Continuous free parameters: 0.** Once mₑ and α_s are given, every number in the table above is computed, not fitted.
- **Discrete selections: 4.** (i) Γ₀ family [L0 postulate], (ii) D₀ twist from 4 candidates [selected by 10/10 signs + BVP, §G.5], (iii) additive form Φ−Lℓ [postulated, Gap 3], (iv) K_d = √2 [from EWSB, outside B₁ lattice]. When the paper states "zero free parameters", it means (0 continuous). The four discrete selections are structural choices, each motivated but not derived from a single principle.

Φ(n) values: Φ(1) = 6/7 = 0.857, Φ(3) = 108/7 = 15.43, Φ(4) = 192/7 = 27.43, Φ(5) = 250/7 = 35.71, Φ(6) = 216/7 = 30.86, Φ(7) = 0.

### Honest assessment: F.1 / G.0 as LO rule (S140–S141, verified S142)

F.1 is a **leading-order (LO) mass rule**, not an exact formula:
- **Signs:** 10/10 correct [THM]. Non-trivial constraint on any exact mass function.
- **Improvement over tree:** 8/10 masses improved, factor 1.84× (RMS: 2.74% → 1.49%). Worsened: μ (tree +1.7%, LO −2.2%) and W (tree +0.0%, LO −1.3%).
- **R² = 0.68** (δK_pred vs δK_obs, 10 particles, excluding anchor e and composite p).
- **Residual:** RMS_resid / RMS_obs = 0.54. Not perturbative — over half the signal is unexplained residual.
- **τ/μ ratio** worsens: tree +3.8%, LO +5.3%.
- **Non-additivity:** Φ_exp at same n differs by up to 33 (μ vs s at n=3). Exact δK depends on full (n, ℓ, K) triple jointly, not additively as Φ(n) − Lℓ.
- **Median mass error:** 1.9% (tree) → 1.1% (LO).

**Erratum S140:** "RMS_resid/RMS = 0.80" and "86% unexplained" were wrong — included anchor e as prediction (dK_obs = 0 for anchor), which was the largest single residual. Corrected S141.

**Implication for paper:** F.1 should be presented as "leading-order mass rule" with 10/10 signs. The 0 continuous parameters claim is valid. The formula is approximate — NLO correction G.0b (S168) introduces face(σ₁)-dependent multiplier h, improving R² from 0.68 to 0.89 at 0 free params. See reformulated Gap 3 (§Y.1).


### G.0a [THM-arith, S153] Irrep decomposition of Φ−Lℓ

The δK numerator vector Φ(n)−L·ℓ on the 12-particle set decomposes as:

| Irrep | ‖P_ρ(Φ−Lℓ)‖² | Fraction | % | Dim/12 |
|-------|---------------|----------|---|--------|
| V₁   | 49152/49      | 1003.1   | 14.4% |  8.3% |
| V₂   | 2919/2        | 1459.5   | 20.9% | 16.7% |
| V₃   | 123196/49     | 2514.2   | **36.0%** | 25.0% |
| V₆   | 196349/98     | 2003.6   | 28.7% | 50.0% |

‖Φ−Lℓ‖² = 342038/49. SPW check: Σ = 342038/49 ✓.

All values computed in exact Fraction arithmetic from n derived via F.7 formulas
applied to O.1 monodromy (DERIVE-NOT-HARDCODE rule, S153).

**Key observations:**

**(a)** V₃ (triv_{S₃}⊗std_{A₄}) is the **dominant** irrep of Φ−Lℓ at 36.0%, despite dim V₃ = 3 (25% of dim 12). The A₄-standard representation carries the largest share.

**(b)** V₂ content = 20.9%, close to its dimensional share (16.7%). NOT dominant.

**(c)** V₁ component: Σ(Φ−Lℓ) = −768/7 = −d₁⁸d₂/L.
  768 = 2⁸·3 = d₁⁸·d₂. Clean LD monomial.

**(d)** Correct sums: Σn = 44 (NOT 39). ⟨n⟩ = 11/3 (NOT 13/4).

**σ₁-pair structure of Φ−Lℓ:**

| σ₁-pair | Φ−Lℓ(1)  | Φ−Lℓ(2)  | Sum       | Diff      |
|---------|----------|----------|-----------|-----------|
| u, t    | −141/7   | −21      | −288/7    | 6/7       |
| c, p    | 45/7     | 192/7    | 237/7     | −21 = −d₂L |
| b, μ    | 103/7    | −235/7   | −132/7    | 338/7     |
| d, e    | −141/7   | −49      | −484/7    | 202/7     |
| s, W    | −39/7    | −78/7    | −117/7    | 39/7      |
| τ, H    | −151/7   | 167/7    | 16/7      | −318/7    |

Note: (c,p) diff = −21 = −d₂L is the only clean LD monomial among differences.
This follows from ℓ(c)−ℓ(p) = 3−0 = d₂ and Φ(4)−Φ(4) = 0 → diff = −L·d₂ = −d₂L.

Dependencies: F.7 (n, derived from monodromy), G.0 (ℓ, derived from G.8/F.7e), S.6 (irreps), O.1 (σ₁-pairs).


### [OBS, S168] G.0b: NLO mass rule with face(σ₁) modifier

#### Statement

$$\frac{\delta K}{K} = h(F_{\sigma_1}) \cdot \frac{\alpha}{2\pi} \cdot [\Phi(n) - L\ell]$$

where F_{σ₁} = face(σ₁(e)) = size of σ∞-cycle containing the σ₁-partner of e,
and:

| F_{σ₁} | h | LD monomial | Particles with this F_{σ₁} |
|---------|---|-------------|---------------------------|
| 1 (anchor) | 2 | d₁ | c (σ₁→p) |
| 2 (boson) | 9/4 | d₂²/d₁² | s (σ₁→W), τ (σ₁→H) |
| 3 (lepton) | 1 | 1 | d (σ₁→e), b (σ₁→μ), H (σ₁→τ) |
| 6 (quark) | 2/3 | d₁/d₂ | u (σ₁→t), t (σ₁→u), μ (σ₁→b), W (σ₁→s) |

#### Performance

| Metric | F.1 (LO) | G.0b (NLO) |
|--------|----------|-----------|
| R² | 0.676 | **0.891** |
| RMS | 1.46% | **0.84%** |
| Signs | 10/10 | 10/10 |
| Continuous free params | 0 | **0** |

#### Full prediction table

| Particle | n | ℓ | F_{σ₁} | h | δK_pred (%) | δK_obs (%) | resid (%) |
|----------|---|---|---------|---|------------|------------|----------|
| u | 1 | 3 | 6 | 2/3 | −1.56 | −3.14 | −1.58 |
| d | 1 | 3 | 3 | 1 | −2.34 | −1.28 | +1.06 |
| s | 3 | 3 | 2 | 9/4 | −1.46 | −2.26 | −0.80 |
| c | 4 | 3 | 1 | 2 | +1.49 | +1.52 | +0.02 |
| b | 5 | 3 | 3 | 1 | +1.71 | +2.08 | +0.38 |
| t | 7 | 3 | 6 | 2/3 | −1.63 | −1.58 | +0.05 |
| μ | 3 | 7 | 6 | 2/3 | −2.60 | −1.71 | +0.89 |
| τ | 4 | 7 | 2 | 9/4 | −5.64 | −5.31 | +0.32 |
| W | 6 | 6 | 6 | 2/3 | −0.86 | −0.05 | +0.77 |
| H | 6 | 1 | 3 | 1 | +2.77 | +3.84 | +1.07 |

W anomaly (G.7) persists: δK_obs ≈ 0, δK_pred = −0.86%. Gauge protection.
Without W: R² = 0.902 (9 particles).

#### Discovery path

Doublet diagnostic: within same-n pairs, Φ cancels → pure ℓ-splitting test.

| Pair | n | Δ(δK)_pred | Δ(δK)_obs | Ratio | Status |
|------|---|-----------|----------|-------|--------|
| u/d | 1 | 0 | −1.86% | ∞ | BLIND (Δℓ=0) |
| s/μ | 3 | +3.25% | −0.54% | **−0.17** | ✗ WRONG SIGN |
| c/τ | 4 | +3.25% | +6.83% | **+2.10 ≈ d₁** | ✓ (G.6) |
| W/H | 6 | −4.06% | −3.89% | **+0.96** | ✓ exact |

n=3 wrong sign → face(σ₁) identified as hidden variable.
Grouping α_eff by face(σ₁): monotonic trend, within-group scatter ≪ between-group.

#### Structural properties of h

**(a) h(2) = tan γ_CKM [THM, via V.4].**
h(2) = d₂²/d₁² = P_triple/ΔP = tan γ_CKM = 9/4.
The boson-face multiplier equals the CKM CP-violating phase tangent.
Mass corrections and flavor mixing share the same UST geometric origin.

**(a') h-factors as mixing tangents (X.102d, S205) [THM-arith].**
h(6) = d₁/d₂ = CR(j=0,q,l,b) = tan θ₁₂(PMNS). h(2) = d₂²/d₁² = CR⁻² = tan γ_CKM.
h(1) = d₁ = tan γ/tan θ₂₃. All NLO mass corrections expressible via PMNS/CKM mixing tangents.

**(b) ∏h = d₂ [OBS].**
h(1)·h(2)·h(3)·h(6) = 2·(9/4)·1·(2/3) = 3 = d₂ = e₃.
Product over Div(6) = ramification index at j = 0. Not fitted.

**(c) All ratios (d₁,d₂)-monomial [OBS].**
h(f₁)/h(f₂) ∈ lattice ⟨d₁, d₂⟩ for all pairs:
h(1)/h(6) = d₂, h(2)/h(3) = d₂²/d₁², h(3)/h(6) = d₂/d₁,
h(2)/h(6) = (d₂/d₁)³, h(1)/h(3) = d₁, h(1)/h(2) = d₁³/d₂².

**(d) All h expressible via ramification indices [OBS].**
h(1) = e₂, h(2) = e₃²/e₂², h(3) = 1, h(6) = e₂/e₃,
where e₂ = d₁ (ramification at j=1728) and e₃ = d₂ (ramification at j=0).

**(e) Triple constraint uniqueness [OBS].**
From 625 LD-monomial combinations (5 candidates per face):
- ∏h = d₂: 19/625 survive (3.0%)
- All ratios (d₁,d₂)-monomial: 8/625 survive (1.3%)
- h(2) = tan γ_CKM: further restriction
- **All three simultaneously: 1/625** — unique: h = (d₁, d₂²/d₁², 1, d₁/d₂).

#### Statistical validation (scramble tests, DUAL-COMPUTE)

| Test | Method | p-value | N_trials |
|------|--------|---------|----------|
| A | Permute face(σ₁), fit optimal h (4 free) | 0.108 | 50000 |
| B | Permute face(σ₁), scan 625 LD combos (full LEE) | **0.008** | 10000 |
| C | Permute face(σ₁), scan 19 combos (∏h=d₂) | **0.004** | 20000 |
| D | Random Div(6) assignment, scan 625 LD combos | **0.003** | 10000 |

Test A: R² = 0.89 with 4 fitted params NOT significant alone (p = 0.11).
Tests B–D: LD-monomial constraint provides statistical power (p < 0.01).

**Interpretation:** The signal is in the combination "correct monodromy-derived
face(σ₁) assignment" + "h = specific LD monomials". Neither alone suffices.

#### Explains previous observations

**G.6 (d₁-multiplier at n=d₁²):** NOW EXPLAINED.
c: face(σ₁)=1, h=d₁=2. τ: face(σ₁)=2, h=d₂²/d₁²=9/4≈2.
Both face(σ₁) ∈ {1,2} → h ≈ d₁ → doublet ratio ≈ d₁.

**n=3 anomaly:** NOW EXPLAINED.
s: face(σ₁)=2, h=9/4 (enhanced). μ: face(σ₁)=6, h=2/3 (suppressed).
F.1 predicted μ with larger |Φ−Lℓ| → larger correction. NLO inverts
via h(2)/h(6) = (d₂/d₁)³ ≈ 3.4.

Deps: G.0 (LO rule), O.1 (σ₁ map → face(σ₁)), V.4 (tan γ = h(2)).


### [DER cond., S169; REVISED S171] G.0c: Derivation of h(f) from constraints

#### Statement

h(f) = (d₁, d₂²/d₁², 1, d₁/d₂) for f ∈ {1,2,3,6} is the **unique** positive solution of:

| # | Constraint | Formula | Source | Status |
|---|-----------|---------|--------|--------|
| (1) | CKM tangent | h(2) = d₂²/d₁² | V.4 [THM] | [THM] |
| (1') | Anchor scattering | h(1) = d₁ = e₋(d₁)/e₋(d₂) | X.56 [THM-arith] | [THM-arith] S171 |
| (⊥) | v_{d₂}-mode suppression | c₃(h·f) = 0 ⟺ h(1) = d₂·h(6) | X.49 [OBS], C.8.8 | [OBS] |
| (2) | Scattering ratio | ⟨π,h⟩ = d₂²/d₁³ = Π₊₋/Π₋₊ | X.50 [OBS] | [OBS] |

#### Proof

**Step 1 (fixing h₁, h₂).** Constraints (1) and (1') directly fix h(2) = 9/4 and h(1) = 2.

**Step 2 (fixing h₆).** Constraint (⊥): h·f ⊥ v_{d₂} in the T-eigenbasis, where v_{d₂}(f) = 1 if d₂|f, else −d₂. This gives Σ f²h(f)v_{d₂}(f) = 0, which on the family h₁=s, h₂=9/4 from (1)+(1') reduces to 6(3h₆ − h₁) = 0 (see S171 audit). With h₁ = d₁ = 2: h₆ = h₁/d₂ = d₁/d₂ = 2/3.

**Step 3 (fixing h₃).** Constraint (2): ⟨π,h⟩ = Σfh(f)/index = d₂²/d₁³, i.e., Σfh = d₂³/d₁ = 27/2. With h₁, h₂, h₆ fixed: 2 + 9/2 + 3h₃ + 4 = 27/2 → h₃ = 1. ∎

#### Consequences

- **∏h = d₂** follows: 2·(9/4)·1·(2/3) = 3 = d₂. NOT an input.
- **Σhf² = 44 = Σn** follows: 2 + 9 + 9 + 24 = 44. NOT an input.
- **Extremal principle (X.51) NOT needed.** Four linear constraints → unique solution.

#### Z₂ ambiguity [S171]

Replacing (⊥) with the weaker ∏h = d₂ (together with (1)+(1')+(2)) yields two solutions via the quadratic 6h₆² − 7h₆ + 2 = (3h₆ − 2)(2h₆ − 1) = 0:

| | Physical: h₆ = d₁/d₂ | Alternative: h₆ = 1/d₁ |
|---|---|---|
| h | (2, 9/4, 1, 2/3) | (2, 9/4, 4/3, 1/2) |
| Σhf² | **44 = Σn ✓** | **41 ✗** |
| h·f ⊥ v_{d₂} | **0 ✓** | **−3 ✗** |
| AL coefficients (χ₂, χ₂χ₃) | (−L, −d₂) = (−Φ₃(d₁), −Φ₆(d₁)) | (−d₂, −L) = (−Φ₆(d₁), −Φ₃(d₁)) |
| d₁fh set | {4, 9, 6, 8} | {4, 9, 8, 6} |

Both solutions are LD-monomial with ∏h = d₂. They differ by swapping {N, d₁³} between faces 3 and 6. The physical solution is uniquely selected by (⊥), equivalently by Σhf² = Σn or by cyclotomic matching (χ_p coefficient = −Φ₃(p)).

#### DOF count [S175-CONSOLIDATED, verified S172–S174]

**(1)+(1') fix h(1) and h(2).** Two unknowns remain: h(d₂) = h(3) and h(N) = h(6).

**(⊥) and (2) are not independent** [THM-arith, X.57a]: given (1)+(1'), each reduces to a single linear equation in (h(3), h(6)):
- (⊥): h(d₂) + d₁²·h(N) = dim M₁₀/d₂ = 11/3
- (2): h(d₂) + d₁·h(N) = L/d₂ = 7/3

Subtracting: d₁(d₁−1)·h(N) = 4/3 → h(N) = d₁/d₂. Back-substituting: h(d₂) = 1. The **consistency** of the pair (⊥)+(2) requires d₂²−d₁³ = 1 (Catalan/Mihailescu) [THM, path #20].

**Independent constraint count:** (1) [THM] + (1') [THM-arith] + ONE of {(⊥),(2)} [OBS] = **3 independent constraints** → unique h. The 4th constraint is redundant modulo Catalan.

**Equivalent reformulations of the remaining [OBS]** (any one suffices, verified S172–S174):
- h(d₂) = 1 ("j=0 cusp neutral")
- h(N) = d₁/d₂ ("level-cusp correction = ramification ratio")
- (⊥): h·f ⊥ v_{d₂} ("no autonomous q-oscillation")
- (2): ⟨π,h⟩ = Π₊₋/Π₋₊ = d₂²/d₁³
- Ratio of AL projections: ⟨hf, u_{++}⟩/⟨hf, u_{+-}⟩ = −ι(d₂) = −d₁ [X.59]
- q-marginal equilibrium: R = d₂ [X.60b]
- Spectral product: c₁(w)·c₆(w) = −c₂(w) [C.8.6, L8.18]

(7 equivalent reformulations, any one suffices.)

#### Dependencies
V.4 ((1)), X.56 ((1')), path #20 (Catalan), ONE of {X.49, X.50} [OBS].

#### Alternative constraint system (S176/S177, C.8.4)

The cubic approach (C.8.4) provides an independent route to uniqueness:
(1) V.4, (2) ∏h = d₂ [OBS], (3) Σf²h = Σn [THM-arith, C.8.3], (4) ⟨π,h⟩ [OBS, X.50]
→ cubic 135c³−177c²+52c+4 = (3c−2)(45c²−29c−2) = 0, unique positive LD-monomial root c = d₁/d₂.
Uses 2 [OBS] (same count as G.0c), but constraint (3) is new and independently meaningful.


## [THM] G.1: Sign Window Theorem
Source: Paper §6, Thm 6.1
Status: [THM]
Dependencies: Table 1 (empirical δK signs)
Verified: Sage (all integers k = 1..20)

### Statement
In the formula δK/K = (α/2π)[n^k(1−n/L)^b − L·ℓ] with b = d₁−1 = 1, the parameter k = d₂ = 3 is the unique integer giving 10/10 correct signs. The sign window is (2.807, 3.172), width 0.365.

### Proof
For each integer k, compute sign(n^k(1−n/7) − 7ℓ) for all 10 particles. The critical particles are:
- **Lower bound (charm, k → 2.807):** Φ(4) must exceed 7·ℓ(c) = 21. At k=3: 4³·(3/7) = 27.43 > 21 ✓. At k=2: 4²·(3/7) = 6.86 < 21 ✗.
- **Upper bound (W boson, k → 3.172):** Φ(6) must be less than 7·ℓ(W) = 42. At k=3: 6³·(1/7) = 30.86 < 42 ✓. At k=4: 6⁴·(1/7) = 185.1 > 42 ✗.

Only k = 3 = d₂ sits in the window. Width 3.172 − 2.807 = 0.365 — just barely containing one integer. ∎

Out of 48 tested integer pairs (a,b) with a ∈ {1,...,8}, b ∈ {0,...,5}: (3,1) is the UNIQUE pair with 10/10.


## [THM] G.2: BVP well-posedness (d₁+d₂ = 5)
Source: Paper §6, Thm 6.2; S65; corrected S78
Status: [THM]
Dependencies: none (pure ODE)
Verified: analytical

### Statement
The BVP D⁴Φ = ρ on [0, L] with boundary conditions from ramification:
- At x = 0 (j = 0, ramification e = d₂ = 3): Φ(0) = Φ'(0) = Φ''(0) = 0 (d₂ conditions)
- At x = L (j = 1728, ramification e = d₁ = 2): Φ(L) = 0 (d₁−1 = 1 condition)

is well-posed if and only if d₂ + (d₁−1) = 4, i.e., **d₁ + d₂ = 5**.
Among integer pairs with d₁ ≥ 2, d₁ < d₂: uniquely **(d₁, d₂) = (2, 3)**. No genus-0 filter needed.

### Proof
D⁴ has 4 free constants. Ramification gives d₂ + (d₁−1) BCs. Well-posedness: d₂ + d₁ − 1 = 4, i.e., d₁ + d₂ = 5. With d₁ ≥ 2, d₁ < d₂: only (2, 3). ∎

### Algebraic coincidence
The identity 1+d₂ = d₁² also holds at (2,3). This connects BVP to the Residual Tree Theorem (E.8), where C(N,2)−C(d₁²,2) = d₂² requires 1+d₂ = d₁². The two conditions (d₁+d₂ = 5 from D⁴ BVP, 1+d₂ = d₁² from trees) are **independent** but simultaneously satisfied only at (2,3) — a non-trivial coherence.

### CORRECTION NOTE (S78)
Paper v4 Thm 6.2 and earlier companion stated "iff 1+d₂ = d₁²" for the D⁴ BVP. This is a false equivalence: d₁+d₂ = 5 (from D⁴) and 1+d₂ = d₁² (from Residual Tree) are distinct conditions. The family (3,7),(4,13),... satisfies d₂ = d₁²−d₁+1 (from variable-order D^{d₁²}, S65), not d₁+d₂ = 5. All three conditions coincide at (2,3) only. Paper v5 must correct Thm 6.2.

### Explicit solution
With BCs Φ(0) = Φ'(0) = Φ''(0) = 0, the homogeneous part reduces to Φ_h = Ax³. Adding particular: Φ = Ax³ + (ρ/24)x⁴. Condition Φ(L) = 0: AL³ + (ρ/24)L⁴ = 0 → A = −ρL/24.

Φ(x) = (−ρ/24)x³(L − x). With ρ = −24/L: **Φ(n) = n³(1 − n/7)**. ✓


## [THM] G.3: 4D Weyl uniqueness
Source: Paper §6, Thm 6.3
Status: [THM]
Dependencies: none (standard QFT)
Verified: analytical

### Statement
The prefactor α/(2π) in the δK formula is the unique 1-loop vacuum polarisation amplitude for a d = 4 spacetime dimension with Weyl fermion (Tr I = 2).

### Proof
The Schwinger anomalous magnetic moment of the electron gives the 1-loop QED correction factor α/(2π) (Schwinger 1948). This factor is specific to d = 4 with Weyl fermions (Tr I = 2):

| d | Fermion type | 1-loop factor | Match? |
|---|-------------|---------------|--------|
| 4 | Weyl (Tr = 2) | α/(2π) | ✓ |
| 4 | Dirac (Tr = 4) | α/π | ✗ (×2) |
| 4 | Scalar | α/(4π) | ✗ (×1/2) |
| d ≠ 4 | Any | Different structure | ✗ |

The factor α/(2π) = e²/(8π²) is the unique 1-loop contribution from a single Weyl fermion in 4D. It is charge-independent: the charge e² entering the loop is the same that defines α = e²/(4π), so the ratio α/(2π) is universal. ∎

**Note:** The paper uses α/(2π) as the **prefactor of the δK formula**. Its identification with the 1-loop Weyl amplitude is the content of this theorem — the δK correction has the structure of a 1-loop radiative correction.


## [DER] G.4: EW operator from cusps
Source: Paper §6, Prop 6.4
Status: [DER] (superseded by G.8, which derives ℓ from dessin without external SM quantum numbers)
Dependencies: A.1

### Statement
ℓ = −2(T₃ − d₂|Q|) equals the width of the "gauge cusp" associated with each particle's SM quantum numbers.

### Full table

| Particle | T₃ | |Q| | T₃ − d₂|Q| | ℓ = −2(T₃−d₂|Q|) | Cusp interpretation |
|----------|-----|-----|------------|---------|-----|
| u | +1/2 | 2/3 | +1/2−2 = −3/2 | 3 | w = d₂ (SU(3) cusp) |
| d | −1/2 | 1/3 | −1/2−1 = −3/2 | 3 | w = d₂ |
| e | −1/2 | 1 | −1/2−3 = −7/2 | 7 | w = N+1 = L (boundary) |
| μ | −1/2 | 1 | −7/2 | 7 | w = L |
| τ | −1/2 | 1 | −7/2 | 7 | w = L |
| ν | +1/2 | 0 | +1/2 | −1 | (neutrino sector) |
| W | 0 | 1 | 0−3 = −3 | 6 | w = N (full level cusp) |
| H | −1/2 | 0 | −1/2 | 1 | w = 1 (∞ cusp, singlet) |

All quarks: ℓ = 3 = d₂ regardless of flavour. All charged leptons: ℓ = 7 = L. This is isospin universality: ℓ depends only on the SU(3)×U(1) quantum numbers, collapsed to a single cusp width.

### Theorem (isospin universality, r = 3 unique)
ℓ_up − ℓ_down = 0 for quarks iff r = d₂ = 3 in ℓ = −2(T₃ − r|Q|). This is the unique integer r for which up-type and down-type quarks share the same ℓ. ∎


## [THM] G.5: Φ from ramification — 4 candidates
Source: S53/S62
Status: [THM]
Dependencies: C.2

### Statement
The canonical divisor ω_{X/Y} of the j-map X₀(6) → ℙ¹ can be twisted by divisors supported at j = 0 and j = 1728. This gives the vanishing orders of Φ at the boundary:

| Twist | Orders at (j=0, j=1728) | (a, b) | BCs total | Signs | Bridge Φ(d₁²)=j/(d₂²L) |
|-------|------------------------|--------|-----------|-------|--------------------------|
| ω_{X/Y} bare | (e−1, e−1) = (2, 1) | (2, 1) | 2+0=2 ≠ 4 | 7/10 | ✗ |
| **ω_{X/Y}(D₀)** | **(e, e−1) = (3, 1)** | **(3, 1)** | **3+1=4=d₁²** | **10/10** | **✓** |
| ω_{X/Y}(D₁₇₂₈) | (e−1, e) = (2, 2) | (2, 2) | 2+1=3 ≠ 4 | 7/10 | ✗ |
| ω_{X/Y}(D₀+D₁₇₂₈) | (e, e) = (3, 2) | (3, 2) | 3+1=4=d₁² | 9/10 (charm killed) | ✗ |

D₀ is the reduced divisor at j = 0. The twist ω_{X/Y}(D₀) is the unique choice satisfying ALL three criteria: 10/10 signs, well-posed BVP (total BCs = d₁² = 4), and d₁-multiplier bridge (Φ(d₁²) = j(i)/(d₂²L) = 192/7).

### Connection to Gap 3
The form "polynomial − c·ℓ" itself is NOT derived from the twist. The twist determines (a,b) = (3,1), hence Φ. The EW term (−L·ℓ) and the coupling α/(2π) are separately derived. But their assembly into one formula remains postulated.


## [OBS] G.6: d₁-multiplier at n = d₁²
Source: S43/S44/S61
Status: [OBS]
Dependencies: G.0

### Statement
At n = d₁² = 4 (charm and tau): replacing δK → d₁·δK dramatically improves fit:

| Particle | δK_pred | d₁·δK_pred | δK_obs | Improvement |
|----------|---------|------------|--------|-------------|
| charm | +0.75% | +1.49% | +1.52% | Δ = 0.03% (L1 accuracy!) |
| tau | −2.51% | −5.01% | −5.31% | 6× better |

Optimal multiplier M_opt = 2.11, δ from exact d₁ = 2: +5.4%. Effect coherent ONLY at n = d₁² (other nodes show no improvement).

### Bridge theorem [S61, THM]
Φ(d₁²) = (d₁²)³(1 − d₁²/L) = d₁⁶·(L−d₁²)/L.

For this to equal j(i)/(d₂²L) = 1728/(9·7) = 192/7, need d₁⁶(L−d₁²) = 192 = d₁⁶·d₂ (using L = d₁d₂+1).

This gives d₁^{2d₁−1} = d₁⁶/d₁⁴ · d₁ = d₁^{2d₁−1}. At d₁ = 2: 2³ = 8, and d₁⁶·d₂/L = 64·3/7 = 192/7 ✓.

Holds ONLY at d₁ = 2. ∎

### Status
Observation (2 data points). Bridge is [THM]. Mechanism: EXPLAINED by G.0b (S168).

**Explained by G.0b (S168):** The d₁-multiplier at n=d₁² arises because both particles
in this doublet have small face(σ₁): c has face(σ₁)=1 (h=d₁=2), τ has face(σ₁)=2
(h=d₂²/d₁²=9/4). Both h ≈ d₁, so the doublet ℓ-splitting is preserved with a
global d₁ enhancement. The bridge theorem (Φ(d₁²) = j(i)/(d₂²L)) may connect
to the anchor face(σ₁)=1 being uniquely available at n=d₁².


## [OBS] G.7: W anomaly
Source: S43
Status: [OBS]

### Statement
δK_pred(W) = −1.29%, δK_obs(W) = −0.04%. Ratio = 32×. The W boson is the unique particle where |δK_obs| ≈ 0 while |δK_pred| is substantial.

Interpretation: gauge protection — the W mass receives SM radiative corrections that cancel most of the "bare" δK predicted by the formula. This is expected: gauge boson masses are protected by gauge symmetry in a way fermion masses are not. The formula predicts the "pre-protection" value.


## [DER] G.8: EW operator ℓ from dessin
Source: S76, upgraded S127
Status: [THM-arith] (upgraded from [DER]: F.7e provides ℓ for ALL 12 particles from ε-η polynomial)
Dependencies: C.1 (dessin), C.3 (uniqueness 36/36), F.3a (σ₁-sector dichotomy)
Verified: Sage (8/8 dessins × 12/12 edges)
Replaces: G.4 [DER] (which derived ℓ from SM quantum numbers; now ℓ derived from dessin itself)

### Dependency note (S98 audit, updated S127/DFT)
Fermion ℓ values (quarks: d₂=3, leptons: L=7, anchor: 0) are derived purely from face sizes — **no SM input**. Boson ℓ values (H: 1, W: 6) were originally marked as requiring SM quantum numbers (T₃, |Q|). **DFT S127 upgrade:** The global ℓ-polynomial (§F.7e) ℓ = L − N·εF − d₁²·ηF − d₁·εF·ηF + (N−1)·εF·η₁ gives ℓ(W) = 6 and ℓ(H) = 1 from the distinguishing bit η₁ = η(Fσ₁) — pure dessin data. **SM_QN dependency REMOVED.** The SM formula ℓ = −2(T₃−d₂|Q|) is now an OUTPUT interpretation, not an input.

### Definitions
- **F(e)** = face(e) = length of σ∞-cycle containing edge e
- **S(e)** = face(σ₁(e)) = face size of σ₁-partner

### Statement
For every edge e of the X₀(6) dessin:

| F(e) | S(e) | ℓ(e) | Particle type |
|------|------|------|---------------|
| N = 6 | any | d₂ = 3 | quarks |
| d₂ = 3 | any | L = 7 | leptons |
| 1 | any | 0 | anchor |
| d₁ = 2 | d₂ = 3 | 1 | H (Higgs) |
| d₁ = 2 | N = 6 | N = 6 | W boson |

Equivalently: ℓ(e) = −2(T₃(e) − d₂|Q(e)|), where T₃ and |Q| are SM quantum numbers. Verified 12/12 edges, 8/8 dessins.

### Proof

**Part 1: Fermions + anchor (F alone suffices).**
Quarks (F=6): isospin universality (§G.4) gives ℓ = d₂ = 3 for all quarks regardless of flavour.
Leptons (F=3): all share ℓ = L = 7.
Anchor (F=1): ℓ = 0.

**Part 2: Bosons — σ₁-partner resolves degeneracy.**

**Lemma (Boson σ₁-dichotomy).** Among the two edges of the 2-face, exactly one has σ₁-partner in the 3-face (leptons), and the other has σ₁-partner in the 6-face (quarks). Verified 8/8 dessins.

*Proof:* From BB^T structure (§D.2), bosonic edges occupy positions BV₂–WV₃ and BV₃–WV₅ (or equivalent). Their σ₁-partners are the other edges at WV₃ and WV₅. By BB^T off-diagonal structure, these partners lie in distinct faces. Exhaustive check: one partner always in 3-face, other in 6-face. ∎

Identification: S(e) = d₂ → e = H, ℓ = 1. S(e) = N → e = W, ℓ = N = 6.

Physical: σ₁(H) = τ (lepton→boson link, cf. §I.3). σ₁(W) = quark.

**Part 3: Invariance.** The (n, ℓ) multiset is identical for all 8 valid σ₀-orientations and hence all 36 isomorphic dessins (§C.3). ∎

### Consequence for Gap 3

**Before G.8:** δK formula required 4 inputs: n [THM], Φ [THM], ℓ [external SM], α/(2π) [THM for value].

**After G.8:** ℓ derived from dessin. ALL discrete content reads from (σ₀, σ₁, σ∞):

| Input | Source | Status |
|-------|--------|--------|
| n(e) | ecc → g → n-formula | [THM] (F.3, F.3a) |
| Φ(n) | ramification orders | [THM] (G.5) |
| ℓ(e) | ε-η polynomial (F.7e) | **[THM-arith] (F.7e, S127)** |
| α/(2π) | 4D Weyl 1-loop | [THM] for value; reason = **sole remaining Gap 3** |

**Gap 3 reduces to: why does the overall coupling = α/(2π)?**

### Chain: dessin → SM quantum numbers

```
face(e)                → particle type (quark/lepton/boson/anchor)
face(σ₁(e))           → W vs H discrimination
ecc(e)                → generation g
σ₁-sector(e)          → isospin T₃ (up vs down) [F.3a]
face(e) + face(σ₁(e)) → ℓ = −2(T₃ − d₂|Q|) [G.8]
```

SM quantum numbers (T₃, |Q|) are **outputs** of dessin combinatorics, not inputs.

### σ₁ as electroweak involution

| Role | Section | Mechanism |
|------|---------|-----------|
| Isospin pairing | F.3a | σ₁-sector → T₃ |
| W/H discrimination | G.8 | face(σ₁(e)) → ℓ for bosons |
| μ-τ breaking | I.3 | σ₁(τ) = H (unique lepton→boson link) |

### No-go: unified formula
No polynomial ℓ(F, S) of degree ≤ 2 with |coefficients| ≤ 5 reproduces all 5 cases. Branching by face type is irreducible — same structural reason as K-cipher (§F.5): Div(N) has no polynomial parameterization.


## [THM] G.9: Logarithmic residue decomposition of j
Source: S76 (corrected same session — P₄ error detected and fixed)
Status: [THM] for decomposition; connection to δK [MOTIVATED by THM]
Dependencies: K.1 (j-factorisation)
Verified: SymPy (partial fractions, residues, Riemann-Hurwitz)

### Statement
The logarithmic derivative of j with respect to the Hauptmodul t₆ decomposes as:

ω(t) = d(ln j)/dt₆ = R(t) + C(t)

where R (ramification) has all positive residues and C (cuspal) has all negative residues.

### Cuspal part
C(t) = −6/t − 3/(t+9) − 2/(t+8)

Residues at cusps: {−6, −3, −2} at {t=0, t=−9, t=−8}. Fourth cusp (t=∞): Res = −1.
Sum of cuspal residues = −6−3−2−1 = −12 = −index.

### Ramification part (CORRECTED — uses P₄ from K.1)
With P₄ = (t+12)(t³+252t²+3888t+15552) [the correct Hauptmodul numerator]:

R(t) = 3P₄'/P₄ = 3/(t+12) + 3·[3(t²+168t+1296)]/(t³+252t²+3888t+15552)

**4 simple poles** (roots of P₄): t = −12 = −index and three roots of R₃ = t³+252t²+3888t+15552.

**ALL residues = +3 = +d₂** (uniform). Each root of P₄ is simple; Res(d ln P₄^3/dt) = 3 × 1 = 3.

Sum of ramification residues = 4 × 3 = +12 = +index. ✓

### Residue table

| Pole | Type | Residue | = |
|------|------|---------|---|
| t = 0 | Cusp (w=6) | −6 | −w₀ |
| t = −9 | Cusp (w=3) | −3 | −w₂ |
| t = −8 | Cusp (w=2) | −2 | −w₃ |
| t = ∞ | Cusp (w=1) | −1 | −w₁ |
| t = −12 | j=0 (simple, e=d₂) | +3 | +d₂ |
| t = r₁ ∈ R₃ | j=0 (simple, e=d₂) | +3 | +d₂ |
| t = r₂ ∈ R₃ | j=0 (simple, e=d₂) | +3 | +d₂ |
| t = r₃ ∈ R₃ | j=0 (simple, e=d₂) | +3 | +d₂ |

R₃ = t³+252t²+3888t+15552, coefficients: 252 = d₁²d₂²L, 3888 = d₁⁴d₂⁵, 15552 = d₁⁶d₂⁵ (all monomials in (d₁,d₂) per K.1).

### Key properties
- Cuspal residues = negative cusp widths (−w), ramification residues = +d₂ (uniform)
- All 4 ramification poles have identical residue +d₂ — reflects uniform ramification e = d₂ at j=0
- Total: Σ Res = 0 (meromorphic 1-form on ℙ¹, degree counting)
- Sign structure: R > 0, C < 0 → ω = (positive ramification) − (negative cusps)

### Connection to δK (qualitative)
The additive structure ω = R + C mirrors δK/K = (α/2π)[Φ − Lℓ]: a positive polynomial term (from ramification at j=0) minus a negative EW term (from cusps at j=∞). The cuspal residues {−6, −3, −2, −1} encode particle-type information; the ramification residues {+3, +3, +3, +3} encode the uniform j=0 geometry.

Status: [MOTIVATED by THM] — the structural parallel is suggestive but not a derivation of the additive form. Gap 3 narrowed but not closed.

### Correction note (S76)
Original S76 computation used wrong P₄ = (t+3)²(t²+12t+24), giving non-uniform ramification {6,3,3} at j=0 and breaking Riemann-Hurwitz. Corrected same session to P₄ = (t+12)·R₃ from K.1/paper. Qualitative conclusions (R+C decomposition, sign structure) survive; residue table and partial fractions corrected. The corrected version is CLEANER: uniform residues +d₂ directly reflect C.2 (uniform ramification).


---


## [MOTIVATED] G.10: Partial Fractions ↔ δK Additivity
Source: S91
Status: [MOTIVATED]
Dependencies: K.1 (j-factorisation), G.9 (logarithmic residue)
Verified: Numerical (cuspal positions); structural parallel qualitative

### Cuspal positions of t₆

| Cusp | Width w | t₆ → | LD expression |
|:----:|:-------:|:----:|:-------------:|
| ∞ | 1 (anchor) | +∞ | — |
| 0 | 6 (quarks) | 0 | — |
| 1/2 | 3 (leptons) | **−9** | **−d₂²** |
| 1/3 | 2 (bosons) | **−8** | **−d₁³** |

### 3P₄'/P₄ at cusps [THM]

| Cusp position | 3P₄'/P₄ | LD |
|:------------:|:--------:|:--:|
| t = 0 (quarks) | **1** | 1 |
| t = −9 (leptons) | **−4** | −d₁² |
| t = −8 (bosons) | **3** | d₂ |

**Sum = 0** [THM]. All quarks share ℓ = d₂ = 3 (single cusp). t²+d₂t+d₂²|_{t=−d₁³} = L² = 49 (K.7b).

### Structural parallel

| d(ln j)/dt₆ | δK/K = (α/2π)[Φ−Lℓ] |
|:-------------|:---------------------|
| 3P₄'/P₄ (ramification, j=0) | Φ(n) = n^{d₂}(1−n/L)^{d₁−1} |
| −Σ wᵢ/(t−tᵢ) (cusps, j=∞) | −L·ℓ |
| Additive: partial fractions of rational function | Additive: BVP |

**Key insight:** Additivity of δK = Φ − Lℓ inherits from partial-fraction decomposition ln j = ln(N) − ln(D).

### Status for Gap 3
[MOTIVATED, not THM]. To upgrade: find exact "height" y(n) mapping σ∞-positions to cuspal coordinates; coupling α/(2π) enters at quantum level, not in classical partial fractions.


# H. α FORMULA AND RING

## [DER] H.1: The α formula
Source: Paper §5.4 (Form A replaces paper v5.5; see H.1d for Form B death)
Status: BULK [DER via QTC, §N], IR [DER + 1 bit empirical, S103+S108+S123]
Dependencies: A.1, N.1–N.5
Verified: Python 42/42 (S106), mpmath 50 digits (S102)

### Statement (Form A, correct)

α⁻¹ = index²·E₂(i)·cos²(1/(Nπ)) − [index·E₂(i)]⁻¹·(j(i)+N)/(j(i)+L)

= (432/π)·cos²(1/(6π)) − (π/36)·(1734/1735)

Numerically: BULK = 432/π · 0.997188162113 = **137.123215366823**.
IR = π/36 · 1734/1735 = 0.087266463 · 0.999423631 = **0.087216164927**.
Result: α⁻¹ = **137.035999201896**.

Self-duality: Ω = index·E₂(i) = 36/π. BULK_coeff = Ω·index = 432/π. IR_coeff = 1/Ω = π/36. Product: BULK_coeff × IR_coeff = index = 12. [OBS, S104]

### H.1a: BULK identification [THM, S101]

432/π = index² · E₂(i), where E₂(i) = 3/π (Hurwitz 1883).
All factors are standard modular invariants: index = ψ(6) = 12, E₂ = Eisenstein series.
No new content beyond identification. Status: [THM].

### H.1b: cos² derivation [DER, QTC chain, S105–S106]

Full 12-step chain in §N. Summary:
(1) vol(X₀(6)) = 4π [THM, Gauss-Bonnet].
(2) C = vol/n_cusps = π [THM+PHYS: integer phase lattice, perturbative minimality, §N.3].
(3) Holonomy Hol = k/π, cusp-independent [THM, standard connection].
(4) Intensive phase φ(w) = k/(πw) [THM+PHYS: minimal m-range, §N.4].
(5) k = 1 from dimension matching h⁰(O(1)) = 2 = n_matter [THM, §N.5].
(6) Matter pair (d₁,d₂) unique Catalan Fricke pair [THM, Gap C].
(7) |d₁−d₂| = 1 [THM, Catalan/Mihailescu].
(8) Δφ = 1/(Nπ) [THM, algebra from (4)–(7)].
(9) 2×2 unitary survival = cos²(δ) [THM, O(1) Hermitian metric → U(1)].
(10) σ₁-dichotomy selects EW sector = {d₁,d₂} [THM, F.3a 36/36].
(11) cos²(1/(Nπ)) = 0.997188162113479 [DER].

Two standard physics inputs: perturbativity (steps 2,4), Born interpretation (step 9). Both universal QM, not LD-specific. 42/42 numerical checks pass (S106).

### H.1c: IR derivation [DER conditional, S103+S108 chain]

Form A: IR = (π/36) · (j(i)+N)/(j(i)+L) = (π/36) · 1734/1735.

5-step chain:
(1) Path A → genus 0 → X₀(6) = ℙ¹ [THM].
(2) ℙ¹ → Cauchy kernel = unique propagator [THM].
(3) Self-energy Σ = −χ(O(N)) = −L. The bundle O(N) arises as the dual determinant of the W₆-odd Grothendieck factor of f_* O_{X₀(6)} (H.1i [THM]). The Atkin-Lehner factorization provides exactly two candidates: O(N) [odd, χ = L = 7] and O(N−1) [even, χ = N = 6]. The odd choice gives α⁻¹ = 137.035999202 (−1.2σ CODATA 2022); the even choice gives 137.035948904 (+2394σ, dead). Selection of W₆-odd is empirical (1 bit at ≈2400σ). Status: [DER + 1 bit empirical], upgraded from [DER conditional on weight=level].
  (3a) Hodge bundle ω on ℙ¹ = X₀(6) has deg(ω) = index/12 = 1 [THM].
  (3b) ω^⊗N = O(N). Sections = M_N(Γ₀(6)), dim = N+1 = L = 7 [THM: Riemann-Roch].
  (3c) O(N) is UNIQUE line bundle on ℙ¹ with χ = L: n+1 = L has unique solution n = N [THM].
  (3d) Action S[φ] = ∫_{ℙ¹} |∂̄φ|² ω_FS, unique gauge-invariant second-order action [DER].
  (3e) 1-loop: Σ = −[a₂ in heat kernel of ∂̄*∂̄ on O(N)] = −ind(∂̄) = −χ(O(N)) = −L [DER: index theorem].
  Sign: QFT convention G⁻¹_dressed = G⁻¹_bare − Σ = j − (−L) = j + L.
(4) Fricke W_N: tadpole shift = N [THM].
(5) Dyson resummation: G_dressed = (j+N)/(j+L) [DER from 1–4].

**Remaining caveat:** The upgrade (S123) reduces the candidate space from infinite (any O(k)) to **binary** (W₆-odd O(N) vs W₆-even O(N−1)). This is structural (Grothendieck [THM]), but the 1-bit selection of the odd piece remains empirical (≈2400σ confirmed, not derived). The physical argument "gauge field = W_N-odd" is an analogy between modular and spacetime parity (different spaces, no proven bridge — see X.20). Status: [DER + 1 bit empirical].

Factorizations: j(i)+N = 1734 = N·17² = N·(index+d₁+d₂)² [THM, S102, 28th path]. j(i)+L = 1735 = 5·347 (347 prime, no LD structure).

### H.1d: Form B death [THM, S102]

**Paper v5.5 uses Form B (WRONG).** Paper formula: IR = (π/36)·(1 − 1/j + 11/j²) with c₂ = dim M₁₀ = 11. This is a Taylor approximation that does not equal any exact closed form precisely.

Form B exact: IR_B = (π/36)·(j+|B₁|)/(j+dim M₁₀) = (π/36)·1738/1739.
α⁻¹(B) = 137.035999086. α⁻¹(A) = 137.035999202. Separation: 10.5σ_Rb.

| Measurement | α⁻¹(exp) ± σ | Pull A | Pull B |
|---|---|---|---|
| CODATA 2022 | 137.035999177(21) | **−1.2σ** | +4.3σ |
| Rb Morel 2020 | 137.035999206(11) | +0.4σ | +10.9σ |
| ae Fan 2023 | 137.035999166(15) | **−2.4σ** | +5.3σ |
| Cs Parker 2018 | 137.035999046(27) | −5.8σ | −1.5σ |
| χ² (first 3 meas.) | | **7.3** | **166.2** |

**Form B DEAD.** Paper v6 MUST replace with Form A.

Former "HF selects CODATA" argument (c₂ = dim M₁₀ = 11) is INVALIDATED by Form B death. Form A has no c₂ parameter.

### H.1e: 137 = index · Σ(1/K) [THM, S104, 29th path]

Over 11 rational-K particles (d-quark excluded):
Σ(1/K) = 137/12. index × 137/12 = 137.
Sector decomposition: quarks = 81/12 = d₂⁴/12, leptons = 34/12, bosons = 22/12 = d₁·dim M₁₀/12.

Uniqueness: substituting d₂ = d₁²−1, the identity factors as d₁·(d₁−2)·(quadratic)·(cubic) = 0; unique integer root d₁ ≥ 2 is d₁ = 2.

Status: [THM] (verified against F.5a K-values). Beautiful identity but disconnected from α formula: 137 ≈ α⁻¹ but BULK−137 = 0.1232 ≠ IR = 0.0872. The coincidence 137 = integer part of α⁻¹ remains unexplained.

### H.1f: E₂* variational principle [THM, S101, 27th path]

E₂*(τ) = E₂(τ) − 3/(π·Im τ) vanishes on X₀(6) at exactly |B₁| = 10 points: 6 over j = 1728 (ramification e = d₁) + 4 over j = 0 (ramification e = d₂). Count: index/|Stab(i)| + index/|Stab(ρ)| = 12/2 + 12/3 = 10.

Corollary: E₂*(τ)=0 ∧ j(τ)≠0 → τ=i (unique on X₀(6)). This REPLACES the postulate "evaluate at τ=i" with a derived principle.

### H.1g: Honest overall status

| Element | Status | Note |
|---|---|---|
| 432/π = index²·E₂(i) | [THM] | identification |
| cos²(1/(Nπ)) | [DER] | QTC chain, §N, 2 physics inputs |
| τ = i selection | [THM] | E₂* variational, H.1f |
| IR: Σ = −L via O(N) | [DER + 1 bit] | H.1i: W₆-odd from Grothendieck binary, ≈2400σ confirmed |
| π/36 = 1/(index·E₂) | [THM] | self-duality |
| Form A vs B | [THM] | B dead at 10.5σ |

Overall α formula: ~80% [THM/DER]. Σ=−χ upgraded [MOT]→[DER cond.] (S108)→[DER + 1 bit empirical] (S123: Grothendieck binary ∞→2 candidates, W₆-odd at ≈2400σ). The ~20% non-[THM/DER]: Born rule (standard QM), W₆-odd selection (1 bit), QFT 1-loop identification (standard), k=1 dimension matching (N.5).

### H.1h: VMF — saddle at τ=i [THM, S108]

h(τ) = −log(y^{1/2}|η(τ)|²) has E₂*(τ)=0 as Euler-Lagrange equation [THM]. τ=i is a **saddle point** (not minimum): Hessian eigenvalues 1/4 ± π²E₄(i)/36 ≈ +0.649, −0.149, Morse index 1 [THM]. h is SL₂(ℤ)-invariant → descends to X(1) → **cannot select Γ₀(6)** [structural barrier]. No Γ₀(6)-specific functional with E₂*=0 as EL equation was found (5 attempts DEAD). Constrains future VMF attempts: any variational principle for τ=i must break SL₂(ℤ)-invariance.


### H.1i: Grothendieck Splitting of the Covering [THM, S123]

Source: S123
Status: [THM] (mathematics); physical selection of W_N-odd = [1 bit empirical, ≈2400σ confirmed]
Dependencies: A.1 (N=6, genus 0), C.2 (ramification)
Verified: analytical (Grothendieck + χ + H⁰ constraints); numerical (mpmath 30 digits, S123)

**Statement.** For the j-map f: X₀(6) → X(1) (both ℙ¹, deg = index = 12):

f_* O_{X₀(6)} ≅ O ⊕ O(−1)^{⊕11}

**Proof.** Grothendieck: every vector bundle on ℙ¹ splits as ⊕ O(aᵢ). Three constraints: (1) H⁰(f_* O) = H⁰(O_Y) = 1 (f finite → R^i f_* = 0), so exactly one aᵢ = 0, rest ≤ −1. (2) χ(f_* O) = χ(O_Y) = 1 → Σaᵢ = 1 − 12 = −11. (3) Eleven values ≤ −1 summing to −11 → all equal −1. ∎

det(f_* O) = O(−11) = O(−dim M₁₀). Trace-free part O(−1)^{⊕11}, rank = index − 1 = 11.

**Atkin-Lehner factorization.** The j-map factors through the Fricke quotient:

X₀(6) →[h, deg 2] X₀(6)/W₆ →[g, deg N=6] X(1)

All three curves genus 0. Degrees: [SL₂(ℤ) : Γ₀⁺(6)] = index/2 = N = 6.

**W₆-even part** (descends to quotient): g_* O_Z = O ⊕ O(−1)^{N−1} = O ⊕ O(−1)^5. (rank N=6, χ=1, H⁰=1, same Grothendieck argument.)

**W₆-odd part** (anti-invariant under W₆): g_* O_Z(−1) = O(−1)^{⊕N} = O(−1)^6. (rank N=6, χ=0, H⁰=0; six values ≤−1 summing to −6 → all=−1.)

**Combined:** f_* O = [O ⊕ O(−1)^{N−1}] ⊕ O(−1)^N = O ⊕ O(−1)^{2N−1} = O ⊕ O(−1)^{11}. ✓

**Key determinants:**

| Piece | Rank | det | dual det | χ(dual det) |
|-------|------|-----|----------|-------------|
| W₆-even: O ⊕ O(−1)^{N−1} | N = 6 | O(−5) | O(5) | N = 6 |
| W₆-odd: O(−1)^N | N = 6 | O(−N) = O(−6) | O(N) = O(6) | L = 7 |
| Total: O ⊕ O(−1)^{11} | index = 12 | O(−11) | O(11) | 12 |

**Consequence for IR: binary selection.** The IR self-energy Σ = −χ(dual det of loop bundle). Two candidates from Atkin-Lehner:

| Choice | Dual det | χ | Σ | IR = (π/36)·(j+N)/(j−Σ) | α⁻¹ |
|--------|----------|---|---|--------------------------|------|
| W₆-odd | O(N) = O(6) | L = 7 | −7 | (π/36)·1734/1735 | 137.035999202 |
| W₆-even | O(N−1) = O(5) | N = 6 | −6 | (π/36)·1734/1734 | 137.035948904 |

Difference: π/(36·1735) = 0.0000503 = 0.367 ppm.

**Experimental discrimination:**

| Measurement | α⁻¹ ± σ | Pull (odd) | Pull (even) |
|-------------|----------|------------|-------------|
| CODATA 2022 | 137.035999177 ± 0.000000021 | −1.2σ | +2394σ |
| Rb (Morel 2020) | 137.035999206 ± 0.000000011 | +0.4σ | +4573σ |

The even choice is killed at ≈2400σ (CODATA) / ≈4600σ (Rb). The odd choice survives within 1.2σ.

**Honest status.** The splitting, factorization, and both determinants are [THM]. The selection of W₆-odd over W₆-even is an **empirical 1-bit input** (confirmed at ≈2400σ), not a derivation. The physical argument "gauge field = W_N-odd = modular parity" is an **analogy** (W_N acts on τ, SM parity acts on spacetime — different spaces, no proven bridge). The space of IR candidates is reduced from infinite to **binary** — a real structural refinement. But the 1-bit selection remains empirical, so the overall ~80% [THM/DER] does not change.


## [DER] H.2: μ₀ = 6π⁵ and the μ formula
Source: Paper §5.1–5.3
Status: LO [DER], NLO [DER], series [THM]
Dependencies: A.1

### Leading order: μ₀ = N · π^{N−1} = 6π⁵

μ₀ = 6π⁵ ≈ 1836.118 (19 ppm from μ_exp = 1836.15267).

First noted by Lenz (1951). Structural embedding: N = 6 from Γ₀(6), exponent N−1 = 5 from index = 2N (uniquely determines the power of π), π from SL₂(ℝ)-invariance of the hyperbolic metric.

### NLO coefficient: C = 10/9

$$C = \frac{|B_1|}{|B_1 \setminus \{\sqrt{2}\}|} = \frac{\text{index} - d_1}{\text{index} - d_2} = \frac{10}{9}$$

Three independent expressions give the same C:
1. Cardinality ratio of B₁ with/without √2
2. Index minus ramification indices ratio
3. Unique (C, p, q) triple satisfying μ NLO constraint

Residual after NLO: 0.009 ppm.

### NNLO series: cₙ from Riemann-Roch [THM 5.1]

$$c_n = -\frac{\dim S_{2n+2}(\Gamma_0(6))}{\dim M_{2n+2}(\Gamma_0(6))} = -\frac{2n-1}{2n+3}$$

**Proof:** For Γ₀(6) with g = 0, ν₂ = ν₃ = 0, #cusps = 4, the standard dimension formulas give (verified by Sage for all k ≤ 20):

dim M_{2n+2}(Γ₀(6)) = 2n + 3
dim S_{2n+2}(Γ₀(6)) = 2n − 1 (for n ≥ 1)

Ratio: dim S / dim M = (2n−1)/(2n+3). With sign convention: cₙ = −(2n−1)/(2n+3). ∎

### Full μ formula

$$\mu = 6\pi^5\left(1 + \frac{10\alpha^2}{9\pi}\left(1 + \sum_{n=1}^{\infty} c_n \left(\frac{\alpha}{\pi}\right)^n\right)\right), \quad c_n = -\frac{2n-1}{2n+3}$$

Series converges rapidly: c₁ = −1/5, c₂ = −3/7, c₃ = −5/9, ... with α/π ≈ 0.00232.


## [DER] H.3: Formula G
Source: Paper §7
Status: [DER]
Dependencies: H.1, H.2

### Statement
$$G = \frac{e^2}{\varepsilon_0 \cdot m_e^2 \cdot \alpha^{-2q}}, \qquad q = \frac{1}{\alpha^2 \cdot \mu_G}$$

where μ_G = (3μ + μ_n − B_d/m_e)/4 = (m_p + m_d/2)/(2m_e) = 1835.697. This is the weighted nucleon mass average, involving the neutron mass m_n and deuteron binding energy B_d — **nuclear data external to LD**. The difference Δ = μ − μ_G = 0.456 = (B_d − Δm_np)/(4m_e) encodes nuclear isospin splitting and binding. μ_G is NOT derivable from §H.2 at any truncation order: H.2 gives μ ≈ 1836.153 at all orders (the series converges at α/π ≈ 0.002), not 1835.697.

### Leading order q
q_LO = (index · ∏wᵢ)² / (N · π^{N+1}) = 432² / (6π⁷) = 186624 / (6 · 3020.29) = 10.298 (δ = 0.67% from exact q = 10.2298).

### Numerical result
G_pred = 6.67407 × 10⁻¹¹ m³/(kg·s²).
- vs CODATA 2018 (6.67430): −35 ppm (with CODATA α)
- vs CODATA 2014 (6.67408): −0.1 ppm
- Previous companion value 6.67410 was rounded incorrectly (S115 verification)

### Hierarchy formula
M_Pl/m_e = α^{−q}/√(4πα). The exponential hierarchy arises because α²·μ_G ≈ 0.098 ≪ 1, making q ≈ 10.23 ≫ 1 and α^{−q} ≈ 10²².

### G is a prediction given nuclear data [S110 CORRECTED]
G is predicted by the forward pass α(H.1) → μ(H.2) → μ_G(nuclear) → G(H.3). It is NOT a ring-closure condition: the ring is open at G because μ_G requires nuclear masses (m_n, B_d) not derived from Γ₀(6). The −35 ppm deviation measures the precision of the forward prediction, not the weakest link of a closed ring.

### Ring is open at G [S110, KEY]
The ring is closed at L1 (α, μ): both are derived from Γ₀(6) without external inputs. The ring is **open** at L1b (G): the formula G requires μ_G = (3μ + μ_n − B_d/m_e)/4, which involves nuclear masses that LD does not derive. The 248 ppm gap between μ and μ_G is amplified ×101 by the G-elasticity (H.3a), producing the observed −35 ppm deviation. This was known from constitution v4.4 (§G5) but obscured in the companion by the incorrect description of μ_G as "NLO truncated H.2" (corrected S110).

### Δ = μ − μ_G = 0.456 (0.025%)
This is the SOLE channel through which particle content enters G [S44]. μ comes from all particles; μ_G is the truncated version entering q. The difference Δ encodes all the information about individual particle masses that gets amplified into G.

### Ultrasensitivity
δq = 10⁻⁴ shifts G by ~1000 ppm. This is why G is the most sensitive test: it amplifies tiny errors in μ by ~100×.


### [THM] H.3a: G-elasticity (S110)

For G = C₀ · α^{2q} with q = 1/(α²·μ_G):

∂(ln G)/∂(ln α)|_{μ_G} = 2q(1 + 2·ln α⁻¹) = 221.8

∂(ln G)/∂(ln μ_G)|_{α} = 2q·ln α⁻¹ = 100.7

Ratio: α-sensitivity = 2.20× μ_G-sensitivity.

Proof: direct differentiation. |F'(α*)| = 2·ln(α⁻¹) = 9.84 >> 1 → naive iteration diverges (not Banach contraction). Verified numerically <0.001%. ∎

Error budget: α precision (0.03 ppb Form A) → δG = 0.007 ppm. μ_G gap (248 ppm) → δG ≈ 25000 ppm = 2.5%. G-error entirely μ_G-dominated.


## [DER] H.4: √2-knockout
Source: S40, corrected S42
Status: [DER]
Dependencies: H.3

### Statement
Removing √2 from B₁ (setting C = |B₁|/(|B₁|−1) = 1 instead of 10/9):
- δμ = −1.88 ppm (μ shifts down)
- Amplification through G: ×100.7
- δG = −189 ppm → **8.4σ from CODATA 2018**

One irrational number (√2, from EWSB) is necessary for ring closure.

**CORRECTED (S42):** Original claim was 14σ, ×200. Correct: 8.4σ, ×100.7.

### Implication
C₂f · C₂f = 1 ⟺ (d₁,d₂) = (2,3). The quadratic Casimir condition that ensures √2 ∈ B₁ uniquely selects the LD generator pair. This is path #4 to (2,3).


## [DER] H.5: Self-consistent ring
Source: Paper §5.5, S38
Status: [DER]

### Statement
The forward pass H.1 → α → H.2 → μ → (nuclear data) → μ_G → H.3 → G predicts G without G as input:
- G_pred = 6.67407 × 10⁻¹¹, δG = −35 ppm (CODATA 2018).
- Inputs: α (from H.1), μ (from H.2), **plus nuclear masses** (m_n, B_d) for μ_G.

**The ring is NOT a Banach contraction mapping.** The naive iteration F(α) = (G_exp/C₀)^{α²μ_G/2} has |F'(α*)| = 2·ln(α⁻¹) ≈ 9.84 >> 1 and diverges. The "3 iterations" convergence uses Newton's method (quadratic convergence from a good initial guess), not geometric contraction.

**The ring is NOT closed at G.** Substituting μ from H.2 (= 1836.153) instead of μ_G (= 1835.697) into H.3 gives δG = +2.5% — unacceptable. The gap μ − μ_G = 0.456 = (B_d − Δm_np)/(4m_e) requires nuclear physics that LD does not derive. G is a **prediction given nuclear data**, not a ring-closure condition.

α is determined by H.1 independently of G. μ is determined by H.2 given α. The system is a forward pass with a consistency check, not a fixed-point iteration.

### How it works
1. Start with α_guess (e.g., CODATA value)
2. Compute μ from §H.2
3. Compute g = μ^{1/4}
4. Compute all 12 masses from m_n = m_e·g^n·K(n)
5. Compute G from §H.3
6. Extract α from G (inverting §H.3)
7. Compare with α_guess → iterate

The ring uses Newton's method near the fixed point (not geometric contraction). The proton (m_p = m_e·μ, anchor) fixes g without relying on the δK formula, making the ring insensitive to L2 errors.

### Ring blindness [S63, KEY]
The ring is BLIND to the choice of (a,b) in the δK formula. Reason: the proton has ℓ = 0, K = 1, so δK_pred(p) = (α/2π)·Φ(4) regardless of (a,b) — and the proton is the sole L1↔L2 channel (it determines μ_G).

Consequence: the ring CANNOT select between bare ω_{X/Y} (a=2, b=1) and D₀ twist (a=3, b=1). In fact, without anchor p, bare ω is BETTER (0.20% vs 0.80% ring residual). D₀ is justified ONLY by ramification + 10/10 signs, not by the ring.

### Hierarchy of theory levels [S63, KEY]
```
L0: Γ₀(6) exists                     [POSTULATE]
L1: α, μ from Γ₀(6)                 [DER/THM] — closed, no external inputs
L1b: G from α + μ_G                  [DER] — OPEN: μ_G requires nuclear data (m_n, B_d)
L2: Φ, ℓ → individual masses         [THM for (a,b), DER for ℓ] — tested by signs
L3: CKM, PMNS → mixing/dynamics      [OBS for CKM, CONJ for PMNS]
```

### Structural inputs (complete honest list)

| Input | Role | Type |
|-------|------|------|
| mₑ | Sole dimensionful scale | INPUT |
| α_s(M_Z) | QCD (enters only through proton) | INPUT |
| A_F = ℂ⊕ℍ⊕M₃(ℂ) | d₁=2, d₂=3 → N=6 | STRUCTURAL (NCG) |
| Γ₀ family | Motivated (Lemma 4.1), not derived | MOTIVATED |

Everything else — B₁, μ, α, G, all 13 masses, PMNS angles — follows from Γ₀(6).


---

# I. NEUTRINOS AND PMNS

## [CONJ] I.1: Neutrino masses (0 free parameters)
Source: Paper §8
Status: [CONJ] (n-assignments not derived from dessin; K values from B₁)

### Assignments and masses

| Neutrino | n | K | m (meV) | m² (10⁻³ eV²) |
|----------|---|---|---------|---------------|
| ν₁ | −9 | 1/3 | 7.72 | 5.96×10⁻⁵ |
| ν₂ | −9 | 1/2 | 11.58 | 1.34×10⁻⁴ |
| ν₃ | −8 | 1/3 | 50.52 | 2.55×10⁻³ |

Σmν = 69.8 meV. Normal hierarchy required.

### Mass-squared differences
- Δm²₂₁ = m₂² − m₁² = 7.446 × 10⁻⁵ eV² (NuFIT 6.0: 7.49±0.19 → **+0.23σ**)
- Δm²₃₁ = m₃² − m₁² = 2.493 × 10⁻³ eV² (NuFIT 6.0: 2.513±0.020 → **+1.0σ**)

### Computation
m = mₑ · g^n · K, with g = μ^{1/4} = 6.546.

For n < 0: g^n = 1/g^{|n|}. Key values: g⁸ = μ² = 3.371×10⁶, g⁹ = μ²·g = 2.206×10⁷.

- ν₁: m = 0.511/(2.206×10⁷ · 3) = 7.72×10⁻⁹ MeV = **7.72 meV** ✓
- ν₂: m = 0.511/(2.206×10⁷ · 2) = 1.158×10⁻⁸ MeV = **11.58 meV** ✓
- ν₃: m = 0.511/(3.371×10⁶ · 3) = 5.052×10⁻⁸ MeV = **50.52 meV** ✓

### Parameter count caveat
The neutrino sector uses 6 discrete inputs (n₁, n₂, n₃, K₁, K₂, K₃) to predict 3 observables (Σmν, Δm²₂₁, Δm²₃₁). This is formally **overfit** (6 > 3). The defence: all K ∈ B₁ (10-element discrete set, not continuous), and n-values are constrained by the lattice. But unlike the charged fermion sector, **neutrino (n,K) assignments are NOT derived from the dessin** — they are chosen from B₁ to match data. Status: conjecture with plausible inputs, not prediction.

### Cosmological status
- DESI DR2 (2025): excludes Σmν = 69.8 meV at 2.9σ in ΛCDM
- BUT DESI itself excludes ΛCDM at 2.8–4.2σ
- In w₀wₐCDM: LD prediction is inside allowed region
- If ΛCDM confirmed → LD neutrino sector falsified

### Relation to I.28 (S153.1 audit, updated S192)
I.28 presented an alternative: m₁ = 0 from L_eff null mode (Σmν = 58.8 meV). **I.28.2 item 1 (m₁=0) is KILLED (S192):** the forced ν₁↔ν₂ swap maps ν₂ (not ν₁) to the null mode, making f(0) = 0 unphysical under normal ordering. I.1 (fitted, m₁ = 7.72 meV) remains the only active neutrino mass prediction. DESI full (2026+) can test Σmν at ±15 meV.


## [DER] I.2: sin²θ₁₂ = 4/13 = 0.30769
Source: S8 (original ansatz), Paper §8 Conj 8.1, **upgraded S204 via X.100**
Status: **[DER]** (was [CONJ] pre-S204)

### Origin (K-ratio ansatz, S8)
tan θ₁₂ = K₁/K₂ = (1/3)/(1/2) = 2/3. Then sin²θ₁₂ = tan²/(1+tan²) = (4/9)/(1+4/9) = 4/13.

Equivalently: sin²θ₁₂ = d₁²/(d₁²+d₂²) = 4/13.

### Cross-ratio derivation (X.100, S204) — upgrades to [DER]

The cross-ratio of four canonical points on the Hauptmodul ℙ¹ gives:

  CR(−index, 0; −d₂², −d₁³) = d₁/d₂ = 2/3 = tan θ₁₂

Four-tuple: a = −12 (unique rational j=0 preimage, W₃-fixed), b = 0 (quark cusp), c = −9 (lepton cusp), d = −8 (boson cusp). All four points are canonical: j=0 triple point (K.5) + 3 non-anchor cusps. No selection.

CR = (−12+9)(0+8)/((−12+8)(0+9)) = (−3)(8)/((−4)(9)) = 2/3. ∎

**Why [DER]:** Cross-ratio = projective invariant of the Belyi map (dessin-intrinsic). Four-tuple = j=0 rational root + 3 non-anchor cusps (canonical). Satisfies DESSIN-PRIMACY (A.0). The one selection step: the identification tan θ₁₂ = CR, which follows from the cusp-width ratio K_bos/K_lep = (1/3)/(1/2) = w_bos/w_lep (same as original K-ratio ansatz, but now the 2/3 is the canonical CR, not an ad hoc ratio).

Deps: C.9f, K.5, E.2, V.4.

### Experimental test
JUNO (November 2025, arXiv:2511.14593): sin²θ₁₂ = 0.3092 ± 0.0087. Pull: **+0.17σ** ✓.
NuFIT 6.0 IC19 (NO): sin²θ₁₂ = 0.307 ± 0.012. Pull: **−0.06σ** ✓.
TBM (1/3): **−2.8σ** (JUNO) ✗.

### Status upgrade attempt (S73)
det(M_lep) = 13 = d₁²+d₂² (§D.5). This connects the denominator 13 to the leptonic block of BB^T. sin²θ₁₂ = d₁²/det(M_lep) = 4/13 [DER cond.].

**BUT:** BB^T eigenvectors give θ₁₂ = 0.211 (WRONG, −7.7σ). The K-ratio ansatz tan = 2/3 gives the correct value, but is not derived from M_lep. The det = 13 observation connects denominators, but eigenvectors don't match.

### CKM connection (X.100, S204)
tan γ_CKM = CR⁻² = d₂²/d₁² = 9/4, giving γ = 66.04°. Exp: (65.5 ± 2.8)°, pull = −0.19σ. **Both PMNS θ₁₂ and CKM γ are functions of the same projective invariant CR = d₁/d₂.**

### Anharmonic group orbit (X.100a, S204) [THM-arith]
The 6 values of S₃ acting on CR = 2/3: {2/3, 1/3, 3/2, 3, −1/2, −2} = {d₁/d₂, 1/d₂, d₂/d₁, d₂, −1/d₁, −d₁}. All 6 = LD fundamental constants. The anharmonic group of the cross-ratio IS the (d₁,d₂) arithmetic.

### h-factors as CR powers (X.100b, S204) [THM-arith / OBS]
h(face 6) = CR = d₁/d₂ = tan θ₁₂. h(face 2) = CR⁻² = d₂²/d₁² = tan γ_CKM. NLO mass corrections and mixing angles share the same cross-ratio origin.


## [THM-arith / CONJ] I.3: Tree-level PMNS from μ-τ symmetry
Source: S73 §4.4
Status: **[THM-arith]** for eigenvector structure; **[CONJ]** for PMNS identification
Dependencies: D.5 (leptonic block); **[CONJ I.3-ID]:** M_lep eigenvectors = PMNS columns

### Statement
From μ-τ symmetry of M_lep (§D.5):
- **sin²θ₁₃ = 0** exactly at tree level
- **sin²θ₂₃ = 1/2** (maximal atmospheric mixing)

### Proof
The eigenvector of M_lep with eigenvalue λ₃ = 1 is (0, −1/√2, +1/√2) — antisymmetric under μ↔τ. This gives |U_{e3}|² = 0, hence sin²θ₁₃ = 0. And |U_{μ3}| = |U_{τ3}| = 1/√2, hence sin²θ₂₃ = 1/2.

Qualitative match: θ₁₃ is the smallest PMNS angle (exp: 0.022 ≈ 0), θ₂₃ is near maximal (exp: 0.57 ≈ 0.50).

### ⚠ Identification caveat (S98 audit)
The eigenvector computation is [THM-arith]: pure linear algebra of a concrete 3×3 matrix. The identification «these eigenvectors = PMNS columns» is [CONJ]: M_lep is a block of BB^T (dessin biadjacency), not a neutrino mass matrix. The physical bridge M_lep → M_ν is not proven. See §I.25 (Identification Hierarchy) for the precise logical chain and the seesaw structural analogy that motivates but does not close this gap.

### What breaks μ-τ [OBS, S73 §4.5]
τ is the UNIQUE lepton whose S-partner (σ₁-image) exits the fermionic sector: σ₁(τ) = H (boson). For e and μ: S-partners are quarks (d and b respectively; see §O.1). This provides the sole qualitative source of μ-τ breaking. Quantitative mechanism: OPEN.


## [DER] I.4: sin²θ₁₃ = 2/91
Source: S73 §3, **upgraded S217 via X.129**
Status: **[DER]** (was [CONJ] pre-S217, upgraded via X.129; channel rule closed by X.130).

### Index formula derivation (X.129, S217)

sin²θ₁₃ = [SL₂(ℤ):Γ₀(N)] / (N·∏_{p|N} Φ₃(p)) = index/(N·L·det_M) = 12/546 = **2/91**.

Euler product: ∏ Φ₂(p)/(p·Φ₃(p)) = (3/14)·(4/39) = 2/91.

Identification step same type as θ₁₂ (X.100: CR→tan) and θ₂₃ (X.101: CR→tan). Supported by: uniqueness at 1σ among 17 invariants (X.128), forced assignment (4/13 unreachable from Res, 2/91 unreachable from CR), canonical Γ₀(N) form.

### Original scan (S73)

From scan of ~50,000 expressions over Γ₀(6) invariant pool:

| Candidate | Formula | Value | Pull (NuFIT 6.0 IC19: 0.02195±0.00054) |
|-----------|---------|-------|-----|
| A | d₁³/(d₂·dim²M₁₀) = 8/363 | 0.022039 | **−0.17σ** |
| B | d₁/(L·(d₁²+d₂²)) = 2/91 | 0.021978 | **−0.05σ** |

Candidate B preferred: 91 = 7·13 = L·det(M_lep). Gives sin²θ₁₃ = sin²θ₁₂/(d₁·L) = (4/13)/14. Transparent hierarchy: θ₁₂ ≫ θ₁₃ by factor d₁·L = 14.


## [DER] I.5: sin²θ₂₃ = 81/145 = 0.55862
Source: Paper §8, S73, corrected S77, **upgraded S204 via X.101**
Status: **[DER]** (was [CONJ] pre-S204)

### Cross-ratio derivation (X.101, S204)

The cross-ratio of the four cusps of X₀(6) on the Hauptmodul ℙ¹ gives:

  CR(∞, 0; −d₁³, −d₂²) = d₂²/d₁³ = 9/8

Four cusps: ∞ (anchor, w=1), 0 (quark, w=6), −8 (boson, w=2), −9 (lepton, w=3). Maximally canonical four-tuple (all cusps, no selection).

  sin²θ₂₃ = CR²/(1+CR²) = d₂⁴/(d₂⁴+d₁⁶) = 81/145 = 0.55862

### Key identities (X.101a) [THM-arith]
- d₂⁴ + d₁⁶ = index² + 1 = 145 ⟺ d₁ = 2. **Path 43 to N=6.**
- Equivalent: sin²θ₂₃ = d₂⁴/(index²+1), cos²θ₂₃ = d₁⁶/(index²+1).

### Pythagorean structure
- θ₁₂: (A,B) = (d₁, d₂), diff = 1 (consecutive). sin² = d₁²/(d₁²+d₂²) = 4/13.
- θ₂₃: (A,B) = (d₂², d₁³), diff = 1 (Catalan). sin² = d₂⁴/(d₂⁴+d₁⁶) = 81/145.

### Octant prediction [PRED, falsifiable]
d₂² > d₁³ (Catalan: 9 > 8) → sin²θ₂₃ > 1/2 → **UPPER OCTANT**.
Deviation: sin²θ₂₃ − 1/2 = 17/290, numerator 17 = d₂²+d₁³ (Catalan sum).
- NuFIT 6.0 IC19 (0.561 ± 0.015): pull = **+0.16σ** ✓
- NuFIT 6.0 IC24+SK (0.470 ± 0.017): pull = **−5.2σ** (lower octant, 5.2σ conflict)

### Previous candidates (S73–S77)
Tree-level from μ-τ symmetry: sin²θ₂₃ = 1/2. Exp: 0.561 ± 0.015 → **+4.1σ** (IC19).
13/24 = 0.5417: post-hoc [S77], 6 competing ratios. Not unique.
Heat kernel (I.17): 0.6048. Too high: IC19 pull −2.92σ.

**CORRECTION (S77):** Paper v4 prediction "θ₂₃ lower octant" is **WRONG**. LD consistently predicts upper octant: 1/2 = maximal, 81/145 = 0.559 = upper, HK = 0.605 = upper.

Deps: W.1, A.1 (cusp widths), X.100 (mechanism).

### Unified CR table (X.101b) [THM-arith]

| Angle | tan θ | Cross-ratio source | sin²θ |
|-------|-------|-------------------|-------|
| γ_CKM | d₂²/d₁² = 9/4 | CR₁₂⁻² | 81/97 |
| θ₁₂(PMNS) | d₁/d₂ = 2/3 | CR{j=0,q,l,b} | 4/13 |
| θ₂₃(PMNS) | d₂²/d₁³ = 9/8 | CR{4 cusps} | 81/145 |


## [THM] I.6: Cayley graph Laplacian spectrum
Source: S77
Status: [THM]
Dependencies: C.1 (dessin), C.3 (uniqueness 36/36)
Verified: Sage (3/3 dessins, exact char poly)

### Statement
The Cayley graph of X₀(6) dessin with generators {σ₀, σ₀⁻¹, σ₁} is 3-regular. Its Laplacian L = 3I − A has characteristic polynomial:

char(L) = x(x−1)(x−3)²(x−4)(x−5)³(x²−5x+1)(x²−5x+5)

Discriminants: Δ₁ = 21 = d₂·L, Δ₂ = 5 = N−1. Sum Δ₁+Δ₂ = 26 = 2·13 = 2(d₁²+d₂²). Identification with LD invariants is [OBS].

Dessin-invariant: identical for all 36 isomorphic dessins (verified 3/3).

### [THM-computational] Isospectrality X₀(6) ↔ X₀(11) (S108)

The Cayley graphs on P¹(ℤ/6ℤ) and P¹(ℤ/11ℤ) have **identical** Laplacian spectra (same char poly above). Graphs are SNI (spectral non-isomorphic): σ∞ cycle types differ ({6,3,2,1} vs {11,1}). All Tr(Aᵏ) coincide. **Consequence:** Cayley spectrum CANNOT distinguish N=6 from N=11. Any spectral invariant (traces, det', heat kernel, zeta) is shared. Distinction lies in cuspal structure (σ∞), invisible to undirected graph. **STM program DEAD** (S108).

### [THM-computational] det'(L) = N²(N−1)⁴ uniquely at N=6 (S108)

det'(L_Cayley) = 22500 for both X₀(6) and X₀(11). The equation N²(N−1)⁴ = 22500 = 2²·3²·5⁴ has unique positive integer solution N=6. Spanning trees: τ(G) = det'/n = 1875 = d₂·(N−1)⁴. **Status:** formula verified numerically; analytic proof connecting Cayley det' to N²(N−1)⁴ not yet written.

### [THM-comb] Graph automorphism (S112, corrects S109)

The undirected Cayley graph has |Aut(G)| = 2. The sole non-trivial automorphism is **(c ↔ p)**: the swap of the two multi-edge endpoints. **Proof:** Only c and p have non-distinct neighbor multisets (nbrs(c) = {u,p,p}, nbrs(p) = {c,c,u}); all other 10 vertices have 3 distinct neighbors (verified computationally, §O.1). Undirected operator basis has rank 11 (not 12). **Consequence:** any operator approach to Φ−Lℓ via undirected Cayley graph is blocked at rank 11; directed operators restore rank 12 but give tautological interpolation (dim ℝ¹² = 12).

**S109 CORRECTION:** The S109 claim "φ = (W↔H)(e↔b)(s↔μ)(τ↔d)" was computed from an incorrect σ₁ map and is **WRONG**. The "minimal breaking word (σ₀σ₁)³" claim is also wrong. See §Z corrections log.


## [THM] I.7: No-go for f(M_lep) → 4/13
Source: S77
Status: [THM]
Dependencies: D.5 (μ-τ symmetry)
Verified: Sage + numpy (25 matrix variants)

### Statement
No function f(M_lep) can yield sin²θ₁₂ = 4/13.

### Proof
M_lep has μ-τ symmetry → eigenvector with λ₃ = 1 has U_e = 0. The three possible sin²θ₁₂ values from any eigenvector ordering of f(M_lep) are:

{0, (3+√3)/6 ≈ 0.789, 1}

4/13 ≈ 0.308 is not among them. Since f(M_lep) and M_lep share eigenvectors for any analytic f, this is a no-go. ∎

Tested: 25 variants (D⁻¹/²MD⁻¹/², M⁻¹, M^{1/2}, exp(−M), adj(M), etc.). All give sin²θ₁₂ ∈ {0, 0.789, 1}.

Extension: M_lep + arbitrary symmetric perturbation, 14400-point scan. 4/13 achievable only with sin²θ₁₃ > 0.45 (exp: 0.022). DEAD.


## [THM] I.8: Double-transversal triples
Source: S77
Status: [THM]
Dependencies: D.1 (Anchor Lemma), I.6
Verified: Sage (3/3 dessins, exhaustive)

### Definition
A triple T = (a,b,c) with one edge per non-anchor BV is **σ₁-double-transversal** if σ₁(T) also contains one edge per non-anchor BV.

### Theorem
There are exactly **4** double-transversal triples among C(12,3) = 220 BV-transversal triples.

### Proof
Anchor Lemma (D.1) → exactly 1 non-anchor edge has σ₁-partner in anchor BV. This edge is in BV₁. Remaining eligible from BV₁: 2 choices.

σ₁ acts as derangement on non-anchor BVs (no non-anchor edge maps to its own BV, verified 3/3). Double-transversality requires σ₁|_T to be a derangement of {BV₁, BV₂, BV₃}. There are exactly 2 derangements of 3 elements. Count = 2 × 2 = 4. ∎

### Lepton uniqueness [THM]
The leptonic triple is the UNIQUE double-transversal triple lying entirely within a single σ∞-face (the 3-face). The other 3 cross multiple faces.


## [OBS] I.9: Heat kernel |U_e|² = 4/13 at t = 1/d₁
Source: S77
Status: [OBS]
Dependencies: I.6 (spectrum), I.8 (double-transversal)
Verified: Sage + scipy (3/3 dessins)

### Statement
exp(−tL) at t = 1/d₁, i.e. exp(−L/d₁), restricted to any double-transversal triple T gives a 3×3 matrix H_T whose top eigenvector has:

|U₀|² = 0.30769089 ≈ 4/13 = 0.30769231

Δ = −1.42 × 10⁻⁶ (**4.6 ppm relative**). NOT exact: crossing at t = 0.49997, not 1/2.

### Key equivalence [THM]
{triples with |U₀|² ≈ 4/13 (±0.1%)} = {double-transversal triples} = 4 of 220.

### PMNS-like angles (leptonic triple, ecc-ordered)

| Angle | Heat kernel | Experiment |
|-------|------------|------------|
| sin²θ₁₂ | 0.310 | 0.304±0.012 |
| sin²θ₁₃ | 0.006 | 0.022±0.001 |
| sin²θ₂₃ | 0.556 | 0.57±0.02 |

### What is NOT proven
1. t = 1/d₁ not derived (observational choice)
2. |U₀|² ≠ 4/13 exactly (4.6 ppm relative gap)
3. H_T eigenvectors = PMNS columns not derived
4. Leptonic triple selection from face type, not heat kernel


## [OBS] I.9a: t* transcendentality
Source: Flavor session A.1 (2026-03-18)
Status: [OBS]
Dependencies: I.6, I.9
Verified: mpmath (40 digits), PSLQ

### Statement
The exact crossing |U_e|²(t*) = 4/13 occurs at:

t* = 0.4999712606661622389708884849984233828336

Δ(t* − 1/2) = −2.874 × 10⁻⁵.

PSLQ tests: t* ∉ ℚ (denom ≤ 10⁶), t* ∉ ℚ(√5), t* ∉ ℚ(√21), no minimal polynomial degree ≤ 8 with coefficients ≤ 10⁶.

**The 4.6 ppm gap is STRUCTURAL and UNCLOSABLE** by choice of diffusion time. t = 1/d₁ is the best motivated rational choice.


## [RECORD] I.9b: Spectral decomposition of heat kernel
Source: Flavor session A.2 (2026-03-18)
Status: [RECORD]
Dependencies: I.6, I.9

### Statement
Decomposition of ⟨u₀|H_T(1/2)|u₀⟩ by Cayley Laplacian eigenvalue:

| λ | Contribution | Fraction |
|---|-------------|----------|
| 0 (flat) | 0.2498 | 61.1% |
| (5−√21)/2 ≈ 0.209 | 0.0770 | **18.8%** |
| 3 (×2) | 0.0301 | 7.4% |
| 5 (×3) | 0.0410 | 10.0% |
| (5±√5)/2 (φ-pair) | 0.0001 | **0.015%** |
| others | ~2.6% | |

**Key finding:** φ-eigenvalues contribute 0.015% — golden ratio is IRRELEVANT for heat kernel. The √21-discriminant pair (disc = d₂·L = 21) is dominant non-trivial (18.8%). The 4/13 near-miss is a full interference effect of {0, 0.209, 3, 5}; no subset produces it.


## [DEAD] I.9c: Alternative operators
Source: Flavor session A.3 (2026-03-18)
Status: [DEAD]

L = 3I−A at t = 1/d₁ is OPTIMAL among 11 operators tested (L, L_norm, Q, A, L^{1/3}, W_face·L, L², A², √L, L_weighted, αI−A). Minimum gap = 4.6 ppm. Structural reason: exp(−(αI−A)t) = e^{−αt}·exp(tA); scalar cancels in eigenvectors. Only the adjacency A matters.


## [ALIVE-WEAK] I.9d: φ-perturbation mechanism
Source: Flavor session B.2b (2026-03-18)
Status: [ALIVE-WEAK]

### Statement
H_T(1/2) + ε·P_φ with ε ≈ −0.005 gives all PMNS angles within 2σ:

| Angle | Prediction | Experiment | Pull |
|-------|-----------|------------|------|
| sin²θ₁₂ | 0.314 | 0.304±0.012 | −0.8σ |
| sin²θ₁₃ | 0.020 | 0.022±0.001 | +2.0σ |
| sin²θ₂₃ | 0.597 | 0.570±0.020 | −1.4σ |

One free parameter (ε). No LD derivation of ε found: ε ≠ 1/K, d₂²/L, 1/|B₁|, 1/φ, etc.


## [DEAD] I.9e: φ-eigenvector as PMNS column
Source: Flavor session B.1 (2026-03-18)
Status: [DEAD]

Normalized leptonic restriction of φ-eigenvector: |v|² = (0.096, 0.655, 0.250). Best PMNS match: ν₁ column, ||diff|| = 0.053. Too far.

Leptonic weight = 2/5 exactly [confirmed S90 analytically].


## [DEAD] I.9f: Triple eigenvector → PMNS
Source: Flavor session B.3 (2026-03-18)
Status: [DEAD]

All 220 BV-transversal triples of Laplacian eigenvectors restricted to leptons scanned. Best χ²(PMNS) = 31.9. sin²θ₁₂ = 0.342 (+3.2σ), sin²θ₁₃ = 0.026 (+4.0σ). No viable triple.


## [THM-comp / THM-arith / OBS] I.9g: Modular Flavor Symmetry Bridge (S147, corrected S148)
Source: S147 (corrected S148 audit)
Status: mixed (see per-item)
Dependencies: I.6, I.9, I.9b, S.6, D.5
External: Li, Liu, Ding — arXiv:2108.02181, JHEP 10 (2021) 238

### I.9g.1 [THM-comp] Structural matches with Li-Liu-Ding (6/6)

| # | LD | Li-Liu-Ding (Γ'₆ framework) | Match |
|---|-----|-------------------------------|-------|
| 1 | Mon = PSL₂(ℤ/6ℤ), |Mon|=72 | Γ'₆/{±1} = Γ₆, |G|=72 | exact |
| 2 | CRT: P¹(𝔽₂) × P¹(𝔽₃) [C.7] | S₃ × T' | exact |
| 3 | dim M₁(Γ₀(6)) = 3 | dim M₁(Γ₀(6)) = 3 | exact |
| 4 | j(i) = 1728, E₂(i) = 3/π | same | verified 30 digits |
| 5 | m₁ = 0 [I.28 PRED → **KILLED** S192] | Type V: L₁-Nᶜ coupling forbidden at τ=i | structural |
| 6 | μ-τ symmetry [I.3, D.5] | h₂ = 0 limit at τ = i | structural |

First external confirmation of N = 6 from independent formalism.

### I.9g.2 [THM-arith] 4/13 vs 1/3: trimaximal correction

Modular flavor symmetry at τ = i gives sin²θ₁₂ = 1/3 (trimaximal, from Y⁽⁴⁾₃₀(i) ∝ (1,1,1)).
LD gives 4/13 from heat kernel at t = 1/d₁ on dessin geometry (I.9).

4/13 − 1/3 = −1/39 = −1/(d₂ · det M_lep)

where 39 = 3 · 13 = d₂ · (d₁² + d₂²). NuFIT6.0: LD better by 2.1σ. JUNO: 8.5σ discriminating power.

Physical interpretation: trimaximal = democratic limit (t → 0 or ∞ on Cayley graph). 4/13 = finite-time diffusion at t = 1/d₁ on dessin. The correction is encoded by det M_lep = 13.

### I.9g.3 [THM-comp] Irrep decomposition of HK(e,e; 1/2)

| Irrep (S.6) | Contribution | % of 4/13 |
|-------------|-------------|-----------|
| V₁ (triv⊗triv) | 0.0833 | 27.1% |
| V₃ (triv⊗std_A₄) | 0.1385 | 45.0% |
| V₂ (std_S₃⊗triv) | 0.0196 | 6.4% |
| V₆ (std_S₃⊗std_A₄) | 0.0851 | 27.6% |
| **Total** | **0.3265** | **106.1%** |

Projectors P_ρ from group algebra (unique normal S₃ order 6 and A₄ order 12, verified). Cross-check: Σ_ρ HK_ρ = eᵀ exp(−Lt) e = 0.3265 ✓.

**Note:** HK(e,e; 1/2) = 0.3265 ≠ 4/13. The 4/13 arises from the 3×3 RESTRICTION to DT triple {e,μ,τ} (I.9), not the 12×12 diagonal element. Updates I.9b with irrep labels.

### I.9g.4 [THM-comp] CRT factorization of Cayley spectrum

| Irrep (S.6) | dim | L-eigenvalues | Modular form |
|-------------|-----|---------------|--------------|
| V₁ | 1 | {0} | constant |
| V₃ | 3 | {1, d₁², N−1} | Y⁽²⁾₃₀ |
| V₂ | 2 | {d₂, N−1} | Y⁽²⁾₂₀ |
| V₆ | 6 | {(5±√21)/2, (5±√5)/2, d₂, N−1} | Y⁽²⁾₆ |

Irrational eigenvalues (disc 21 = d₂L, disc 5 = N−1) reside ENTIRELY in V₆. Verified with irrep projectors.

### I.9g.5 [OBS] √d₂ in sextet modular forms

Y⁽⁶⁾₆ᵢᵢ(i) components: (a, a, a, −a/√3, −a/√3, −a/√3). Ratio = −√d₂.

V₆ = std_{S₃} ⊗ std_{A₄}. At τ = i (S-fixed point), A₄-factor democratic, S₃-factor contributes √d₂ via sin(2π/d₂) = √d₂/2. Likely [THM] from CRT structure, not proven.

Same √d₂ in M_lep eigenvalues d₁² ± √d₂ (D.5), but independent channel (graph combinatorics, disc = 4d₂). Two independent √d₂ channels. Does NOT close Gap 9. See D.8.

### I.9g.6 [THM-comp] t-interpolation

| t | |U_e2|² | Regime |
|-------|---------|--------|
| → 0 | 1/3 | trimaximal (modular forms at τ = i) |
| 1/d₁ = 0.5 | 4/13 | LD prediction |
| → ∞ | 1/3 | return to democratic |

### I.9g.7 [DEAD, #45] Naive HK–modular form bridge

w_ρ(e) ≠ |Y_ρ(i)|² (numerically verified for all irreps). w_ρ = projector weight on P¹(ℤ/6ℤ) (function on G/B). Y_ρ(i) = modular form on ℍ/Γ(6) (section of line bundle). Two different geometric objects, one group. Bridge requires dessin geometry (Belyi function), not just group algebra. Formal framework: finite Langlands for PSL₂(ℤ/6ℤ).



### I.9g.8 [THM-comp]: A^k|_lep mu-tau hierarchy (S189)

Source: S189
Dependencies: O.1, I.6
Verified: Two independent implementations, integer arithmetic

**Statement.** The leptonic restriction A^k|_lep of the k-th power of the Cayley adjacency matrix has exact mu-tau symmetry for k <= 3, and first breaking at k = 4:

| k | A^k\|_lep | mu-tau? | Delta_diag | Delta_off |
|---|-----------|---------|------------|-----------|
| 1 | [[0,0,0],[0,0,0],[0,0,0]] | YES | 0 | 0 |
| 2 | 2I+J = [[3,1,1],[1,3,1],[1,1,3]] | YES | 0 | 0 |
| 3 | [[2,1,1],[1,2,2],[1,2,2]] | YES | 0 | 0 |
| **4** | **[[15,9,8],[9,15,10],[8,10,17]]** | **NO** | **-2** | **+1** |
| 5 | [[20,16,16],[16,22,24],[16,24,24]] | NO | -2 | 0 |
| 6 | [[93,74,68],[74,99,87],[68,87,115]] | NO | -16 | +6 |

Where Delta_diag = A^k(mu,mu) - A^k(tau,tau), Delta_off = A^k(e,mu) - A^k(e,tau).

**Structural explanation for k <= 3:** k=1: leptons disconnected (A^1|_lep = 0). k=2: every 2-step walk lepton->X->lepton goes through one non-leptonic intermediate; count equal for all pairs (A^2 = 2I+J). k=3: BV structure treats mu and tau equivalently (both have 3 non-leptonic neighbors in distinct sectors).


### I.9g.9 [THM-comp]: Boson circuit mechanism (S189)

Source: S189
Dependencies: O.1
Verified: Explicit enumeration of all 3^4 = 81 words of length 4

**Statement.** The mu-tau breaking at A^4 is caused by 2 closed 4-step walks (the "boson circuit") that exist for tau but not for mu:

  **Loop 1:** tau -> H -> s -> W -> tau   (word: s1.s0.s1.s0)
  **Loop 2:** tau -> W -> s -> H -> tau   (word: s0inv.s1.s0inv.s1)

Face sequence: lepton(3) -> boson(2) -> quark(6) -> boson(2) -> lepton(3).

**Root cause:** s1(tau) = H (boson, face 2). The boson pair (W,H) forms a 2-cycle under s_inf, and s1(s) = W creates a short circuit back to tau via s0(W) = tau. In contrast, s1(mu) = b (quark, face 6) leads into BV_index, where s0 orbits lead to anchor BV, not back to leptons.

**Quantitative:** 81 words enumerated per lepton. Self-returns: e = 15, mu = 15, tau = 17. Difference tau-mu = 2 (exact, = Delta_diag in I.9g.8). tau-only words = 2 (boson circuits), mu-only words = 0. e-mu democracy exact at A^4 diagonal.

**Group-theoretic form:** In walk convention (s0 o s1), the element (s0 o s1)^2 fixes tau but not mu or e. The boson circuit IS the 4-step word (s1.s0)^2 applied in walk order.


### I.9g.10 [THM-arith]: Resistance distances between leptons (S189)

Source: S189
Dependencies: I.6
Verified: Pseudoinverse of Laplacian, two independent implementations, Fraction approximations to 1e-10

**Statement.** The effective resistance distances on the Cayley graph between leptons:

| Pair | R | Exact fraction |
|------|---|----------------|
| (e, mu) | **1** | 1 |
| (e, tau) | 1.0933... | **82/75** |
| (mu, tau) | 0.8933... | **67/75** |

**Key identities:**
- R(e,tau) - R(mu,tau) = **1/5 = 1/(N-1)** -- total mu-tau asymmetry
- R(e,tau) - R(e,mu) = 7/75 = L/(d2*(N-1)^2)
- R(e,mu) - R(mu,tau) = 8/75 = d1^3/(d2*(N-1)^2)
- Common denominator 75 = d2*(N-1)^2

R(e,mu) = 1 exactly: the electron-muon distance in the graph metric is the simplest possible value.


### I.9g.11 [THM-arith]: L_eff breaking decomposition (S189)

Source: S189
Dependencies: I.6, I.11, O.1
Verified: Exact Fraction Gauss-Jordan inversion of 9x9 L_rr

**Statement.** The mu-tau breaking amplitude in L_eff is controlled by a single LD invariant:

  **Delta = 7/55 = L/((N-1)*dim M_10)**

The breaking matrix: L_eff_break = (7/110)*M_break, where M_break = [[0,-1,1],[-1,1,0],[1,0,-1]] with eigenvalues {-sqrt(3), 0, sqrt(3)}.

**Connection to boson circuit (I.9g.9):** The Schur complement adds diagonal self-energy correction to raw A^4 path-counting breaking. Both originate from s1(tau) = H.

**Relative breaking strength:** In A^4: Delta_diag/Tr = 2/47 ~ 4.3%. In L_eff: 7/224 = 1/d1^5 = 1/32 ~ 3.1%.

Note: the parameter 7/55 already appears in I.11. This section traces its origin to the boson circuit.


### I.9g.12 [DER]: k_break -> P_phi -> t chain (S189, upgraded S193/S194)

Source: S189, spectral bridge upgrade S193 (verified S194)
Dependencies: I.9g.8, I.9g.9, I.6, I.26.4, K.7, D.8b
Verified: Cross-verified (SymPy char poly, word enumeration, Fraction arithmetic, spectral bridge S194)

**Statement.** The diffusion time t = sqrt(5)/2 is determined by the boson circuit length through the chain:

1. s1(tau) = H (boson) -> [O.1]
2. Boson circuit tau->H->s->W->tau, word (s1.s0)^2, length 4 = 2*d1 -> [I.9g.9, THM-comp]
3. k_break = 4 = 2*d1 -> [I.9g.8, THM-comp]
4. det(M^{mu,tau}) = d2^2 - d1^2 = 5 -> [THM-arith, Catalan]
5. P_phi = det(M^{mu,tau}) = N-1 = 5 -> [THM-arith, spectral bridge D.8b]
6. d2 = d1+1 (Catalan) => P_phi - k_break = d1^2 - d1 - 1 = 1 for d1=2 -> [K.7, THM]
7. t = sqrt(P_phi)/d1 = sqrt(5)/2 -> [I.26.4, DER]

**Structural identity:** P_phi - k_break = d1^2 - d1 - 1 for d2 = d1+1. This equals 1 iff d1 = 2 (positive root of x^2 - x - 2 = 0).

**Phi-pair cross-check:** Characteristic polynomial factor x^2 - 5x + 5: trace = product = N-1 = 5 [I.9g.13].

**Status:** [DER]. All gaps closed. Step 5 (P_phi = det(M^{mu,tau})) was the last open gap, closed by spectral bridge D.8b: spec(L_bip)\{d1} ⊂ spec(L_Cayley) [THM-arith] implies the φ-pair eigenvalues of L_bip match L_Cayley, and their product P_phi = det(M^{mu,tau}) = 5. Single remaining selection step: I.26.4 (t = sqrt(P)/d1).


### I.9g.13 [THM-arith]: Phi-pair self-duality (S189)

Source: S189
Dependencies: I.6
Verified: SymPy exact factorization of char(L)

**Statement.** The phi-pair of the Cayley Laplacian (factor x^2 - 5x + 5 of char(L)) satisfies:

  trace(phi) = product(phi) = N-1 = 5

Equivalently: **1/lambda_+ + 1/lambda_- = 1** (harmonic unit).

This is the unique quadratic factor of char(L) with trace = product.

**Duality with 21-pair:**

| Property | phi-pair (x^2 - 5x + 5) | 21-pair (x^2 - 5x + 1) |
|----------|--------------------------|--------------------------|
| Product | 5 = N-1 | 1 (algebraic unit) |
| Trace | 5 = N-1 | 5 = N-1 |
| Harmonic sum 1/lambda | **1** (harmonic unit) | **5 = N-1** |
| Discriminant | 5 = N-1 | 21 = d2*L |


### Spectral decomposition of mu-tau breaking at A^4 [RECORD, S189]

A^4(mu,mu) - A^4(tau,tau) = -2, decomposed by Laplacian eigenspaces:

| Eigenspace | A-eigenvalue | a^4 | mt_diff | Contribution |
|-----------|-------------|------|---------|-------------|
| sqrt21- | +2.791 | 60.7 | -0.0233 | -1.42 |
| lambda=5 (x3) | -2.000 | 16.0 | -0.1000 | -1.60 |
| lambda=1 | +2.000 | 16.0 | -0.0556 | -0.89 |
| phi- | +1.618 | 6.85 | +0.1618 | +1.11 |
| sqrt21+ | -1.791 | 10.3 | +0.0567 | +0.58 |
| lambda=4 | -1.000 | 1.0 | +0.2222 | +0.22 |
| phi+ | -0.618 | 0.15 | -0.0618 | -0.01 |
| **TOTAL** | | | | **-2.00** |

At k=3, these 7 contributions cancel to 0 exactly. At k=4, the cancellation breaks -- controlled by power growth rates.


### h-weighted Schur -> TBM [OBS, S189]

The Schur complement of the h-weighted Cayley Laplacian gives eigenvectors with sin^2 theta_12 ~ 1/3, sin^2 theta_23 ~ 1/2, sin^2 theta_13 ~ 0 (tri-bimaximal). Interpretation: h-weighting restores mu-tau symmetry. L_eff = "TBM + LD correction", and 4/13 - 1/3 = -1/(d2*det M_lep) is the effect of removing h-weights. Status: [OBS]. Connects Gap 3 (h function) to Gap 9 (PMNS).

## [THM-arith / OBS] I.9h: P¹(ℤ/6ℤ) as SL₂ coset space (S149)
Source: S149, alternative convention to Q.3 (table rebuilt from O.1 using T = σ∞)
Status: [THM-arith] (CM invariance), [OBS] (min-norm monomials)
Dependencies: O.1, I.6, I.9g

### Standard identification

S and T act on Γ₀(6)\SL₂(ℤ) ≅ P¹(ℤ/6ℤ) by right multiplication. This gives **T = σ∞, S = σ₁** — a standard property of Belyi maps on modular curves, not specific to LD.

### Corrected P¹ coordinates

| (c,d) | Particle | min ‖ci+d‖² |
|-------|----------|:-----------:|
| (0,1) | p | 1 |
| (1,0) | c | 1 |
| (1,1) | u | **d₁ = 2** |
| (1,2) | b | **N−1 = 5** |
| (1,3) | s | **|B₁| = 10** |
| (1,4) | d | **N−1 = 5** |
| (1,5) | t | **d₁ = 2** |
| (2,1) | e | **N−1 = 5** |
| (2,3) | τ | **det M_lep = 13** |
| (2,5) | μ | **N−1 = 5** |
| (3,1) | W | **|B₁| = 10** |
| (3,2) | H | **det M_lep = 13** |

Assignment: (0,1) = p because T ∈ Γ₀(6) fixes the identity coset and σ∞(p) = p. T-orbit of (1,0): (1,0)→(1,1)→...→(1,5)→(1,0) = σ∞-cycle (c u b s d t). σ₁-pairs verified 6/6 via S-action on representatives.

### Convention note (S156 audit)

This table uses T = σ∞ (Shimura/CCW convention). Q.3 uses T⁻¹ = σ∞ (computational/CW convention), exchanging (c,d) within pairs {u↔t}, {b↔d}, {e↔μ}. Neither is "wrong" — the ambiguity T↔T⁻¹ is standard in Belyi theory for modular curves.

### CM invariance [THM-arith]

**|j(γ,i)|² = |j(γ·S,i)|²** for all γ ∈ SL₂(ℤ), since j(γS,i) = j(γ,i)·j(S,i) and |j(S,i)| = |i| = 1.

Consequence: σ₁-pairs share the same automorphy factor norm at τ = i. This is verified: min ‖ci+d‖² equal for all 6 pairs: {c,p}=1, {u,t}=2, {b,μ}={d,e}=5, {s,W}=10, {τ,H}=13.

### Min-norm values [OBS]

The 5 distinct values {1, 2, 5, 10, 13} = {1, d₁, N−1, |B₁|, d₁²+d₂²} are all LD monomials. **Caveat:** these are the only possible min-norms for (c,d) coprime to 6 with |c|,|d| ≤ 3, hence forced by the level N=6 arithmetic. Not an independent path to (d₁,d₂).

Deps: O.1 (monodromy), C.7 (CRT).


## [THM-arith] I.9j: Unique Elliptic σ₁-Pair (S166)
Source: S166
Status: [THM-arith]
Dependencies: O.1 (monodromy), I.9h (coset representatives), standard SL₂(ℤ) theory

### Statement

For each σ₁-pair {a,b} in P¹(ℤ/6ℤ), the linking transformation
L_{a,b} = γ_a · γ_b⁻¹ ∈ SL₂(ℤ) classifies as:

| Pair | L | |Tr| | Type | Order (PSL₂) | Fixed pt in ℍ |
|------|---|------|------|---------------|----------------|
| **{p,c}** | **±S** | **0** | **elliptic** | **2** | **i** |
| {u,t} | [[5,1],[4,1]] | 6 | hyperbolic | ∞ | ℝ only |
| {b,μ} | [[3,−1],[1,0]] | 3 | hyperbolic | ∞ | ℝ only |
| {d,e} | [[2,−1],[−7,4]] | 6 | hyperbolic | ∞ | ℝ only |
| {s,W} | [[3,−1],[−8,3]] | 6 | hyperbolic | ∞ | ℝ only |
| {τ,H} | [[−1,1],[−5,4]] | 3 | hyperbolic | ∞ | ℝ only |

**Proof:** |Tr(L)| < 2 ⟺ L elliptic in SL₂(ℤ). |Tr| = 0 ⟺ L conjugate to S.
Only {p,c} has |Tr| = 0. All others |Tr| ≥ 3 > 2. ∎

### |Tr| trichotomy

- |Tr| = 0 (elliptic): {p,c} — unique
- |Tr| = 3 (weakly hyperbolic): {b,μ}, {τ,H}
- |Tr| = 6 (strongly hyperbolic): {u,t}, {d,e}, {s,W}

### Corollary 1: n-coincidence [THM-arith]

{p,c} is the ONLY σ₁-pair with n_a = n_b.

| Pair | n_a | n_b | same? |
|------|-----|-----|-------|
| **{p,c}** | **4** | **4** | **YES** |
| {u,t} | 1 | 7 | no |
| {b,μ} | 5 | 3 | no |
| {d,e} | 1 | 0 | no |
| {s,W} | 3 | 6 | no |
| {τ,H} | 4 | 6 | no |

n(p) = n(c) = 4 = d₁² = d₂+1 (Residual Tree identity E.8).

Consequence: (Φ−Lℓ)(p) − (Φ−Lℓ)(c) = L·Δℓ = 7·3 = d₂·L = 21 ∈ ℤ.
Mass polynomial Φ cancels completely; difference purely electroweak.
This is the ONLY pair where Φ drops out.

### Corollary 2: Null-space concentration [THM-comp, DUAL-COMPUTE]

The right null vector of the 11×12 weight-10 eval matrix E(τ₀) is concentrated
≥ 98% on {p,c} at all tested generic τ₀.

| τ₀ | %{p,c} in null-space | %{p,c} in residual |
|-----|---------------------|-------------------|
| 0.13+1.7i | **100.0%** (p=74.6%, c=25.3%) | **98.4%** |
| 0.5+2.0i | **99.8%** (p=82.9%, c=16.9%) | **100.0%** |

Geometric cause: S is elliptic → d_hyp(τ_p, τ_c) < d_hyp(τ_a, τ_b) for all
other pairs → weight-10 constraint concentrated exponentially on {p,c}.

**Status upgrade:** S158 anchor pair dominance X.45a: [OBS] → [THM-arith + THM-comp].
Not numerical accident — geometric theorem from elliptic linking.

Deps: O.1, I.9h, D.6–D.7 (n(p)=n(c)=4 from independent mechanisms).


## [THM-comp / THM-arith / OBS] I.9i: Weight-k Cusp Form Irrep Content (S151, verified S152)
Source: S151, verified S152
Status: [THM-comp] (f₄ decomposition, weight boundary), [THM-arith] (fusion blocking), [OBS] (selection rule)
Dependencies: O.1, I.9h, I.9g.4, S.6, S.11

### I.9i.1 [THM-comp] f₄ = η₁²η₂²η₃²η₆² ∈ V₆

The unique cusp form f₄ ∈ S₄(Γ₀(6)) (LMFDB: 6.4.a.a) has irrep decomposition:

  V₁ = 0%, V₂ = 0%, V₃ = 0%, V₆ = 100%

Verified at 5 base points τ₀ ∈ {i, 0.3+0.8i, 0.5+0.866i, 0.1+1.5i, 0.4+0.5i} with mpmath 50 digits. V₂ = 0 to machine precision at all points. NOT a CM artifact: V₂ = 0 at generic (non-CM) τ₀ confirmed.

σ₁-pair structure at τ₀ = i: all 6 pairs have |ratio| = 1 exactly, consistent with CM invariance |j(γ,i)|² = |j(γS,i)|² (I.9h).

### I.9i.2 [THM-comp] M₄(Γ₀(6)) irrep content

dim M₄(Γ₀(6)) = 5 = 4 Eisenstein + 1 cusp. Irrep content (τ₀-dependent for Eisenstein, fixed for cusp):

| Form    | V₁ content | V₂ content | V₃ content | V₆ content |
|---------|:----------:|:----------:|:----------:|:----------:|
| E₄(τ)  | 100%       | 0          | 0          | 0          |
| E₄(2τ) | nonzero    | **nonzero**| 0          | 0          |
| E₄(3τ) | nonzero    | 0          | **nonzero**| 0          |
| E₄(6τ) | nonzero    | nonzero    | nonzero    | nonzero    |
| f₄      | 0          | **0**      | 0          | **100%**   |

**Eisenstein percentages are τ₀-dependent.** Cusp form f₄ has τ₀-independent decomposition (100% V₆). V₂ rank in M₄ = 1 (filled only by E₄(2τ) and E₄(6τ)).

### I.9i.3 [THM-comp] Weight-6: V₂-free cusp space

dim S₆(Γ₀(6)) = 3. Basis: {f₄·G₂, f₄·G₃, f₄·G₆} where G_d = E₂(τ)−d·E₂(dτ) ∈ M₂(Γ₀(6)).

Hadamard factorization: (f₄·g)|₆ γⱼ = (f₄|₄ γⱼ)·(g|₂ γⱼ).

All three weight-6 cusp forms have **V₂ = 0** (< 10⁻¹⁷ at 50-digit precision). S₆(Γ₀(6)) is V₂-free.

### I.9i.4 [THM-arith + OBS] V₂-free mechanism (fusion + selection rule)

Fusion blocking: f₄ ∈ V₆ and G_d has components in V₁, V₂, V₃. By S.11 fusion rules:
- V₆⊙V₁ → no V₂ ✓
- V₆⊙V₂ → no V₂ ✓ (explains f₄·G₂ V₂-freedom for G₂'s dominant V₂ component)
- V₆⊙V₃ → rank 2 in V₂ ← CAN leak V₂

Selection rule [OBS]: The bilinear map Φ(f₄,·): V₃→V₂ has rank 2 and 1-dim kernel. G₃ and G₆ have **identical** V₃ directions (|⟨G₃,G₆⟩_V₃| = 1.000). This direction lies EXACTLY in ker Φ(f₄,·), explaining V₂-freedom for f₄·G₃ and f₄·G₆ despite fusion allowing rank-2 leakage.

Note: G₂'s V₃ direction is NOT in ker Φ(f₄,·) (|⟨ker,G₂⟩| = 0.05). For G₂, V₂-freedom follows from fusion V₆⊙V₂ = no V₂ (G₂'s dominant irrep is V₂, not V₃).

The selection rule is an arithmetic property of the specific newform 6.4.a.a, not a representation-theoretic constraint.

### I.9i.5 [THM-comp] Sharp V₂ boundary at weight 8

f₄² ∈ S₈(Γ₀(6)). Irrep decomposition:

| τ₀      | V₁   | V₂     | V₃     | V₆     |
|---------|------|--------|--------|--------|
| i (CM)  | 0    | 31.7%  | 21.1%  | 47.2%  |
| generic | 0    | 28.7%  | 24.1%  | 47.3%  |

V₁ = 0 exact (cusp form). V₂ ≈ 30% genuine.

Mechanism: V₆⊙V₆ → V₂ (rank 2) by fusion [S.11]. f₄² sits in V₆⊙V₆ and activates the V₂ directions.

**Sharp boundary theorem:**
- k = 2: S₂ = 0 (V₂-free trivially)
- k = 4: S₄ = ⟨f₄⟩ ⊂ V₆ (V₂-free) [I.9i.1]
- k = 6: S₆ = f₄·M₂ (V₂-free by fusion + selection) [I.9i.3–4]
- k = 8: S₈ ∋ f₄² (V₂ ≈ 30%, NOT V₂-free) [I.9i.5]

Structural reason: S₆ = f₄·M₂, and M₂ has no cusp forms → only V₆⊙{V₁,V₂,V₃} terms. S₈ = f₄·M₄, and M₄ contains f₄ → f₄² triggers V₆⊙V₆ → V₂.

### I.9i.6 Consequence for finite Langlands

The cuspidal-Eisenstein partition V₃⊕V₆ vs V₁⊕V₂ is NOT strict starting from weight 8. Cusp forms populate V₂ through V₆⊙V₆ fusion. The V₂-free zone (k ≤ 6) is a low-weight phenomenon.

The HK irrep decomposition (I.9g.3) has V₂ = 6.4%. This V₂ content is purely Eisenstein at weight 2 — no cuspidal partner below weight 8.

Dependencies: O.1, I.9h, I.9g.4, S.6, S.11.


## [DEAD] I.10: S77 killed approaches

| Approach | Result | Why dead |
|----------|--------|----------|
| f(M_lep) → 4/13 | {0, 0.789, 1} only | μ-τ no-go (I.7) |
| M_lep + σ₁-perturbation | sin²θ₁₂ ∈ (0.82, 1.0) | Wrong direction |
| M_lep + arbitrary P → 4/13 | Only with θ₁₃ > 0.45 | Kills small θ₁₃ |
| d₁²/(d₁²+d₂²) as structural | Circular (= tan ansatz) | No independent argument |
| H_BV averaged over orbits | |U_e|² = 0.214 | Averaging kills signal |


---


## [THM] I.11: Schur complement L_eff
Source: S97
Status: [THM]
Dependencies: I.6 (Cayley Laplacian), C.7 (CRT-bijection)
Verified: Fraction arithmetic × 2 prогона, numpy.eigh

### Definition
L_eff = L_ll − L_lr · L_rr⁻¹ · L_rl, where L is partitioned into leptonic (3×3) and rest (9×9).

### Result (exact, rational)

```
         ⎡  67/55   −37/55   −6/11 ⎤
L_eff =  ⎢ −37/55    82/55   −9/11 ⎥
         ⎣ −6/11    −9/11    15/11  ⎦
```

In integer form: 55·L_eff = [[67,−37,−30],[−37,82,−45],[−30,−45,75]].

### Properties
- **Laplacian:** Row sums = 0. det = 0 (null mode).
- **μ-τ breaking:** L_eff[e,μ] − L_eff[e,τ] = −7/55. L_eff[μ,μ] − L_eff[τ,τ] = 7/55. Breaking parameter = **7/55 = L/((N−1)·11)**.
- **L_ll = 3I** (leptons disconnected in Cayley graph — all neighbours are non-leptonic).
- **Physical source:** Asymmetry from σ₁-images: μ→{quark,quark,boson}, τ→{quark,boson,boson}.


## [THM] I.12: L_eff spectrum
Source: S97
Status: [THM]
Verified: Fraction arithmetic, numpy

### Characteristic polynomial
char(55·L_eff) = x(x² − 224x + 12375). Discriminant = 224² − 4·12375 = **676 = 26² = (d₁·det M_lep)²**.

Full square → eigenvalues rational.

### Eigenvalues

| λ | 55·λ | LD formula |
|---|------|-----------|
| 0 | 0 | null mode |
| **9/5** | 99 | **d₂²/(N−1)** |
| **25/11** | 125 | **(N−1)²/dim M₁₀** |


## [THM] I.13: L_eff eigenvectors
Source: S97
Status: [THM]
Verified: Fraction arithmetic (explicit matrix multiplication)

### Eigenvectors (all components = LD monomials)

| λ | v | Components (e, μ, τ) | |v|² |
|---|---|----------------------|------|
| 0 | **(1, 1, 1)** | democratic | d₂ = 3 |
| 9/5 | **(−L, d₁, N−1) = (−7, 2, 5)** | | N·det M_lep = 78 |
| 25/11 | **(1, −d₁², d₂) = (1, −4, 3)** | | d₁·det M_lep = 26 |

Every component is a monomial in LD invariants. Zero free parameters.


## [THM-arith / CONJ] I.14: Schur PMNS matrix |U|²
Source: S97
Status: **[THM-arith]** for numerical matrix; **[CONJ]** for PMNS identification
Dependencies: I.12, I.13; **[CONJ I.14-ID]:** [M_ν, L_eff] = 0

### Formula
|U_{αi}|² = v_i(α)² / |v_i|²

### Robustness Lemma (I.14-R) [THM-math, S98]
Let f: ℝ → ℝ be injective on spec(L_eff) = {0, 9/5, 25/11}. Then |U_{αi}|²(f(L_eff)) = |U_{αi}|²(L_eff) up to column permutation.

*Proof:* Spectral theorem for real symmetric matrices with distinct eigenvalues: f(L_eff) has the same eigenvectors. |U|² depends only on eigenvector directions, not eigenvalues. ∎

*Verified:* 7 functions (x, x², eˣ, √(x+1), log(x+1), 1/(x+0.1), x³−2x) + order-reversing f(x)=−x. All max|ΔU²| < 10⁻¹⁴.

**Consequence:** The PMNS identification does not require M_ν = L_eff or M_ν ∝ L_eff. It requires only **[M_ν, L_eff] = 0** (simultaneous diagonalizability). This is the minimal form of CONJ I.14-ID.

### Result

|  | ν₁ (λ=0) | ν₂ (λ=9/5) | ν₃ (λ=25/11) | Σ |
|--|----------|-----------|-------------|---|
| e | **1/3** | **49/78** | **1/26** | 1 ✓ |
| μ | **1/3** | **2/39** | **8/13** | 1 ✓ |
| τ | **1/3** | **25/78** | **9/26** | 1 ✓ |

### Key value
**sin²θ₁₃(Schur) = 1/26 = 1/(d₁·det M_lep) = 0.0385.**

Exp: 0.02203 ± 0.00056. Pull: **−29σ**. Not viable alone — requires heat kernel correction.

### ⚠ Identification caveat (S98 audit)
The numerical |U|² matrix above is [THM-arith]: exact rational arithmetic from I.12–I.13. The statement «this is the PMNS matrix» is [CONJ I.14-ID], equivalent to [M_ν, L_eff] = 0. This is motivated by the seesaw structural analogy (L_eff = Schur complement, same algebraic form as type-I seesaw M_eff), but not derived from a physical Lagrangian. See §I.25.


## [THM] I.15: Σ self-energy spectrum
Source: S97+
Status: [THM]
Verified: Fraction arithmetic, numpy

### Definition
Σ = L_ll − L_eff = L_lr · L_rr⁻¹ · L_rl (self-energy from integrating non-leptonic modes).

### Result
55·Σ = [[98, 37, 30], [37, 83, 45], [30, 45, 90]].

Eigenvalues of 55·Σ: **{40, 66, 165}**. Sum = 271, product = 435600.

Eigenvectors = eigenvectors of L_eff (L_eff = 3I − Σ, same basis).

### LD mnemonics [OBS]
40 = Kirchhoff, 66 = N·dim M₁₀, 165 = 3·55 = d₂·(N−1)·dim M₁₀. Post hoc: all integers from 9×9 matrix with {2,3}-structure inevitably express through LD invariants. λ₃ = 3 = d₂ is structural (degree of Cayley graph → maximal self-energy = full absorption).


## [THM] I.16: P₂₁ projector on leptons
Source: S97+
Status: [THM]
Verified: Two independent implementations, precision 10⁻¹⁰

### Statement
P₂₁ = spectral projector of L onto 2D subspace with λ = (5±√21)/2 (disc = 21 = d₂L).

Diagonal on physical leptons:

| Lepton | P₂₁(α,α) | Exact |
|--------|-----------|-------|
| e | 0.1000 | **1/10 = 1/|B₁|** |
| μ | 0.1000 | **1/10** |
| τ | 0.0667 | **1/15** |

Tr_lep(P₂₁) = 4/15. e-μ equality reflects σ₁-structure of graph. τ-breaking consistent with σ₁(τ) = H (boson).

**Self-criticism:** 1/10 = 1/|B₁| is tautological: |B₁| = 2(d₁+d₂) = 10 is built from the same graph parameters. Coincidence of cardinalities, not independent evidence.


## [CONJ] I.17: Heat kernel PMNS at t = √5/2
Source: S97+
Status: [CONJ]
Dependencies: I.6, I.11–I.14
Verified: Two independent codes

### Statement
At t = √(d₁²+1)/d₁ = √5/2, the heat kernel exp(−tL) restricted to the leptonic sector gives PMNS angles (with ν₁↔ν₂ swap):

| Angle | Prediction | NuFIT 5.2 (used S97+) | Pull |
|-------|-----------|------------|------|
| sin²θ₁₃ | 0.02204 | 0.02203 ± 0.00056 | **−0.03σ** |
| sin²θ₁₂ | 0.2897 | 0.304 ± 0.012 | **+1.19σ** |
| sin²θ₂₃ | 0.6048 | 0.570 ± 0.020 | **−1.74σ** |

Σ|pull| = 2.96. All within 2σ.

### NuFIT 6.0 update (arXiv: 2410.05380)

The original pulls above used NuFIT 5.x values (S97+ session, pre-2024). With NuFIT 6.0 (2024):

| Angle | Prediction | IC19 no SK-atm (NO) | Pull | IC24 + SK-atm (NO) | Pull |
|-------|-----------|---------------------|------|---------------------|------|
| sin²θ₁₃ | 0.02204 | 0.02195 ± 0.00058 | **−0.16σ** | 0.02215 ± 0.00056 | **+0.20σ** |
| sin²θ₁₂ | 0.2897 | 0.307 ± 0.012 | **+1.44σ** | 0.308 ± 0.012 | **+1.52σ** |
| sin²θ₂₃ | 0.6048 | 0.561 ± 0.015 | **−2.92σ** | 0.470 ± 0.017 | **−7.93σ** |
| | | **Σ\|pull\|** | **4.52** | **Σ\|pull\|** | **9.65** |

### Octant prediction [PRED]

**I.17 predicts sin²θ₂₃ = 0.605 → upper octant (>0.5).** This is a falsifiable prediction:

- NuFIT 6.0 IC24+SK-atm (sin²θ₂₃ = 0.470, **lower** octant): I.17 excluded at 7.9σ.
- NuFIT 6.0 IC19 without SK-atm (sin²θ₂₃ = 0.561, **upper** octant): I.17 at 2.9σ tension.

The θ₂₃ octant is experimentally unresolved: T2K and NOvA individually prefer upper octant, but IceCube/DeepCore (IC24) and SK-atm pull towards lower octant. DUNE and Hyper-Kamiokande will resolve this within 2028–2032.

**Note:** The LO formula from paper v9 (sin²θ₂₃ = 0.449, **lower** octant) survives IC24+SK at −1.6σ but is excluded by IC19 at −7.5σ. The two LD predictions bracket the experimental range from opposite sides. The dynamical mechanism selecting between them is Gap 9 (dynamical part).

### LD motivation for t
t = √(disc_φ)/d₁ where disc_φ = d₁²+1 = 5 is the discriminant of the φ-pair eigenvalues of L. Equivalently: t² = 1 + 1/d₁², t = √(N−1)/d₁.

### Comparison with prior methods

| Method | sin²θ₁₃ (σ) | sin²θ₁₂ (σ) | sin²θ₂₃ (σ) | Σ|p| | Params |
|--------|-------------|-------------|-------------|------|--------|
| Schur (I.14) | −29σ | — | — | — | 0 |
| t=1/d₁, ε-pert (I.9d) | +2.0σ | −0.8σ | −1.4σ | 4.2 | 1 (ε) |
| **t=√5/2 (this)** | **−0.03σ** | **+1.19σ** | **−1.74σ** | **2.96** | **0 (t [DER]; swap forced)** |

### Self-criticism
**LEE:** ~50 LD-motivated t candidates tested; at ~50 trials, ≥1 falling within 0.4% of optimum expected ~10–20% of the time. **Swap (S190–S192):** ν₁↔ν₂ is NOT a free choice — it is FORCED by the Laplacian solar bound [DER, S190/S192]: any 3×3 graph Laplacian has |U_e1|² = 1/3, giving sin²θ₁₂ > 1/2 without swap, contradicting exp ≈ 0.307. **t derivation (S189/S193):** t = √5/2 is derived [DER, I.9g.12] via boson circuit → spectral bridge chain. Combined: parameter count reduced from 1+1bit to **0**. **Honest significance:** ~2σ after LEE correction (LEE still applies to the historical discovery path even though t is now derived). **Counterargument:** disc_φ is the privileged invariant of the same Laplacian — reduces effective trials, but hard to formalize.

### Status
[CONJ] — t = √5/2 is now **derived** [DER, I.9g.12] via the boson circuit → spectral bridge chain (S189/S193). The ν₁↔ν₂ swap is **forced** [DER, S190/S192]. Remaining conjecture: the heat kernel identification itself (exp(−tL) eigenvectors = PMNS columns), i.e. CONJ I.14-ID. The parameter count is 0 free continuous + 0 discrete bits. ~25 functionals tested for independent t derivation, all DEAD (see X.11).

### HK vs CR: two-scale structure (S205) [KEY]

Full HK scan with O.1 Cayley Laplacian reveals two regimes:

| t | sin²θ₁₂ | sin²θ₂₃ | sin²θ₁₃ | Notes |
|---|---------|---------|---------|-------|
| 0.50 | **0.310** | **0.556** | 0.006 | ≈ CR for θ₁₂,θ₂₃! But θ₁₃ too small |
| 0.55 | **0.308** | **0.561** | 0.007 | θ₁₂ ≈ 4/13, θ₂₃ ≈ 81/145 |
| **√5/2 ≈ 1.12** | 0.290 | 0.605 | **0.022** | θ₁₃ correct, θ₁₂ and θ₂₃ off |

**Structural obstruction:** sin²θ₁₂ = 4/13 at t* = 0.547 (at this t: θ₂₃ ≈ 81/145 but θ₁₃ = 0.007). sin²θ₁₃ = 2/91 at t ≈ √5/2 (at this t: θ₁₂, θ₂₃ distorted). No single t gives all three CR values.

**Root cause (T.3):** Cayley L encodes {σ₁, σ₀, σ₀⁻¹} implicitly, but face structure (σ∞) enters only indirectly. CR values are functions of cusp positions = direct σ∞-data. Any f(L) gives the same eigenvectors (I.14-R), so HK at different t gives genuinely different PMNS.

**Comparison (NuFIT 6.0 IC19 NO):**

| | CR (0 param) | HK (0 param) |
|---|---|---|
| sin²θ₁₂ | 4/13 = 0.3077 (−0.06σ) | 0.2897 (+1.44σ) |
| sin²θ₂₃ | 81/145 = 0.5586 (+0.16σ) | 0.6048 (−2.92σ) |
| sin²θ₁₃ | 2/91 = 0.02198 (−0.05σ) | 0.02204 (−0.16σ) |
| **Σ|pull|** | **0.26** | **4.52** |

CR dramatically closer. Direction: operator in ⟨L,σ∞⟩ (T.5: dim=50) that gives PMNS = CR values. See Gap 9(γ₂).


## [THM] I.18: Exact leptonic spectral projectors
Source: S97++
Status: [THM]
Dependencies: I.6
Verified: SymPy exact arithmetic + GramSchmidt × 2

### Statement
For each eigenvalue λ_k of the Cayley Laplacian L, the spectral projector P_k restricted to the 3D leptonic sector (e,μ,τ) in S97-convention is:

| Sector | λ | mult | Tr(P^lep) |
|--------|---|------|-----------|
| flat | 0 | 1 | 1/4 |
| √21⁻ | (5−√21)/2 | 1 | 2/15 − 2√21/315 |
| λ=1 | 1 | 1 | 5/18 |
| φ⁻ | (5−√5)/2 | 1 | 2/5 |
| λ=3 | 3 | 2 | 2/5 |
| φ⁺ | (5+√5)/2 | 1 | 2/5 |
| λ=4 | 4 | 1 | 11/36 |
| √21⁺ | (5+√21)/2 | 1 | 2/15 + 2√21/315 |
| λ=5 | 5 | 3 | 7/10 |

**Σ Tr = 3 ✓.** Σ P_k = I₃ ✓.


## [THM] I.19: φ-pair leptonic structure
Source: S97++
Status: [THM]
Verified: SymPy exact, numpy 10⁻¹⁰

### Exact projector elements

| Element | P_φ⁻ | P_φ⁺ | P_φ (sum) |
|---------|-------|-------|-----------|
| (e,e) | **1/(10φ²)** = (3−√5)/20 | **φ²/10** = (3+√5)/20 | 3/10 |
| (μ,μ) | **φ²/10** | **1/(10φ²)** | 3/10 |
| (τ,τ) | **1/10** | **1/10** | 1/5 |
| (e,μ) | −1/10 | −1/10 | −1/5 |
| (e,τ) | 1/(10φ) | −φ/10 | −1/10 |
| (μ,τ) | −φ/10 | 1/(10φ) | −1/10 |

### Key identities
- **e↔μ mirror symmetry:** P_φ⁻ and P_φ⁺ exchange under e↔μ.
- P_φ⁻(e,e)·P_φ⁻(μ,μ) = **1/100 = 1/|B₁|²**.
- P_φ⁻(μ,μ)/P_φ⁻(e,e) = **φ⁴ = (7+3√5)/2**.
- Tr(P_φ) = **4/5** (leptonic weight of φ-pair = 2 × 2/5).


## [THM] I.20: Q_φ as square root of leptonic Laplacian
Source: S97++
Status: [THM]
Verified: SymPy exact matrix multiplication

### Definition
P_φ± = P_φ_rat ± √5·Q_φ (rational/irrational decomposition).

### Structure
**20·Q_φ = M** where M = [[−1, 0, +1], [0, +1, −1], [+1, −1, 0]].

### Algebra
- Row sums = 0 (Laplacian)
- Tr(M) = 0
- **M² = 3I − J = L(K₃)** (Laplacian of complete graph K₃)
- M³ = 3M (minimal polynomial m(m²−3) = 0)
- Eigenvalues: {0, −√3, +√3}

### Physical meaning
Q_φ acts as a **«square root of diffusion»** on the leptonic triangle: Q_φ² ∝ L(K₃). The φ-pair heat kernel decomposes as:

H_φ(t) = 2e^{−5t/2}[cosh(t√5/2)·P_φ_rat + √5·sinh(t√5/2)·Q_φ]


## [THM] I.21: D_τ duality between φ and √21 sectors
Source: S97++
Status: [THM]
Verified: Fraction arithmetic, 6/6 elements

### Statement
D_τ = diag(1, 1, −1) (τ-parity operator). Then:

**P_φ_rat = d₂ · D_τ · P_√21_rat · D_τ**

Verified all 6 independent elements. D_τ selects τ as the unique lepton with σ₁-partner in the boson sector.

### Note
No analogous relation for Q-matrices: Q_φ ≠ c·D_τ·Q_21·D_τ (Q_φ(e,μ)=0 but D_τ-conjugate ≠ 0). D_τ-duality is a property of rational parts only.


## [THM-math / CONJ] I.22: sin²θ₁₃ factorization
Source: S97++
Status: **[THM-math]** for eigenvector-eigenvalue identity; **[CONJ]** for θ₁₃ identification (depends on I.17)
Dependencies: I.17 (for physical interpretation); none (for mathematical identity)
Verified: numpy at 18 t-points + asymptotic limit; 5 random 3×3 matrices confirm generality

### Statement (eigenvector-eigenvalue identity) [THM-math]
For **any** 3×3 real symmetric matrix H with distinct eigenvalues h₁ < h₂ < h₃, and 2×2 minor M_{(α)} obtained by deleting row/col α with eigenvalues μ₁, μ₂:

**|ψ₃(α)|² = (μ₁ − h₃)(μ₂ − h₃) / [(h₁ − h₃)(h₂ − h₃)] = F₁ · F₂**

This is a general theorem (Thompson 1966; rediscovered by Denton-Parke-Zhang 2019 for neutrinos). Not LD-specific.

### Application to H_lep(t) [CONJ, via I.17]
With H = H_lep(t) (heat kernel restricted to leptons) and α = e:

**sin²θ₁₃ = F₁(t) · F₂(t)**

where F₁ = (μ₁−h₃)/(h₁−h₃), F₂ = (μ₂−h₃)/(h₂−h₃); h_i = eigenvalues of H_lep(t), μ_i = eigenvalues of μ-τ block. Calling this quantity «sin²θ₁₃» presupposes I.17 [CONJ].

### Key values

| t | F₁ | F₂ | sin²θ₁₃ |
|---|----|----|----------|
| 1/2 | 0.711 | 0.009 | 0.006 |
| √5/2 | 0.742 | 0.030 | **0.022** |
| ∞ | **2/3 = d₁/d₂** | 0.065 | 0.043 |

### Mechanism of smallness
sin²θ₁₃ is small because **F₂ ≪ 1** (Cauchy interlacing near-degeneracy: μ₂ ≈ h₃). F₁ is slowly varying, O(1). The asymptotic limit F₁(∞) = d₁/d₂ = 2/3 is exact.


## [OBS] I.23: e-μ democracy classification
Source: S97++
Status: [OBS]

**7 of 9 spectral sectors** preserve P(e,e) = P(μ,μ).

Breaking sectors:
- **λ=1:** μ completely invisible (P₁[μ,·] = 0). Ratio P₁(e,e)/P₁(τ,τ) = d₁² = 4.
- **λ=4:** μ dominates. Ratio P₄(μ,μ)/P₄(e,e) = d₂² = 9.

Combined trace of breaking sectors: Tr(P₁)+Tr(P₄) = 5/18 + 11/36 = **7/12 = L/(index)**.

Ramification indices e₂ = d₁ (j=1728) and e₃ = d₂ (j=0) determine the degree of e-μ symmetry breaking.


## [OBS] I.24: ψ₃ spectral anatomy
Source: S97++
Status: [OBS]

### Spectral decomposition of θ₁₃-eigenvector at t=√5/2

| Sector | ⟨ψ₃|P_k|ψ₃⟩ | ⟨e|P_k|ψ₃⟩ |
|--------|-------------|------------|
| **φ⁻** | **38.3%** | **+0.121** (constructive) |
| **λ=4** | **26.3%** | **+0.085** (constructive) |
| λ=3 (×2) | 15.4% | −0.062 (destructive) |
| λ=5 (×3) | 11.6% | −0.062 (destructive) |
| √21⁺ | 7.7% | +0.086 (constructive) |
| λ=1 | 0.6% | −0.036 (destructive) |

### Mechanism
Constructive: {φ⁻, λ=4, √21⁺} → Σ = +0.292. Destructive: {λ=1, λ=3, λ=5} → Σ = −0.160. Net: ψ₃(e) = 0.148, sin²θ₁₃ = 0.022.

### Key contrast with θ₁₂
φ-pair contributes **0.015%** to θ₁₂ (I.9b) but **38%** to θ₁₃. Golden ratio irrelevant for solar angle, dominant for reactor angle.

### Proximity of θ₁₃-vectors
|⟨ψ₃(HK, √5/2) | v₃(Schur)⟩|² = **0.9964**. |⟨v₃(Schur) | φ⁻_lep⟩|² = 0.9790. All three vectors > 97.9% overlap, but sin²θ₁₃ = ψ₃(e)² is extremely sensitive: 3.6° rotation → 42% relative change.


## I.25: Identification Hierarchy and Precise Logic Frame (S98 audit)

### Purpose
This section maps the exact logical chain from dessin combinatorics to PMNS predictions, marking every identification step. No mathematics changes; only the epistemic status of each link is made explicit.

### The chain

```
LAYER 0: PURE MATHEMATICS (no identification needed)
  C.1–C.7  Dessin structure of X₀(6): 4BV+6WV+12E, monodromy, CRT  [THM-comb/math]
  I.6      Cayley Laplacian L (12×12), spectrum, char poly               [THM-comb]
  I.11     Schur complement L_eff = L_ll − L_lr·L_rr⁻¹·L_rl (3×3)       [THM-arith]
  I.12–13  Eigenvalues {0, 9/5, 25/11}, eigenvectors {(1,1,1),(−7,2,5),(1,−4,3)}  [THM-arith]
  I.14     |U_{αi}|² = v_i(α)²/|v_i|² (numerical matrix)                [THM-arith]
  I.14-R   Robustness: |U|² invariant under M_ν = f(L_eff), f injective  [THM-math]
  I.22     Factorization |ψ₃(e)|² = F₁·F₂ (eigenvector-eigenvalue identity) [THM-math]

IDENTIFICATION STEP 1 (minimal): [CONJ I.14-ID]
  [M_ν, L_eff] = 0
  Physical content: the neutrino mass matrix is diagonalized in the same basis
  as the Schur complement of the Cayley Laplacian.
  Motivation: L_eff has identical algebraic form to type-I seesaw 
  (M_eff = M_LL − M_LR·M_RR⁻¹·M_RL). Structural analogy, not derivation.

LAYER 1: SCHUR PMNS (if CONJ I.14-ID accepted)
  I.14     |U|² matrix = PMNS matrix                                     [CONJ]
  I.3      μ-τ symmetry → sin²θ₁₃ = 0 (tree level)                     [CONJ]
  Result:  sin²θ₁₃ = 1/26 = 0.038 (−29σ). Necessary but insufficient.

IDENTIFICATION STEP 2: [CONJ I.17]
  t = √5/2 (heat kernel parameter) — now [DER] via I.9g.12 chain (S189/S193)
  ν₁ ↔ ν₂ swap — now FORCED [DER] by Laplacian solar bound (S190/S192)
  Physical content: finite diffusion time on dessin determines PMNS corrections.
  Status: t derived from boson circuit → spectral bridge → I.26.4 [DER].
  Swap forced by |U_e1|² = 1/3 (any 3×3 Laplacian) + exp sin²θ₁₂ < 1/2.

LAYER 2: HEAT KERNEL PMNS (if CONJ I.14-ID + CONJ I.17 accepted)
  I.17     All 3 angles within 2σ, Σ|pull| = 2.96                       [CONJ]
  I.22     sin²θ₁₃ = F₁·F₂ with F₁(∞) = d₁/d₂                        [THM-math + CONJ]
  I.18–24  Spectral anatomy, φ-pair dominance, D_τ duality              [THM-arith]
```

### Systematic improvement test
Each layer IMPROVES agreement with experiment:

| Level | sin²θ₁₃ | Pull | Params |
|-------|---------|------|--------|
| μ-τ exact (I.3) | 0 | +39σ | 0 |
| Schur (I.14) | 1/26 = 0.038 | −29σ | 0 |
| Heat kernel (I.17) | 0.022 | −0.03σ | 0 (t [DER], swap forced) |

Monotonic improvement with increasing physical content (tree → Schur → heat kernel) is non-trivial: a random sequence of modifications would not systematically converge.

### What would close the gap
CONJ I.14-ID would become [THM] if one proves any of:
- (a) Dessin Lagrangian: construct L from which L_eff = Schur complement is literally the effective neutrino mass operator after integrating out heavy degrees of freedom.
- (b) Universality argument: any mass matrix respecting the symmetries of L_eff (including its specific μ-τ breaking 7/55) is necessarily f(L_eff) for some f.
- (c) Spectral rigidity: the 3-point spectrum {0, 9/5, 25/11} + eigenvectors are SO constrained that no other 3×3 matrix with comparable physical properties (Laplacian, trace 224/55, det = 0) has different eigenvectors.

CONJ I.17 would become [THM/DER] if one derives t = √5/2 from a variational principle or trace formula (~25 attempts DEAD, but the space of functionals is infinite).

### Parallel: CKM identification chain
For comparison, the CKM sector has an analogous structure:
```
  D.4     Kirchhoff = 40                                                [THM-arith]
  E.8     Residual tree count = d₂² = 9                                 [THM-math]
  E.8     λ = d₂²/K = 9/40                                              [THM-arith]
  ⚠ ID:   λ(graph) = λ(Wolfenstein)                                     [OBS]
```
The CKM gap is narrower (one number, not a full matrix), but structurally identical: a graph quantity is identified with a physical parameter without a derived mechanism.


## [THM] I.26: Representation-Theoretic Derivation of t₁, t₂
Source: S99
Status: [THM] (I.26.1–I.26.2), [THM-arith] (I.26.3–I.26.5), [DER] (I.26.4)
Dependencies: I.6 (Cayley Laplacian), I.12 (L_eff spectrum)

### I.26.1 Irrep Localization [THM] (25th path)

**Statement.** The representation std(S₃)⊗V(A₄) of the monodromy group admits a decomposition into irreps of A₄ such that each quadratic factor of char(L|_{std⊗V}) is localized in a single irrep block.

Eigenvalues of L restricted to the 6D std⊗V subspace:
- φ-pair: (5±√5)/2, product P_φ = 5 = N−1
- 21-pair: (5±√21)/2, product P_{21} = 1
- integers: 3, 5

### I.26.2 Moment Derivation [THM]

**Statement.** From Tr(A²) = 18 and Tr(A⁴) = 94 on the 6D subspace, the system:
- P₁ + P₂ = N = 6 (Vieta for S = Tr(A²)/2 − sum of integer eigenvalue squares)
- P₁·P₂ = N−1 = 5

uniquely gives **P₁ = 1, P₂ = 5**.

### I.26.3 CRT Coupling [THM-arith]

**Statement.** The CRT structure ℤ/6ℤ ≅ ℤ/2ℤ × ℤ/3ℤ forces:
- sin²θ₁₂_tree = d₁²/(d₁²+d₂²) = 4/13 via tan θ₁₂ = d₁/d₂ = 2/3
- t = √P/d₁ for quadratic eigenvalue products P

The factor √3/2 in the CRT coupling equals cos(π/N).

### I.26.4 Prescription t = √P/d₁ [DER]

**Statement.** For each quadratic pair with product Pᵢ: tᵢ = √Pᵢ/d₁.

This gives t₁ = √1/2 = 1/2 and t₂ = √5/2.

**Justification:** Uniqueness by simplicity (tᵢ must separate eigenvalue pairs) + scale matching (Pᵢ is a product of two eigenvalues, d₁² normalises to unit scale via CRT structure). Status [DER]: one selection criterion (simplest square root).

### I.26.5 Fundamental unit identification [THM-arith]

t₂ = √5/2 = √(disc_φ)/d₁, where disc_φ = 5 = discriminant of x²−5x+1.

The fundamental unit of ℚ(√5) is ε = (1+√5)/2 = φ. The heat kernel parameter t₂ is related to the discriminant of the ring ℤ[φ], connecting PMNS physics to the arithmetic of the golden ratio.


## [THM-arith] I.27: S₃-Polarization Theorem
Source: S100
Status: [THM-arith] (26th path to (d₁,d₂)=(2,3))
Dependencies: I.26.1 (irrep localization)
Verified: NumPy (two independent V-basis constructions; weights invariant under V-rotation)

### I.27.1 S₃ weights of eigenvectors [THM-arith]

**Statement.** In the σ₁-eigenbasis of std(S₃), each eigenvector of the adjacency operator on std(S₃)⊗V(A₄) has a well-defined S₃ weight w₊:w₋ (fraction in v₊ vs v₋ sector):

| Eigenvalue λ(L) | w₊ | w₋ | w₊/w₋ | LD identification |
|---|---|---|---|---|
| (5±√5)/2 (φ-pair) | 3/10 | 7/10 | **3/7 = d₂/L** | exact, both eigenvectors |
| 3 | 3/5 | 2/5 | **3/2 = d₂/d₁** | exact |
| 5 | 2/5 | 3/5 | **2/3 = d₁/d₂** | exact |
| (5−√21)/2 | ≈0.438 | ≈0.562 | ≈0.780 | not simple |
| (5+√21)/2 | ≈0.962 | ≈0.038 | ≈25.22 | not simple |

Weights are **invariant** under rotation of the V-basis (depend only on S₃ decomposition).

**[CORRECTED from S99]:** S99 reported φ-pair as 2:3 = d₁:d₂. Correct: **3:7 = d₂:L** (S99 used non-orthonormal basis).

### I.27.2 Sum rules [THM-arith]

```
Σ w₊ = 3 = dim(v₊ ⊗ V)    ✓
Σ w₋ = 3 = dim(v₋ ⊗ V)    ✓
Σ λ·w₊ = 10 = |B₁|         [THM-arith]
Σ λ·w₋ = 8 = d₁³           [THM-arith]
```

### I.27.3 Pythagorean identity [THM]

**Statement.** P₂ − P₁ = N − 2 = d₁².

**Proof.** P₁+P₂ = N, P₁P₂ = N−1 (moment theorem, I.26.2). (P₂−P₁)² = (P₁+P₂)² − 4P₁P₂ = N² − 4(N−1) = (N−2)². ∎

**Corollary.** t₂² − t₁² = (P₂−P₁)/d₁² = d₁²/d₁² = **1** exactly.

Pythagorean triple: (t₁, 1, t₂) = (1/2, 1, √5/2) is a right triangle.

### I.27.4 Ihara zeta function [OBS]

For the 6D irrep std⊗V:

ζ\_Ihara⁻¹(u) = (1+2u²)(1+2u+2u²)(1−u+3u²−2u³+4u⁴)(1−u−u²−2u³+4u⁴)

All 12 zeros lie on |u| = 1/√2 = 1/√(k−1). **Ramanujan property** [OBS].

**[THM-arith]** det(L|_{std⊗V}) = ∏λᵢ = **75 = 3·5²**. Proof: P_φ·P_{21}·3·5 = 5·1·15 = 75. ✓

**[THM-arith]** det'(L\_eff) = λ₂·λ₃ = (9/5)·(25/11) = **45/11 = d₂²(N−1)/(2N−1)**.


## I.28: Neutrino Mass Predictions
Source: S100
Dependencies: I.12 (L_eff spectrum), I.17 (heat kernel PMNS)

### I.28.1 L_eff eigenvalues ≠ mass² [DEAD]

| Hypothesis | Predicted Δm²₃₁/Δm²₂₁ | Experimental (~33.5) | Verdict |
|---|---|---|---|
| m² ∝ λ | 125/99 ≈ 1.26 | 33.5 | DEAD (26× off) |
| m ∝ λ | (125/99)² ≈ 1.59 | 33.5 | DEAD |
| m ∝ √λ | same as m²∝λ | — | DEAD |
| m² ∝ (λ_max−λ) | wrong sign (IO) | — | DEAD |

**Conclusion:** L_eff determines **mixing angles** (via heat kernel eigenvectors), not **masses**. Mass hierarchy requires a separate mechanism (δK formula or dynamics).

### I.28.2 Structural predictions [CONJ conditional on I.14-ID; item 1 KILLED S192]

1. **m₁ = 0** (lightest neutrino massless). **KILLED (S192, verified S194).**
   Original basis: zero eigenvalue of L_eff is structural (Laplacian property: row sums = 0).

   **Caveat (S153.1 audit):** Requires f(0) = 0 where f is the mass-eigenvalue map. I.28.1 shows f is not any simple function of λ. The link "zero mode → zero mass" requires [M_ν, L_eff] = 0 (CONJ I.14-ID) AND f(0) = 0 (unproven). See I.1 for alternative m₁ = 7.72 meV.

   **KILLED (S192):** The forced ν₁↔ν₂ swap (S190 Laplacian solar bound [DER]) maps ν₂ ↔ λ=0 (null mode), not ν₁. Normal ordering m₁ < m₂ < m₃ then requires f(9/5) < f(0) < f(25/11) — the mass function is non-monotone. If f(0) = 0 then m₂ = 0 and m₁ ≤ 0 → unphysical. Therefore f(0) ≠ 0 and m₁ = 0 from the null mode is impossible.

2. **Normal ordering** (NO).
   Basis: λ₁ < λ₂ < λ₃ maps to ν₁ < ν₂ < ν₃.

3. **Σmν = 0.0588 eV** (minimal NO value with m₁=0).
   = √Δm²₂₁ + √Δm²₃₁ = 8.65 + 50.13 meV.
   Using NuFIT 6.0 (IC24+SK-atm, NO best fit): Δm²₂₁ = 7.49×10⁻⁵ eV², Δm²₃₁ = 2.513×10⁻³ eV².

### I.28.3 Derived observables [PRED]

```
|m_ee|_max = 3.70 meV  (0ν2β, Majorana phases aligned)
|m_ee|_min = 1.49 meV  (phases anti-aligned)
m_β = 8.82 meV         (β-decay endpoint)
```

### I.28.4 Comparison with DESI DR2 (arXiv: 2503.14744, PRD 112 083513)

| Analysis | Bound (95% CL) | LD prediction 0.059 eV | Status |
|---|---|---|---|
| ΛCDM Bayesian | Σmν < 0.0642 eV | **compatible** | ✓ |
| Feldman-Cousins | Σmν < 0.053 eV | **above** by 5.8 meV | tension |
| w₀wₐCDM | Σmν < 0.163 eV | **compatible** | ✓ |

DESI reports 3σ tension between cosmological constraints and the oscillation floor using a Bayesian analysis with effective parameter Σm_{ν,eff} (allowing negative energy densities); the direct F-C upper bound 0.053 eV lies below the oscillation floor 0.059 eV by 6 meV. This tension is between cosmological data and oscillation experiments, independent of LD. In w₀wₐCDM (dynamical dark energy) the tension disappears.

### I.28.5 Status
[PRED, partially KILLED] — Item 1 (m₁=0) **KILLED** by forced swap (S192). Items 2–3 (NO, Σmν) remain [PRED] conditional on I.14-ID, but the original basis (null mode → zero mass) is invalidated. NO and Σmν predictions survive only through I.1 (fitted) or independent physical arguments, not through graph-theoretic null mode reasoning.


---


## [THM-arith] I.29: Commutator [M_lep, L_eff] and Exact Mixing Formula
Source: S116
Status: [THM-arith] (exact rational arithmetic, SymPy-verified)
Dependencies: D.5 (M_lep), I.11 (L_eff)
Verified: SymPy symbolic (commutator, decomposition, eigenbasis rotation, tan formula)

### I.29.1 Noncommutativity [THM-arith]

```
              ⎡  0      6/11    37/55 ⎤
[M_lep, L_eff] = ⎢−6/11    0     −7/55 ⎥  ≠  0
              ⎣−37/55   7/55     0    ⎦
```

In integer form: 55·C = [[0,30,37],[−30,0,−7],[−37,7,0]].

Entries in LD invariants:
- C_eμ = 6/11 = N/dim M₁₀ (= 30/55)
- C_μτ = −7/55 = −L/((N−1)·dim M₁₀) (= μ-τ breaking parameter of L_eff)
- C_eτ = 37/55

**Sum rule:** C_eτ = C_eμ + |C_μτ|, i.e., 37 = 30 + 7.

**||C||²_F = 4636/3025** (= 2²·19·61 / 5²·11², irreducible).

### I.29.2 Orthogonal Decomposition [THM-arith]

55·C = (67/2)·A₁ + (7/2)·A₂, equivalently C = (67/110)·A₁ + (L/110)·A₂

where 110 = 2(N−1)·dim M₁₀, and:

**A₁ = [[0,1,1],[−1,0,0],[−1,0,0]]** — μ-τ symmetric incompatibility
- Rotation axis: ω₁ = (0, −1, 1), purely in μ-τ plane
- |ω₁|² = d₁ = 2

**A₂ = [[0,−1,1],[1,0,−2],[−1,2,0]]** — μ-τ breaking
- Rotation axis: ω₂ = −(d₁, 1, 1) = −(2, 1, 1)
- |ω₂|² = d₁² + 2 = N = 6

**Orthogonality:** tr(A₁·A₂ᵀ) = 0. ω₁·ω₂ = 0. [THM-arith, SymPy exact]

Norm contributions: A₁ carries 4489/4636 = **96.8%** of ||C||²_F, A₂ carries 147/4636 = **3.2%**.

### I.29.3 67-Cancellation and Exact Mixing Formula [THM-arith]

In the M_lep eigenbasis (v₁ for λ₁=1, v₂ for λ₂=4−√3, v₃ for λ₃=4+√3):
- L̃₂₂ = (201/4 + 335√3/12)/55
- L̃₃₃ = (201/4 − 335√3/12)/55
- L̃₂₃ = 67√6/(12·55)

All (2,3)-block elements of 55·L̃ factor through 67 = (N−1)·dim M₁₀ + index = 55 + 12.
The 67 cancels in the mixing angle:

**tan(2θ) = √d₁/(N−1) = √2/5**

**sin²(2θ) = d₁/d₂³ = 2/27**

where θ is the rotation angle between the 2nd and 3rd M_lep eigenstates (both μ-τ symmetric, λ = 4±√3) in the L_eff frame.

sin²θ = (9−5√3)/18 ≈ 0.01887 (small branch).

### I.29.4 Physical comparison [OBS]

Numerically sin²θ ≈ 0.019 is near sin²θ₁₃(exp) ≈ 0.022 but pull = +5.6σ (NuFIT 5.x: 0.02203±0.00056).

**Structural caveat:** This angle measures mixing between two μ-τ SYMMETRIC eigenstates of M_lep. Physical θ₁₃ is μ-τ BREAKING. The angle lives in the A₁ sector (96.8% of ||C||²), not the A₂ sector. Numerical proximity may be coincidental.

### I.29.5 Consequence: Independence of CONJ I.3-ID and CONJ I.14-ID [THM-arith]

[M_lep, L_eff] ≠ 0 ⟹ M_lep and L_eff have different eigenvectors ⟹ proving [Mν, L_eff] = 0 does NOT prove M_lep eigenvectors = PMNS columns.

PMNS has **3 independent root gaps**:
- (α) CONJ I.14-ID: [Mν, L_eff] = 0
- (β) CONJ I.3-ID: M_lep eigenvectors = PMNS columns
- (γ) ~~CONJ I.17: t = √5/2~~ → t and swap now [DER]. Split S205:
  - (γ₁) Structural: sin²θ = CR²/(1+CR²) from cusp data in two metrics [X.102, DONE]
  - (γ₂) Operator: M ∈ ⟨L,σ∞⟩ giving PMNS = CR values. NOT f(L). [OPEN]

### I.29.6 Identity d₁ + (N−1)² = d₂³ [THM-arith, 31st path]

For (d₁,d₂) = (2,3) with N = d₁d₂: 2 + 25 = 27 = 3³. ✓

**Uniqueness:** Exhaustive scan 1 ≤ d₁,d₂ ≤ 50, N = d₁d₂: only (1,1) and (2,3) satisfy. Trivial (1,1) excluded by any LD condition (N ≥ 2, or Catalan). Arises from sin²(2θ) = d₁/d₂³ formula.

---


# J. L-FUNCTIONS

## [THM] J.1: η-product relations
f₁=η(τ)η(2τ), f₂=η(τ)η(3τ), f₃=η(2τ)η(6τ), f₄=η(3τ)η(6τ).
U₂(f₃)=f₂, U₃(f₄)=f₁, f₁f₄=f₂f₃.

## [THM] J.2: L-function ratios (9th path)
L(f₂)/L(f₃) = d₁ˢ = 2ˢ. L(f₁)/L(f₄) = d₂ˢ = 3ˢ. Exact, from Hecke actions on η-product Fourier coefficients.

## [DEAD] J.3: ρ ≈ 1.389 (NOT √C)
S55 value 1.051 was convergence artifact. True ρ≈1.389. PSLQ NULL deg≤6.


---

# K. HAUPTMODUL

## [THM] K.1: j-factorisation (expanded)
Source: Paper §5, S30–S31, S92
Status: [THM]
Verified: Sage (9/9 tests, S31), mpmath (S92)

### Statement
j(t₆) = P₄(t₆)³ / [t₆⁶ (t₆ + d₂²)³ (t₆ + d₁³)²]

**P₄(t) = (t + index)(t³ + 252t² + 3888t + 15552)**

### Scaled form
P₄(12s) / 12⁴ = (s + 1)(s³ + d₂L·s² + d₂³·s + d₂²)

where 12 = index = [SL₂(ℤ) : Γ₀(6)].

### R₃ coefficients [THM, S31]

| Coefficient | Value | LD monomial |
|-------------|-------|-------------|
| a₂ | 252 | d₁²d₂²L |
| a₁ | 3888 | d₁⁴d₂⁵ |
| a₀ | 15552 | d₁⁶d₂⁵ |

ALL coefficients of P₄ and R₃ are monomials in (d₁, d₂).

### Cuspal values [THM, S31 Sage-verified]

| t₆ | Cusp | P₄(t₆) | LD expression | {2,3} content |
|----|------|---------|--------------|---------------|
| 0 | 0 (quarks, w=6) | 186624 = 432² | (index·∏wᵢ)² | d₁⁸·d₂⁶ |
| −9 | 1/2 (leptons, w=3) | 729 | d₂⁶ | **pure d₂** |
| −8 | 1/3 (bosons, w=2) | 256 | d₁⁸ | **pure d₁** |
| −12 | j=0 rational | 0 | — | — |

### 3P₄'/P₄ at cusps [THM, S31 Sage-verified]

| t₆ | 3P₄'/P₄ | LD expression |
|----|---------|---------------|
| 0 | 1 | 1 |
| −d₂² = −9 | −4 | −d₁² |
| −d₁³ = −8 | 3 | d₂ |

**Identity:** Σ(3P₄'/P₄) = 1 + (−4) + 3 = **0** [THM].

### Regular parts c₀ of d(ln j)/dt₆ [THM, S31 Sage-verified]

| Cusp | c₀ | LD expression |
|------|----|---------------|
| 0 (w=6) | 5/12 | (N−1)/index |
| 1/2 (w=3) | −4/3 | −d₁²/d₂ |
| 1/3 (w=2) | 3/4 | d₂/d₁² |

**Sum rules [THM, S31]:**
- Σ c₀ = 5/12 − 4/3 + 3/4 = **−1/N = −1/6**
- Σ c₀·w = (5/12)·6 + (−4/3)·3 + (3/4)·2 = **0**
- c₀(lep)·c₀(bos) = (−4/3)·(3/4) = **−1**

### R₃ special value [THM, S31]
R₃(−index) = R₃(−12) = 3456 = 2j(i).

### Discriminants [THM, S31]

| Polynomial | Discriminant | LD expression |
|-----------|-------------|---------------|
| R₃ (scaled: R₃(12s)/12³ = s³+21s²+27s+9) | −972 | −d₁²d₂⁵ |
| P₄ (full quartic) | −2²⁸·3¹⁷ | pure {d₁, d₂} |
| Q₂ (j=1728 quadratic) | 432 | N³(N−4) = index·∏wᵢ |

ALL discriminants have pure {2,3}-content.

### q-expansion [THM, S31]
t₆ = q⁻¹ − (N−1) + N·q + (#cusps)·q² − d₂·q³ + ...
   = q⁻¹ − 5 + 6q + 4q² − 3q³ + ...

First 4 sub-leading coefficients = LD invariants.


## [THM] K.1a: Q₂ structure (j = 1728 quadratic)
Source: S31, S92
Status: [THM]
Verified: Sage (S31), SymPy (S92)
Note: Q₂ = f₁ of K.4.

### Statement
P₄³ − 1728·D = Q₂²·Q₄², where:

**Q₂(t) = f₁(t) = t² + N²t + N³** (= t² + 36t + 216)

Roots: t = N(−3 ± √d₂) = −18 ± 6√3. In ℚ(√d₂).
Discriminant: N³(N−4) = 432 = index·∏wᵢ.

**Q₄(t) = t⁴ − 504t³ − 13824t² − 124416t − 373248**

Scaled: Q₄(12s)/12⁴ = s⁴ − d₁d₂L·s³ − 96s² − d₁³d₂²·s − d₁d₂²
disc(Q₄) = −2³⁰·3¹⁹ (pure {2,3}).

### Numerator of d(ln j)/dt [THM, S92]
num[d(ln j)/dt₆] = Q₂·Q₄

Zeros of the logarithmic derivative = preimages of j = 1728 (σ₀-ramification). Consequence of Hurwitz: d(ln j)/dt = 0 at the non-cuspal, non-j=0 ramification points = j=1728 fiber.

## [THM-arith] K.1b: Ramification Product/Sum/Cross-Ratio Identities (S203)
Source: S203
Status: [THM-arith]
Verified: sympy exact + Fraction arithmetic (S203 session)
Deps: K.1, K.1a.

### Products

**C.9a** (j=0 fiber): ∏(j=0 roots) = P₄(0) = **186624 = 432²** = (d₁⁴d₂³)².

**C.9b** (j=1728 fiber): ∏(j=1728 roots) = Q₂(0)·Q₄(0) = **−432³** = −(d₁⁴d₂³)³.
Sub-products: Q₂(0) = N³ = 216, Q₄(0) = −Mon³ = −373248.

**C.9c** (432 universality): 432 = d₁⁴d₂³ appears in three independent ramification expressions:
1. √(∏ j=0 roots) = 432
2. ∛(|∏ j=1728 roots|) = 432
3. disc(Q₂) = 432 = N³(N−4)

Also: 432 = index·∏wᵢ = j(i)/d₁².

[OBS]: 432 = BULK·π where BULK = E₂(i)·index² = 432/π (H.1a). The triple ramification appearance and the α-formula connection share the same arithmetic origin d₁⁴d₂³, but no derivation links them.

### Sums

**C.9d**: Σ(all j=1728 roots) = **468** = d₁²·d₂²·Φ₃(d₂).
Sub-sums: Σ(Q₂ roots) = −36 = −∏wᵢ, Σ(Q₄ roots) = 504 = L·Mon.

Note: Φ₃(d₂) = 13 = d₂²+d₂+1 = d₁²+d₂² coincides with det(M_lep) (§D.5). Structural explanation OPEN.

### Resolvent

**C.9e**: Resolvent cubic of Q₄ has rational root **−4320** = −N³·d₁²·(N−1).

### Cross-ratios

**C.9f**: CR(−index, 0; −d₂², −d₁³) = **d₁/d₂ = 2/3 = tan θ₁₂(PMNS)** (X.100, S204).
Four-tuple: j=0 rational root (−12), quark cusp (0), lepton cusp (−9), boson cusp (−8). Upgrades I.2 [CONJ→DER].

**C.9g**: CR(−N, −index; −d₂², −d₁³) = **d₁ = 2**.
Four-tuple: W₃ fixed point (−6), j=0 rational root (−12), lepton cusp (−9), boson cusp (−8).

### Coefficient structure

**C.9h**: R₃(12s)/12³ = s³ + d₂L·s² + d₂³·s + d₂² (coefficients 21, 27, 9 — pure d₂ powers with L).

**C.9i**: Q₄ = t⁴ − Mon·L·t³ − Mon·d₁⁶d₂·t² − Mon·j(i)·t − Mon³.
All non-leading coefficients = Mon × LD monomial.


## [THM-comp] K.1c: Q₂/Q₄ CRT Decomposition (S203)
Source: S203
Status: [THM-comp] (9/12 cosets verified numerically)
Deps: K.1a, C.7 (CRT bijection)

### Statement
The j=1728 fiber (6 preimages on X₀(6)) splits Q₂ ∪ Q₄. Under CRT P¹(ℤ/6ℤ) ≅ P¹(𝔽₂) × P¹(𝔽₃):

- **Q₂ roots**: all have P₂ = [1:1] ∈ P¹(𝔽₂) (generic element)
- **Q₄ roots**: all have P₂ ∈ {[0:1], [1:0]} ∈ P¹(𝔽₂) (cusps)

Q₂ lives in ℚ(√d₂). Q₄ has Galois group S₄.
Physical point t₆(i) ≈ 530.503 is in Q₄ (coset (0,1), P₂ = [0:1]).

## [THM] K.2: Q₆ factorisation
F₁₂ = Q₆². f₁ roots ratio = 2+√3. Discriminants purely {2,3}.

## [THM / THM-arith] K.3: Atkin-Lehner Involutions and Klein (ℤ/2)² (S86, expanded S203)
Source: S86 (formulas), S203 (fixed points, group structure)
Status: [THM] (formulas), [THM-arith] (fixed points, products)
Verified: SymPy (S86), Python exact (S203)

### Formulas
W₂(t) = −8(t+9)/(t+8). W₃(t) = −9(t+8)/(t+9). W₆(t) = 72/t.
j∘W₂≠j. W₂²=W₃²=W₆²=Id. W₂∘W₃=W₃∘W₂=W₆. Group = (ℤ/2)².

### Cusp permutations
| Involution | Permutation of cusps (∞,−8,−9,0) ↔ (w₁,w₂,w₃,w₆) |
|---|---|
| W₂ | (w₁↔w₂)(w₃↔w₆) |
| W₃ | (w₁↔w₃)(w₂↔w₆) |
| W₆ | (w₁↔w₆)(w₂↔w₃) |

Klein group acts transitively on the 4-element cusp set.

### Fixed points [THM-arith, S203]
| Involution | Fixed points | Type | Product |
|---|---|---|---|
| W₂ | −d₁³ ± d₁√d₁·i = −8 ± 2i√2 | complex conjugate | **72 = Mon** |
| W₃ | **−N = −6**, **−index = −12** | real, LD monomials | **72 = Mon** |
| W₆ | ±N√d₁ = ±6√2 | real irrational | **−72** |

Universal product: |product of fixed-point pair| = 72 = d₁³d₂² = Mon for all three involutions.

Note: W₃ fixes −N and −index: the two fundamental scale parameters of X₀(6).
W₂ has Re = −d₁³ (= cusp position w=2) and |Im| = d₁√d₁.
K.5: t = −12 = −index is simultaneously W₃-fixed, j=0 rational root, and BV-anchor preimage.

Deps: K.1 (cusps).

## [THM] K.4: W₂-Equivariance of f₁
Source: S86
Status: [THM]
Dependencies: K.2 (Q₆ factorisation)
Verified: SymPy

### Statement
Q₆(t) = f₁(t) · Q₄(t) where f₁ = t² + 36t + 216 (j=1728 fiber).

$$f_1(W_2(t)) = -d_1^3 \cdot \frac{f_1(t)}{(t+8)^2}$$

Constant −d₁³ = −8. W₂ permutes roots of f₁: acts as Galois conjugation √3 → −√3 on ℚ(√d₂)/ℚ.

Q₄ is NOT W₂-equivariant (SymPy: remainder ≠ 0). The decomposition Q₆ = f₁·Q₄ separates W₂-equivariant from non-equivariant sectors. ∎

## [THM] K.5: The Triple Point t = −2N = −12
Source: S86
Status: [THM]
Dependencies: K.1, K.3
Verified: SymPy

### Statement
t = −12 is simultaneously:
1. Unique rational root of P₄ (j=0 fiber, ramification e=d₂=3)
2. W₃-fixed point (the other W₃-fixed point t=−6 has P₄(−6) ≠ 0)
3. BV\_anchor preimage

W₂ has no real fixed points (discriminant of t²+16t+72 is −32 < 0). ∎

## [THM] K.6: W₆ on f₁ Roots
Source: S86
Status: [THM]
Verified: SymPy

f₁(W₆(t))·t² = N³·(t² + 12t + 24). W₆ maps f₁-roots −N(d₂±√d₂) to roots of t²+12t+24 = 0 at −d₁(d₂∓√d₂), combining rescaling N→d₁ with sign-flip of √d₂. ∎


## [THM] K.7: Catalan Prime Separation
Source: S92
Status: [THM]
Dependencies: K.1
Verified: SymPy, mpmath

### Statement
The leading j-coefficient at each finite cusp is a **pure power of a single prime**:

| Cusp | Width | j leading | Purity |
|------|-------|-----------|--------|
| 0 (quarks) | 6 | (d₁³d₂²)⁶/t⁶ | d₁ AND d₂ |
| 1/2 (leptons) | 3 | d₂⁶/(t+d₂²)³ | **pure d₂** |
| 1/3 (bosons) | 2 | d₁⁶/(t+d₁³)² | **pure d₁** |

### Proof
At t = −d₂² (lepton cusp): factor (t+d₁³) = d₁³−d₂² = 8−9 = −1. Power (−1)² = 1. d₁ drops. P₄(−d₂²) = d₂⁶ [K.1]. Result: j ~ d₂⁶/(t+d₂²)³.

At t = −d₁³ (boson cusp): factor (t+d₂²) = d₂²−d₁³ = 9−8 = +1. Power 1³ = 1. d₂ drops. P₄(−d₁³) = d₁⁸ [K.1]. Result: j ~ d₁⁶/(t+d₁³)².

### Necessity
Prime separation requires |d₂² − d₁³| = 1, i.e. d₂² and d₁³ consecutive integers.

### Connection to Mihailescu
Catalan conjecture (Mihailescu 2002): unique solution |xᵖ−yᵍ| = 1 with x,y,p,q > 1 is 3²−2³ = 1. Therefore:

**Prime separation at cusps ⟺ (d₁,d₂) = (2,3) ⟺ N = 6.**

Path 20 to (2,3). Cluster: ramification/j-geometry (shares j-map structure with paths 3, 8, 10, 15–18). NOT independent of that cluster, but provides a clean arithmetic formulation.


## [THM] K.7a: Cusp distance uniqueness
Source: S46
Status: [THM]
Verified: Python (exhaustive d₁,d₂ ∈ [2,19])

### Statement
The rational j=0 point t = −index = −2d₁d₂ satisfies:

|t − t(cusp 1/2)| = |−2d₁d₂ + d₂^{d₁}| = d₂
|t − t(cusp 1/3)| = |−2d₁d₂ + d₁^{d₂}| = d₁²

Both conditions simultaneously ⟺ **(d₁,d₂) = (2,3)**.

Product of all three cusp distances from j=0: index · d₂ · d₁² = 12·3·4 = 144 = index².


## [THM] K.7b: Restricted cubic at boson cusp
Source: S91
Status: [THM]
Verified: SymPy

### Statement
At the boson cusp t₆ = −d₁³: t² + d₂t + d₂² = d₁⁶ − d₂·d₁³ + d₂² = 64 − 24 + 9 = L² = 49.

Restricted cubic (from face-adjacency at cusps): x³ − Nx² + d₁³x − 1 [THM].


## [THM] K.8: Face-Projected Laplacian
Source: S91
Status: [THM]
Dependencies: I.6 (Cayley Laplacian), C.1 (dessin faces)
Verified: Python/numpy, SymPy

### Statement
The 4×4 matrix L_face obtained by projecting L onto the σ∞-invariant subspace (one basis vector per face, weighted by face size) has:

- Diagonal: **(N−d₁², d₂, d₂, d₂) = (2, 3, 3, 3)**
- **Trace = 2+3+3+3 = 11 = dim M₁₀(Γ₀(6))**
- Eigenvalues: **{0, 5/2, d₁², d₂²/2} = {0, 2.5, 4, 4.5}**
- Product of nonzero eigenvalues: **45 = d₂²(d₁+d₂)**

### Inter-face connectivity

| Pair | # cross-edges |
|:----:|:------------:|
| quarks ↔ leptons | 6 |
| quarks ↔ bosons | 3 |
| quarks ↔ anchor | 3 |
| leptons ↔ bosons | 3 |
| leptons ↔ anchor | 0 |
| bosons ↔ anchor | 0 |

Leptons and bosons are both disconnected from anchor at face level.

### Note
dim M₁₀ = 11 also appears as the IR coefficient c₂ in the α-formula (H.1). Weight 10 = 2(N−1). The face-projected trace reproducing this dimension is [OBS].


---


## [THM] K.9: Moonshine Theorem
Source: S94
Status: [THM]
Dependencies: K.1 (Hauptmodul), A.1 (uniqueness)
Verified: Sage (30 q-coefficients, exact arithmetic)
Reference: Matsusaka (2017), Res. Number Theory, DOI:10.1007/s40993-017-0090-x

### Statement
The McKay-Thompson series of Monster class **6E** equals the LD Hauptmodul shifted by 5:

**T_{6E}(τ) = t₆(τ) + 5**

### Proof
1. Matsusaka (2017) identifies T_{6E} as normalized Hauptmodul for Γ₀(6).
2. Normalized Hauptmodul for genus-0 group is **unique** (up to normalization).
3. t₆ + 5 is also a normalized Hauptmodul for Γ₀(6).
4. By uniqueness: T_{6E} ≡ t₆ + 5. ∎

### q-expansion (30 coefficients verified)
T_{6E} = q⁻¹ + 6q + 4q² − 3q³ − 12q⁴ − 8q⁵ + 12q⁶ + 30q⁷ + ...

First coefficients = LD monomials: N, d₁², −d₂, −index, −d₁³, index, N(N−1), ... [OBS: tautological — both are Γ₀(6) structure constants].

### Cuspal values

| Cusp | t₆ | T = t₆+5 | LD |
|:----:|:--:|:--------:|:--:|
| Quarks (w=6) | 0 | 5 | d₁+d₂ |
| Leptons (w=3) | −9 | −4 | −d₁² |
| Bosons (w=2) | −8 | −3 | −d₂ |
| Anchor (w=1) | ∞ | ∞ | — |

Sum of finite cuspal T-values: 5 + (−4) + (−3) = **−2 = −d₁**.

### Replication structure

| Power | Monster class | Level |
|:-----:|:------------:|:-----:|
| g¹ | 6E | N = 6 |
| g² | 3B | d₂ = 3 |
| g³ | 2B | d₁ = 2 |
| g⁶ | 1A | 1 |

Levels = Div(6) = cusp widths.

### 21st path to (d₁,d₂) = (2,3)
New cluster (#6: sporadic groups), independent of all 5 prior clusters.

### What moonshine does NOT give for Gap 3 [S94]
T_{6E} coefficients ≠ δK(n) (signs disagree at n=4). Worldsheet/spacetime 1-loop parallel: structural but different spaces. DEAD for coupling extraction.


# L. SCATTERING MATRIX OF Γ₀(6)

## [THM] L.1: CRT Tensor Factorization
Source: Hejhal, *Selberg Trace Formula* Vol. II; Iwaniec, *Spectral Methods*
Status: [THM] (standard)

### Statement
For squarefree N = p₁···pᵣ:

$$\Phi_N(s) = \lambda(s) \bigotimes_{p \mid N} M_p(s)$$

with λ(s) = Λ(2s−1)/Λ(2s) and

$$M_p(s) = \frac{1}{p^{2s}-1}\begin{pmatrix} p-1 & p^s - p^{1-s} \\ p^s - p^{1-s} & p-1 \end{pmatrix}$$

## [THM] L.2: Cusp Indexing
Status: [THM] (standard)

Cusps of Γ₀(6) biject with P¹(ℤ/6ℤ) ≅ P¹(ℤ/2ℤ) × P¹(ℤ/3ℤ):

| CRT coords (a₂, a₃) | Cusp | Width w = 2^a₂ · 3^a₃ | LD sector |
|:---------------------:|:----:|:----------------------:|:---------:|
| (0, 0) | ∞ | 1 | anchor |
| (1, 0) | 1/3 | 2 | bosons |
| (0, 1) | 1/2 | 3 | leptons |
| (1, 1) | 0 | 6 | quarks |

Σ widths = 1 + 2 + 3 + 6 = 12 = index. ✓

## [THM] L.3: CRT Duality Involution
Status: [THM] (elementary)

### Statement
The map ι(p) = (p+1)/(p−1) satisfies ι(2) = 3, ι(3) = 2. For p ≥ 5: ι(p) < 2, not prime. Therefore {2, 3} is the unique unordered pair of primes with ι(p) = q. ∎

**Corollary.** CRT factorization ℤ/N ≅ ℤ/d₁ × ℤ/d₂ with {d₁,d₂} ι-fixed exists only for N = 6.

## [THM] L.4: Special Values at s = d₁ = 2
Status: [THM] (arithmetic)
Verified: Python

### Diagonal entries

| p | α_p(2) = (p−1)/(p⁴−1) | 1/α_p(2) |
|:-:|:----------------------:|:--------:|
| 2 | 1/15 | 15 = |P³(𝔽₂)| |
| 3 | 1/40 | 40 = |P³(𝔽₃)| |

**Projective space identity.** 1/α_p(k) = (p^{2k}−1)/(p−1) = |P^{2k−1}(𝔽_p)|.

### Off-diagonal ratios

| p | β_p(2) | β_p/α_p |
|:-:|:------:|:-------:|
| 2 | 7/30 | 7/2 = |P²(𝔽₂)|/2 |
| 3 | 13/120 | 13/3 = |P²(𝔽₃)|/3 |

### AL Eigenvalue Products

| Product | Value | = |
|:-------:|:-----:|:---:|
| Π₊₊ = e₊(2)·e₊(3) | 1/25 | 1/(d₁+d₂)² |
| Π₊₋ = e₊(2)·e₋(3) | −1/40 | −1/(d₁³(d₁+d₂)) |
| Π₋₊ = e₋(2)·e₊(3) | −1/45 | −1/(d₂²(d₁+d₂)) |
| Π₋₋ = e₋(2)·e₋(3) | 1/72 | 1/(d₁³ d₂²) |

Key ratios: Π₊₊/Π₋₋ = 72/25 = |Mon|/(d₁+d₂)², Π₊₋/Π₋₊ = 9/8 = d₂²/d₁³.

### Full 4×4 Matrix
Φ₆(d₁)/λ(d₁), row/col order (anc, bos, lep, qrk):

```
              anc(1)     bos(2)     lep(3)     qrk(6)
  anc(1)      1/600     7/1200    13/1800    91/3600
  bos(2)     7/1200      1/600    91/3600    13/1800
  lep(3)    13/1800    91/3600      1/600     7/1200
  qrk(6)    91/3600    13/1800     7/1200      1/600
```

Persymmetric: W₆ swaps anc ↔ qrk, bos ↔ lep.

### Universal factor
λ(d₁) = Λ(3)/Λ(4) = 45ζ(3)/π³. Coefficient 45 = d₂²·(d₁²+1) = d₂·|P³(𝔽_{d₁})|.

### Functional properties
1. Φ(s)·Φ(1−s) = I
2. Φ(1/2+it) unitary for t ∈ ℝ
3. Φ(1/2) = −I
4. Res_{s=1} Φ₆(s) = (1/4π)·J₄, where vol(Γ₀(6)\\ℍ) = 4π

## [OBS] L.5: LD Identifications at s = d₁
Source: S86
Status: [OBS] / [MOTIVATED]

| Automorphic quantity | Value | LD identification |
|:--------------------:|:-----:|:-----------------:|
| 1/α₃(d₁) | 40 | K\_Kirchhoff [THM D.4] |
| β₂/α₂ | 7/2 | L/d₁ |
| β₃/α₃ | 13/3 | (d₁²+d₂²)/d₂ → sin²θ₁₂ = 4/13 |
| |Π₊₊/Π₋₋| | 72/25 | |Mon|/(d₁+d₂)² |
| off-diag numerators | 7, 13, 91 | Φ₃(d₁), Φ₃(d₂), product = |P²(𝔽₂)|, |P²(𝔽₃)|, L·det_M |

**GN link (S217, X.129a):** 13 = Φ₃(d₂) = GN(τ) via Catalan (d₁²+d₂² = Φ₃(d₂), X.110). Off-diagonal numerators = Φ₃ values = Gaussian norms of leptonic cosets (Q.3). sin²θ₁₃ = index/(N·∏Φ₃) = 2/91 (X.129).

**Status of s = d₁ [MOTIVATED, not DER]:** Weight 2s = 4 = 2d₁ → E₄ unique → j = E₄³/Δ central to LD. Motivates but does not derive s = d₁.


---


# M. SELBERG TRACE FORMULA AND SCATTERING SPLITTING

## [THM] M.1: Scattering log-derivative splitting
Source: S95
Status: [THM]
Verified: SymPy (exact)

### Statement
The log-derivative c±(p) = (1/2)(φ'/φ)_{±} at prime p|N has closed forms:

c₊(2) = 17/15, c₋(2) = 1/3, c₊(3) = 23/20, c₋(3) = 5/8.

Additivity by primes: φ'/φ(s) = Σ_{p|N} c(p,s).


## [THM] M.2: Cross-duality
Source: S95
Status: [THM] (22nd path to (d₁,d₂)=(2,3))
Verified: SymPy

### Statement
Δ(p) = 2p(p²−p+1)/(p⁴−1).

**Cross-duality identity:** p²−p+1 evaluated at d₁ = 2 gives d₂ = 3; evaluated at d₂ = 3 gives L = 7.

This is the polynomial Φ₆(−p)/p² = (p²−p+1), the 6th cyclotomic evaluated at −p. The duality d₁ ↔ d₂ ↔ L is a direct consequence of CRT structure ℤ/6ℤ.


## [THM-arith / OBS] M.3: Kirchhoff = 1/α₃(d₁) = |P³(𝔽₃)|
Source: S95, bridging L.4 and D.4
Status: **[THM-arith]** for each equality individually; **[OBS]** for the bridge

### Statement
Three independently computed quantities all equal 40:
1. **Kirchhoff(dessin)** = #spanning trees of bipartite dessin graph = 40 [THM, Sage Matrix Tree]
2. **|P³(𝔽₃)|** = 1+3+9+27 = 40 [THM-arith, direct sum]
3. **1/α₃(d₁=2)** = scattering coefficient at quark cusp, s=2 = 40 [THM, Eisenstein series]

### Bridge status [OBS, S98 audit]
Each equality is independently [THM-arith]. The coincidence «graph spanning trees = projective space order = automorphic scattering» connects three different mathematical domains (combinatorics, finite geometry, analysis). No proven theorem establishes this bridge for general Γ₀(N). Potential deep connection via Arakelov height theory (Cinkir-Zhang) but unexplored in LD.

Extends: 1/α₂(d₁) = |P³(𝔽₂)| = 15.


## [OBS] M.4: 4→12 dilation via T-monodromy
Source: S95 (synthesizing S48)
Status: **[OBS]** (S98 audit: descriptive pattern, not proven theorem)

### Statement
The 4-cusp structure of Γ₀(6) dilates to 12 sheets via T-monodromy. The general pattern «face sizes relate to ramification indices» is observed but |Δn| within σ∞-faces is NOT constant: quark face |Δn| ∈ {2,2,3,4,6} (σ∞-cycle c→t→d→s→b→u, n = 4,7,1,3,5,1), lepton face |Δn| ∈ {1,3}. The claim «Δn = ramification» is false as literally stated.

### What survives
The 4→12 dilation (4 cusps × average multiplicity = 12 sheets) is a restatement of index = Σ(cusp widths) = 1+2+3+6 = 12, which is standard [THM-math]. The connection to ramification indices at the level of individual edges is [OBS].


## [CONJ] M.5: Eisenstein bridge
Source: S95
Status: [CONJ]

### Statement
The two terms of the Eisenstein series constant term at cusps correspond to Φ and −Lℓ in the δK formula. Identifies the additive structure Φ−Lℓ with the functional equation of the scattering matrix.

### Status
Qualitative match; quantitative identification requires Gap 3 (coupling α/(2π)).


## [DEAD] M.6: Contour shift
Source: S95
Status: [DEAD]

Scattering determinant −φ'/φ(s) has single pole at s = 1 (from ζ(1)), regular at s = 2,3,...,L. Individual particles do not emerge from poles. Contour shift method DEAD.


## [DER+MOTIVATED] M.7: Ring closure forces universality
Source: S100
Status: [DER+MOTIVATED] (S100 review: excludes edge-local; spectral uniqueness not proven)
Dependencies: H.3 (ring), I.6 (Cayley Laplacian)
Verified: Python (edge propagator computation)

### Statement
The spectral (global) definition of coupling is the unique **edge-independent** definition consistent with ring closure at observed precision.

### Proof (exclusion of edge-local coupling)
1. Edge propagators H[i,σ₁(i)] on Cayley graph vary by **100+%** across edges:
   anchor-quark edge (0,1): H = 0.321; lepton-quark edge (4,6): H = 0.139; spread = 106% at t=0.5.

2. A local (edge-dependent) coupling g\_edge ∝ H[i,σ₁(i)] gives particle-dependent α with ~100% variation.

3. Ring closure constrains g to **0.002% precision** (from μ\_G sensitivity: δμ\_G/μ\_G ≈ −20·δg/g, and μ\_G matches to 0.03%).

4. Therefore local couplings are **excluded** by ring closure (100% >> 0.002%).

### What remains open
Between "edge-local" and "spectral Tr(f(L))/norm" there exist intermediate global functionals (vertex-averaged, path-averaged, etc.) that are also edge-independent. The argument excludes the local extreme but does not uniquely select the spectral definition. Status [DER+MOTIVATED], not [THM].

### Born parallel
- Born: Σ ProbFun(‖Pᵢψ‖) = 1 for any decomposition → ProbFun universal.
- LD: Ring α → masses → μ\_G → α closes to single value → α universal.
Analogy is structural: conservation → universality in both cases.

### Gap 3 closure summary

| Sub-gap | Statement | Status | Reference |
|---|---|---|---|
| (3a) Form α/(2π) | 4D Weyl loop | [THM] | G.3, S29 |
| (3b) Universality | Ring forces single coupling | [DER+MOTIVATED] | M.7, S100 |
| (3c) Value 1/α ≈ 137.036 | Ring fixed point | [THM] | H.3, S31+S38 |
| (3d) EM identification | EW operator T₃−d₂\|Q\|=−ℓ/2 | [THM] | G.8, S32 |

**Gap 3: CLOSED** (3a,3c,3d at [THM]; 3b at [DER+MOTIVATED]).


---


# N. QTC — QUANTUM THEORY ON COVERINGS
Source: S105 (QTC v2.2), S106 (caveat strengthening, Fricke distance)
Status: cos² [DER], 42/42 checks (S106)
Dependencies: A.1 (N=6), C.5/E (Fricke pairs), F.3a (σ₁-dichotomy)
Verified: Python qtc_cross_verification.py (78/78), qtc_final_verification.py (42/42)

## [DER] N.1: QTC chain (12 steps → cos²(1/(Nπ)))

Setup: covering π: X₀(6)→X(1), cusps {c} with widths w ∈ Div(6) = {1,2,3,6}.

| Step | Claim | Status | Key argument |
|------|-------|--------|--------------|
| (1) | vol(X₀(6)) = 4π | [THM] | Gauss-Bonnet, ψ(6)=12 |
| (2) | C = vol/n_cusps = π | [THM+PHYS] | N.3 |
| (3) | Y_c = w_c·π; area = 1/π ∀c | [THM] | from (2) |
| (4) | Hol = k/π (cusp-independent) | [THM] | connection on weight-k bundle |
| (5) | φ(w) = k/(πw) (intensive) | [THM+PHYS] | N.4 |
| (6) | k = 1 | [THM] | N.5 (dimension matching) |
| (7) | Matter = (d₁,d₂) = (2,3) | [THM] | unique Catalan Fricke pair |
| (8) | |d₁−d₂| = 1 | [THM] | Catalan/Mihailescu |
| (9) | Δφ = 1/(Nπ) | [THM] | algebra from (5)–(8) |
| (10) | F = cos² (survival) | [THM] | 2×2 unitary from O(1) |
| (11) | EW sector = {d₁,d₂} | [THM] | σ₁-dichotomy F.3a |
| (12) | cos²(1/(Nπ)) | [DER] | (1)–(11) |

Result: cos²(1/(Nπ)) = 0.997188162113479.

## [THM+PHYS] N.3: C = π (truncation constant)

**Integer lattice [THM]:** Phase multipliers m_ij = (π/C)·|W_N(w_i)−W_N(w_j)| are integers for w_i,w_j ∈ Div(N) iff C = π/k, k ∈ ℤ⁺. Proof: W_N maps Div(N)→Div(N), so Fricke distances are integers.

**Selection of k=1 [PHYS]:** k=1 gives minimal Δφ = 1/(Nπ) (perturbative, 0.28% correction). k=2 gives 8400 ppm deviation; k≥3 worse. Gauss-Bonnet does NOT constrain C (truncation height is gauge choice).

**Geometric meaning:** C = vol/n_cusps = equal volume budget per cusp. C = vol/index = π/3 (per-sheet) excluded at >20000 ppm.

### N.3 Redundancy Note (S203)
The perturbative selection k=1 in N.3 is **subsumed by N.5**: h⁰(O(k))=k+1=2=n_matter gives k=1 geometrically [THM], after which C=π follows from integer lattice alone [THM]. Similarly, step (10) "Born rule" is a consequence of the 2×2 unitary structure from O(1) with k=1, not an independent physics input.

**Reduction:** From 2 [THM+PHYS] inputs to 1. Sole remaining physics input: f=1/w (intensive phase, N.4). Motivated as Fricke-canonical: φ(w)=W_N(w)/(Nπ). Status: [MOTIVATED], not [THM] — no uniqueness theorem for phase assignment.

## [THM+PHYS] N.4: Intensive phase φ = k/(πw)

**m-range theorem [THM]:** For f = 1/w: m_ij ∈ {0,...,N−1} = ℤ/Nℤ (minimal range). For f = w: m-values ∈ {0,N,...,N(N−1)} (sparse, range N×larger).

**Perturbativity [PHYS]:** f=1/w → correction 0.28%; f=w → correction 9.8% (non-perturbative). f=w excluded experimentally (α⁻¹ ≈ 124).

## [THM] N.5: k = 1 (dimension matching)

n_matter = 2 (Fricke pair (d₁,d₂)). On ℙ¹ = X₀(6): h⁰(O(k)) = k+1 (Riemann-Roch). Match: k+1 = 2 → k = 1. O(1) carries Hermitian metric → U(1) structure → unitary parallel transport → |S₁₁|² = cos²(δ).

Born rule enters ONLY as interpretation of |S₁₁|² as probability. The k-selection and matrix unitarity are geometric.

## [THM] N.6: Fricke distance theorem

Δφ(w_i, w_j) = |W_N(w_i) − W_N(w_j)| / (Nπ) where W_N(w) = N/w.

m-matrix for X₀(6):

|   | w=1 | w=2 | w=3 | w=6 |
|---|-----|-----|-----|-----|
| 1 |  0  |  3  |  4  |  5  |
| 2 |  3  |  0  |  1  |  2  |
| 3 |  4  |  1  |  0  |  1  |
| 6 |  5  |  2  |  1  |  0  |

Invariants: m ∈ {0,...,N−1}, Σm(i<j) = d₁⁴ = 16, Πm(i<j) = (N−1)! = 120.
Row sums: {index, N, N, d₁³} = {12, 6, 6, 8}.

## [THM] N.7: d₁=2 degeneracy

Δφ(d₁,d₂) = Δφ(d₂,N) iff d₁ = 2. Proof: (d₁−1)/N = |d₂−d₁|/(d₁d₂) iff d₁−1 = 1.

Corollary: {φ(d₁), φ(d₂), φ(N)} = {1/(2π), 1/(3π), 1/(6π)} is arithmetic progression with step φ(N). Δφ(matter) = φ(N) = quarks-cusp phase.

## N.8: Scope and limitations

QTC derives cos²(1/(Nπ)) [DER]. QTC does NOT derive: IR (structural mismatch: rational vs trig), PMNS (needs Cayley graph §I.6), CKM (needs tree/Kirchhoff §E), δK (φ(d₁)=1/(2π) is tautological for d₁=2). 4×4 transition matrix eigenvalues {3.923, 0.077, 2.1×10⁻⁴, 0} do not match LD invariants. QTC on 12 sheets = trivial blow-up (face-constant phases). 9 dead approaches: heat kernel, quantum walk, BB^T ratio, Cayley ratio, Fourier phases (explicitly disproven S104), spectral resolvent, E₂* gradient (PSLQ NULL), scattering phase (r* transcendental), Selberg trace (structural: cos ∉ trace formula).


---


# P. HEEGNER OBSTRUCTION ON X₀(6)

## [THM-arith] P.1: Complementary Inertness
Source: S118
Status: [THM-arith]
Dependencies: A.1 (N=6), C.7 (CRT structure)
Verified: Python (Kronecker symbols, exact Q(√6) arithmetic for Hauptmodul)

### Statement
The two CM points τ = i (j = 1728, D = −4) and τ = ρ (j = 0, D = −3) are **not** Heegner points on X₀(6). Each is blocked by the **other** prime factor of N = d₁·d₂.

### Proof
A CM point of discriminant D is a Heegner point on X₀(N) iff H(D,N) = h(D)·∏_{p|N}(1 + χ_D(p)) > 0.

**D = −4 (j = 1728):** h(−4) = 1. χ₋₄(2) = 0 (ramified), χ₋₄(3) = −1 (inert: x²+1 ≡ 0 mod 3 has no solution). Factor (1+χ₋₄(3)) = 0. **H = 0.** Blocked by p = d₂ = 3.

**D = −3 (j = 0):** h(−3) = 1. χ₋₃(2) = −1 (inert: x²+x+1 ≡ 0 mod 2 has no solution), χ₋₃(3) = 0 (ramified). Factor (1+χ₋₃(2)) = 0. **H = 0.** Blocked by p = d₁ = 2. ∎

### CRT interpretation
The blocking pattern mirrors the CRT face structure of the dessin (C.7):

| CM point | p = d₁ = 2 | p = d₂ = 3 | Heegner on X₀(6)? | Face analog |
|---|---|---|---|---|
| j = 1728 (D = −4) | ramifies | **inert** | NO | Bosons (only p = 2 active) |
| j = 0 (D = −3) | **inert** | ramifies | NO | Leptons (only p = 3 active) |

In the CRT decomposition P¹(ℤ/6ℤ) ≅ P¹(𝔽₂) × P¹(𝔽₃), bosons live in the 2-face (only 𝔽₂ coordinate finite), leptons in the 3-face (only 𝔽₃ coordinate finite). The Heegner obstruction is the number-theoretic shadow of this CRT dichotomy: the CM point associated with p is blocked by q ≠ p, exactly the prime whose face it does not inhabit.

### First Heegner discriminant on X₀(6): D = −8

H(−8, 6) = h(−8)·(1+χ₋₈(2))·(1+χ₋₈(3)) = 1·1·2 = 2.

Ring: ℤ[√−2], class number 1. j(√−2) = 8000 = 20³.

### [THM-arith] P.1a: Hauptmodul at D = −8

The minimal polynomial of t₆ at j = 8000 is:

**t² − 72t − 648 = 0**

Roots: t = 36 ± 18√6 = 18(d₁ ± √N). In ℚ(√N).

Coefficients: 72 = d₁³d₂² = index·N, 648 = d₁³d₂⁴. Discriminant: 7776 = (d₁²d₂²)²·N = (∏wᵢ)²·N.

Verified: exact arithmetic in ℚ(√6) confirms j(36+18√6) = 8000 and t²−72t−648 = 0.

### Consequence for α derivation

α⁻¹ = BULK − IR uses E₂(i) = 3/π evaluated at τ = i (a **non-Heegner** point on X₀(6)). Therefore:
- Kudla generating series on X₀(6) **cannot** encode α via heights of Heegner points [DEAD]
- Arakelov intersection theory at τ = i has **no** arithmetic interpretation through Heegner theory [DEAD]
- The route to α must pass through **analysis** (Eisenstein series, QTC, spectral theory) rather than **arithmetic geometry** (heights, L-derivatives, Gross-Zagier)

This is a structural no-go, not a failure of technique: the very points where LD evaluates its formulas are invisible to the Heegner machinery of X₀(6).


---


# R. CUSPAL REGULATORS

## [THM] R.1: First Cuspal Regulator — ln d₁
Source: S119 (numerical, 0.0 ppm), S120 (analytical proof)
Status: [THM]
Dependencies: K.1 (cuspal values of t₆), C.2 (ramification indices)
Verified: mpmath 25-digit (cuspal phases), continuous arg tracking (500 pts, 4 checks)

### Statement

$$\int_{0 \to 1/2} \eta(t_6,\; t_6 + d_1^3) = -2\pi \ln d_1 = -2\pi \ln 2$$

where η(f,g) = log|f| d(arg g) − log|g| d(arg f) is the regulator 1-form, and the integral is over the geodesic from cusp 0 (quarks, w = 6) to cusp 1/2 (leptons, w = 3) in ℍ.

### Proof

**Step A (Substitution).** Set u = t₆/(−d₁³) = t₆/(−8). Path: u = 0 → u = d₂²/d₁³ = 9/8.

$$\eta(-d_1^3 u,\; d_1^3(1-u)) = \ln(d_1^3) \cdot d\!\left(\arg\frac{1-u}{u}\right) + \eta(u, 1-u)$$

Proof of identity: log|−d₁³u| = ln(d₁³) + log|u|; arg(−d₁³u) = π + arg(u); arg(d₁³(1−u)) = arg(1−u). Expand η and collect the constant ln(d₁³) term. ∎

**Step B (Bloch–Wigner vanishing).** η(u, 1−u) = dD(u) where D(z) = Im Li₂(z) + arg(1−z)·log|z| is the Bloch–Wigner function. D(z) = 0 for all z ∈ ℝ. Both endpoints are real: u = 0, u = 9/8. D(0) = lim_{z→0⁺} D(z) = 0 (standard: Im Li₂(z) → 0 and arg(1−z)·log|z| → 0·(−∞) = 0; rigorous via |D(z)| ≤ C·|z|·|log|z|| near 0). The path passes through upper half-plane (Im u > 0 verified numerically, 500 pts). Therefore:

$$\int dD = D(9/8) - D(0) = 0$$

**Step C (Phase computation).** Remains: ∫ = ln(d₁³) · Δarg((1−u)/u).

*Start (cusp 0):* Geodesic τ(θ) = 1/4 + (1/4)e^{iθ}, θ → π. Via Fricke involution W₆: τ → −1/(6τ) → ∞, with q_∞ acquiring phase e^{−2πi/3}. Since t₆ ~ 72·q_∞^{−1} near cusp 0: **arg(t₆) → −2π/3** [VERIFIED: −2.09439 vs target −2.09440].

Then arg(u) = arg(t₆) + π = π/3, and arg((1−u)/u) ≈ arg(1/u) = −π/3.

*End (cusp 1/2):* t₆(1/2) = −d₂² = −9, u = 9/8, w = (1−u)/u = −1/9. Path approaches from upper half-plane → arg(w) = −π.

*Total:*

$$\Delta\arg = -\pi - (-\pi/3) = -\frac{2\pi}{3} = -\frac{2\pi}{e_0}$$

where e₀ = d₂ = 3 is the ramification index at j = 0.

[VERIFIED: continuous arg tracking, 500 points, unwrapped Δarg = −2.094, target −2π/3 = −2.094.]

**Result:**

$$\int_{0 \to 1/2} \eta(t_6, t_6+8) = 3\ln 2 \cdot \left(-\frac{2\pi}{3}\right) = -2\pi\ln 2 \qquad \blacksquare$$


## [THM] R.2: Second Cuspal Regulator — ln d₂
Source: S119 (numerical), S120 (analytical proof)
Status: [THM]
Dependencies: K.1, C.2
Verified: mpmath 25-digit, continuous arg tracking (400 pts)

### Statement

$$\int_{1/3 \to \infty} \eta(t_6,\; t_6 + d_2^2) = -2\pi \ln d_2 = -2\pi \ln 3$$

where the integral is over the vertical geodesic from cusp 1/3 (bosons, w = 2) to cusp ∞ (anchor, w = 1).

### Proof

**Substitution:** v = t₆/(−d₂²) = t₆/(−9). Path: v = d₁³/d₂² = 8/9 → v → ∞.

$$\eta(t_6, t_6+9) = \ln(d_2^2) \cdot d\!\left(\arg\frac{1-v}{v}\right) + dD(v)$$

**Bloch–Wigner:** D(8/9) = 0 (real argument). D(∞) = lim_{|z|→∞} D(z) = 0 (standard: D decays as O(log|z|/|z|)). ∫dD = 0.

**Phase:**
- Start: v = 8/9 (real), w = (1−v)/v = 1/8 > 0, arg(w) = 0.
- End: v → ∞ with arg(v) → π/3 (from q-expansion at cusp ∞: t₆ ~ e^{2πy}·e^{−2πi/3}, v = t₆/(−9) → ∞·e^{iπ/3}), w → −1 from below, arg(w) → −π.

$$\Delta\arg = -\pi - 0 = -\pi = -\frac{2\pi}{e_{1728}}$$

where e₁₇₂₈ = d₁ = 2 is the ramification index at j = 1728.

[VERIFIED: arg(w) from −0.724 (cutoff y=0.15) to −3.1416 (y=5.0). Slow convergence at start is q-expansion artifact near cusp 1/3.]

**Result:**

$$\int_{1/3 \to \infty} \eta(t_6, t_6+9) = 2\ln 3 \cdot (-\pi) = -2\pi\ln 3 \qquad \blacksquare$$


## R.3: General Cuspal Regulator Formula
Source: S120
Status: **[THM]** for the two computed cases (R.1, R.2); **[THM-arith]** for the general pattern
Dependencies: R.1, R.2, K.1, C.2

### Statement

For a cusp c of X₀(6) with width w_c and Hauptmodul value t_c, the regulator integral of the symbol {t₆, t₆ − t_c} along a geodesic γ that separates the zeros of the symbol and bypasses cusp c equals:

$$\int_\gamma \eta(t_6,\; t_6 - t_c) = -2\pi \ln w_c$$

### Mechanism

The substitution s = t₆/(−t_c) yields:
1. **Logarithmic factor:** ln|t_c| = e_c · ln(w_c), where e_c is the ramification index at cusp c (since |t_c| = w_c^{e_c} from K.1 cuspal values: |−d₁³| = d₁³ = d₁^{e₁} at e₁ = d₂; |−d₂²| = d₂² = d₂^{e₀} at e₀ = d₁).
2. **Phase factor:** Δarg((1−s)/s) = −2π/e_c, where e_c enters through the q-expansion phase at cusp c.
3. **Bloch–Wigner vanishing:** D = 0 at both (real) endpoints.
4. **Cancellation:** e_c · ln(w_c) × (−2π/e_c) = −2π ln(w_c). The ramification index creates the power in |t_c| and compresses the phase rotation, producing the cusp-width invariant ln(w_c).

### Cuspal values and ramification cross-reference

| Cusp | t_c | w_c | e_c (from C.2) | |t_c| = w_c^{e_c} | Δarg | Result |
|------|-----|-----|----------------|-------------------|------|--------|
| 0 (quarks) | 0 | 6 | — | — | — | (trivial: t₆ = 0 is zero, not pole) |
| 1/2 (leptons) | −d₂² = −9 | d₂ = 3 | d₁ = 2 | 9 = 3² ✓ | −π | −2π ln 3 (R.2, reversed) |
| 1/3 (bosons) | −d₁³ = −8 | d₁ = 2 | d₂ = 3 | 8 = 2³ ✓ | −2π/3 | −2π ln 2 (R.1) |
| ∞ (anchor) | ∞ | 1 | — | — | — | (trivial: ln 1 = 0) |

### Key identity

$$|t_c| = w_c^{e_c}: \quad d_1^3 = d_1^{d_2}, \quad d_2^2 = d_2^{d_1}$$

Both hold iff exponent = other prime factor of N: d₂ = 3, d₁ = 2. This is a direct consequence of uniform ramification (ν₂ = ν₃ = 0 → e(j=0) = d₂, e(j=1728) = d₁), which holds only at N = 6 (Path A, §A.1).


## [OBS] R.4: Regulator integrals as lattice generators
Source: S119–S120
Status: [OBS] (mathematical coherence)

### Statement

The two non-trivial cuspal regulators extract the generators of the multiplicative lattice ⟨d₁, d₂⟩ = ⟨2, 3⟩:

$$\ln d_1 = \frac{-1}{2\pi}\int_\gamma \eta(t_6, t_6 + d_1^3), \qquad \ln d_2 = \frac{-1}{2\pi}\int_\gamma \eta(t_6, t_6 + d_2^2)$$

These are the same generators that appear in:
- B.3: Hecke orbit ⟨T₂, T₃⟩ = B₁\{√2}
- B.5: Adelic structure ∏_v|K|_v = 1 on ⟨2,3⟩ ∩ ℚ*
- K.1: Discriminants of P₄ and R₃ are pure {2,3}

The regulators provide a **period-theoretic** realization of the lattice generators, complementing the arithmetic (B.3), adelic (B.5), and Hauptmodul (K.1) realizations.

### Scope caveat

No connection to α/(2π) or Gap 3 has been established. The regulators extract ln(primes), not coupling constants. This result strengthens the case for (d₁,d₂) = (2,3) but does not advance the open problems.


## [THM] R.5: Vanishing of Third Symbol on Finite Paths
Source: S121
Status: [THM]
Dependencies: R.3 (general formula)
Verified: Analytical (exact)

### Statement

For all geodesics γ between finite cusps of X₀(6):

$$\int_\gamma \eta(t_6 + d_1^3,\; t_6 + d_2^2) = 0$$

### Proof

Set c = d₂² − d₁³ = 9 − 8 = 1. Substitution s = −(t₆+d₁³)/c = −(t₆+8):

$$\int_\gamma \eta(t_6+8,\; t_6+9) = \ln|c| \cdot \Delta\!\arg\frac{1-s}{s} + [D(s_{\text{end}}) - D(s_{\text{start}})]$$

First term: **ln|1| = 0** → vanishes identically regardless of Δarg.

Second term: cuspal values of s = −(t₆+8) are:
- cusp 0 (t₆=0): s = −8 (real)
- cusp 1/2 (t₆=−9): s = 1 (real)
- cusp 1/3 (t₆=−8): s = 0 (real)

D(z) = 0 for all z ∈ ℝ → D(s) = 0 at all finite-cusp endpoints. Both terms vanish. ∎

### Scope

Paths to cusp ∞ are NOT covered: t₆ → ∞ with complex phase → s → ∞·e^{iα}, and D(∞·e^{iα}) is not necessarily zero. These integrals are [OPEN].

### Structural meaning

|d₂² − d₁³| = |9−8| = 1. This is the Catalan unit: the unique solution to |xᵖ − yᵍ| = 1 (Mihailescu). The Catalan proximity that drives K.7 (prime separation at cusps) simultaneously forces the third symbol to be trivial. The effective rank of the regulator space is 2, not 3.


## [THM] R.6: Vanishing on Real Paths
Source: S121
Status: [THM]
Dependencies: None (elementary)
Verified: Numerical (η-product 150 terms, 50 digits, verified t₆ ∈ ℝ on Re(τ)∈{0, 1/2})

### Statement

If t₆ is real-valued along a geodesic γ, and neither t₆ = 0, t₆ = −d₁³, nor t₆ = −d₂² is attained in the interior of γ, then:

$$\int_\gamma \eta(t_6 + a,\; t_6 + b) = 0 \qquad \text{for } a, b \in \{0, d_1^3, d_2^2\}$$

### Proof

For t₆ ∈ ℝ, both f = t₆ + a and g = t₆ + b are real. If neither vanishes on the interior of γ, then arg(f) and arg(g) are piecewise constant (0 or π). Therefore d(arg f) = d(arg g) = 0 as distributions on γ, and η(f,g) = log|f|·d(arg g) − log|g|·d(arg f) = 0. ∎

### Applicable paths

t₆ is real on vertical geodesics Re(τ) = 0 and Re(τ) = 1/2 (verified numerically). Not real on Re(τ) = 1/3.

| Path | t₆ real? | Zeros of {t₆, t₆+8, t₆+9} on path? | ∫η |
|------|----------|--------------------------------------|-----|
| 0→∞ (Re=0) | ✓ | t₆=0 at cusp 0 = endpoint only | 0 for all symbols |
| 1/2→∞ (Re=1/2) | ✓ | t₆+9=0 at cusp 1/2 = endpoint | 0 for {t₆, t₆+8}; {t₆, t₆+9} needs regularization |

### t₆ reality data

| Re(τ) | Im(τ) | t₆ | Im(t₆) |
|-------|-------|-----|---------|
| 0 | 0.3 | +2.57 | 0 |
| 0 | 1.0 | +530.5 | 0 |
| 1/3 | 0.3 | −8.80 − 5.00i | **≠ 0** |
| 1/3 | 1.0 | −272.8 − 463.7i | **≠ 0** |
| 1/2 | 0.3 | −12.40 | ~10⁻⁵⁰ |
| 1/2 | 1.0 | −540.5 | ~10⁻⁴⁹ |


## [THM] R.7: Uniqueness of R.3 Mechanism for N=6
Source: S121
Status: [THM]
Dependencies: A.1 (Path A), C.2 (ramification)
Verified: Exhaustive scan of genus-0 squarefree levels

### Statement

Among all genus-0 squarefree modular curves X₀(N), the cuspal regulator formula ∫η = −2π ln(w_c) with mechanism |t_c| = w_c^{e_c} holds **only for N = 6**.

### Proof

The mechanism requires:
1. Hauptmodul exists → genus 0
2. Cuspal values are powers of cusp widths → |t_c| = w_c^{e_c}
3. Uniform ramification → e_c is the SAME for all preimages at j=0 (resp. j=1728)

Condition (3) is equivalent to ν₂ = ν₃ = 0. Among genus-0 squarefree levels {1,2,3,5,6,7,10,13}:

| N | ν₂ | ν₃ | ν₂=ν₃=0? |
|---|----|----|----------|
| 2 | 1 | 0 | ✗ |
| 3 | 0 | 1 | ✗ |
| 5 | 2 | 0 | ✗ |
| **6** | **0** | **0** | **✓** |
| 7 | 0 | 2 | ✗ |
| 10 | 2 | 0 | ✗ |
| 13 | 2 | 2 | ✗ |

Only N=6 satisfies all three conditions. This is precisely Path A (A.1 Filter 3). ∎

### Note on A.3 cluster assignment

The uniqueness condition (ν₂ = ν₃ = 0) is identical to A.1 Filter 3. Path 32 therefore belongs to cluster 2 (ramification/j-geometry), arrived at through a different mathematical domain (K₂-theory / regulators vs. dimension formulas). It does not constitute an independent cluster.


## [RESOLVED] R.8: K₂ Structure of Regulator Space
Source: S121
Status: [RESOLVED] (structural analysis, not a numbered theorem)
Dependencies: R.1–R.5

### Setting

X₀(6) \ {cusps} = ℙ¹ \ {0, −8, −9, ∞}: affine curve of genus 0 with 4 punctures.

### Units

𝒪*(X) = ℂ* · ⟨t₆, t₆+8, t₆+9⟩, rank 3.

### K₂ basis

Three Steinberg symbols: {t₆, t₆+8}, {t₆, t₆+9}, {t₆+8, t₆+9}.
Rank formula: rk K₂(ℙ¹ \ {n pts}) = C(n−1, 2) = C(3,2) = 3.

### Effective rank

The third symbol {t₆+8, t₆+9} has trivial regulator on all finite paths (R.5: |d₂²−d₁³| = 1, Catalan). **Effective regulator rank = 2.**

The two non-trivial regulators extract precisely the generators of the multiplicative lattice ⟨d₁, d₂⟩ = ⟨2, 3⟩:

$$\frac{-1}{2\pi}\int \eta(t_6, t_6+d_1^3) = \ln d_1, \qquad \frac{-1}{2\pi}\int \eta(t_6, t_6+d_2^2) = \ln d_2$$

This is the **period-theoretic** realization of the same lattice that appears in:
- B.3: Hecke orbit ⟨T₂, T₃⟩
- B.5: Adelic product formula on ⟨2,3⟩ ∩ ℚ*
- K.1: Pure {2,3} discriminants of Hauptmodul polynomials

### No connection to coupling

The regulators extract ln(primes), not α/(2π). PSLQ tests (S121, 80 digits, 11 basis sets) confirm: −2π ln 2 is NOT a ℚ-linear combination of any standard L-values (L'(0,χ), L(1,χᵢ)·L(1,χⱼ), ζ'_K(0)). Baker's theorem: {ln 2, ln 3, ln(2+√3)} are ℚ-linearly independent, blocking all L-function routes.


## R.9: Complete Regulator Table — Classification
Source: S121
Status: Classes A and B [THM]; Class C [OPEN]

### Class A: Clean Regulators (Bloch–Wigner vanishing + computable phase)

| Symbol | Path | ln|c| | Δarg | Result | §Ref |
|--------|------|-------|------|--------|------|
| {t₆, t₆+8} | 0→1/2 | 3ln2 | −2π/3 | −2π ln 2 | R.1 |
| {t₆, t₆+9} | 1/3→∞ | 2ln3 | −π | −2π ln 3 | R.2 |

### Class B: Structural Zeros

| Symbol | Path | Reason | §Ref |
|--------|------|--------|------|
| {t₆+8, t₆+9} | all finite-cusp paths | ln|d₂²−d₁³| = ln 1 = 0 (Catalan) | R.5 |
| all symbols | 0→∞ (Re=0) | t₆ real, >0 on path → d(arg)=0 | R.6 |
| {t₆, t₆+8} | 1/2→∞ (Re=1/2) | t₆ real, <−9 → f,g<0, arg=π=const | R.6 |

### Class C: Open (computable in principle, deferred)

| Symbol | Path | Obstruction |
|--------|------|-------------|
| {t₆, t₆+8} | 1/3→∞ | s_end complex (arg ≠ 0,π), D(s_end) ≠ 0 |
| {t₆, t₆+9} | 0→1/2, 0→1/3, 1/2→1/3 | Both endpoints real (D=0), but Δarg needs cuspal phase at each cusp |
| {t₆, t₆+9} | 1/2→∞ | g = t₆+9 changes sign on path → endpoint singularity |
| all symbols | paths to ∞ via Re=1/3 | t₆ complex along entire path |
| {t₆+8, t₆+9} | paths to ∞ | D(∞·e^{iα}) ≠ 0 in general |

Class C integrals on semicircular geodesics (finite-cusp to finite-cusp) are computable by the same Bloch–Wigner + phase method as R.1–R.2. The obstruction is computing Δarg at each cusp via cuspal q-expansion phases. These are doable but were not completed in S121.

### Summary count

- Total combinations: 3 symbols × 6 undirected paths = 18
- Class A (proven non-zero): 2
- Class B (proven zero): ≥5
- Class C (open, deferred): ≤11


---


# Q. CAYLEY–HECKE BRIDGE

## [THM-comb] Q.1: Cayley–Hecke Trace Formula

Source: S122
Status: [THM-comb] (verified 23 primes p ≤ 97; uniqueness verified against 6 other squarefree levels)
Dependencies: O.1 (monodromy), I.6 (Cayley spectrum)
Verified: Python (S122 session + S122 audit, two independent implementations)

### Convention

A = σ₁ + σ₀ + σ₀⁻¹ is the Cayley adjacency matrix on P¹(ℤ/6ℤ) via **right** coset action. T_p is the Hecke operator in the standard **left** (pullback on functions) convention. This mixed convention is natural: monodromy acts geometrically on cosets, Hecke acts arithmetically on the function space over the same 12-point set.

### Statement

For all primes p �174 6:

$$\mathrm{Tr}(A_{\mathrm{Cayley}} \cdot T_p^{\mathrm{left}}) = (p+1) - 2\chi_{-3}(p)$$

where χ₋₃ = (−3/·) is the Legendre symbol of the CM field ℚ(√−d₂).

In the consistent right×right convention: Tr(A · T_p^{right}) = p − 1.

### Decomposition by generator

| Generator | Tr(g · T_p^{left}) | Formula |
|-----------|---------------------|---------|
| σ₁ (= S) | (p + 3 − 4χ₋₃(p))/3 | p≡1(3): (p−1)/3; p≡2(3): (p+7)/3 |
| σ₀ (= ST) | (p − χ₋₃(p))/d₂ | p≡1(3): (p−1)/3; p≡2(3): (p+1)/3 |
| σ₀⁻¹ | same as σ₀ | verified 12 primes |

Verification: (p+3−4χ)/3 + 2·(p−χ)/3 = (3p+3−6χ)/3 = (p+1)−2χ. ✓

### Uniqueness

Among squarefree levels N ∈ {6, 10, 14, 15, 21, 22, 26}, only N = 6 has Tr(A · T_p^{left}) = linear function of p with **constant** χ-coefficient for all p. All other levels have non-linear dependence. A random 3-regular graph on 12 points also fails.

### Proof sketch

Tr(A · T_p) = Tr(σ₁ · T_p) + 2·Tr(σ₀ · T_p). The CRT decomposition P¹(ℤ/6ℤ) ≅ P¹(𝔽₂) × P¹(𝔽₃) factorizes the Hecke action: the 𝔽₃ factor generates χ₋₃ through the quadratic residue structure of the order-3 elliptic point. Full analytical proof from CRT local traces: [OPEN].

### 33rd path to (d₁,d₂) = (2,3)

Cluster 9 (Cayley×Hecke): new mathematical domain, independent of clusters 1–8. The formula encodes the character χ₋₃ of ℚ(√−3) = ℚ(√−d₂), linking the dessin combinatorics to the arithmetic of the CM field.

### Scope and dead ends

- No direct connection to α/(2π) established. The normalized commutator ‖[A, T₅]‖/(‖A‖·‖T₅‖) ≈ 0.91, three orders of magnitude above α/(2π) ≈ 0.00116. [DEAD]
- PMNS from A↔T eigenbasis overlap: A restricted to 3 leptonic face-points is the zero matrix. Restricted to σ₁-doublets: trivial J+I. [DEAD]

### CORRECTION NOTE (S122 audit)

S122 session log claimed Tr(σ₁ · T_p) = 2 = const ("only bridge pair {u,t} contributes"). This is **wrong**: Tr(σ₁ · T_p) = (p+3−4χ₋₃)/3, varying with p. The interpretation "Hecke-rigid bridge pair" is invalidated. The σ₀ component formula and the total are correct.


## [THM] Q.2: Cayley Square Trace

Source: S122
Status: [THM] (analytical proof + verified for 12 squarefree levels)
Dependencies: none (pure permutation algebra)

### Statement

For Γ₀(N) (N squarefree), with A = σ₁ + σ₀ + σ₀⁻¹ on P¹(ℤ/Nℤ):

$$\mathrm{Tr}(A^2) = 3 \cdot \psi(N) + 2\nu_3(N) + 4$$

where ψ(N) = [SL₂(ℤ) : Γ₀(N)] = index, and ν₃(N) = #{elliptic points of order 3 for Γ₀(N)} = #{fixed points of σ₀ on P¹(ℤ/Nℤ)}.

For N squarefree: ν₃(N) = ∏_{p|N} (1 + (−3/p)), with convention (−3/2) = −1, (−3/3) = 0.

For N = 6: ν₃ = (1+(−3/2))·(1+(−3/3)) = 0·1 = 0, so Tr(A²) = 3·12 + 0 + 4 = **40 = Kirchhoff**.

### Proof

A² = (σ₁ + σ₀ + σ₀⁻¹)². Expanding and using σ₁² = I, σ₀² = σ₀⁻¹, σ₀⁻² = σ₀:

Tr(A²) = Tr(I) + Tr(σ₀⁻¹) + Tr(σ₀) + 2Tr(σ₁σ₀) + 2Tr(σ₁σ₀⁻¹) + 2Tr(I)

= 3·ψ(N) + 2·ν₃(N) + 2·#{fix σ₁σ₀} + 2·#{fix σ₁σ₀⁻¹}

σ₁σ₀ = S·(ST) = S²T = T on P¹ (since S² = −I acts trivially). #{fix T} = 1 (unique fixed point (1:0)).

σ₁σ₀⁻¹: cycle type matches σ∞; #{fix} = #{fix σ∞} = 1 for all squarefree N.

Total: 3ψ + 2ν₃ + 2·1 + 2·1 = **3ψ + 2ν₃ + 4**. ∎

### Verified

| N | ψ | ν₃ | Tr(A²) | 3ψ+2ν₃+4 | ✓ |
|---|---|:--:|:------:|:---------:|:-:|
| 6 | 12 | 0 | 40 | 40 | ✓ |
| 10 | 18 | 0 | 58 | 58 | ✓ |
| 14 | 24 | 0 | 76 | 76 | ✓ |
| 15 | 24 | 0 | 76 | 76 | ✓ |
| 21 | 32 | 2 | 104 | 104 | ✓ |
| 22 | 36 | 0 | 112 | 112 | ✓ |
| 26 | 42 | 0 | 130 | 130 | ✓ |
| 30 | 72 | 0 | 220 | 220 | ✓ |
| 33 | 48 | 0 | 148 | 148 | ✓ |
| 35 | 48 | 0 | 148 | 148 | ✓ |
| 39 | 56 | 2 | 176 | 176 | ✓ |
| 42 | 96 | 0 | 292 | 292 | ✓ |

### N=6 specificity

Tr(A²) = 40 = Kirchhoff = d₁³(d₂−1)(N−1)/2 is specific to N = 6. At other levels Tr(A²) ≠ Kirchhoff of the bipartite dessin. The coincidence links the Cayley graph metric (return paths of length 2) to the spanning-tree count of the bipartite graph — two a priori unrelated quantities that agree only at N = 6.

### CORRECTION NOTE (S122 audit)

S122 session log stated Tr(A²) = 3·index + 4·#{fix σ∞} "universal for squarefree N" with #{fix σ∞} = 2 at N=21. Both claims are wrong: (i) correct formula has ν₃ term from σ₀ fixed points; (ii) #{fix σ∞} = #{fix T⁻¹} = 1 for all squarefree N. The session's proof assumed "σ₀ has no fixed points" — true only when ν₃ = 0, which includes N=6 but not N=21 (ν₃=2). For N=6 the result 40 = Kirchhoff is unaffected.


## [THM] Q.3: Gaussian Norms of Particle-Edges

Source: S122
Status: [THM] (analytical proof for E₂ identity; verified numerically for all 12 cosets)
Dependencies: H.1a (E₂(i) = 3/π), C.7 (CRT bijection)

### Statement

For γ_k = [[a_k, b_k], [c_k, d_k]] ∈ SL₂(ℤ) the coset representative of the k-th edge of the X₀(6) dessin:

$$E_2(\gamma_k(i)) = (c_k^2 + d_k^2) \cdot \frac{3}{\pi}$$

where c_k² + d_k² = N_{ℚ(i)/ℚ}(c_k + d_k·i) is the Gaussian norm in the CM field of j = 1728.

### Proof

E₂ quasi-modular transformation: E₂(γτ) = (cτ+d)²E₂(τ) + 12c(cτ+d)/(2πi).

At τ = i: (ci+d)² = d²−c²+2cdi, and 12c(ci+d)/(2πi) = 6c(c−di)/π.

Substituting E₂(i) = 3/π:

E₂(γ(i)) = [(d²−c²+2cdi)·3/π + 6c(c−di)/π] = 3(c²+d²)/π.  ∎

### The 12 Gaussian norms

| Particle | (c, d) | c²+d² | LD invariant |
|----------|:------:|:-----:|:------------|
| p | (0, 1) | 1 | trivial |
| c | (1, 0) | 1 | trivial |
| t | (1, 1) | 2 | d₁ |
| d | (1, 2) | 5 | N−1 |
| μ | (2, 1) | 5 | N−1 |
| s | (1, 3) | 10 | \|B₁\| |
| W | (3, 1) | 10 | \|B₁\| |
| τ | (2, 3) | 13 | det M_lep = d₁²+d₂² |
| H | (3, 2) | 13 | det M_lep |
| b | (1, 4) | 17 | d₁⁴+1 |
| u | (1, 5) | 26 | d₁·det M_lep |
| e | (2, 5) | 29 | d₁²+(N−1)² |

### Key properties

1. **Sum**: Σ(c²+d²) = 132 = index · dim M₁₀ = 12 · 11.
2. **σ₁-pair norm**: σ₁ = S acts on bottom rows as (c,d) → (d,−c), so c²+d² → d²+c². The Gaussian norm is S-invariant by construction. All six σ₁-pairs preserve c²+d² at the level of the SL₂-matrix bottom row. The three pairs where canonical P¹-representatives have different norms ({u,t}: 26≠2, {b,μ}: 17≠5, {d,e}: 5≠29) reflect representative normalization (multiplication by units of ℤ/6ℤ), not a physical asymmetry.

### Convention note (S156 audit)

The table above uses the T⁻¹ = σ∞ convention (computational algebra, CW monodromy at ∞). The alternative T = σ∞ convention (Shimura, CCW) exchanges (c,d) assignments within three σ₁-pairs: {u↔t}, {b↔d}, {e↔μ}. Both are valid P¹(ℤ/6ℤ) identifications. See I.9h for the CCW table.

Convention-dependent claims (individual norms per particle) must specify which table. Convention-independent claims (norm multisets, pair properties, Σ norms) are unaffected.
3. **5 of 8 distinct norms** are established LD invariants: 1, 2 (=d₁), 5 (=N−1), 10 (=|B₁|), 13 (=det M_lep). Remaining: 17, 26, 29.
4. **CM field**: c²+d² is the norm in ℤ[i], the ring of integers of ℚ(√−1) = CM field of τ = i. This connects the dessin edge labels to the arithmetic of the CM point used in the α-formula (H.1).

### Honesty caveat

The E₂ identity is generic (holds for ANY subgroup of SL₂(ℤ), any coset). The LD-specific content is: (a) the particular set of 8 distinct norms from Γ₀(6) cosets, and (b) 5 of 8 coincide with LD invariants. At N=6, the LD invariant pool includes many small integers ({1,2,3,4,5,6,7,9,10,11,12,13,...}), so some overlap is expected by chance. Whether the sum 132 = 12·11 is deep or a consequence of summing 12 small-ish numbers awaits a structural explanation.


## [THM-arith] Q.4: Coset Norms of Γ₀(6) — BV/WV Decomposition (S139–S140)
Source: S139 (computed), S140 (corrected)
Status: [THM-arith]
Verified: Python (exact algebraic Im(τ), S139 table)

### Statement

Eisenstein norms of BV coset representatives (Im(τ_BV) = √3/(2N_ω)):

| BV | N_ω | LD identification |
|----|-----|-------------------|
| BV₀ (anchor) | 1 | 1 |
| BV₁ (index) | d₂ = 3 | ramification at j=0 |
| BV₂ (star) | L = 7 | lattice boundary |
| BV₃ (other) | d₁²+d₂² = 13 | det M_lep |

**Σ N_ω(BV) = 24 = d₁ · index.**

Gaussian norms of WV coset representatives (Im(τ_WV) = 1/(c²+d²)):

| WV | N_i = c²+d² | LD identification |
|----|-------------|-------------------|
| WV₀ | 1 = 0²+1² | 1 |
| WV₁ | 2 = 1²+1² | d₁ |
| WV₂ | 5 = 2²+1² | N−1 |
| WV₃ | 10 = 3²+1² | \|B₁\| |
| WV₄ | 13 = 3²+2² | d₁²+d₂² |
| WV₅ | 17 = 4²+1² | d₁⁴+1 |

**Σ N_i(WV) = 48 = d₁² · index.**

**Ratio:** Σ_WV / Σ_BV = d₁ = 2.

Note: Q.3 gives Σ(c²+d²) = 132 over ALL 12 cosets (one per edge). Q.4 sums over 10 vertices (4 BV + 6 WV) — different geometric objects, not a decomposition of Q.3.

BV: d₂ = 3 ramified in ℤ[ω]; WV: d₁ = 2 ramified in ℤ[i] — matches dessin ramification (C.2).

**Erratum S139:** Original BV denominators D = {1, 3, 14, 26}, Σ = 44 contained factor-2 error (used √3/Im instead of √3/(2·Im) for BV[2,3]). Corrected S140. The coincidence "Σ = 44 = Σn" was spurious.

Deps: Q.3, C.2.


---


# S. CIPHER OPERATOR AND REPRESENTATION THEORY (DFT S125–S132)

Source: DFT sessions S125–S131 (consolidated), S132 (V₂ eigenbasis)
Status: 24 [THM], ~200 assertions verified, 28 dead directions
Dependencies: O.1 (monodromy SSoT), I.6 (Cayley Laplacian), F.7 (ε-η bits)
Reference: DFT_consolidated_S125_S131.md for full proofs and tables


## [THM-arith] S.1: Reciprocal Cusp Theorem (34th path)
Source: S125 (DFT §8)
Status: [THM-arith]
Verified: Python (6 two-prime squarefree levels)

### Statement

The ε indicator ε(w) = δ(gcd(w,d₂)=1), interpolated as a cubic on Div(N), has a third root at r = 1/d₂ iff d₂ = d₁+1, i.e. **(d₁,d₂) = (2,3)**.

Explicit: ε(w) = (w−d₂)(d₂w−1)(w−N)/[d₁²(N−1)]. Third root r = 1/d₂ requires d₂²−1 = (d₂−1)(d₂+1) divisible in a way forcing d₂ = d₁+1.

Control: η root s = N+1 = L is universal for all N = d₁d₂ (NOT a path). Only ε gives uniqueness.

**34th path.** Cluster 2 (ramification/j-geometry: shares ν₂=ν₃=0 filter).


## [THM-comb/arith] S.2: Cipher Operator C_sym
Source: S128 (DFT §3)
Status: [THM-comb/arith]
Dependencies: O.1 (monodromy)
Verified: Python (all assertions)

### Definition

The σ∞-conjugacy class of type (6,3,2,1) in Mon has 12 elements, each fixing exactly one particle. The **cipher operator** is:

C_n = Σₑ n(e) · P_{σ∞ᵉ}

where σ∞ᵉ = h·σ∞·h⁻¹ fixes particle e, and P_g is the permutation matrix.

Mon has two conjugacy classes of type (6,3,2,1). The **symmetric cipher** C_sym = (C⁺ + C⁻)/2 uses both.

### Properties [ALL VERIFIED]

- diag(C_sym) = n (12/12)
- C_sym = C_symᵀ (real symmetric)
- All row/column sums = 44 = Σn = d₁²·dim M₁₀
- 2·C_sym has integer entries, all LD monomials

### Boson block [THM-arith]

C_sym|_{W,H} = [[N, d₁²], [d₁², N]] = [[6, 4], [4, 6]]

Eigenvalues: **{d₁, |B₁|} = {2, 10}**. Both LD monomials.


## [THM-comb/arith] S.3: σ₁-Block Structure
Source: S129 (DFT §4)
Status: [THM-comb/arith]
Verified: Python (all block eigenvalues)

### Four σ₁-paired triples

| Block | Particles | Description |
|:-----:|:---------:|:-----------:|
| A | {u, d, μ} | σ₁(BV₁) |
| B | {b, t, e} | BV₁ (index BV) |
| C'| {W, H, p} | Fix(σ∞²) |
| D | {c, s, τ} | σ₁(Fix(σ∞²)) |

σ₁ swaps A↔B and C'↔D.

### Block eigenvalues

| Block | Eigenvalues | All LD? |
|:-----:|:-----------:|:-------:|
| A={u,d,μ} | **{N−1, ±d₁} = {5, ±2}** | ✓ |
| B={b,t,e} | {index, ±√39} = {12, ±6.245} | ½ |
| C'={W,H,p} | **{d₁⁴, ±d₁} = {16, ±2}** | ✓ |
| D={c,s,τ} | **{dim M₁₀, ±1} = {11, ±1}** | ✓ |

**10/12 block eigenvalues are LD monomials.** Only ±√39 irrational (39 = d₂·det M_lep = d₂·13).

### Off-diagonal blocks [THM-arith]

All off-diagonal blocks of 2·C_sym are circulant with LD entries. B–D block is entirely **uniform = L** — cipher cannot distinguish individual particles across these two triples.


## [THM-arith] S.4: Key Trace Identities
Source: S129–S130 (DFT §5)
Status: [THM-arith]
Verified: Python (k = 0..6)

### Statement

| Identity | Value | LD form |
|:--------:|:-----:|:-------:|
| Tr(L·C_n) | −11 | **−dim M₁₀ = −(L+d₁²)** |
| Tr(L³·C_n) | −252 | −d₁²d₂²L |
| Tr(σ₀·C_n) | 46 | Σℓ |
| Tr(σ₁·C_n) | 51 | Σn + L |
| Tr(L·C_ℓ) | −5 | −(N−1) |

### Derivation of Tr(L·C_n) = −dim M₁₀

Tr(L·C_n) = 3·Σn − Tr(A·C_n) = 3·44 − Tr((σ₁+σ₀+σ₀⁻¹)·C_n) = 132 − (51+46+46) = −11.

The modular form dimension dim M₁₀ = 11 has representation-theoretic origin (see S.7).

### Trace integrality [THM-arith]

Tr(Lᵏ · C_n,sym) ∈ ℤ for all k ≥ 0. Verified k = 0..6.


## [THM-arith] S.5: Projector Traces (Spectral Cipher Values)
Source: S130 (DFT §6)
Status: [THM-arith]
Verified: Python

### Statement

c_λ(f) = Tr(P_λ · C_f,sym), where P_λ = projector onto ker(L−λI):

| λ | mult | c_n | c_ℓ |
|:-:|:----:|:---:|:---:|
| 0 | 1 | 44 | 46 |
| 1 | 1 | **d₂ = 3** | 1 |
| d₁² = 4 | 1 | **−d₁³ = −8** | d₁ = 2 |
| d₂ = 3 | 2 | d₂³/(N−1) = 27/5 | 1 |
| N−1 = 5 | 3 | −d₁/(N−1) = −2/5 | −d₁² = −4 |
| (5±√5)/2 | 1 each | −4/5 ∓ (11/10)√5 | **9/2** (degenerate) |
| (5±√21)/2 | 1 each | 4/5 ± (31/70)√21 | −9/2 ± (1/7)√21 |

Key features: all c_n at integer λ are LD monomials over ℤ[1/(N−1)]. All c_ℓ at integer λ are powers of d₁. The ℓ-cipher is **blind to √5 splitting**: c_ℓ = d₂²/d₁ = 9/2 at both φ-eigenvalues.

### Pairing theorem [THM-arith]

Eigenvalue pairs have LD-monomial sum: {1,d₁²} → Σc_n = −(N−1); {d₂,N−1} → Σc_n = N−1. Perfect anti-symmetry between pairs.


## [THM-comb/arith] S.6: Irrep Decomposition
Source: S131 (DFT §7.1–7.2)
Status: [THM-comb/arith]
Verified: Python

### Statement

V_perm = V₁ ⊕ V₂ ⊕ V₃ ⊕ V₆, dims **{1, 2, 3, 6} = Div(N)**.

Each irrep has multiplicity 1. Image dim = 1+4+9+36 = **50**. Commutant dim = **4** = ⟨χ_perm, χ_perm⟩.

L-eigenvalue distribution: V₁: {0}. V₂: {d₂, N−1}. V₃: {1, d₁², N−1}. V₆: {(5±√21)/2, (5±√5)/2, d₂, N−1}.

### Algebraic completeness [THM]

**L and C_sym generate the full 50-dim image of ℂ[Mon].** Neither alone suffices (dim ℂ[L] = 9, dim ℂ[C_sym] = 12). Any Mon-equivariant observable on V_perm is a polynomial in L and C_sym.


## [THM-arith] S.7: V₂ Cipher — Cross-Duality Value 31
Source: S131 (DFT §7.3), S132 (§7.3a)
Status: [THM-arith] (35th path to (d₁,d₂) = (2,3))
Verified: Python

### S.7.1 Determinant [THM-arith]

**det(C_n|_{V₂}) = −(N²−N+1) = −31**

Eigenvalues: ±√31. Cross-duality chain: d₁=2 → d₂=3 → L=7 → **31** → 43 via p²−p+1.

**35th path.** Cluster 7 (automorphic/scattering: shares cross-duality p²−p+1 with path 22).

### S.7.2 V₂ Cipher Matrix in L-Eigenbasis [THM-arith, S132]

C_n|_{V₂} = (L/d₁)·[[1, (N−1)√d₂/L], [(N−1)√d₂/L, −1]]
           = [[7/2, 5√3/2], [5√3/2, −7/2]]

- Trace = 0. det = −31 = −Φ₆(N). Eigenvalues: ±√31.
- tan(2θ) = (N−1)√d₂/L = 5√3/7.
- sin²(2θ) = d₂(N−1)²/(d₁²·31) = 75/124.
- cos²(2θ) = L²/(d₁²·31) = 49/124.
- Level repulsion: bare gap d₁ → dressed gap 2√31 (cross-duality).
- All entries = LD monomials × √d₂.

### S.7.3 V₂ Trace Closed Form [THM-arith]

Tr(Lᵏ · C_n)|_{V₂} = (L/d₁)(d₂ᵏ − (N−1)ᵏ) for all k ≥ 0.

Ratio: Tr(Lᵏ·C_n)|_{V₂} / Tr(Lᵏ·C_ℓ)|_{V₂} = −L for all k ≥ 1.

### S.7.4 Irrep Trace Decomposition of dim M₁₀ [THM-arith]

Tr(L·C_n) = −dim M₁₀ decomposes across irreps:

| Irrep | Tr(L·C_n)|_{V_d} |
|:-----:|:-----------------:|
| V₁ | 0 |
| V₂ | **−L = −7** |
| V₃ | **−d₁² = −4** |
| V₆ | 0 |

The d₁-irrep (V₃) and d₂-irrep (V₂) contribute the two summands of dim M₁₀ = L + d₁² = 7 + 4.

### S.7.5 Tr(C²) Irrep Decomposition [THM-arith]

| Irrep | Tr(C_n²) | Factorization |
|:-----:|:--------:|:-------------:|
| V₁ | 1936 | (Σn)² |
| V₂ | **62** | **d₁·31** |
| V₃ | **124** | **d₁²·31** |
| V₆ | 161 | L·23 |

V₂ and V₃: d₁^{dim−1}·31 pattern. The cross-duality value 31 controls cipher's quadratic invariant in the small irreps.


## [THM-arith] S.8: V₃ Cipher Structure
Source: S131 (DFT §7.4)
Status: [THM-arith]
Verified: Python

### Characteristic polynomial

char(C_n|_{V₃}) = x³ − d₁(N²−N+1)·x + d₁²d₂(N−1) = x³ − 62x + 60

**[ERRATA: S131 session log wrote −60 for constant term. Correct sign is +60.]**

### V₃ cipher values in L-eigenbasis

| λ | c^{V₃}(n) | c^{V₃}(ℓ) |
|:-:|:----------:|:----------:|
| 1 | d₂ = 3 | 1 |
| d₁²=4 | −d₁³ = −8 | d₁ = 2 |
| N−1=5 | N−1 = 5 | −d₂ = −3 |

Off-diagonal² sum (upper triangle) = **13 = d₁²+d₂² = det(M_lep)**.


## [THM-arith] S.9: Φ and Δ Face Sum Rules
Source: S126–S127 (DFT §2)
Status: [THM-arith]
Verified: Python (all sums)

### Δ face sums (Δ = Φ − L²·ℓ, integer convention)

| Face | ΣΔ | LD factorization |
|:----:|:---:|:----------------:|
| Quarks | −320 | −d₁⁶(N−1) |
| Leptons | −729 | −d₂⁶ |
| Bosons | +89 | prime (forced) |
| Anchor | +192 | d₁⁶d₂ |
| **All** | **−768** | **−d₁⁸d₂** |

### Φ face sums

ΣΦ_L = 300 = d₁²d₂(N−1)². ΣΦ_B = 432 = d₁⁴d₂³ = BULK·π. ΣΦ_A = 192 = d₁⁶d₂.

### Up-type Δ factoring [THM-arith]

All up-type quark Δ values factor d₂ uniformly: Δ(t)=−d₂L², Δ(c)=d₂²(N−1), Δ(u)=−d₂(L²−d₁).

### Structural lesson

Δ polynomial coefficients are NOT LD monomials (D13 dead). Composition Φ∘n = n³(L−n) creates LD-irreducible primes {103, 151, 167}. This is structural: Φ is cubic, n is degree 2 in ε-η bits → degree 6 composite.


## S.10: Structural Barrier for Gap 3 (28 DFT dead directions)
Source: S125–S131 (DFT §9)
Status: Confirmed barrier

28 independent approaches within the monodromy/cipher framework failed to produce α/(2π). Key lessons:

1. **No operator has eigenvalues = n.** The cipher encodes n on the DIAGONAL, not in the spectrum. Monodromy distinguishes particles by conjugacy (which particle is FIXED), not by eigenvalue.

2. **Monodromy operator diagonals cannot see face-internal position.** σ∞-dependent part of particle identity is invisible to products of σ₀, σ₁.

3. **The gap is in the COUPLING, not the structure.** H = L + g·C_n is well-motivated but no LD value of g gives clean structure.

4. **L and C_sym are algebraically complete** (50-dim image), yet α/(2π) does not emerge from any polynomial/trace/spectral combination. The coupling must originate from OUTSIDE the dessin combinatorics — likely from the continuous geometry (action principle, QTC, or spectral theory of Γ₀(6)\ℍ).

Full list of 28 dead directions: see DFT_consolidated §9 (D1–D28).


## [THM-arith] S.11: Hadamard Fusion Rules on V_perm (S151, verified S152)
Source: S151, verified S152
Status: [THM-arith] (exact rational, Fraction arithmetic, zero roundoff)
Dependencies: S.6 (irrep decomposition), O.1 (monodromy)

### Statement

Pointwise (Hadamard) product on V_perm = V₁⊕V₂⊕V₃⊕V₆. For basis vectors u ∈ V_ρ, v ∈ V_σ, the Hadamard product w_j = u_j·v_j is projected onto each V_τ. The rank of the resulting space gives the fusion content.

### Fusion table (rank of V_ρ ⊙ V_σ → V_τ)

| ρ⊙σ   | →V₁ | →V₂ | →V₃ | →V₆ |
|--------|-----|-----|-----|-----|
| V₁⊙V₁ |  1  |  0  |  0  |  0  |
| V₁⊙V₂ |  0  |  2  |  0  |  0  |
| V₁⊙V₃ |  0  |  0  |  3  |  0  |
| V₁⊙V₆ |  0  |  0  |  0  |  6  |
| V₂⊙V₂ |  1  |  2  |  0  |  0  |
| V₂⊙V₃ |  0  |  0  |  0  |  6  |
| V₂⊙V₆ |  0  |  0  |  3  |  6  |
| V₃⊙V₃ |  1  |  0  |  3  |  0  |
| V₃⊙V₆ |  0  |  2  |  0  |  6  |
| V₆⊙V₆ |  1  |  2  |  3  |  6  |

### Key properties

**(a)** V₁ is the identity: V₁⊙V_ρ = V_ρ.

**(b)** Parity rule: V₂⊙V₃ has NO V₂ and NO V₃ — only V₆.

**(c)** V₆⊙V₆ fills ALL irreps (rank = full dim for each).

**(d)** V₂ column: V₂ appears in V₁⊙V₂, V₂⊙V₂, V₃⊙V₆, V₆⊙V₆. Absent from V₂⊙V₃, V₂⊙V₆, V₃⊙V₃.

**(e)** Critical for cusp forms: V₆⊙V₁ → no V₂, V₆⊙V₂ → no V₂, V₆⊙V₃ → rank 2 in V₂, V₆⊙V₆ → rank 2 in V₂.

### Langlands partition consistency

Fusion table respects the partition into Eisenstein sector V₁⊕V₂ (rational L-eigenvalues) and cuspidal sector V₃⊕V₆ (V₃ rational, V₆ irrational). V₂⊙V₃ = only V₆ shows strict sector crossing under Hadamard product.

Dependencies: S.6, O.1.


## [THM-arith] S.12: Rank Barrier for Modular Form → δK (S153)
Source: S153
Status: [THM-arith]
Dependencies: G.0a (rank of Φ−Lℓ), notation (dim M_k = k+1)

### Statement

Φ−Lℓ takes 11 distinct values on 12 particles (sole collision: u = d, both n=1, ℓ=3).
Therefore rank(Φ−Lℓ) = 11 as element of ℝ¹².

dim M_k(Γ₀(6)) = k+1 for even k ≥ 2. A linear combination of k+1 modular forms
evaluated at the 12 coset points of P¹(ℤ/6ℤ) produces a vector in ℝ¹² of rank ≤ k+1.

**Corollary:** No linear combination of weight-k modular forms on Γ₀(6), evaluated
at the 12 particle coset points, can reproduce Φ−Lℓ for k < 10.

The first weight where rank allows a solution is **k = 10**, where dim M₁₀ = 11.

### Significance

dim M₁₀ = 11 is already a fundamental LD invariant:
- Tr(L·C_n) = −dim M₁₀ = −11 (S.7.4)
- S.7.4 irrep decomposition: V₂ contributes −L = −7, V₃ contributes −d₁² = −4
- W.2: ΣR = 224 = d₁⁵L, with Tr(55·L_eff,nonzero) = 224

The coincidence rank(Φ−Lℓ) = dim M₁₀ may be structural (the formula "knows" about
weight-10 forms) or coincidental (both = 11 for independent reasons). Status: [OPEN].

### Dead directions killed by this barrier

X.34 (weight-2, r=0.52), X.39 (weight-2 rank), X.43 (Eisenstein g_k, r=0.52),
S141 scan (3936 tests), S153 (weight-4, r=0.65) — all structurally precluded.


---

# T. NCG LAGRANGIAN AND BURNSIDE-MONODROMY OPERATOR (S134–S135)

## [DEF] T.1 — NCG bridge parameter Ω (S134)

Ω ≡ BULK/index = (432/π)/12 = **36/π ≈ 11.459**

Equivalently: Ω = index · E₂(i) = 12 · (3/π), using E₂(i) = 3/π (Hurwitz 1883).

Self-dual parametrization of H.1:
- BULK = Ω · index = (36/π) · 12 = 432/π
- IR_coeff = 1/Ω = π/36
- Product: BULK_coeff × IR_coeff = index = 12

In NCG language: f₀ = Ω plays the role of the cutoff-function moment in Connes-Chamseddine spectral action, determining the gauge coupling via α⁻¹ = (f₀/(2π²)) · c where c = 2π² · (BULK·cos² − IR)/Ω ≈ 2π²·index.

**Status: [DEF].** S134 originally marked [THM], but S135 correctly noted this is a repackaging of H.1 BULK = 432/π, not an independent result. The identification f₀ = Ω gives a clean NCG interpretation of the LD coupling constant, but adds no predictive content beyond H.1.

Deps: H.1. Verified: numerically to 10⁻⁸.

## [OBS] T.2 — a₄ = index · dim M₁₀ = 132 (S134)

Tr(D_F⁴) = 2 · Σ σ²ᵢ = 2(1² + 2² + 5² + 6²) = 2 · 66 = **132 = index · (|B₁| + 1) = index · dim M₁₀**

where σ² = {N, N−1, d₁, 1} = {6, 5, 2, 1} are the BB^T eigenvalues (D.3).

Alternative form: 2(1 + d₁² + (N−1)² + N²) = N · ∏(1 + 1/p) · (2(d₁ + d₂) + 1).

**Uniqueness claim: CIRCULAR.** S134 claimed unique for (2,3) among coprime pairs, but σ² = {N, N−1, d₁, 1} is proven only for X₀(6) (D.3). The eigenvalue formula depends on the specific dessin structure (anchor lemma D.1), which has not been generalized. Cannot substitute (d₁, d₂) → (d₁', d₂') without re-deriving σ² for each new dessin.

**Status: [OBS].** Numerically correct identity linking index, dim M₁₀, and BB^T spectrum. Not an independent path to (2,3).

Deps: D.3.

## [DER] T.3 — NCG Lagrangian structure (S134)

S_LD[Ψ, A, H] = S_gravity + S_gauge + S_Higgs + S_Yukawa + S_δK

| Term | Formula | What determines | Status |
|------|---------|-----------------|--------|
| S_gravity | (f₂Λ²a₀)/(24π²) ∫R√g | Newton G | [DER] via H.3 |
| S_gauge | (Ω/(2π²))·c · ¼∫F² | α⁻¹ = 137.036 | [DER] ≡ H.1 |
| S_Higgs | f₀·Tr(X²) − f₂Λ²·Tr(X) | m_H | [OBS/~] |
| S_Yukawa | ⟨Ψ, (D_F+Φ)Ψ⟩ | Yukawa couplings | [OBS/~] via MCT |
| S_δK | (α/2π)⟨Ψ, [Φ−Lℓ]Ψ⟩ | δK corrections | **POSTULATED** |

Determined parameters: Ω = 36/π [DEF], f₂Λ² = 3π M_Pl²/(2|B₁|) [DER, EH matching], D_F = [[0,B],[B^T,0]] [THM-comb], A_F = ℂ⊕ℍ⊕M₃(ℂ) [L0 postulate].

Higgs mass: standard NCG normalization gives m_H = 93 GeV (−25%); LD tree ratio K_H/K_W = 3/2 gives m_H = 121 GeV (−3.7%). Neither is exact.

**Key structural finding (S134):** δK = (α/2π)[Φ−Lℓ] does NOT follow from variation of S_LD.

Reason: spectral action yields traces (a₂, a₄ = summed invariants), not per-particle diagonal elements. Φ−Lℓ requires all three monodromy generators σ₀, σ₁, σ∞ simultaneously (through MCT and the cubic Φ(n)), while spectral functionals (heat kernel, resolvent, determinant) are functions of L alone.

Deps: H.1, H.3, D.3, F.1.

## [THM-comb] T.4 — Commutative diagonal rank and W≡H degeneracy (S135)

**(a)** The full non-commutative algebra ⟨L, σ∞⟩ has diagonal rank **12** (full resolution of all particles).
S134 incorrectly claimed rank 11; error caused by restriction to commutative sub-algebra {L^a · σ∞^b}.

**(b)** The commutative algebra {L^a · σ∞^b} has diagonal rank **11**. The missing direction is **exactly δ_H − δ_W**.

**Proof:** L^k(W,W) = L^k(H,H) for all k = 0, 1, ..., 7 (verified numerically). This is an exact local symmetry: the neighborhoods of W and H in the Cayley graph are isomorphic under the permutation that swaps their σ₁-partners and σ₀-successors. Since σ∞ acts identically on W and H (both in 2-face), no power of σ∞ distinguishes them either. Products L^a·σ∞^b therefore cannot separate W from H.

**(c) Minimal splitter:** L · σ∞² · L, depth 4 in word metric. Δ(W−H) = −1 (exact integer). Only 2 words out of 81 at depth 4 split W and H. Depth < 4 does not split.

**Physical content:** n(W) = n(H) = 6 (same); ℓ(W) = 6, ℓ(H) = 1 (different by N−1 = 5). The splitting bit is η₁ = η(Fσ₁) from F.7e: σ₁(W) = s (6-face, η = 1), σ₁(H) = τ (3-face, η = 0).

Verified: numerical computation, errors < 10⁻¹⁴. Deps: I.6, O.1.

## [THM] T.5 — ⟨L, σ∞⟩ = ℂ[Mon], dim = 50 (S135)

The matrix algebra generated by L (Cayley graph Laplacian) and σ∞ (face permutation) equals the full group algebra ℂ[Mon(X₀(6))].

dim ⟨L, σ∞⟩ = 50 = 1² + 2² + 3² + 6² (Artin-Wedderburn decomposition).

Consequence: any operator in ℂ[Mon] — including M_opt (T.7) — is expressible as a polynomial in L and σ∞.

Verified: BFS word products to depth 8, rank = 50 (SVD). All 72 permutation matrices project onto word-span with residual < 10⁻¹¹. Consistent with S.6 (irrep decomposition).

Deps: I.6, O.1, S.6.

## [THM-arith] T.6 — DDT eigenvalues = LD monomials (S135)

The Burnside kernel DDT(i,j) = |Stab(i) ∩ Stab(j)| (where stabilizers are in Mon(X₀(6))) has eigenvalues:

| Irrep | dim | λ(DDT) | LD monomial |
|-------|-----|--------|-------------|
| V₁ | 1 | **24** | d₁²N |
| V₂ | 2 | **6** | N |
| V₃ | 3 | **8** | d₁³ |
| V₆ | 6 | **2** | d₁ |

Multiplicities = dim V_k = Div(N) = {1, 2, 3, 6}. Tr(DDT) = |Mon| = 72.

DDT⁻¹ eigenvalues: 1/(d₁²N), 1/N, 1/d₁³, 1/d₁. The quark irrep V₆ is amplified by factor d₁²N/d₁ = index = 12 relative to V₁.

Verified: exact diagonalization, all eigenvalues integer. Deps: O.1.

## [THM-arith] T.7 — Burnside weight vector w (S135, corrected S138)

w = DDT⁻¹ · (Φ − Lℓ) ∈ (1/56)ℤ¹²

Universal denominator: **56 = d₁³ · L = 8 · 7**.

56 · w values:

| u | d | c | s | t | b | e | μ | τ | W | H | p |
|---|---|---|---|---|---|---|---|---|---|---|---|
| +95 | −291 | +81 | +131 | −59 | +555 | −755 | −193 | −229 | −451 | +143 | +717 |

Σ(56 · w) = **−256 = −d₁⁸**. (S135 originally claimed −312; corrected in S138, verified analytically: 56 · Σtarget / 24 = 56 · (−768/7) / 24 = −256.)

Note: the individual numerators {95, 291, ...} are NOT LD monomials (e.g., 95 = 5 · 19).

Deps: T.6, F.1 (target = Φ − Lℓ).

## [THM] T.8 — M_opt coefficient formula (S135)

M_opt = Σ_{g ∈ Mon} a(g) · P_g is the unique operator in ℂ[Mon] with:
- diag(M_opt) = Φ − Lℓ (exact, error 10⁻¹⁵)
- minimal ||a||² (equivalently, minimal ||M||²_F over the Gram structure)

Coefficient formula: **a(g) = Σ_{k ∈ Fix(g)} w(k)**, where w = DDT⁻¹ · target.

Properties:
- M_opt symmetric (= Hermitian): ||M − M^T||_F < 10⁻¹⁴
- Tr(M_opt) = −768/7 = Σ(Φ − Lℓ)
- 7 · M_opt has entries in ℚ with denominators ∈ {1, 2, 4} = {1, d₁, d₁²}
- 36 of 72 coefficients a(g) = 0 (conjugacy classes with cycle type (2⁶), (3⁴), (6²) vanish)
- M_opt ∈ ⟨L, σ∞⟩ = ℂ[Mon] (by T.5, tautologically)

Notable diagonal elements (× 7): p = 192 = d₁⁶d₂, e = −343 = −L³, t = −147 = −d₂L², W = −78 = −N · 13.

Verified: 72/72 coefficients via formula, full 12×12 matrix reconstruction. Deps: T.6, T.7.

## [OPEN] T.9 — Physical principle for M_opt (S135)

M_opt is the minimum-norm element of ℂ[Mon] with prescribed diagonal. This is equivalent to minimizing ||M||²_F subject to diag(M) = target (over the Gram structure induced by Mon).

**Tested and rejected:**
- Projection of diag(target) onto ℂ[Mon] in Frobenius norm: does NOT preserve diagonal.
- Minimum commutator energy Σ||[M, s]||²: found solutions with same diagonal but lower energy.
- DDT as polynomial of L: error 36%. Not expressible via {I, L, L², face projectors} (error 58%).
- M_opt² = f(M_opt): error 67%. No simple algebraic relation.

**Open:** Why should nature select the minimum-norm representative? Maximum entropy / Jaynes principle? Lattice gauge theory ground state?

---

# U. BELYI CONNECTION (S137)

## [THM-arith] U.1 — Regularized connection values at cusps (S137)

The 1-form ω = d(ln j)/dt₆ = 3P₄'/P₄ − 6/t − 3/(t+9) − 2/(t+8) has simple poles at all cusps and BV.

Divisor of ω on ℙ¹: BV = 4 simple poles (residue +d₂ = +3), cusps = 4 simple poles (residues −w). Σ residues = 0. deg(ω) = −2 (1-form on ℙ¹).

Regularized value at cusp t_c ≡ finite part of ω after subtracting the principal pole −w/(t − t_c):

**reg(ω) = 3P₄'/P₄|_{t=t_c} + Σ_{other cusps} w_k/(t_c − t_k)**

| Cusp | w | 3P₄'/P₄ | cross-cusp | **reg(ω)** | LD monomial |
|------|---|----------|------------|------------|-------------|
| t=0 (quarks) | 6 | 1 | −7/12 | **5/12** | (N−1)/index |
| t=−9 (leptons) | 3 | −4 | 8/3 | **−4/3** | −d₁²/d₂ |
| t=−8 (bosons) | 2 | 3 | −9/4 | **3/4** | d₂/d₁² |

Note: (N−1)/index = (d₁+d₂)/index = 5/12 (coincidence N−1 = d₁+d₂ specific to (2,3)).

Verified: exact rational arithmetic via P₄ = (t+12)(t³+252t²+3888t+15552). Uses Catalan separation: P₄(−9) = 729 = d₂⁶, P₄(−8) = 256 = d₁⁸.

Deps: K.1 (Hauptmodul).

### Mixing tangent connection (X.102b, S205) [THM-arith]
**reg(ω)_boson = 3/4 = tan θ₁₂ · tan θ₂₃** (product of PMNS solar and atmospheric mixing tangents).
tan θ₁₂ · tan θ₂₃ / reg(ω)_quark = (3/4)/(5/12) = **9/5 = λ₂(L_eff)** (second L_eff eigenvalue, I.12).

## [THM-arith] U.2 — Sum rules (S137, extended S138)

| k | Σ w^k · reg(ω) | LD interpretation |
|---|-----------------|-------------------|
| **−1** | **0** | **(new, S138)** |
| 0 | −1/6 | −1/N |
| **1** | **0** | **0** |
| 2 | 6 | N |
| 3 | 60 | N · |B₁| |

Two zeros at k = ±1 suggest w ↔ 1/w duality symmetry.

Verified: exact computation with Fraction arithmetic.

## [THM-arith] U.3 — Ramification duality (S137)

**reg(leptons) · reg(bosons) = (−d₁²/d₂) · (d₂/d₁²) = −1**

This holds for ALL (d₁, d₂), not just (2,3). Geometrically: σ₁ connects the 3-face (leptons) and 2-face (bosons) via pairs (τ,H), (e,d), (W,s).

Deps: U.1.

## [DER] U.4 — Genus 0 forces additive δK (S137)

On ℙ¹, any meromorphic 1-form decomposes into partial fractions uniquely. For ω = d(ln j)/dt₆, this gives:

ω = Σ_{cusps} (−w_c)/(t − t_c) + Σ_{BV} (+d₂)/(t − t_{BV}) + (regular at ∞)

Genus 0 → Hauptmodul unique → connection ω unique → partial-fraction decomposition unique → additive structure of δK = Φ − Lℓ **forced**.

At genus > 0: a 2g-dimensional space of holomorphic differentials introduces free parameters, destroying uniqueness.

This upgrades the "additive form" of δK from [MOT, discrete selection] to [DER from genus 0].

Deps: A.1 (genus 0), K.1 (Hauptmodul).

## [THM-arith] U.5 — Face sums of Φ − Lℓ (S137, verified S138)

| Face | w | particles | Σn | LD | Σℓ | LD | 7·Σ(Φ−Lℓ) | LD |
|------|---|-----------|----|----|----|----|-----------|-----|
| quarks | 6 | c,u,b,s,d,t | 21 | d₂L | 18 | Nd₂ | **−320** | −d₁⁶(N−1) |
| leptons | 3 | e,τ,μ | 7 | L | 21 | d₂L | **−729** | −d₂⁶ |
| bosons | 2 | W,H | 12 | index | 7 | L | **89** | **prime** |
| anchor | 1 | p | 4 | d₁² | 0 | 0 | **192** | d₁⁶d₂ |
| **Total** | | | 44 | d₁²·dim M₁₀ | 46 | | **−768** | −d₁⁸d₂ |

Note: 89 is prime, so "all face sums = LD monomials" is **FALSE** for Σ(Φ−Lℓ) at bosons.

Verified: exact computation. Deps: F.3, F.7e, G.0.

## [STRUCTURAL] U.6 — Two logarithmic connections (S137)

The LD coupling structure involves two logarithmic derivatives of modular objects:
- d(ln j)/dt₆ → connection on dessin → Φ − Lℓ (per-particle operator), partial fractions forced by genus 0
- d(ln Δ)/dτ |_{τ=i} = E₂(i) = 3/π → connection on modular line bundle → α (coupling constant)

Product: δK = α/(2π) · (Φ − Lℓ) is the product of these two aspects.

Gap 3 reformulated: the question is not "why δK?" but "why logarithmic connection?" Answer: ln is the unique multiplicative → additive map, and on genus-0 curves, partial-fraction decomposition is unique.

---

# V. UST FRAMEWORK — CKM AND PMNS FROM SPANNING TREES (S138)

## [THM-comb] V.1 — Edge inclusion probabilities (S138)

For uniform spanning trees (UST) of the bipartite dessin of X₀(6) (4 BV + 6 WV, 12 edges, 10 vertices):

**Kirchhoff number = 40 spanning trees** (consistent with D.4).

| Edge type | Edges | P(e ∈ UST) | 40·P | LD monomial |
|-----------|-------|------------|------|-------------|
| bridge | {u, t} | **1** | 40 | Kirchhoff |
| multi | {c, p} | **1/2** | 20 | K/d₁ |
| interior | {b, μ, d, e} | **4/5** | 32 | d₁²K/(N−1) |
| boundary | {s, W, τ, H} | **7/10** | 28 | LK/|B₁| |

All 4 values are LD monomials (rational, only primes 2, 3, 5, 7 in denominators).

Edge types are determined by bipartite graph structure (bridge = cut-edge, multi = parallel, interior/boundary from E.8 classification).

Verified: explicit enumeration of all 40 spanning trees, edge-by-edge count.

Deps: D.4 (Kirchhoff), E.8 (edge classification), O.1 (monodromy).

## [THM-arith] V.2 — Palindromic difference structure (S138)

| Transition | ΔP | LD monomial |
|------------|-----|-------------|
| P(bridge) − P(interior) | **1/5** | 1/(N−1) |
| P(interior) − P(boundary) | **1/10** | 1/|B₁| |
| P(boundary) − P(multi) | **1/5** | 1/(N−1) |

Palindrome: d₁ : 1 : d₁ (scaling by d₁ gives 2 : 1 : 2).

Deps: V.1.

## [THM-comb] V.3 — Boundary triple probability (S138)

**P(boundary triple ∈ UST) = d₂²/K = 9/40**, uniform over all 8 triples.

The 8 boundary triples are {c ⊕ p} × {s ⊕ W} × {τ ⊕ H} from E.8. Verified: explicit count in all 40 spanning trees, 9 trees per triple, identical for all 8.

Deps: V.1, E.8.

## [THM-comb / DER] V.4 — CKM Wolfenstein from UST (S138)

Two fundamental UST quantities:
- **P_triple** = P(boundary triple ∈ UST) = d₂²/K = **9/40**
- **ΔP** = P(interior) − P(boundary) = d₁²/K = **1/10**

| CKM parameter | UST formula | LD value | Pull (PDG 2024) |
|---------------|-------------|----------|-----------------|
| λ | P_triple | 9/40 = 0.22500 | **−0.04σ** |
| A | √(P_triple/(ΔP+P_triple)) | 3/√13 = 0.83205 | **+0.63σ** |
| γ | arctan(P_triple/ΔP) | arctan(9/4) = 66.04° | **−1.25σ** |
| R_b | √(N/K) | √(3/20) = 0.38730 | **+0.13σ** |
| J (Jarlskog) | A²λ⁶η̄(1−λ²/2) | 3.099 × 10⁻⁵ | **−0.15σ** |

**Identity:** R_b² = λ · d₁/d₂ → 3 independent predictions, 0 fit parameters. **dof = 3.**

**χ² = 1.97, χ²/dof = 0.66** (excellent fit). Max pull: γ at 1.25σ.

Experimental values (PDG 2024): λ = 0.22497 ± 0.00070, A = 0.839 ± 0.011. γ = (62.8 ± 2.6)° (LHCb combination, per companion). R_b from ρ̄, η̄.

**Status upgrade: CKM [OBS]×4 → [DER] with 1 physical identification** (UST edge probability = tree-level propagator, Step 3 below).

Deps: V.1, V.3, E.2–E.6.

## [DER] V.5 — Physical bridge: transfer current theorem (S138)

The derivation chain has 3 steps:

**Step 1:** Dessin = lattice (≡ L0 content of LD model).

**Step 2:** Gaussian free field on lattice → tree-level propagator = effective resistance = P(edge ∈ UST). This is the transfer current theorem (Kirchhoff 1847, Burton–Pemantle 1993): for any edge e in a graph G, the probability that e belongs to a uniformly random spanning tree equals the effective resistance between its endpoints.

**Step 3:** CKM = flavor current = joint probability in UST ensemble. This is the one physical identification: Wolfenstein parameters correspond to edge-inclusion probabilities of the bipartite dessin viewed as a lattice gauge theory at tree level.

No new postulate beyond L0 is needed. The content of Step 3 is that "dessin = lattice" (already in L0) applied to the free-field sector yields CKM through spanning-tree combinatorics.

## [THM-arith] V.6 — CKM-PMNS complementarity (S138)

From the SAME two UST quantities:
- **CKM:** A² = P_triple/(ΔP + P_triple) = **9/13**
- **PMNS:** sin²θ₁₂ = ΔP/(ΔP + P_triple) = **4/13**

**Exact identities:**
- A² + sin²θ₁₂ = 9/13 + 4/13 = **1** (tautological given the fraction form, but now both sides are derived)
- tan γ(CKM) · tan²θ₁₂(PMNS) = (9/4) · (4/9) = **1**

sin²θ₁₂ = 4/13 pull: JUNO +0.17σ, NuFIT 6.0 IC19 (NO): exp = 0.307 ± 0.012, pull = **−0.06σ**.

**Structural meaning:** CKM and PMNS solar angle share the same geometric origin — the ratio d₁²/d₂² = 4/9 of contributions to the Kirchhoff polynomial.

Deps: V.4.

## [THM-comb] V.7 — μ-τ breaking from UST (S138)

The three leptons have σ₁-partners:
- σ₁(e) = d (interior type, P = 4/5)
- σ₁(μ) = b (interior type, P = 4/5)
- **σ₁(τ) = H** (boundary type, P = 7/10)

τ is the **unique** lepton whose σ₁-partner lies in the boundary class. This geometric asymmetry is the origin of μ-τ symmetry breaking.

Combined with UST: ΔP = P(interior) − P(boundary) = 1/10 gives the strength of this breaking.

Deps: O.1 (σ₁ map), V.1 (edge types).


## [THM-comb] V.8 — Joint UST probabilities and transfer current (S149)
Source: S149, verified S149-review (independent Fraction recomputation, 40 trees enumerated)
Status: [THM-comb] (exact enumeration), [THM-arith] (conditional probabilities, covariance)
Dependencies: V.1 (marginals), D.4 (Kirchhoff = 40), E.8 (boundary choices), O.1 (monodromy)

### V.8.1: Full joint probability matrix [THM-comb]

Joint probabilities P(eᵢ ∈ T ∧ eⱼ ∈ T) for uniform spanning trees. Forced edges u, t: joint with any edge = marginal of partner. Non-trivial 10×10 block:

| Pair type | P(i,j) | Count |
|-----------|:-------:|:-----:|
| multi-edge {c,p} | **0** | 1 |
| interior–interior {b,μ,d,e}×{b,μ,d,e} | **3/5** | 6 |
| interior–boundary | **11/20** | 16 |
| competing far-end {s,W}, {τ,H} | **2/5** | 2 |
| boundary cross-pair (s↔τ, s↔H, etc) | **9/20** | 4 |

All values uniform within type (verified 40/40 trees).

### V.8.2: Conditional probabilities = LD monomials [THM-comb]

Six distinct non-trivial conditional values P(eᵢ | eⱼ):

| Conditional | Value | LD form |
|-------------|:-----:|---------|
| P(c\|p) = P(p\|c) | 0 | multi-edge exclusion |
| P(s\|W) = P(W\|s) = P(τ\|H) = P(H\|τ) | **4/7** | d₁²/L |
| P(b\|μ) = P(μ\|b) = P(b\|d), etc (int–int) | **3/4** | d₂/d₁² |
| P(s\|b), P(W\|μ), etc (bdy\|int) | **11/16** | dim M₁₀/d₁⁴ |
| P(b\|s), P(μ\|W), etc (int\|bdy) | **11/14** | dim M₁₀/(d₁L) |
| P(τ\|s) = P(s\|τ), etc (bdy cross) | **9/14** | d₂²/(d₁L) |

Cross-conditional numerator = dim M₁₀ = 11 for ALL interior↔boundary pairs.
Boundary cross numerator = d₂² = 9 (Residual Tree count, E.8).

Three additional values arise for pairs involving {c,p}: P = 1/2, 7/10, 4/5. These are the marginals themselves (since joint with forced edge = marginal, and joint involving c,p factorizes due to the 0-correlation block).

### V.8.3: Within-pair conditional splits = ramification ratios [THM-arith]

Competing pairs {s,W} and {τ,H}:
- P(W|s) = d₁²/L = 4/7, complement P(W̄|s) = d₂/L = 3/7
- **Ratio d₁² : d₂ = 4 : 3 = e(j = 1728)² : e(j = 0)**

Interior pairs {b,μ}, {d,e}:
- P(μ|b) = d₂/d₁² = 3/4, complement = 1/d₁² = 1/4
- **Ratio d₂ : 1**

Deps: V.8.2, C.2 (ramification indices).

### V.8.4: Transfer current theorem — ΔP palindrome derived [THM-arith]

Burton–Pemantle (1993): for UST as determinantal point process, Cov(𝟙ₑ, 𝟙_f) = −I(e,f)² where I(e,f) is the transfer current.

Five distinct transfer current magnitudes:

| Pair type | −Cov = \|I\|² | \|I\| |
|-----------|:-------------:|:-----:|
| {c,p}↔others | 0 | 0 |
| interior–boundary | 1/100 | 1/\|B₁\| |
| interior–interior; bdy cross | 1/25 | 1/(N−1) |
| competing {s,W}, {τ,H} | 9/100 | d₂/\|B₁\| |
| multi {c,p} | 1/4 | 1/d₁ |

**This derives the V.2 palindrome.** The differences ΔP between UST classes are

ΔP(bridge→interior) = 1/5 = 1/(N−1), ΔP(interior→boundary) = 1/10 = 1/|B₁|

which are exactly the transfer current magnitudes |I| = 1/(N−1) and 1/|B₁|. The palindromic structure d₁ : 1 : d₁ is the transfer current hierarchy.

**Status upgrade:** V.2 [THM-arith, observed] → [THM-arith, derived via transfer current].

### V.8.5: Covariance eigenvalue spectrum [THM-comb/arith]

Eigenvalues of 10×10 covariance matrix Cov(𝟙ₑᵢ, 𝟙ₑⱼ) over the 10 non-forced edges:

| Eigenvalue | Mult | LD monomial |
|:----------:|:----:|:------------|
| 1/2 | 1 | 1/d₁ |
| 3/10 | 2 | d₂/\|B₁\| |
| 1/5 | 4 | 1/(N−1) |
| 2/25 | 1 | d₁/(N−1)² |
| 0 | 2 | — |

(In the full 12×12 matrix, 0 has multiplicity 4 due to forced edges u, t.)

Trace: Tr(Cov) = 99/50. Numerator 99 = d₂² · dim M₁₀. Denominator 50 = d₁ · (N−1)².

Eigenvalue ratios: λ₁/λ₂ = (N−1)/d₂ = 5/3; λ₂/λ₃ = d₂/d₁ = 3/2; λ₃/λ₄ = (N−1)/d₁ = 5/2. All LD monomials.

**Top three eigenvectors = E.8 boundary choices [THM-comb]:**
- λ = 1/2: eigenvector c − p (multi-edge flip)
- λ = 3/10 (×2): eigenvectors s − W and τ − H (competing pair flips)

These are exactly the three binary choices of E.8 boundary layer. The covariance spectrum reproduces the E.8 decomposition spectrally.

The four-fold degenerate eigenspace λ = 1/5 mixes interior {b,μ,d,e} with boundary {s,W,τ,H} components (verified numerically: boundary coefficients up to ±0.41). It does NOT span only the interior register.

The λ = 2/25 eigenvector = (boundary − interior)/√8: uniform +1/√8 on {s,W,τ,H}, uniform −1/√8 on {b,μ,d,e}.

Verified: exact Fraction arithmetic for eigenvalues; numpy eigenvectors consistent to 10⁻¹⁵.

### V.8.6: DPP identity [THM, not LD-specific]

For all 12 edges: Σ_{f≠e} I(e,f)² = P(e)·(1 − P(e)). This is a general property of determinantal point processes (UST = DPP with kernel K² = K). Serves as consistency check.

### V.8.7: δK from UST joint [DEAD #46]

Pearson r(Φ − Lℓ, ΣI²) = 0.60. Within each UST class (e.g. interior: {b,μ,d,e}), all four particles share identical ΣI² = 4/25 but their Φ − Lℓ values differ by factor ~3. UST classes are too coarse to resolve σ∞-position — consistent with S.10 barrier (graph doesn't see within-cycle order).


## [THM-comp] V.9 — Hitting times on Cayley graph (S149)
Source: S149, verified S149-review (Gaussian elimination in Fraction, 12×12)
Status: [THM-comp] (exact linear algebra), [THM-arith] (monomial identifications)
Dependencies: I.6 (Cayley spectrum), D.6–D.7 (φ-zero, golden hierarchy), O.1 (monodromy)

Random walk on Cayley (Schreier) graph of X₀(6) dessin with generators {σ₁, σ₀, σ₀⁻¹}, 3-regular, 12 vertices.

### V.9.1: Hitting time classes from anchor = golden hierarchy [THM-comp]

Mean first passage time h(p → x) from anchor p:

| h(p→x) | LD form | Particles | φ-amplitude (D.7) |
|:-------:|---------|:---------:|:------------------:|
| 0 | — | {p} | 0 (Z_φ) |
| 3 | d₂ | {u} | 0 (Z_φ) |
| 36/5 | ∏w/(N−1) | {c} | 0 (Z_φ) |
| 12 | index | {t} | 0 (Z_φ) |
| 576/25 | d₁⁶d₂²/(N−1)² | {b, e} | 1/(φ√10) |
| 891/25 | d₂⁴·dim M₁₀/(N−1)² | {d, μ} | φ/√10 |
| 1044/25 | — | {s, τ, W, H} | 1/√10 |

**Six distinct hitting time classes reproduce the golden hierarchy of D.6–D.7 exactly:**
- Z_φ = {p, c, u, t}: 4 distinct values (individually resolved)
- |v| = 1/(φ√10): {b, e} (minimal non-zero φ-amplitude)
- |v| = φ/√10: {d, μ} (maximal, golden pair)
- |v| = 1/√10: {s, τ, W, H} (intermediate)

Numerator notes: 576 = 2⁶·3² = d₁⁶d₂² ✓. 891 = 3⁴·11 = d₂⁴·dim M₁₀ ✓. **1044 = 2²·3²·29** — the prime 29 has no clean LD expression; boundary hitting time numerator is not a pure LD monomial.

### V.9.1a: Eigenspace coherence [OBS]

The φ-eigenvector occupies 1 of 8 independent spectral sectors (eigenspaces λ = 1, 3, 4, 5, (5±√21)/2, (5±√5)/2). The hitting time formula

h(p → x) = 12 · Σ_{λₖ≠0} (vₖ(x) − vₖ(p))² / λₖ

requires **all 8 eigenspace contributions** to match within each group. Explicit decomposition (verified numerically):

For {b, e}: contributions from each eigenspace agree to machine precision in 7 out of 8 sectors. In the 3-fold degenerate sector λ = 5, individual basis-dependent components differ, but the basis-invariant sum ‖P_{λ=5}(δ_b − δ_p)‖² = ‖P_{λ=5}(δ_e − δ_p)‖² (verified: both = 1.68/12).

This is **not** from graph automorphism (Aut(G) = ⟨c↔p⟩ does not map b↔e), and σ₁ does not commute with L (‖[L,σ₁]‖ = 6). The vertices b and e have different neighbourhoods: nbrs(b) = {μ,t,e}, nbrs(e) = {d,b,t}. The spectral equivalence is unexplained by any known symmetry of the walk.

**Meaning:** The φ-grouping, visible in a single 1D spectral slice, is coherently reproduced across all eight eigenspaces. This is stronger than D.7 alone.

### V.9.2: Anchor hitting times for Z_φ [THM-arith]

For the 4 individually resolved Z_φ members:
- h(p→u) = **3 = d₂** (pre-anchor = σ₀⁻¹(p))
- h(p→c) = **36/5 = ∏wᵢ/(N−1)** (σ₁(p))
- h(p→t) = **12 = index** (antipodal on 6-face)

Key ratios:
- h(p→t)/h(p→u) = 4 = d₁²
- h(p→c)/h(p→u) = 12/5 = index/(N−1)

### V.9.3: Hitting time symmetry — c uniquely reversible [THM-comp]

h(p→c) = h(c→p) = 36/5. The particle c = σ₁(p) is the **unique** particle with symmetric hitting time to/from anchor.

Asymmetry ratios h(p→x)/h(x→p):

| Particles | h(p→x)/h(x→p) | LD form |
|-----------|:--------------:|---------|
| c | **1** | symmetric (unique) |
| b, e | **2/5** | d₁/(N−1) |
| s, τ, W, H | **3/5** | d₂/(N−1) |
| d, μ | 99/185 | no clean form |
| u | 5/31 | (N−1)/31 |
| t | 5/19 | (N−1)/19 |

Interior asymmetry = d₁/(N−1), boundary asymmetry = d₂/(N−1): ramification indices in hitting time ratios. The primes 31 and 19 in the u, t denominators, and 185 = 5·37 for d, μ, are not LD monomials.

### V.9.4: Commute time C = ∏wᵢ = 36 for exactly 3 pairs [THM-comp]

| Pair | σ₁-pair | Commute time |
|------|---------|:------------:|
| {u, t} | bridge pair (WV_A) | **36** |
| {b, d} | cross: (bμ)×(de), first halves | **36** |
| {e, μ} | cross: (bμ)×(de), second halves | **36** |

These are the **only** three pairs with C = 36 = ∏wᵢ = 1·2·3·6 among all 66 pairs. σ₁ maps {b,d} ↔ {μ,e} (transposes halves).

**Note:** 36 is NOT the minimum commute time. The global minimum is C(c,p) = 72/5 = 2·∏wᵢ/(N−1). Out of 66 pairs, the three C = 36 pairs rank 24th–26th by increasing commute time.

### V.9.5: Kemeny constant [THM-arith]

**κ = 511/20 = 25.55**

Verified by three independent methods: (1) spectral Σ 3/λ_comb, (2) h-sum from p, (3) h-sum from u. All give 511/20 exactly.

Spectral decomposition (κ = Σ_{λ_comb ≠ 0} 3/λ):

| Eigenspace | λ_comb | mult | 3/λ × mult | LD monomial |
|:----------:|:------:|:----:|:----------:|:------------|
| λ = 1 | 1 | 1 | 3 | d₂ |
| λ = 3 | 3 | 2 | 2 | d₁ |
| λ = 4 | 4 | 1 | 3/4 | d₂/d₁² |
| λ = 5 | 5 | 3 | 9/5 | d₂²/(N−1) |
| x²−5x+1 | (5±√21)/2 | 1+1 | **15** | \|P³(𝔽₂)\| |
| x²−5x+5 | (5±√5)/2 | 1+1 | 3 | d₂ |

All six sectors = LD monomials. The √21-sector (disc = d₂L) contributes 15 = |P³(𝔽₂)| = 1/α₂(d₁), linking Cayley random walk to projective geometry over 𝔽₂ and scattering matrix (L.4).

Note: 511 is prime; κ itself is not an LD monomial in numerator.

### V.9.6: Step entropy [OBS]

H(next step from x) = log₂(3) ≈ 1.585 bits for 10 of 12 particles (3 distinct neighbours). For c and p only: H ≈ 0.918 bits (2 distinct neighbours due to multi-edge). Information-theoretic shadow of Anchor Lemma D.1.


## [THM-comb] V.10 — Dessin as linear code (S149)
Source: S149, verified S149-review (GF(2) rank computation, brute-force kernel)
Status: [THM-comb]
Dependencies: C.1 (dessin structure), D.1 (Anchor Lemma), E.8 (boundary choices), C.6 (dessin address)

### V.10.1: Code parameters [12, 3, 2] [THM-comb]

Edges of the bipartite dessin = bits of a binary codeword. Parity checks:
- σ₀ (BV-orbits): 4 weight-d₂ checks (rows of BV incidence matrix)
- σ₁ (WV-pairs): 6 weight-d₁ checks (rows of WV incidence matrix)

Combined check matrix H = [H_BV; H_WV] has GF(2)-rank **9**. Code parameters:

**[n, k, d] = [12, 3, 2]**

- n = 12 = index
- k = 3 = β₁ (first Betti number of the bipartite graph)
- d = 2 (multi-edge {c,p} = shortest cycle)

**Arithmetic origin of k:** β₁ = |E| − |V| + 1 = index − (index/d₂ + index/d₁) + 1 = index(1 − 1/d₁ − 1/d₂) + 1 = index/N + 1 = 3 for (d₁,d₂) = (2,3). The coincidence k = d₂ follows from the bipartite valence structure.

**Origin of d:** d = 2 because the Anchor Lemma (D.1) guarantees a multi-edge. Without it, the girth of a bipartite graph gives d = 4.

### V.10.2: Codewords = E.8 boundary choices [THM-comb]

The 2^k = 8 codewords (kernel of H over GF(2)):

| Weight | Support | E.8 interpretation |
|:------:|---------|:-------------------|
| 0 | ∅ | trivial |
| 2 | {c, p} | multi-edge flip |
| 4 | {s, W, τ, H} | both far-end pairs |
| 6 | {c, s, τ, W, H, p} | multi + both far-end |
| 6 | {b, μ, d, e, s, W} | interior + far-end E |
| 6 | {b, μ, d, e, τ, H} | interior + far-end F |
| 8 | {c, b, μ, d, e, s, W, p} | complement of {u,t,τ,H} |
| 8 | {c, b, μ, d, e, τ, H, p} | complement of {u,t,s,W} |

The cycle space = symmetric differences of spanning trees. The 3 generators of the cycle space are precisely the E.8 binary choices: {c ⊕ p}, {s ⊕ W, τ ⊕ H pair 1}, {s ⊕ W, τ ⊕ H pair 2}. This is a standard theorem of algebraic graph theory, here identified with the UST choice structure of V.3–V.4.

### V.10.3: σ∞ resolves the code [THM-comb]

Adding face checks (σ∞-cycles): rank rises from 9 to **12**, k → 0. Three of the four faces add independent constraints (the 1-face check is redundant mod 2).

**Interpretation:** σ₀ and σ₁ leave 3 bits of freedom; σ∞ resolves them completely. This is the standard Euler relation for sphere embeddings: cycle rank + cut rank = |E|, and for S² the cycle/cut spaces are complementary.

### V.10.4: Syndrome = dessin address [THM-comb]

The syndrome s(x) = H · δₓ (column of H corresponding to edge x) identifies 10 of 12 particles uniquely. The sole collision: **c and p share the same syndrome** — they appear in the same BV-orbit (BV₀) and the same WV-pair (WV_B).

This reproduces C.6 (dessin-address theorem): the triple (BV, WV, Face) uniquely identifies all 12 edges, but (BV, WV) alone fails for the multi-edge pair. Resolving c from p requires face data (σ∞), consistent with V.10.3.


---

# W. η-QUOTIENT IDENTITY ON X₀(6) (S144)

## [THM-arith] W.1: R-identity for Hauptmodul
Source: S144
Status: [THM-arith]
Dependencies: K.1 (Hauptmodul), C.2 (ramification)
Verified: Numerical (6 values of Im(τ), precision 10⁻⁵⁰); q-expansion analytic to q³

### Statement

$$R(t_6) \;\equiv\; \left[\frac{\eta(2\tau)\,\eta(3\tau)}{\eta(\tau)\,\eta(6\tau)}\right]^{12} \;=\; \frac{(t_6 + d_2^2)(t_6 + d_1^3)}{t_6}$$

### Proof sketch

Both sides are modular functions on X₀(6) of degree 2 (poles at t₆ = 0 and ∞, i.e. cusps w = 6 and w = 1). Zeros of RHS at t₆ = −d₂² and t₆ = −d₁³ (cusps w = 3 and w = 2). LHS has the same divisor (verification via q-expansion). Ratio = constant on compact Riemann surface; q⁰ coefficient fixes constant = 1. ∎

### Expanded form

R(t₆) = t₆ + 17 + 72/t₆ = t₆ + (d₁³ + d₂² + N) + |Mon|/t₆

### q-expansion

R = q⁻¹ + index + 78q + 364q² + 1365q³ + ...

First coefficients: 1, index, 78, 364, 1365 match C(n+12, n+1) for n = −1, ..., 3 (general formula not verified). The 72 in 72/t₆ = |Mon| = d₁³d₂².

### Zeros and Catalan

**Zeros:** t₆ = −d₂² = −9 (cusp w=3, j=0) and t₆ = −d₁³ = −8 (cusp w=2, j=1728).

Product of zeros: d₁³d₂² = 72 = |Mon|.

Separation: |d₂² − d₁³| = |9 − 8| = 1 ⟺ Catalan (Mihailescu). This is path #20 (Catalan) reformulated in modular-function language (**path #38 = #20 alt**, not independent).

### Derivatives at zeros

R'(t) = 1 − |Mon|/t². At the zeros:
- R'(−d₂²) = 1 − 72/81 = **1/d₂²** = 1/9
- R'(−d₁³) = 1 − 72/64 = **−1/d₁³** = −1/8

### Level-set symmetry

R(t) = R(|Mon|/t) for all t ≠ 0. Proof: R = t + 17 + 72/t is invariant under t ↔ 72/t. ∎

### R = −1 level set

R(t) = −1 ⟺ t² + 18t + 72 = 0 ⟹ t = −N = −6 or t = −index = −12.

Product = N · index = 72 = |Mon|. Discriminant = 36, √Δ = 6 = N.

### Special values

| t₆ | R | LD interpretation |
|----|---|-------------------|
| 1 | 90 | d₂² · |B₁| |
| d₁ = 2 | 55 | = 5 · 11 |
| **d₂ = 3** | **44** | **Σn = d₁² · dim M₁₀** |
| d₁² = 4 | 39 | d₂ · 13 |
| **N = 6** | **35** | **N² − 1** |
| d₁³ = 8 | 34 | 2 · 17 |
| d₂² = 9 | 34 | R(8) = R(9) since 8 · 9 = |Mon| |
| **index = 12** | **35** | **= R(N)** since N · index = |Mon| |
| −1 | −56 | −d₁³L |
| −d₁ = −2 | −21 | −d₂L |
| **−d₂ = −3** | **−10** | **−|B₁|** |
| **−N = −6** | **−1** | |
| −d₁³ = −8 | 0 | zero (cusp j = 1728) |
| −d₂² = −9 | 0 | zero (cusp j = 0) |
| **−index = −12** | **−1** | R(−N) = R(−index) |

### CM point τ = i/√6

Fixed point of W₃ = W₆ (Atkin-Lehner). Discriminant −24, class number h(−24) = 2.

- t₆(i/√6) = 6√2, i.e. **t₆² = 72 = |Mon|** (PSLQ confirmed)
- **R_min on ℝ₊** = (√(d₁³) + d₂)² = (2√2 + 3)² = **17 + 12√2**

### Scope and limitations

R encodes the **ramification data** d₁³, d₂² of the Belyi map j: X₀(6) → ℙ¹, not the UST data d₁², d₂² used in CKM (§V). The bridge d₁³ ↔ d₁² is absent: **R does not yield CKM directly** (dead direction #42, §X.33).


## [THM-arith] W.2: R-values at cusp widths and PMNS bridge (S145)
Source: S145
Status: [THM-arith]
Dependencies: W.1 (R-identity), I.11–I.12 (L_eff)
Verified: numerical (R values), analytical (det(L_rr) from 9×9 Cayley Laplacian block)

### R at cusp widths

| w | R(w) | LD monomial |
|---|------|-------------|
| 1 | 90 | d₂² · |B₁| |
| d₁ = 2 | 55 | (N−1) · dim M₁₀ |
| d₂ = 3 | 44 | Σn = d₁² · dim M₁₀ |
| N = 6 | 35 | N² − 1 |

Consecutive differences: R(1)−R(d₁) = 35 = N²−1, R(d₁)−R(d₂) = 11 = dim M₁₀, R(d₂)−R(N) = 9 = d₂².

**Sum: Σ R(w) over w ∈ Div(6) = 224 = d₁⁵ · L.** Fails for all other (d₁, d₂) tested.

### Derivative product

R'(−d₂²) · R'(−d₁³) = (1/d₂²)(−1/d₁³) = −1/|Mon| = −1/72.

### det(L_rr) bridge to PMNS

L_eff (§I.11) has eigenvalues {0, 9/5, 25/11}. Integer form: 55 · L_eff with eigenvalues {0, 99, 125}.

**R(d₁) = 55 = lcm(N−1, dim M₁₀)** = lcm of L_eff eigenvalue denominators.

**det(L_rr) = R(d₁) · (N−1)² = 55 · 25 = 1375.** Verified: det of 9×9 non-leptonic Cayley Laplacian block = 1375 exactly.

**Tr(55 · L_eff, nonzero) = 99 + 125 = 224 = Σ R(w).** Links PMNS sector (L_eff trace) to η-quotient (W.1 evaluated at cusps).


## [THM-arith] W.3: (s, W) self-duality (S146)
Source: S146
Status: [THM-arith]
Dependencies: F.1 (n, ℓ values), D.5 (det M_lep = 13)
Verified: exhaustive check — no other particle has n = ℓ

### Statement

s and W are the **unique** particles with n = ℓ: s has n = ℓ = d₂ = 3, W has n = ℓ = N = 6. No other particle among the 12 satisfies n = ℓ.

### Common factor

For n = ℓ, the quantity 7(Φ − Lℓ) = n³(L−n) − L²n = n[n²(L−n) − L²]. The bracket evaluates to −13 = −(d₁²+d₂²) = −det(M_lep) at **both** n = d₂ and n = N.

Proof: n²(L−n) = N² in both cases: d₂²(L−d₂) = d₂²·d₁² = N², and N²(L−N) = N²·1 = N². Hence bracket = N² − L² = 36 − 49 = −13. ∎
- n = 3: 3·(−13) = −39. ✓
- n = 6: 6·(−13) = −78. ✓

Ratio: 7(Φ−Lℓ)(W) / 7(Φ−Lℓ)(s) = −78/−39 = **d₁ = 2** exactly.

### Reformulation

The identity 2N+1 = d₁²+d₂² = 13 is equivalent to |d₁−d₂| = 1 (consecutive integers with product N). Not a new path (tautological from N = d₁d₂, L = N+1), but connects det(M_lep) to the self-dual pair structurally.


## [THM-comp] W.4: Newform decomposition S₁₀(Γ₀(6)) (S159)
Source: S159 (PARI/GP mfinit/mfeigenbasis), cross-checked S163 (LMFDB download)
Status: [THM-comp]
Deps: standard (PARI mfinit/mfeigenbasis). See LD_LMFDB_reference.md.

### Statement

dim S₁₀(Γ₀(6)) = 7. Four rational newform orbits, decomposition 7 = 2 + 2 + 2 + 1:

| Form | Level | a₂ | a₃ | W₂ | W₃ | Copies at Γ₀(6) |
|------|-------|-----|-----|-----|-----|------------------|
| 2.10.a.a | 2 | 16 | −156 | −1 | — | 2 (f, f|V₃) |
| 3.10.a.a | 3 | 18 | 81 | — | −1 | 2 (g_a, g_a|V₂) |
| 3.10.a.b | 3 | −36 | −81 | — | +1 | 2 (g_b, g_b|V₂) |
| **6.10.a.a** | **6** | **−16** | **81** | **+1** | **−1** | **1** |

The unique level-6 newform h = 6.10.a.a:
- a₂ = −d₁⁴, a₃ = d₂⁴ [VERIFIED LMFDB]
- a_{2^k} = (−d₁⁴)^k, a_{3^k} = (d₂⁴)^k (geometric at bad primes)
- All {2,3}-smooth index coefficients are LD monomials
- Fricke-odd: W₆ = W₂·W₃ = (+1)(−1) = −1
- Self-dual, CM = no, analytic rank = 0


## [THM-comp] W.5: Period polynomial P⁺(u) of 6.10.a.a (S159)
Source: S159 (PARI lfun), verified S163 (algebraic expansion), verified S164 (independent recomputation)
Status: [THM-comp]
Deps: W.4, PARI lfun.

### Statement

r⁺(X)/Ω⁺ = (X/d₂³)·P⁺(X²) where

**P⁺(u) = −N³u³ + d₁d₂L·u² − L·u + 1 = −(6u−1)(36u²−u+1)**

### Properties (all verified S164)
- ALL coefficients are LD monomials: {−N³, d₁d₂L, −L, 1} = {−216, 42, −7, 1}
- Root: u₀ = 1/N = 1/6 (reciprocal level)
- Cofactor discriminant: 1−4·36 = −143 = −det(M_lep)·dim M₁₀ = −13·11
- P⁺(1/L) = 78/343 = N·det(M_lep)/L³
- P⁺(1/index) = 7/12 = L/index
- u² coefficient 42 = d₁·(d₂L) = d₁·21 (anchor splitting)

### Uniqueness
Only 6.10.a.a (among the 4 newforms spanning S₁₀) has P⁺ root at 1/N AND all-LD-monomial coefficients. Others: 2.10.a.a root 1/d₁, 3.10.a.a root 1/d₂. [FROM S159, not independently verified for other forms]


## [THM-comp] W.6: Period polynomial P⁻(u) of 6.10.a.a (S159)
Source: S159 (PARI lfun), verified S163 (coefficient identities), verified S164 (independent recomputation)
Status: [THM-comp]
Deps: W.4, PARI lfun.

### Statement

**P⁻(u) = 5184u⁴ − 2772u³ + 385u² − 77u + 4**

### Coefficient decomposition (all verified S164)
- u⁴: 5184 = index²·∏w = 144·36
- u³: −2772 = −∏w·77 = −∏w·L·dim M₁₀
- u²: 385 = (N−1)·77 = (N−1)·L·dim M₁₀
- u¹: −77 = −L·dim M₁₀
- u⁰: 4 = d₁²

Middle three coefficients are multiples of **77 = L·dim M₁₀**. Irreducible over ℚ.


## [OBS] W.7: L-value algebraic parts of 6.10.a.a (S159)
Source: S159 (PARI lfun)
Status: [OBS]
Deps: W.4, PARI lfun.

### Statement

dim M₁₀ = 11 appears in ALL odd-parity algebraic parts:
r⁻(3) = 11/576 = dim M₁₀/(d₁³d₂)², r⁻(5) = 11/10368 = dim M₁₀/(d₁⁷d₂⁴), r⁻(7) = 11/20736 = dim M₁₀/index⁴.

Even-parity: r⁺(4) = 1/∏wᵢ = 1/36, r⁺(6) = r⁺(8) = 1/N³ = 1/216.

Form-specific: other newforms have different ratios.

### Caveat
These ratios depend on the choice of Manin period Ω^±. The stated values use the LMFDB normalization convention. The claim "11 appears in all odd parts" is convention-dependent; what is invariant is that odd and even parts have structurally different denominators.

### S202–S203 Period Audit

**S202 BUG [ERRATUM]:** The L-function computation in S202 used an incorrect prefactor — both Mellin sums received the same (√N/(2π))^s factor instead of distinct s and (k−s) factors. This produced wrong period values Ω⁺ ≈ 0.00379, Ω⁻ ≈ 0.01652 and a spurious "period inconsistency" (Ω⁺ from m=4 vs m=8).

**Resolution (S203):** With correct L-function values, ALL period ratios are rational and the functional equation Λ(m) = Λ(10−m) holds to 60-digit precision. No inconsistency exists. See W.9 for corrected values.


## [THM-comp] W.8: AL Sector Structure of S₁₀(Γ₀(6)) (S186, ERRATUM S200)
Source: S186, erratum S200 (verified S201)
Status: [THM-comp] (downgraded from [THM-arith])
Dependencies: W.4 (newform decomposition)

### Traces
Tr(W₂) = Tr(W₃) = Tr(W₆) = −1 on S₁₀(Γ₀(6)).

Source: W.4 newform decomposition (verified independently S200–S201).
Tr(W₂) = 2·w₂(2.10.a.a) + 0 + 0 + w₂(6.10.a.a) = 2·(−1) + 0 + 0 + 1 = −1.

### S200 Erratum

**DELETED (S200):** The claim "For Γ₀(N) squarefree with ν₂ = ν₃ = 0: elliptic contribution to Tr(W_Q) vanishes, parabolic contribution = −1" was stated for ALL even k ≥ 4. This is **FALSE**.

**Counterexample (k = 4):** dim S₄(Γ₀(6)) = 1. Unique newform 6.4.a.a (η-product η²η₂²η₃²η₆²). Verified by exact Fraction q-expansion: a₂ = −2, a₃ = −3.
w₂(6.4.a.a) = −a₂/2¹ = **+1**. w₃(6.4.a.a) = −a₃/3¹ = **+1**. w₆ = **+1**.
Therefore **Tr(W₂ | S₄(Γ₀(6))) = +1 ≠ −1.** ∎

**Root cause:** S186 conflated (a) elliptic fixed points of Γ₀(6) (counted by ν₂, ν₃; both 0 for N=6) with (b) CM fixed points of W_Q (which contribute to the trace formula through class numbers H(4Q − t²) weighted by Chebyshev U_{k−2}(t/(2√Q))). These are distinct geometric objects: (a) vanishes ⇏ (b) vanishes. For even k, U_{k−2}(0) = (−1)^{(k−2)/2} ≠ 0, so CM contribution NEVER vanishes.

**Impact on LD:** NONE. All companion uses of Tr(W_Q) = −1 are at k = 10 specifically. The k = 10 result is correct [THM-comp from W.4].

### Sector dimensions
dim S₁₀^{(ε₂,ε₃)} = (7 + ε₂(−1) + ε₃(−1) + ε₂ε₃(−1))/4.

| Sector (ε₂,ε₃) | W₆ | dim S₁₀ | dim M₁₀ | Face f | h(f) |
|---|---|---|---|---|---|
| (+,+) | +1 | **1** | 2 | anchor (f=1) | d₁ = 2 |
| (+,−) | −1 | 2 | 3 | leptons (f=3) | 1 |
| (−,+) | −1 | 2 | 3 | bosons (f=2) | d₂²/d₁² |
| (−,−) | +1 | 2 | 3 | quarks (f=6) | d₁/d₂ |

Sum S₁₀: 1+2+2+2 = 7. Sum M₁₀: 2+3+3+3 = 11.
Face→sector: f → ((-1)^{v₂(f)}, (-1)^{v₃(f)}).
6.10.a.a in lepton sector (+,−) where h = 1.
Anchor sector (+,+) uniquely 1-dimensional.

### Sector contents
| Sector | Forms |
|---|---|
| (+,+) | 3.10.a.b₊ (single level-3 oldform) |
| (+,−) | **6.10.a.a** + 3.10.a.a₊ |
| (−,+) | 3.10.a.b₋ + 2.10.a.a₊ |
| (−,−) | 3.10.a.a₋ + 2.10.a.a₋ |

### AL transition picture
h is NOT multiplicative on (ℤ/2)²: h(W₂)·h(W₃) = 4/3 ≠ 9/4 = h(W₆).

Deps: W.4.


## [THM-arith] W.9: Period Rational Parts of 6.10.a.a — Corrected (S203)
Source: S203 (corrected S202 bug)
Status: [THM-arith] (rationality from Eichler-Shimura; values verified 50 digits, 1000 q-coefficients)
Deps: W.4, W.7

### Statement
With normalization r(m) = L(f,m)·(m−1)!/(2π)^{m−1}, the Manin period ratios:

**Odd m (period Ω⁺ ≈ 20.974):**
| m | r⁺(m) | Denominator | LD expression |
|---|--------|-------------|---------------|
| 1 | 1 | 1 | — |
| 3 | 11/576 | 2⁶·3² | (index·d₁)² |
| 5 | 11/10368 | 2⁷·3⁴ | index⁴/d₁ |
| 7 | 11/20736 | 2⁸·3⁴ | index⁴ |
| 9 | 1/1296 | 2⁴·3⁴ | N⁴ |

**Even m (period Ω⁻ ≈ 2.700):**
| m | r⁻(m) | Denominator | LD expression |
|---|--------|-------------|---------------|
| 2 | 1 | 1 | — |
| 4 | 1/36 | 2²·3² | N² |
| 6 | 1/216 | 2³·3³ | N³ |
| 8 | 1/216 | 2³·3³ | N³ |

### Properties
1. ALL denominators are pure {d₁,d₂}-monomials.
2. dim M₁₀ = 11 appears in numerators at m = 3, 5, 7 (same 11 as S.12 rank barrier).
3. Functional equation pairings: r⁺(1)/r⁺(9) = N⁴, r⁺(3)/r⁺(7) = N², r⁻(2)/r⁻(8) = N³, r⁻(4)/r⁻(6) = N.
4. Ω⁺/Ω⁻ is NOT rational (PSLQ null, maxcoeff=10⁵).
5. Neither Ω⁺ nor Ω⁻ is in ℚ[π] (PSLQ null).

### Transcendence obstruction (S202, confirmed S203)
sin²(1/(6π)) ∉ ℚ-span{1, Ω⁺, Ω⁻, L(f,5)}.
α⁻¹ ∉ ℚ-span{1, Ω⁺, Ω⁻, L(f,5), E₂(i)}.
Root cause: sin²(1/(6π)) is Lindemann-Weierstrass transcendent; Ω± are algebro-geometric. Different classes.


# X. DEAD DIRECTIONS

## X.1: Pre-publication (S1–S41)
~40 directions including CKM, Wannier-Stark, Selberg/Maass, DSI, Fourier, RG, Ihara, Epstein, geodesics, growing graphs, QED/NCG/graph→n³, Lee-Wick, 4×FG derivation.

## X.2: S42–S60
Σℓ correction, «current» 6×NULL, Hecke correlations, spec(L)→n, heat kernel, variational tautology, row monotonicity (FALSE), u↔d through AL.

## X.3: S61–S68
M=d₁ as THM (FAILED), SM 1-loop→Φ (DEAD), ℂ[Mon] no-go (≤3 values), ring test D₀ (blind), ES period poly, Hauptmodul roots 110k scan (NULL), Schreier eigenvectors→CKM (M≈0).

## X.4: S69–S72
Cross-ratio, word metric, K from CRT/isolation, linear a₂ (empty), polynomial a₂ deg≤2, ρ=√C (DEAD), 10 graph CKM methods (inverted hierarchy).

## X.5: S73
Face-width weighting M_lep (preserves μ-τ). BB^T eigenvectors as full PMNS (θ₁₂ wrong).

## X.6: S74–S77
Linear a₂ formula (171 pairs, empty). Polynomial a₂ deg≤2 (fails). 10 graph CKM methods (inverted hierarchy, S72 carry-over). f(M_lep) → 4/13 (no-go: μ-τ forces {0, 0.789, 1}, 25 variants tested). M_lep + perturbation → 4/13 (only with θ₁₃ > 0.45). d₁²/(d₁²+d₂²) as structural argument (circular = tan ansatz). H_BV averaged over orbits (|U_e|² = 0.214, kills signal). P₄ = (t+3)²(t²+12t+24) wrong Hauptmodul (corrected same session S76). θ₂₃ lower octant prediction (WRONG — no LD candidate gives lower octant).

## X.7: S80–S87
~150 operators on dessin vs n-values — ALL DEAD: spec(O)=n hits algebraic wall (√5,√21 vs ℤ); embedding {0..7}↪ℙ¹(t₆) gives complex preimages; periods ∫ω→R²≈0; w_L·w_R→no correlation [S80]. Единая K(x₂,x₃) without branching — DEAD: CRT-irreducibility proven, v₃(K)≠f(x₃) for all 4 columns [THM, S83]. Mon-irreps and stabilisers: Mon transitive on 12 edges, |Stab(e)|=6 ∀e, K not class function [DEAD, S84]. Gap 3 via ω = d(ln j)/dt₆: per-edge residue uniform +1−1 = 0, cannot distinguish particles; ω(WV)=0 tautology; MOTIVATED for sign structure (R>0↔Φ, C<0↔−Lℓ) but DEAD as quantitative bridge [S87].

## X.8: Growth 1–3 + Flavor (2026-03-18)
**Eisenstein forms → PMNS [DEAD]:** M₂(Γ₀(6)) is 3-dim, indexed by cusps = sectors. Eisenstein forms are w-periodic at width-w cusps → rank-1 restriction on leptonic sector → blind to flavor. 3×3 scattering matrix eigvecs ≠ PMNS. L-value ratios: no LD match within 0.1%. **Structural theorem: automorphic forms see SECTORS, not FLAVORS. PMNS lives at flavor level (graph).**

**α/(2π) from L-values [DEAD]:** ~500k combinations of (LD₁·LD₂)/(LD₃·LD₄) × L(k,χ) × πⁿ, k=1..4, χ ∈ {χ₃,χ₄,χ₆,trivial}. Threshold 0.01%. ZERO hits. Near-miss: α⁻¹ ≈ 144−13+12L(1,χ₃)/ζ(3) = 137.035652 (−2.5 ppm), ad hoc.

**Neutrino tower Γ₀(N) [DEAD]:** Index 15 unreachable: ψ(N) ≠ 15 for any N ≤ 500. 15 ∤ 12. Γ₁(6) = Γ₀(6). No genus-0 Γ₀(N) with index 15.

**φ-eigenvector = PMNS column [DEAD]:** See I.9e.

**Alternative operators → exact 4/13 [DEAD]:** See I.9c.

**Triple eigenvectors → PMNS [DEAD]:** See I.9f.


---

## X.9: S88–S91

**Heat kernel diagonal h(e,e) ∝ Φ−Lℓ [DEAD, S88]:** Ratios h(e,e)/Φ(n) range 0.006–0.21. Fundamental obstacle: L_Sch involves {σ₁, σ₀, σ₀⁻¹} but NOT σ∞. The σ∞-cycle structure (defining n, ℓ, K, face type) is invisible to L_Sch.

**Spectral decomposition h_int/h_irr [DEAD, S90]:** Integer part ≠ Φ, irrational part ≠ −Lℓ. Algebraic split, not physical.

**Combined operators L+α·σ∞ [DEAD, S91]:** Best correlation 0.64 with 2 parameters on 12 points = overfitting.

**Any Schreier-graph operator → n, ℓ, K [DEAD, S91, PRINCIPLED]:** Schreier graph knows σ₁ and σ₀ but not ordering within σ∞-cycles. Since n = position in σ∞-face, no L_Sch operator can reproduce n or ℓ. Kills ALL operator-based approaches to Gap 3 via Cayley/Schreier graph.

## X.10: S94–S95

**Moonshine aₙ → δK(n) [DEAD, S94]:** Signs disagree at n=4.

**1-loop VOA ↔ 1-loop QED [DEAD, S94]:** Structural parallel but different spaces (V_n^♮ vs 4D particle spectrum).

**Contour shift [DEAD, S95]:** Single pole at s=1, regular at s=2,...,L. Individual particles do not emerge from poles.

## X.11: S97–S97++

**S97 Schur → PMNS alone [DEAD]:** sin²θ₁₃(Schur) = 1/26 = 0.0385 vs exp 0.022 (−29σ). Schur complement necessary but insufficient without heat kernel correction.

**S97+ interpolation α = 1/|B₁| [OBSOLETE]:** Replaced by pure heat kernel t = √5/2 (fewer parameters, better fit).

**S97++ extremum derivation of t [DEAD]:** ~25 functionals tested (det, Tr, entropy, purity, coherence, condition number, Fisher information, sensitivity, F₁ max, inflection points, crossings with LD values). **None** has extremum or zero within ±0.05 of √5/2. t = √5/2 does not emerge from variational principle.

**S97++ Rankin-Selberg divergence [DEAD]:** T_{6E} Rankin-Selberg L-function diverges at s=1. Cannot extract finite coupling.


## X.12: S99 (13 dead directions)

| # | Direction | Why dead |
|---|---|---|
| 1 | m² ∝ λ(L_eff) for neutrinos | Ratio 1.26 vs 33.5 (26× off) |
| 2 | m ∝ λ | Ratio 1.59 vs 33.5 |
| 3 | m ∝ √λ | Same as #1 |
| 4 | m² ∝ (λ_max − λ) | Wrong ordering (IO) |
| 5 | seesaw m ∝ 1/λ | Diverges at λ=0 |
| 6 | Ihara zeros ↔ t₁,t₂ | ζ⁻¹(tᵢ) ≠ 0 |
| 7 | Spectral ζ(L_eff) zeros | All purely imaginary |
| 8 | det(L|_{std⊗V}) → masses | 75 = 3·5²: no mass structure |
| 9 | det'(L_eff) → masses | 45/11: no mass structure |
| 10 | Cayley discriminants = geodesic | {5,21} ∉ Γ₀(6) hyperbolic spectrum |
| 11 | L_eff eigenvalues directly | Only 2 nonzero: insufficient for 3 masses |
| 12 | Ihara ζ analytic continuation | Polynomial, no interesting continuation |
| 13 | Selberg trace → t derivation | Geometric side not LD-rational at t₁,t₂ |


## X.13: S100 (25 dead directions)

| # | Direction | Why dead |
|---|---|---|
| 14 | Modular τ = i·t₂ on ℍ | t₆, j not LD-rational |
| 15 | Heegner D=−20 | t₆ complex, not LD-special |
| 16 | Heegner D=−84 | t₆≈−126.4, not LD-special |
| 17 | Ihara zeros ↔ t | ζ⁻¹(t₁)≠0, ζ⁻¹(t₂)≠0 |
| 18 | Spectral ζ(L_eff) zeros | All purely imaginary |
| 19 | Selberg geometric side | LD discriminants {5,21} forbidden in Γ₀(6): ad≡1(mod 6) has no solution for T=3,5 |
| 20–25 | Self-consistency fixed point (6 variants) | Fixed points miss √5/2 by 0.4–2.7% |
| 26 | H_lep factorization (off-diag norm) | ‖H_off‖ monotone increasing, no minimum |
| 27 | H₁₂(t)=0 (φ↔√21 mixing zero) | Zero at t≈1.97, far from t₂ |
| 28 | Tr(H_lep)/Tr(H_full) rationality | Not LD-rational |
| 29 | Eigenvalue ratios of H_lep | Not LD-rational |
| 30 | det(H_lep) rationality | Not LD-rational |
| 31 | \|U_PMNS\|² exact rationality | Not exact at any tested t |
| 32 | n·H_lep integrality | No integer matrix |
| 33 | char(H_lep) coefficients | Not LD-rational |
| 34 | Born linearity at 2 points | Underdetermined (2 points, any function passes) |
| 35 | m² ∝ λ(L_eff) | Ratio 1.26 vs 33.5 |
| 36 | m ∝ λ | Ratio 1.59 vs 33.5 |
| 37 | m² ∝ (λ_max−λ) | Wrong sign (IO) |
| 38 | seesaw 1/λ | Diverges at λ=0 |

**Cumulative dead directions S99+S100: ≥38.** (Additional pre-S99 dead: contour shift S95, Rankin-Selberg S96, h_int∝Φ S90, DT-eigenvector, f(M_lep)→4/13 etc. — see X.1–X.11.)

## X.14: S101–S106 (QTC + α-formula)

**S101–S102:** Spectral resolvent ζ_L(1) = 511/60 (no clean IR connection). j=−L NOT CM (verified numerically). Form B (a=|B₁|=10) experimentally dead (χ²=165.6). All standard modular-geometric objects (Kronecker limit, Green's function, Arakelov height) give logarithmic outputs, not rational IR. Structural mismatch: IR is resolvent, not spectral.

**S104:** Fourier phases at cusps explicitly disproven (KR12): phases 2πx/w at τ=i are NOT 1/(wπ). Heat kernel → cos², quantum walk → cos², BB^T ratio → cos², Cayley eigenvalue ratio → cos²: all 4 approaches fail. cos² = [MOT] even with the 6 new dead.

**S105:** E₂* gradient (PSLQ NULL 150 digits, X(1) not X₀(6)). Scattering phase at r* (r* transcendental, PSLQ NULL). det'Δ/Selberg (structural: cos never appears in trace formula). Total 9 DEAD approaches to cos² before QTC.

**S106:** QTC on 12 sheets = trivial blow-up of 4×4 (face-constant phases give rank 3). IR through QTC = structural mismatch (rational vs trigonometric, 5 attempts fail). φ(d₁)=1/(2π) tautological for d₁=2. 4×4 eigenvalues do not match LD invariants.

## X.15: S110 (Ring contraction analysis)

**DEAD: Ring as Banach contraction [S110].** Naive iteration F(α) = (G_exp/C₀)^{α²μ_G/2} has |F'(α*)| = 2·ln(α⁻¹) = 9.84 >> 1. Not a contraction in any neighborhood. "3 iterations" = Newton's method, not geometric convergence. The ring is a forward prediction (α → μ → μ_G → G), not a fixed-point iteration.

**CORRECTED: μ_G description [S110].** Companion H.3 stated "μ_G is μ from H.2 at NLO only". This is false: H.2 at all truncation orders gives ~1836.15, not 1835.70. Correct: μ_G = (3μ + μ_n − B_d/m_e)/4 (nuclear masses). Error introduced during S93, not caught through S109.

**WORKFLOW RULE: CLOSURE-TEST.** Every closure claim must be verified by substituting only derived quantities and checking the numerical result. If miss >1%, claim is false.

## X.16: S108–S109 (Spectral, variational, operator)

**DEAD: STM for IR or any N-specific quantity [S108, PRINCIPLED].** Cayley graphs X₀(6) and X₀(11) are isospectral (SNI). All spectral invariants (Tr Lᵏ, det', ζ_L(s), heat kernel) shared. Distinction lies in σ∞ (cuspal structure), invisible to undirected spectrum.

**DEAD: VMF as minimum principle for τ=i [S108].** h(τ) = −log(y^{1/2}|η|²) has τ=i as saddle (Morse index 1), not minimum. Hessian eigenvalues: 1/4 ± π²E₄(i)/36. h is SL₂(ℤ)-invariant → cannot select Γ₀(6). Five Γ₀(6)-specific variants tested, all fail.

**DEAD: ω = d(ln j)/dt for per-particle Φ(n) [S109].** R(t) = 3P₄'/P₄ is flat near cusps: R ≈ 1 ± 0.22 for |t| < 2, but Φ(n) ranges [0, 35.7] for quarks (35× mismatch). j depends on t⁶ near 6-cusp, killing angular information. ω resolves face type → ℓ [✓] but not face position → n [✗]. G.9 parallel remains [MOTIVATED], not upgradeable.

**DEAD: Weighted Laplacian A_w = d₂(σ₀+σ₀⁻¹) + d₁σ₁ [S109].** Global weights do not break graph automorphism (c↔p). Rank 6, correlation 0.52 with Φ−Lℓ.

**DEAD: ALL operator-diagonal approaches to Φ−Lℓ [S109, PRINCIPLED].** 12 unique cuspal triples → 12-dimensional space. Any 12-vector decomposes in rank-12 basis. This is interpolation (dim ℝ¹² = 12), not derivation. Applies to: A^k (rank 6), (σ₀σ₁)^k extended (rank 12), polynomial in (F,Fσ₁,Fσ₀) (rank 12), face-weighted D_F·A^k (rank 12 with D_{Fσ₁}).

**WORKFLOW: GREP-BEFORE-COMPUTE [S109].** F.7 (ε₀ = ε(Fσ₀)) rediscovered from scratch instead of reading companion line 1224. Recurrence of S84 failure. Rule: `grep` companion for relevant keywords before any new computation.

**WORKFLOW: IRREP-PROJECTOR [S148].** ONLY P_ρ = (dim ρ / |G|) Σ χ̄_ρ(g)·ρ(g) from group algebra. NEVER eigh-matching (degeneracy → double-counting). Root cause: S147 HK error.

**WORKFLOW: MONOMIAL-CHECK [S148].** Fraction before writing any LD monomial. Root cause: S147 −1/39 ≠ −2/39.

**WORKFLOW: SUM-PARTS=WHOLE [S148].** After irrep decomposition: Σ parts ≡ total, else bug.

**WORKFLOW: DERIVE-NOT-HARDCODE [S153].** n, ℓ, K must be computed from monodromy (F.7/G.8), NEVER hardcoded. Valid n ∈ {0,1,3,4,5,6,7}; n ∉ {2,8,9,10,11} → immediate stop. Root cause: S152 forensic audit (7/12 wrong n-values from hardcoded dict).

**WORKFLOW: VERIFY-BOTH [S153].** If companion and code disagree, re-derive BOTH from first-principles (monodromy). Do not assume either is correct. Root cause: S152 code wrong, companion correct — but this was not guaranteed a priori.

**WORKFLOW: BARRIER-CHECK [S153].** Before ANY new Gap 3/Gap 9 computation: search project knowledge for "barrier", check proposed direction against Classes A–H (LD_barriers). If match → cite class and STOP.

**WORKFLOW: CONVENTION-SPEC [S156].** Any result citing individual (c,d) ↔ particle assignment MUST state convention: "T = σ∞" (Shimura/I.9h) or "T⁻¹ = σ∞" (Q.3). Exempt: results depending only on pair-level or multiset-level norms. Root cause: Q.3 and I.9h use different valid conventions without declaration.

**WORKFLOW: PROPAGATION-CHECK [S153.1].** When correcting any numerical value in companion, grep the old value across the ENTIRE companion. Patch ALL occurrences. Root cause: H.3 G_pred corrected S115; H.5 copy missed.

**WORKFLOW: SIGN-CHECK [S153.1].** Every σ-pull must satisfy: sign(pull) = sign(exp − theory). If theory > exp, pull MUST be negative. Root cause: V.4 J pull sign wrong.

**WORKFLOW: VALUE-VS-PULL [S153.1].** In χ² formulas or pull table entries, confirm each number is (exp−theory)/σ, not a raw prediction value. Diagnostic: if number = known prediction value (e.g. 0.15 = 3/20), suspect error. Root cause: E.6 χ² and V.4 R_b both confused prediction value with pull.

**WORKFLOW: PREDICTION-XREF [S153.1].** Any section making a quantitative prediction MUST grep companion for competing predictions of the same observable. If found, add cross-reference with explicit incompatibility note. Root cause: I.1 (m₁=7.72 meV) and I.28.2 (m₁=0) coexisted without cross-ref.

**WORKFLOW: CONFLICT-RESOLVE [S163].** При расхождении с результатом предыдущей сессии → сначала conversation_search контекста → прочитать ЛОГИКУ предыдущего Логоса (не только результат) → классифицировать: (a) предыдущий Логос ошибся (указать где), (b) текущий Логос неверно интерпретирует (уточнить), (c) разные вопросы (согласовать формулировку) → только после этого — вердикт. Root cause: S163 claimed "τ=ρ: 9 distinct, not 4" — bug in numerical code; S157 algebraic argument was correct.

## X.17: S118 (Heegner obstruction)

**Kudla generating series → α [DEAD, S118, PRINCIPLED].** τ = i is not a Heegner point on X₀(6) (P.1: 3 inert in ℤ[i]). Kudla's generating series encodes heights of Heegner divisors; non-Heegner points are invisible. No arithmetic generating series on X₀(6) can produce E₂(i) at a structurally relevant point.

**Arakelov height → α [DEAD, S118, PRINCIPLED].** Gross-Zagier and its generalizations relate L'(1) to Néron-Tate heights of Heegner points. τ = i is not Heegner on X₀(6) → Arakelov intersection at τ = i decouples from L-function derivatives. The analytic route (H.1a–H.1c) is not an inferior alternative but the structurally forced one.


## X.18: S119–S121 (Cuspal regulators and related)

**Categorical initiality [DEAD, S119, PRINCIPLED].** No natural category makes X₀(6) initial. Belyi₀ has one object (tautology). Full X₀(N) genus-0: X₀(1) terminal, not X₀(6). Functor F already constructed (F.7b-K [THM]).

**Beilinson regulator on X₀(6) [DEAD, S119, PRINCIPLED].** genus 0 → K₂(ℙ¹) torsion → regulator = 0. P.1 (τ=i not Heegner) blocks Kudla/Arakelov. cos² not algebraic period.

**C*-algebra on {2,3} [DEAD, S119].** A_F finite-dim → 3 characters, trivial. NCG doesn't fix masses. No bridge to X₀(6).

**Brunault Theorem 1 (direct) [DEAD, S121, PRINCIPLED].** dim S₂(Γ₀(6)) = 0. No cusp forms to pair with. Formula inapplicable.

**Eisenstein regulators → L-values [DEAD, S121, PRINCIPLED].** PSLQ NULL (80 digits, 11 tests) for −2π ln 2 against all {L'(0,χ mod 12), L'(0,χ prim), L(1,χᵢ)·L(1,χⱼ), ζ'_K(0), mixed L'·L products}. Root cause: Baker's theorem ⟹ {ln 2, ln 3, ln(2+√3)} are ℚ-linearly independent. The only L-values of class π·ln(algebraic) contain ln(2+√3), never ln 2 or ln 3. Incompatible transcendence classes. Direction dead forever.

**Regulators → α/(2π) [NOT ESTABLISHED, S120–S121].** Cuspal regulators give −2π ln(w_c) with w_c ∈ {1,2,3,6}. No combination produces α/(2π) ≈ 0.001161. Regulators live in K₂(ℙ¹\{cusps}); coupling lives in spectral theory of Γ₀(6)\ℍ — different mathematical domains.

**EW-operator from regulators [DEFERRED, S121].** No concrete proposal. Regulators give ln p ∈ ℝ (transcendental); ℓ ∈ {0,1,3,6,7} (integer). Bridge requires exponentiation with no evident mechanism.


## X.19: S122 (Cayley–Hecke bridge)

**‖[A, T_p]‖ as quantitative bridge to α/(2π) [DEAD, S122].** Normalized commutator ‖[A,T₅]‖/(‖A‖·‖T₅‖) = 0.912, three orders of magnitude above α/(2π) ≈ 0.00116. No suppression mechanism found. The commutator is O(1) — monodromy and Hecke are maximally non-commuting, not perturbatively non-commuting.

**PMNS from A↔T eigenbasis overlap [DEAD, S122, TWO ATTEMPTS].** (1) Restrict A and T₅ to 3 leptonic face-points: A|_lep = 0 (all entries zero — σ₁ ejects every lepton outside its face). Overlap undefined. (2) Restrict to 3 leptonic σ₁-doublets: A|_dbl = J+I = [[2,1,1],[1,2,1],[1,1,2]], eigenvalues {1,1,4}. Trivial "fully connected" matrix, not LD-specific. Neither attempt produces PMNS angles.

**Correlation ΔT₅ vs |δK/K| [DEAD, S122].** Pearson correlation 0.009 (null).

**Tr(f(A,T)) → α [DEAD, S122].** No combination of traces of products of A and T_p matrices produces α/(2π) or any known LD coupling constant.

**Continuous spectral theory of Γ₀(6)\ℍ [CONFIRMED NULL, S122].** Full scan: (a) det Φ(s): no zeros or poles in [0.55, 10]. (b) 153 primitive geodesics (trace ≤ 500): no length matches any LD invariant within 0.05%. (c) Z(s) → 1 exponentially for s ≥ 3, Z(1) = 0.881 not LD-rational. (d) Trace formula geometric side: implementation broken (K_geom < 0 from wrong parabolic normalization). Confirms and extends X.8, X.16.


## X.20: S123 (Grothendieck splitting)

**W_N = spacetime parity analogy [DEAD, S123].** W_N is the Fricke involution on the modular curve, acting on τ → −1/(Nτ). SM parity P acts on spacetime: x → −x, A_μ → −A_μ. The two operations act on different spaces and have no established mathematical relationship. The claim "gauge field is W_N-odd because A_μ is P-odd" conflates modular and spacetime symmetries. The 1-bit selection of W₆-odd remains empirical (≈2400σ confirmed, not derived).


## X.21: S125–S132 (DFT cipher operator, 28 dead directions)

28 independent approaches within the monodromy/cipher framework tested, all DEAD. Key categories:

**Operator spectrum → n** (D1,D5,D17,D20,D25,D28): No operator has eigenvalues = n. The cipher encodes n on the DIAGONAL, not in the spectrum.

**Graph operator → face-internal position** (D1,D3,D15): Monodromy operator diagonals cannot see position within σ∞-cycles. σ∞-dependent part of particle identity is invisible to products of σ₀, σ₁.

**Polynomial Δ from bits** (D13): Composition Φ∘n = n³(L−n) creates LD-irreducible primes {103, 151, 167}. Structural: Φ cubic × n degree-2 = degree 6.

**Spectral flow / coupling** (D17,D19,D21–D23,D26–D28): H = L + g·C_n well-motivated but no LD value of g gives clean structure.

**Hodge / CW approaches** (D6,D7,D9,D10): Hodge Laplacian Δ₁ does not correlate with n, ℓ, or Φ−Lℓ.

Full list D1–D28: see DFT_consolidated_S125_S131.md §9 and companion §S.10.

## X.22: S134 — Heat kernel diagonal → δK (DEAD)

h(e,e;t) = [exp(−tL)]_{ee} cannot reproduce Φ−Lℓ at any t. Root cause: exp(−tL) is a function of L; Φ−Lℓ has 68% energy off-diagonal in L-eigenbasis. Quantitative: ||[L, diag(Φ−Lℓ)]||/||diag(Φ−Lℓ)|| = 2.47. Best Pearson r = 0.522, R² = 0.267. Structural: ℓ = f(σ∞), n = f(σ∞, σ₀), but L encodes {σ₀, σ₁} not σ∞.

## X.23: S134 — det variation d/dv[ln det(BB^T)] → δK (DEAD)

Correlation r = −0.06. Self-energy from rank-1 perturbation does not reproduce δK.

## X.24: S135 — Heat equation exp(−t(L+a·diag(w))) → δK (DEAD)

Best R² = 0.37. Exponential of any L-based operator cannot produce the cubic Φ(n).

## X.25: S137 — Kaluza-Klein on M⁴ × ℙ¹ (DEAD)

4 kill-tests: (1) operator order 2 ≠ 4; (2) continuous spectrum [1/4,∞); (3) best R²=0.57; (4) m²∝eigenvalue (polynomial) vs m∝μ^{n/4} (exponential).

## X.26: S134 — Additional dead directions

2D CFT / Moonshine: conformal dimensions ≠ cubic Φ(n). Pre-killed.
det'(D_F + twist): algebraic equation, not differential. Pre-killed.
Variational reformulation of BVP: repackaging of G.2, no new content.

## X.27: S138 — Heat kernel on C₆ → CKM (DEAD)

u, d diametrically opposite in 6-cycle. Diffusion gives INVERSE hierarchy: λ_eff > 1 for all t.

## X.28: S138 — Schur complement up vs down → CKM (DEAD)

L_ud ≈ 0: up and down quarks almost isolated in Cayley graph. V_CKM ≈ I.

## X.29: S139 — Edge Laplacian, UST cycles, t₆-roots (DEAD #30–32)

(#30) Edge Laplacian (B^TB, D^TD, Hodge, line graph): best r = 0.56, signs 4/12. Structural: graph Laplacians constant within Aut(G) = ⟨c↔p⟩ orbits.
(#31) UST fundamental cycles: only 5 distinct profiles (= edge type classes V.1). R² ≈ 0. Structural: cycles are graph objects, don't encode σ∞-position within face.
(#32) t₆-root values at j = 0, j = 1728: best R² = 0.33. Vertex data; edges need pair data.

## X.30: S140 — Coset norms, UST fund. cycles, ℂ[Mon] diagonal, ring NLO (DEAD #33–36)

(#33) Coset Eisenstein/Gaussian norms → Φ−Lℓ: best r = −0.43. c and p have SAME norms but Φ−Lℓ = 6.4 vs 27.4 (Aut(G) symmetry).
(#34) UST fundamental cycles → Φ−Lℓ: r = 0.14. Bridges (u, t) undefined.
(#35) ℂ[Mon] diagonal tautology: rank of diag(P(L,σ∞), deg ≤ 8) = 12 = full. ANY 12-vector expressible. Φ−Lℓ not distinguished. Confirms X.16.
(#36) Ring NLO → individual δK: per-particle effect ~10⁻⁷, negligible vs δK ~ 10⁻².

## X.31: S141 — t₆-plane edges, τ-plane modular forms (DEAD #37–38)

(#37) t₆-plane edge invariants: 1194 Newton steps, 0 lost assignments. ∫ω dt₆ ≈ constant for all edges. Best single-feature r ~ 0.53. Structural: t₆ is rational, carries only combinatorial info.
(#38) τ-plane modular forms (E₂, E₄, E₆, η, E₂*, f₁–f₄) at 12 coset τ-points: Im(E₂) vs δK: r = −0.75, p = 0.005 — BUT same |r| at ALL j-values (not j-specific). Re(τ_k) fixed by coset structure, ranking invariant. 2D fit R² = 0.57 < F.1 R² = 0.68.

## X.32: S141 — Full modular scan and multi-feature fits (DEAD #39, 39b)

(#39) 130 j-values × 16 features × 2 assignments = 3936 tests. Global best: |r| = 0.79 (E₆_im, j = 1286.2, assignment B). j = 1286.2 not LD-special. LEE corrected: p ≈ 1.
(#39b) 16 LD-special j × 39 features × all 2-param, 3-param fits. Best adj R² = 0.67 (j = 1296 = 6⁴, 3 params). Scramble p = 0.007 (real but weak). ALL below F.1 R² = 0.68 at 0 parameters.

**Cumulative dead: 39 directions (S139–S141).** Structural barrier: X₀(6) geometry fully encodes (n, ℓ, K) but does NOT determine δK without dynamics (action principle). Edge-level modular invariants at coset-specific τ-points contain no per-particle information beyond what (n, ℓ, K) already encode.

## X.33: S143–S144 — τ*, CG coefficients, R→CKM (DEAD #40–42)

(#40) **τ* = i·ln(μ)/π as derivation of mass hierarchy** [DEAD, S143–S144]. Inversion, not derivation: 1 parameter (Im τ) on 1 observable (μ). Precision ~1.8 ppm is trivial consequence of small nome |q*| = μ⁻² ≈ 3×10⁻⁷. Any three η-quotients with distinct leading q-powers give comparable match.

(#41) **K from Clebsch–Gordan of S₃ × A₄** [DEAD, S144]. V₆ component of v₂, v₃ has rank 2 (C.7b). K-cipher structurally CRT-irreducible without additional physics beyond Mon representation theory.

(#42) **R-identity (W.1) → CKM directly** [DEAD, S144]. R encodes ramification data d₁³, d₂² (zeros at −d₁³, −d₂²), while CKM uses UST data d₁², d₂² (§V.4). d₁² ≠ d₁³; modular-function bridge absent.

**Cumulative dead: 42 directions (S143–S144).**

## X.34: S145 — Eisenstein g_k basis (DEAD #43)

G_d(τ) = E₂(τ) − d·E₂(dτ) for d ∈ {2,3,6}, spanning dim M₂(Γ₀(6)) = 3. Analytic results: G₂ zero set = {u,t,s,W} = P¹(𝔽₂)-coset (σ₁-closed) [THM-arith]; |G₃|/(c²+d²) takes exactly 2 values with ratio 2+√3 = fund. unit ℤ[√d₂] [THM-arith, 80-digit]; G₆ = G₂ + 2G₃(2τ) [THM, err < 10⁻⁸⁰]; intrinsic phase arg(G₃) − 2arctan(c/d) = kπ/2, 4 values = P¹(𝔽₃) [THM-arith].

**DEAD for δK:** correlation |G₂·G₃|/(c²+d²)² vs Φ−Lℓ: r = 0.52. Confirms X.21 barrier. Eisenstein forms analytically realize CRT (C.7) but do NOT reach δK.

## X.35: S145 — M_opt quark/lepton blocks → CKM/PMNS (DEAD #44)

Full 12×12 M_opt reconstructed from monodromy (T.8). Per-irrep trace = −192/7 = −d₁⁶d₂/L: tautological (transitivity of Mon action). CKM from quark UU/DD block: |V_ud| = 0.82 vs exp 0.97. DEAD. PMNS from lepton block: sin²θ₁₂ = 0.088 vs 4/13 = 0.308. DEAD. M_opt eigenvalues not LD monomials (except V₁). 84.9% off-diagonal norm. M_opt is not a physical mass matrix. 7M_opt denominators {1, d₁, d₁²}.

**Cumulative dead: 44 directions (S145–S146).**

## X.36: S147 — Naive HK–modular form bridge (DEAD #45)

w_ρ(e) ≠ |Y_ρ(i)|² (verified all irreps). Projector weight on P¹(ℤ/6ℤ) vs modular form on ℍ/Γ(6): different geometric objects, one group. Also: √d₂ in M_lep (disc = 4d₂, graph) and √d₂ in std_{S₃} (sin(2π/3), algebra) are structurally independent — M_lep NOT Mon-equivariant, BV-projection spec has no √3 (D.8). Bridge requires dessin geometry, not just group algebra. See I.9g.

**Cumulative dead: 45 directions (S147–S148).**

## X.37: S149 — δK from UST joint probabilities (DEAD #46)

Pearson r(Φ − Lℓ, ΣI²) = 0.60. UST joint probabilities distinguish 4 edge classes (bridge, multi, interior, boundary) but NOT individual particles within a class. The σ∞-position (which determines n and hence Φ) is invisible to UST — consistent with S.10 barrier (graph doesn't see within-cycle order). See V.8.7.

## X.38: S149 — Z₄ charges on P¹(ℤ/6ℤ) elements (DEAD #47)

arg((ci+d)²) at τ = i is exact multiple of π/2 only for 3/12 particles (p, c, u). For 9/12 the phase is irrational × π. Root cause: σ₁ is fixed-point-free on P¹(ℤ/6ℤ) → diagonal elements of ρ(S) = 0 → Z₄ charge ill-defined in permutation representation (Tr(ρ(S)) = 0). Feruglio Z₄ mechanism applies to irrep components V₁⊕V₂⊕V₃⊕V₆, not to individual particles. See I.9h.

## X.39: S149 — Φ−7ℓ as Eisenstein form on coset points (DEAD #48)

Φ − Lℓ takes 11 distinct values for 12 particles. dim M₂(Γ₀(6)) = 3 (all Eisenstein, zero cusp forms). Rank 11 ≫ 3 → Φ − Lℓ CANNOT be a modular form evaluated at 12 coset points. Φ is polynomial from BVP (G.2), not modular in τ. Connection to modular forms is indirect only.

**Cumulative dead: 48 directions (S149).**

## X.40 (S150): DDT/M_opt as Gap 3 live direction (DEAD #49)

M_opt ∈ ℂ[Mon] (T.5, T.8). The S.10 barrier (28 DFT dead directions) establishes that α/(2π) cannot emerge from Mon/cipher algebra. Since Gap 3 asks for the coupling α/(2π), and M_opt reproduces only the discrete content Φ − Lℓ (which is already [THM]), M_opt is inside the S.10 barrier.

**Note:** The mathematical question "what physical principle selects min ‖a‖²?" (T.9) remains open but is not a Gap 3 direction — it concerns the discrete structure, not the coupling.

## X.41 (S153): Weight-k modular forms at coset points, k < 10 (DEAD #50)

Rank barrier (S.12): dim M_k(Γ₀(6)) = k+1 < 11 = rank(Φ−Lℓ) for all k < 10.
No linear combination of weight-k forms evaluated at 12 coset points can
reproduce Φ−Lℓ. This is a theorem, not a numerical failure.

Explicit verification at weight 4 (dim 5): r = 0.65, adj R² = −0.07 (below F.1 at 0 params).
Weight-2 baseline: r = 0.67. No improvement despite 2 additional degrees of freedom.

Kills retroactively: X.34, X.43, S141 scan, and any future attempt at weight 6, 8.
Class A in barrier taxonomy.

**Cumulative dead: 50 directions.**


## X.42: S156 — E₂ⁿ·fₖ ratio test (DEAD #51+)

**E₂·f₁₀ ratio test [THM-arith, S156]:** For the quasi-modular product (E₂·f_k)|_{k+2} evaluated at 12 coset images of τ=i, the σ₁-pair ratio S/D = (Φ−Lℓ pair sum)/(Φ−Lℓ pair diff) must equal the complex ratio (Δ_a−Δ_b)/(2E₂(i)+Δ_a+Δ_b) where Δ_e is the E₂ correction at coset e.

RHS is purely imaginary for all 6 pairs (5 proven, 1 pole). LHS is real. 6/6 DEAD.

**Universal E₂-modulus identity [THM-arith, S156]:** |E₂(i) + Δ_e| = E₂(i) = 3/π for all e. Proof: (1−2c²/N)² + 4c²d²/N² = 1 (algebraic identity, N = c²+d²).

**Upgrade to all E₂ⁿ:** A_a/A_b ∈ S¹ → (Aⁿ−Bⁿ)/(Aⁿ+Bⁿ) = i·tan(nφ), purely imaginary for all n ≥ 1.

**DEAD: E₂ⁿ·fₖ at τ=i for ALL n ≥ 1, ALL even k.** [THM-arith, S156]. Convention-independent (verified both T=σ∞ and T⁻¹=σ∞).

**S155 erratum confirmed:** n(e) = 0, not 3. Pair sum (d,e) = −484/7. S155 value −376/7 used n(e)=3 (μ-value). Fails Σ control.

Cumulative dead: **51+ directions** (50 from S153 barriers + infinite E₂ⁿ family closed by single theorem).


## X.43 (S157): Elliptic fixed point collapse at τ=i and τ=ρ (DEAD #52)

**Class I barrier [THM-arith].**

S = [[0,−1],[1,0]] fixes τ=i. S ∉ Γ₀(6) (bottom-left c=1, 6∤1).
Cosets (0:1) and (1:0) are distinct in P¹(ℤ/6ℤ) but both map to i.
12 coset images → 11 distinct ℍ-points.

Inconsistency: (0:1) = anchor p with Φ−Lℓ(p) = 192/7;
(1:0) = quark c with Φ−Lℓ(c) = 45/7. f(i) cannot equal both → NO SOLUTION.

Even hypothetically: 11 distinct points with dim M₁₀ = 11 → 11×11 square
→ Class C tautology (fits any target, no discriminating power).

At τ=ρ: Stab(ρ) = ⟨ST⟩ of order 3. Γ₀(6) torsion-free (no solutions to x²≡−1 or x²+x+1≡0 mod 6) → ⟨ST⟩ acts freely on 12 cosets → 4 orbits of size 3 → **4 distinct ℍ-points**. rank(Φ−Lℓ) = 11 ≫ 4.

**Scope:** ALL functions on ℍ (holomorphic, Maass, continuous) evaluated pointwise at coset images of τ=i or τ=ρ. Weight-independent.
**Does NOT cover:** τ₀ ≠ i,ρ; non-pointwise functionals; slash actions at non-CM points.
**Complementarity with Class H:** H proves more at τ=i (kills E₂ⁿ·fₖ for all n,k specifically). I covers broader function class (not just quasi-modular). Non-overlapping proofs.

Deps: O.1, G.0a (Φ−Lℓ values for p and c).

### Erratum X.44 (S157): n(p) = 4, not 0

S157 draft code had n(p) = 0 → Σ = −960/7 (WRONG). Correct: n(p) = 4, ℓ(p) = 0
→ Φ−Lℓ(p) = 192/7, Σ = −768/7 ✓. Cross-checked with G.0a σ₁-pair table.

**Cumulative dead: 52 directions.**


## X.45 (S158–S160): Weight-10 at non-CM τ₀ + Petersson products (DEAD #53–54)

### X.45a: Weight-10 at 3 non-CM τ₀ (S158, 🟡 SOFT DEAD; anchor dominance upgraded S166)

3 non-CM τ₀ tested: i/√6 (Fricke), i√2 (Heegner D=−8), 0.3+0.7i (generic).
10/12 particles fit weight-10 forms to sub-percent at ALL τ₀.
Only {p,c} fails — anchor pair captures 97–99.9% of total residual.

S-constraint [OBS]: for f ∈ M₁₀(Γ₀(6)) and τ₀ ∈ ℍ:
f(−1/τ₀) = τ₀¹⁰·f(τ₀). Since γ_p = I and γ_c = S:
f(τ_p) and f(τ_c) rigidly linked. 11 DOF − 1 = 10 effective for 12 targets.

**Status upgrade (S166, I.9j):** Anchor pair {p,c} dominance is now [THM-arith + THM-comp].
{p,c} is the unique elliptic σ₁-pair (L = ±S, |Tr| = 0). Null-space ≥ 98% on {p,c}
at all tested generic τ₀. Geometric cause: S elliptic → minimal d_hyp(τ_p, τ_c).

### X.45b: Coset-twisted Petersson products (S159–S160, DEAD #54)

Coset-twisted Petersson products give face-constant values:
ψ(e) = μ(w)/w = {1, −1/d₁, −1/d₂, 1/N}. Only 4 values → DEAD for Gap 3.

**Class I′ barrier [THM-arith]:** Γ₀(6)\SL₂(ℤ)/Γ₀(6) = 4 = σ₀(6) double cosets.
Sizes: {1, 2, 3, 6} = cusp widths = Div(6). [Standard result for squarefree N.]
Any bi-Γ₀(6)-invariant functional takes at most 4 values. rank(Φ−Lℓ) = 11 ≫ 4.

Kills: coset-twisted Petersson products, period polynomials for Gap 3,
any Hecke-type trace restricted to Γ₀(6)-automorphic objects.
No loophole within bi-Γ₀(6)-invariance. To see particles, must BREAK Γ₀(6).

Deps: standard (double coset decomposition for congruence subgroups).

## X.46 (S166): M₂(Γ(6)) pointwise eval at generic τ₀ (DEAD #56)

dim M₂(Γ(6)) = 12 = #particles [THM-arith, S165].

Eval map at generic τ₀ ≠ i: rank = 12 (DUAL-COMPUTE at 4 τ₀ values).
Any 12-vector achievable → Class C (no discriminating power).
Random targets fit with residual 10⁻¹¹. LD target: no better.

At τ₀ = i: rank = 11 (Class I, τ_p = τ_c = i confirmed by I.9j).

Codimension argument: zero-residual τ₀ exists for ANY target (2 real
equations on 2 real parameters). Random targets fit BETTER than LD.
Not LD-specific.

Direction 🟢 #4 (barriers file) → 🔴 DEAD #56 (Class C).

Deps: I.9j (elliptic collapse at i), C (tautological dimension match).

## X.47 (S168): Additive δK formula without face(σ₁) (DEAD — structural barrier)

Doublet diagnostic at n=3: ℓ-splitting has WRONG SIGN (ratio = −0.17).
Any formula δK = g(Φ−Lℓ) or δK = g(Φ, ℓ) without face(σ₁) cannot fix this,
because at same n, Φ cancels, and the ONLY prediction comes from ℓ-splitting.

Systematic scan of ~20 functional forms f(n, ℓ, K) confirms: best R² = 0.74
with 2 continuous parameters. R² > 0.90 unreachable without face(σ₁).

The n=3 barrier is structural: s (σ₁→W, face 2) and μ (σ₁→b, face 6) require
opposite corrections relative to F.1 prediction. No function of (Φ−Lℓ) alone
can reverse the sign of one doublet while preserving the others.

Deps: G.0 (LO rule), O.1 (σ₁ map).


## X.48 (S169): σ₁ face Markov chain — Möbius spectrum [THM-arith]

### Statement

The row-stochastic matrix T on Div(N), defined by

T_{f₁,f₂} = #{e ∈ {1..12} : face(e)=f₁, face(σ₁(e))=f₂} / f₁,

has characteristic polynomial

det(T − λI) = ∏_{d|N} (dλ − μ(d))/d

Eigenvalues: **λ_d = μ(d)/d** for each d | N:

| d | μ(d) | λ_d | LD interpretation |
|---|------|-----|-------------------|
| 1 | +1 | 1 | trivial (stationary) |
| 2 | −1 | −1/d₁ | ramification at j = 1728 |
| 3 | −1 | −1/d₂ | ramification at j = 0 |
| 6 | +1 | 1/N | level |

### Eigenvectors (right)

- v₁(f) = 1  (constant)
- v_p(f) = 1 if p|f, else −p  (for each prime p|N)
- v_N(f) = μ(N/f)·(N/f)  (Möbius-weighted)

### Properties [ALL VERIFIED, Fraction arithmetic]

- T is **self-reversible**: T = T̃ (detailed balance with π(f) = f/index). [THM-arith]
- Stationary distribution: π(f) = f/index = f/12. [THM-arith]
- All eigenvalues have |λ| ≤ 1. Spectral gap = 1 − 1/N = 5/6.

### Explicit T matrix

```
T = [[0,     0,    0,    1   ],
     [0,     0,    1/2,  1/2 ],
     [0,     1/3,  0,    2/3 ],
     [1/6,   1/6,  1/3,  1/3 ]]
```

### Proof of eigenvalue formula

Direct verification: sympy factor of char poly gives (λ−1)(2λ+1)(3λ+1)(6λ−1) = ∏_{d|6}(dλ−μ(d)).

Deps: O.1 (monodromy → face(e), face(σ₁(e))).


## X.49 (S169): h spectral decomposition — all coefficients LD monomials [OBS]

### Statement

In the T-eigenbasis {v_d : d|N}:

h = (d₂²/d₁³)·v₁ − (1/d₁⁴)·v_{d₁} − ((N−1)²/(d₁³d₂²))·v_{d₂} − (L/(d₁⁴d₂²))·v_N

All four coefficients are LD monomials.

h·f = (dim M₁₀/d₂)·v₁ + (dim M₁₀/(d₁³d₂))·v_{d₁} + **0**·v_{d₂} − (1/d₁³)·v_N

**Key constraint:** h·f has **zero** v_{d₂} component. (Equivalently: h·f ∈ span{v₁, v_{d₁}, v_N}.)

### Independence status [S171-CORRECTED]

h·f ⊥ v_{d₂} is **NOT** automatic for (1)+(2). On the full 2-parameter (1)+(2) family h(s,t) = (s, 9/4, (9−s−6t)/3, t):

Σ_{f|N} f² h(f) v_{d₂}(f) = 6(3t − s)

This vanishes **iff** s = 3t, i.e., h(1) = d₂·h(6). The orthogonality is an **independent constraint** [OBS], equivalent to h(1)/h(6) = d₂.

**S170 stated** this was automatic (a reformulation of (2)). **S171 audit** showed this was incorrect: S170 verified orthogonality on the *restricted* subfamily h₁ = d₂h₆ (inherited from S169 G.0c's wrong DOF count), not the full (1)+(2) family.

### p-adic weight sums [OBS]

Σ_{f|N} f·v_p(h(f)) = d_q (cross-prime, where {p,q} = {d₁,d₂})

Specifically: Σf·v₂(h(f)) = d₂ = 3, Σf·v₃(h(f)) = −d₁ = −2.

### Additional identities

- Σh(f)·f = d₂³/d₁ = 27/2
- Σh(f)·f² = 44 = Σn = d₁²·dim M₁₀
- ⟨π,h⟩ = d₂²/d₁³ = 9/8
- ∏h = d₂ = 3

Coefficients of h·f involve dim M₁₀ = 11 — linking NLO mass rule to weight-10 modular forms.

Deps: X.48 (eigenbasis), G.0b (h values).


## X.50 (S169): Scattering identification of ⟨π,h⟩ [OBS]

### Statement

⟨π, h⟩ = d₂²/d₁³ = 9/8 = Π₊₋/Π₋₊

where Π_{s₂s₃} = e_{s₂}(d₁)·e_{s₃}(d₂) are products of Atkin-Lehner eigenvalues of the scattering matrix Φ₆(s) at s = d₁.

### Mechanism (refined S171)

Using the closed forms from X.56:

Π₊₋/Π₋₊ = [e₊(d₁)/e₊(d₂)] / [e₋(d₁)/e₋(d₂)] = h(2)/h(1) = (d₂²/d₁²)/d₁ = d₂²/d₁³

The scattering ratio decomposes as the quotient of two h-values:
- Numerator: e₊ cross-ratio = h(2) = tan γ_CKM [THM V.4]
- Denominator: e₋ cross-ratio = h(1) = d₁ [THM-arith X.56]

**Not an algebraic identity:** fails at (d₁,d₂) = (1,6), (3,4), (2,5), (3,2). Specific to (2,3).

### S170 progress (X.55)

The **numerical value** d₂²/d₁³ is now derived from Catalan (X.55). The **identification** ⟨π,h⟩ = Π₊₋/Π₋₊ remains [OBS].

Deps: L.1–L.4 (scattering matrix), G.0b (h), X.56 (closed forms for e₊, e₋).


## X.51 (S169): Extremal principle for ∏h [THM-arith]

### Statement

On the 1-parameter family h(t) = (3t, 9/4, 3−3t, t) defined by constraints (1)+(2)+(⊥):

∏_{f|N} h(f) ≤ d₂

with equality **iff** t = d₁/d₂ (the physical value).

### Proof

P(t) = (81/4)t²(1−t). Maximum at t = 2/3 by calculus: P'(2/3) = 0, P''(2/3) < 0. P(2/3) = 3 = d₂.

The cubic 27t³−27t²+4 = (3t−2)²(3t+1): **double root** at t = d₁/d₂. The product constraint is tangent to the linear family at the physical point.

### Scope [S171-CORRECTED]

This extremal principle operates on the **3-constraint** family (1)+(2)+(⊥), which is 1-dimensional. It does **NOT** operate on the full (1)+(2) family, which is 2-dimensional. On the 2-parameter family, max ∏h = 27/8 > d₂ at h = (3, 9/4, 1, 1/2), and the physical point is NOT extremal (∇P ≠ 0).

With the revised G.0c (4 linear constraints), the extremal principle is **not needed** for uniqueness — but remains a valid theorem about the (1)+(2)+(⊥) subfamily.

Deps: G.0c (derivation).


## X.52 (S169): Direction A — ω at cusps for h(f) — DEAD #57 (new Gap 3)

h(f) ≠ monomial in any combination of {R_cusp(ω,f), reg(ω,f), w(f), dist(BV₀,f), d₁, d₂}. Tested ~10⁶ combinations (integer exponents −4..4, all pairs). Zero exact matches on 3 finite faces.

σ₁ face transition matrix M (unnormalized) has palindromic char poly λ⁴−2λ³−7λ²−2λ+1, det(M)=1, Tr(M)=d₁, but spectrum contains √10 (not LD-algebraic). h is not an eigenvector of M.

Deps: K.1 (Hauptmodul), R.1–R.3 (regulators).


## X.53 (S169): Direction C — UST per-face for h(f) — DEAD #58 (new Gap 3)

**P(e ∈ UST) = P(σ₁(e) ∈ UST)** for all 12 edges. σ₁-pairs inherit edge type (bridge/multi/interior/boundary). All per-face UST statistics (sum P, mean P, product P, within-face |I|², cross-face |I|²) are **blind to face(σ₁)**.

Monomial scan: h(f) ≠ c · q₁(f)^a · q₂(f)^b for any pair of 9 tested face-level UST quantities.

Deps: V.1 (edge probabilities), V.8 (joint/transfer current), O.1 (monodromy).


## X.54 (S170): Character formula for h·f [THM-arith]

### Statement

d₁³ · f · h(f) = d₂³ − L·χ₂(f) − χ₃(f) − d₂·χ₂χ₃(f)

where χ₂(f) = (−1)^{v₂(f)} and χ₃(f) = (−1)^{v₃(f)} are Atkin-Lehner characters on Div(N).

| Character | Coeff ×d₁³ | LD monomial |
|-----------|-----------|-------------|
| 1 (trivial) | 27 | d₂³ |
| χ₂ | −7 | −L = −Φ₃(d₁) |
| χ₃ | −1 | −1 |
| χ₂χ₃ | −3 | −d₂ = −Φ₆(d₁) |

Sum of coefficients: d₂³ − L − 1 − d₂ = 27 − 7 − 1 − 3 = 16 = d₁⁴.

### Proof

Direct substitution, all 4 faces verified. ∎

### CRT partial factorization (X.54a) [THM-arith]

- v₃ = 0 (f ∈ {1,2}): d₁³fh = d₁·Φ₃(d₂) − |B₁|·χ₂(f)
- v₃ = 1 (f ∈ {3,6}): d₁³fh = d₁²·(L − χ₂(f))

Uses: Φ₃(d₂) = d₂²+d₂+1 = 13, |B₁| = L+d₂ = 10, Φ₃(d₁) = L = 7.

### Set identity (X.54b) [THM-arith]

d₁·f·h(f) for f ∈ Div(6) takes values {d₁², d₂², N, d₁³}:

| f | d₁fh | Monomial |
|---|------|----------|
| 1 | 4 | d₁² |
| 2 | 9 | d₂² |
| 3 | 6 | d₁d₂ = N |
| 6 | 8 | d₁³ |

Sum = d₂³ = 27. **Product = j(i) = 1728 = index³.**

### T upper triangular in AL basis (X.54c) [THM-arith]

The σ₁ face Markov chain T (X.48), expressed in the Atkin-Lehner character basis {1, χ₂, χ₃, χ₂χ₃}, is upper triangular:

T_AL = [[1, −1/d₁, −d₁/d₂, 1/d₂], [0, −1/d₁, 0, 1/d₂], [0, 0, −1/d₂, 1/N], [0, 0, 0, 1/N]]

Diagonal entries = T-eigenvalues μ(d)/d. All off-diagonal elements are LD monomials. T preserves the flag generated by AL characters ordered by divisor size.

Deps: G.0b (h values), L.1–L.4 (scattering eigenvalues), M.2 (cross-duality).


## X.55 (S170): Arithmetic chain Catalan → Π₊₋/Π₋₊ = d₂²/d₁³ [THM-arith]

### Statement

The scattering ratio Π₊₋/Π₋₊ = d₂²/d₁³ follows from the Catalan property d₁+1 = d₂ in five arithmetic steps:

| Step | From | To | Mechanism |
|------|------|----|-----------|
| (a) | \|d₁³−d₂²\| = 1 | d₁+1 = d₂ | Mihailescu (Catalan conjecture) |
| (b) | d₁+1 = d₂ | index = d₁N | index = (d₁+1)(d₂+1) = d₂·d₁² |
| (c) | index = d₁N | \|B₁\| = (N−1)d₁ | \|B₁\| = index − d₁ |
| (d) | \|B₁\| = (N−1)d₁ | d₂²+1 = \|B₁\|, d₁²+1 = N−1 | arithmetic |
| (e) | (d) | Π₊₋/Π₋₊ = d₂²/d₁³ | cancellation |

### Proof of step (e)

Π₊₋/Π₋₊ = (d₁+1)²(d₂²+1)/[(d₁²+1)(d₂+1)²] = d₂²·|B₁|/[(N−1)·d₁⁴] = d₂²/d₁³

using |B₁| = (N−1)d₁ from step (c). ∎

### Falsification

|B₁| = (N−1)d₁ ⟺ index = d₁N ⟺ d₁ = 2 (for squarefree N = d₁d₂). Analytical: d₂ = (d₁+1)/(d₁²−d₁−1), integer only at d₁=2.

### Scope

X.55 derives the **numerical value** d₂²/d₁³ = 9/8. It does NOT derive constraint (2) of G.0c, which states ⟨π,h⟩ = Π₊₋/Π₋₊. The **identification** remains [OBS X.50].

Deps: L.4 (Π eigenvalues), path #20 (Catalan), G.0b (|B₁| definition).


## X.56 (S171): Scattering eigenvalue closed forms and cross-prime h-identities [THM-arith]

### Statement

At the evaluation point s = d₁, the Atkin-Lehner scattering eigenvalues for p | N are:

e₊(p) = (p+1)/[p(p²+1)],   e₋(p) = −1/[p(p+1)]

Note: e₋ is **telescoping**: e₋(p) = −(1/p − 1/(p+1)).

| p | e₊(p) | e₋(p) |
|---|--------|--------|
| d₁ = 2 | 3/10 | −1/6 |
| d₂ = 3 | 2/15 | −1/12 |

### Cross-prime ratios = h-values [THM-arith]

e₊(d₁)/e₊(d₂) = d₂²/d₁² = h(2) = tan γ_CKM

e₋(d₁)/e₋(d₂) = d₁ = h(1)

### Proof of e₋ ratio

e₋(d₁)/e₋(d₂) = d₂(d₂+1)/[d₁(d₁+1)] = d₂·d₁²/(d₁·d₂) = d₁

using Catalan consequences d₁+1 = d₂ and d₂+1 = d₁². ∎

### Proof of e₊ ratio

e₊(d₁)/e₊(d₂) = (d₁+1)·d₂·(d₂²+1)/[(d₂+1)·d₁·(d₁²+1)] = d₂²·|B₁|/(d₁³·(N−1)) = d₂²/d₁²

using |B₁| = (N−1)d₁ from X.55. ∎

### Corollary: X.50 decomposition

Π₊₋/Π₋₊ = h(2)/h(1) = (d₂²/d₁²)/d₁ = d₂²/d₁³ = ⟨π,h⟩

This does NOT close X.50 (the identification ⟨π,h⟩ = Π₊₋/Π₋₊ is still [OBS]), but reduces it to the question why the **stationary average** of h equals h(2)/h(1).

### Product identities

e₊(d₁)·e₊(d₂) = 1/(N−1)² = 1/25

e₋(d₁)·e₋(d₂) = 1/(d₁³d₂²) = 1/|Mon| = 1/72

### Cyclotomic link (X.54d) [THM-arith]

(e₊(p) − e₋(p))/(e₊(p) + e₋(p)) = Φ₃(p)/p

| p | Φ₃(p) | Appears in h formula as |
|---|--------|------------------------|
| d₁ = 2 | 7 = L | χ₂ coefficient |
| d₂ = 3 | 13 | CRT branch (v₃=0) |

Key cross-duality identity: **Φ₆(d₂) = Φ₃(d₁) = L** (restatement of M.2).

Deps: L.1–L.4 (scattering eigenvalues), path #20 (Catalan), V.4 (tan γ = h(2)).


**Cumulative dead: 58+ directions.** (X.52 #57, X.53 #58. S172: direction (a) DEAD — 13 functionals, T_h similarity trivial. S173: direction (b) DEAD — Selberg diagonal Φ⁻¹Φ' cusp-blind.)


## X.57 (S172): Tensor factorization of σ₁ face Markov chain [THM-arith]

### Statement

For squarefree N = pq with distinct primes p, q:

T(Γ₀(pq)) = T^(p) ⊗ T^(q)

where T^(r) is the universal 2×2 Markov chain on {r∤f, r|f}:

T^(r) = [[0, 1], [1/r, (r−1)/r]]

Eigenvalues 1 and −1/r. Stationary distribution π^(r) = (1/(r+1), r/(r+1)).

### Proof

By CRT: P¹(ℤ/Nℤ) ≅ P¹(ℤ/pℤ) × P¹(ℤ/qℤ). The involution S = σ₁ acts componentwise on CRT factors: (c_r : d_r) → (d_r : −c_r) independently for each r | N. Edge counts in face f₁ = ∏r^{a_r(f₁)} going to face f₂ = ∏r^{a_r(f₂)} factorize, and normalization by f₁ = ∏r^{a_r} also factorizes. ∎

### Eigenbasis

The 4 eigenvectors factorize as tensor products of per-prime right eigenvectors:

| Mode | Tensor | Eigenvalue | Face vector (1,2,3,6) |
|------|--------|-----------|----------------------|
| v₁ | triv_p ⊗ triv_q | 1 | (1, 1, 1, 1) |
| v_p | sign_p ⊗ triv_q | −1/p | (d₁, −1, d₁, −1) |
| v_q | triv_p ⊗ sign_q | −1/q | (d₂, d₂, −1, −1) |
| v_N | sign_p ⊗ sign_q | 1/N | (N, −d₂, −d₁, 1) |

where triv_r = (1, 1) and sign_r = (r, −1).

π-weighted norms: **‖v_d‖²_π = d** for d | N. Proof: ‖triv_r‖²_{π^(r)} = 1, ‖sign_r‖²_{π^(r)} = r, so ‖v_d‖² = ∏_{r|d} r = d.

### Verification

DUAL-COMPUTE at 6 squarefree levels: N = 6, 10, 14, 15, 21, 35. All match T^(p) ⊗ T^(q) exactly (Fraction arithmetic).

Deps: O.1 (monodromy), CRT (standard).


## X.57a (S172): Catalan equivalence of (⊥) and (2) [THM-arith]

### Statement

Given (1): h(d₁) = d₂²/d₁² and (1'): h(1) = d₁, the constraints (⊥) and (2) reduce to:
- (⊥): h(d₂) + d₁²·h(N) = dim M₁₀/d₂ = 11/3
- (2):  h(d₂) + d₁·h(N)  = L/d₂ = 7/3

[A]−[B]: d₁(d₁−1)·h(N) = (dim M₁₀ − L)/d₂ = 4/3. At h(N) = d₁/d₂: consistency requires d₂² − d₁³ = 1 (Catalan/Mihailescu).

### Proof

Substituting h(N) = d₁/d₂ and checking: LHS = d₁²(d₁−1)/d₂, RHS = (d₁+d₂²−L)/d₂. Equality ⟺ d₁²(d₁−1) = d₁+d₂²−d₁d₂−1. With d₂ = d₁+1 this reduces to (d₂−1)(d₂+1) = d₁³ (Catalan). ∎

### Falsification

5 other prime pairs (2,5), (2,7), (3,5), (3,7), (5,7): derived h(pq) ≠ p/q. Unique to (2,3).

### Corollary

dim M₁₀ = d₁ + d₂² = 11: Class A barrier weight linked to Catalan pair.

**Consequence:** G.0c: **3 independent constraints + Catalan → unique h.** 2 [OBS] → 1 [OBS].

Deps: V.4, X.56, path #20, X.49, X.50.


## X.58 (S172): Kirchhoff identity for AL eigenvalue product [THM-arith]

### Statement

Π₊₋ = e₊(d₁)·e₋(d₂) = −1/K = −1/40

### Proof

e₊(d₁)·e₋(d₂) = (d₁+1)/[d₁(d₁²+1)] · (−1)/[d₂(d₂+1)] = −d₂/[d₁d₂(d₁²+1)(d₂+1)] = −1/[d₁(d₁²+1)(d₂+1)] = −1/40

using d₁+1 = d₂ (Catalan) and K = d₁(d₁²+1)(d₂+1) = 2·5·4 = 40. ∎

Complementary: |Π₋₊|⁻¹ = 45. Ratio: ⟨π,h⟩ = |Π₊₋/Π₋₊| = 45/K = 9/8 = d₂²/d₁³.

Deps: X.56, Catalan, K.1.


## X.58a (S172): Basis identity v_q ↔ AL [THM-arith, S175-CORRECTED]

### Statement

v_q = u_{++} + d₁·u_{+-}

Proof: u_{++} + d₁·u_{+-} = (1+d₁, 1+d₁, 1−d₁, 1−d₁) = (d₂, d₂, −1, −1) = v_q, using d₁+1 = d₂ and d₁−1 = 1. ∎

**S175 correction:** S173 wrote v_q = −(u_{++}+d₁·u_{+-}). The minus sign is incorrect. Impact: none — (⊥) ratio = −d₁ is unaffected.

### Uniqueness

Matching requires 1+d₁ = d₂ AND d₁−1 = 1, uniquely (p,q) = (2,3) among primes.

### Corollary

(⊥) ⟺ ⟨hf, u_{++}⟩_π / ⟨hf, u_{+-}⟩_π = −d₁

Deps: X.57, L.3.


## X.58b (S172): Non-commutativity [T, Φ/λ] ≠ 0 [THM-arith]

T-eigenbasis ≠ AL-eigenbasis (they differ by X.58a basis change). Verified: [T, Φ(d₁)/λ] ≠ 0 (Fraction arithmetic). h is eigenvector of neither T nor Φ(d₁)/λ.

**Consequence:** no T↔Φ simultaneous diagonalization bridge for Gap 3.

Deps: X.48, L.4.


## X.59 (S173): (⊥) via CRT duality involution [THM-arith]

### Statement

All four AL projections of h·f:

| AL mode | ⟨hf, u_mode⟩_π | Formula |
|---------|-----------------|---------|
| u_{++} | 11/3 | dim M₁₀/d₂ |
| u_{+-} | −11/6 | −dim M₁₀/N |
| u_{-+} | −11/6 | −dim M₁₀/N |
| u_{--} | 2/3 | d₁/d₂ |

### Main identity

**(⊥) ⟺ ⟨hf, u_{++}⟩_π / ⟨hf, u_{+-}⟩_π = −ι(d₂) = −d₁**

where ι(p) = (p+1)/(p−1) is the CRT duality involution (L.3). Derivation: from X.58a, (⊥) = ⟨hf, u_{++}+d₁·u_{+-}⟩ = 0 → ratio = −d₁ = −ι(d₂).

### Asymmetry

v_p = [(d₁−1)/2]·u_{++} + [(d₁+1)/2]·u_{-+}. p-ergodicity would require ratio ⟨hf,u_{++}⟩/⟨hf,u_{-+}⟩ = −ι(d₁) = −d₂ = −3. Actual: −2 ≠ −3. Root cause: ι(d₂) = d₁ but ι(d₁) = d₂ ≠ d₁.

Deps: X.57, X.58a, L.3.


## X.59a (S173): dim M₁₀ dominance in AL projections [THM-arith]

Three of four projections have dim M₁₀ = 11 as numerator (u_{++}, u_{+-}, u_{-+}). The fourth: u_{--} = d₁/d₂ = (dim M₁₀ − d₂²)/d₂ (via Catalan).

Deps: X.59, X.57a.


## X.59b (S173): Mixed AL projection equality ⟺ constraint (1) [THM-arith]

⟨hf, u_{+-}⟩_π = ⟨hf, u_{-+}⟩_π ⟺ 4h(d₁) = d₂²·h(d₂) ⟺ h(d₁)/h(d₂) = d₂²/d₁².

Proof: u_{+-} − u_{-+} = (0, 2, −2, 0). Inner product with hf vanishes iff (2/12)·h(2)·2·2 = (3/12)·h(3)·3·2, i.e. 4h(2) = 9h(3). ∎

Deps: X.59, V.4.


## X.60 (S174): q-dirt of face Markov chain [THM-arith]

### Statement

The tensor factorization T = T^(p) ⊗ T^(q) decomposes the q-factor:

T = T^(p) ⊗ I_q + T^(p) ⊗ (T^(q) − I_q)

The first term T^(p) ⊗ I_q is a "q-blind" chain where q-class is frozen. The second term, **q-dirt** ≡ T^(p) ⊗ (T^(q) − I_q), is the nontrivial q-component.

**S175 note (CONFLICT-RESOLVE):** S174 wrote "σ₁ on cusps = W₂ = σ_p ⊗ I_q". Strictly, S = σ₁ does NOT normalize Γ₀(6), so σ₁ does not induce a cusp permutation (S sends 3 of 4 cusps to face 6). However, the Atkin-Lehner W₂ IS a well-defined cusp involution from the normalizer (1↔2, 3↔6 = pure p-flip, q-blind). The comparison D = T − W₂ is a valid tensor-structural decomposition: it measures how much the edge-level Markov chain T differs from the q-blind cusp involution W₂. All downstream mathematics (X.60a, X.60b) is unaffected.

### Per-face T vs W₂ agreement

W₂ maps face f by flipping p-component, preserving q-component (1→2, 2→1, 3→6, 6→3):

| Face | W₂ target | T actual | Match prob |
|------|-----------|----------|-----------|
| 1 | →2 | →6 (100%) | 0% |
| 2 | →1 | →3 (50%), →6 (50%) | 0% |
| 3 | →6 | →2 (1/3), →6 (2/3) | 2/3 |
| 6 | →3 | →1 (1/6), →2 (1/6), →3 (1/3), →6 (1/3) | 1/3 |

Deps: X.57.


## X.60a (S174): v_q spectral shift — q-dirt kills stationarity [THM-arith]

### Statement

| Mode | q-blind T^(p)⊗I_q | actual T^(p)⊗T^(q) | Change |
|------|-------------------|---------------------|-------|
| v₁ | 1 | 1 | — |
| v_p | −1/d₁ | −1/d₁ | — |
| **v_q** | **1** | **−1/d₂** | **stationary → decaying** |
| v_N | −1/d₁ | 1/N | rate change |

v_q is the **unique** mode with qualitative status change. Under q-blind dynamics, v_q would be stationary (preserved forever). The nontrivial T^(q) converts it to decaying with rate 1/d₂.

Deps: X.57, X.60.


## X.60b (S174): (⊥) ⟺ q-marginal equilibrium R = d₂ [THM-arith]

### Statement

Define q-marginal ratio R = [Σ_{q|f} π(f)·h(f)·f] / [Σ_{q∤f} π(f)·h(f)·f].

Then (⊥) ⟺ R = d₂ = 3.

### Proof

Given (1') and (1), the denominator Σ(q∤) = (1/12)·d₁ + (2/12)·(d₂²/d₁²)·2 = 11/12 is fixed. R = d₂ ⟺ Σ(q|) = d₂·(11/12) = 11/4 ⟺ h(d₂)+d₁²h(N) = 11/3 ⟺ (⊥). ∎

**Note:** Constraint (1) forces R(p) = R(q) = 3 = d₂. q-stationarity: R = d₂ (satisfied). p-stationarity: R = d₁ = 2 (violated).

Deps: X.57, X.57a.


### [OBS] (S174): Autonomous vs coupled q-oscillation

h·f energy decomposition: v₁ 96.3%, v_p 3.0%, v_q **0%**, v_N 0.7%.

(⊥) kills v_q (triv_p ⊗ sign_q) = autonomous q-oscillation, but NOT v_N (sign_p ⊗ sign_q) = q-oscillation coupled through p.

Physical motivation [СПЕКУЛЯЦИЯ]: if σ₁ is a "p-operator", it can create q-effects only through p-coupling, not autonomously. Formalization missing: why h inherits this structure from the operator that defines it remains open.


## X.61 (S176): σ₁ = complete CRT scrambler [THM-arith]

σ₁ preserves neither the P¹(𝔽₂) nor the P¹(𝔽₃) CRT coordinate for ANY of the 12 edges. Score: 0/12 for both. σ₁ as Möbius S: (c:d) → (d:−c) is fixed-point-free in affine coordinates on P¹(ℤ/6ℤ).

Deps: C.7, O.1.


## X.62 (S176): face·face(σ₁) ∈ N·Div(N) [THM-arith]

The product face(e)·face(σ₁(e)) takes exactly 4 values:
{6, 12, 18, 36} = N·Div(N) = {N, index, d₁d₂², N²}.

Multiplicities: (4, 2, 4, 2) — palindromic. ∏(all 12) = 2¹⁶·3¹⁸.

| Value | = | Particles | Count |
|---|---|---|---|
| 6 | N | c, τ, H, p | 4 |
| 12 | index | s, W | 2 |
| 18 | d₁d₂² | b, d, e, μ | 4 |
| 36 | N² | u, t | 2 |

Deps: O.1.


## X.63 (S176): Diametrically opposite n-sums in 6-cycle [THM-arith]

σ∞³ pairs diametrically opposite quarks:
- (c, s): n+n' = 4+3 = 7 = L
- (u, d): n+n' = 1+1 = 2 = d₁
- (b, t): n+n' = 5+7 = 12 = index

∏(pair sums) = L·d₁·index = 168 = d₁³d₂L. All three sums = LD invariants.

n-autocorrelation (unnormalized, shift k):
C(0)=55/2, C(1)=−23/2, C(2)=−27/2, C(3)=+45/2.
Shift 3 (opposite) gives maximum positive correlation among k>0.

Deps: O.1, F.3.


## X.64 (S176): Periodic points of (σ₁σ₀)^k [THM-arith]

| k | Fix((σ₁σ₀)^k) | \|Fix\| | Σn | LD |
|---|---|---|---|---|
| 1 | {p} | 1 | 4 | d₁² |
| 2 | {p, H, W} | 3 | 16 | d₁⁴ |
| 3 | {p, e, μ, τ} | 4 | 11 | dim M₁₀ |
| 6 | all 12 | 12 | 44 | d₁²·dim M₁₀ |

k=3 fixes anchor + ALL leptons. Mechanism: σ₁σ₀ has cycle type (6,3,2,1) — quarks in 6-cycle, leptons in 3-cycle, bosons in 2-cycle, anchor fixed. Fixed at k ⟺ cycle length divides k.

Deps: O.1.


## X.65 (S176): Commutator [σ₀, σ₁] structure [THM-arith]

[σ₀, σ₁] = σ₀σ₁σ₀⁻¹σ₁ has cycle type (6, 6). Order = 6 = N.

| Orbit | Members | Σn |
|---|---|---|
| 1 | (c e s b τ t) | 23 |
| 2 | (u H μ W d p) | 21 = d₂L |

Difference: 23 − 21 = 2 = d₁. Orbit 2 contains anchor p and one n=ℓ particle (W).

**S177 correction:** S176 text stated "both n=ℓ particles" in orbit 2 — incorrect. The two n=ℓ particles are s (orbit 1) and W (orbit 2), one in each orbit.

Deps: O.1.


## X.66 (S176): Bilinear sums table [THM-arith]

| Sum | Value | LD identification |
|---|---|---|
| Σ(n+ℓ) | 90 | d₁d₂²(N−1) |
| Σ(n·ℓ) | 154 | d₁L·dim M₁₀ |
| Σ(face·n) | 175 | (N−1)²L |
| Σ(face(σ₁)·n) | 180 | d₁²d₂²(N−1) |
| Σ(face(σ₁)·ℓ) | 200 | d₁³(N−1)² |
| Σ(face(σ)·face(σ')) | 192 | d₁⁶d₂ (all 3 cross-pairs) |

Σ(face(σ₁)·n) − Σ(face·n) = 5 = N−1.
Σ(face(σ₁)·h(face(σ₁))) = 44 = Σn (= C.8.3, since σ₁ is bijection → same distribution).

Deps: O.1, F.7, G.0b.


## X.67 (S176/S177): Cayley closed-walk traces [THM-arith, unique to X₀(6)]

| k | Tr(A^k) | LD identification |
|---|---|---|
| 1 | 0 | — (σ₁ fixed-point-free) |
| 2 | 40 | = K (Kirchhoff) |
| 3 | 30 | = N(N−1) |
| 4 | 224 | = d₁⁵L |

**All three nontrivial identifications unique to X₀(6)** among squarefree levels N ∈ {6, 10, 14, 15, 21, 35} (verified S177, see D.4 addendum).

Deps: I.6 (Cayley graph), D.4 (Kirchhoff).


## X.68 (S178): Tutte polynomial of face graph T(d₁,d₂) = index² [THM-arith]

Face graph: vertices = Div(N), edges from σ₁-pair face transitions. 6 edges (one per σ₁-pair), including 1 self-loop (u,t)→(6,6). Tutte polynomial:

T(x,y) = xy(x² + xy + x + y² + y)

**T(d₁,d₂) = T(2,3) = 6·24 = 144 = 12² = index².** Inner sum 24 = d₁³d₂.
**T(1,1) = 5 = N−1** = number of spanning trees of face graph (= K(face graph)).

Specific to (d₁,d₂) = (2,3): for (3,5), T(3,5) = 855 ≠ 576 = 15² = index² [claimed, NOT independently verified S178].

**38th path to (d₁,d₂) = (2,3).** New cluster: graph-polynomials.

Deps: O.1 (face graph structure). Verified S178: deletion-contraction on 2⁶ subsets.

## X.69 (S178): Face graph cuts [THM-arith]

q-partition {1,2}|{3,6} (by d₂-divisibility): **3 cross-edges = d₂.**
p-partition {1,3}|{2,6} (by d₁-divisibility): **4 cross-edges = d₁².**

Ratio p-cut/q-cut = d₁²/d₂ = **4/3 = K(c).**

**S178 correction (VERIFY-BEFORE-CORRECT applied):** Session text erroneously stated 4/3 = h(2) = tan²γ_CKM. In fact h(2) = d₂²/d₁² = 9/4 ≠ 4/3. The quantity d₁²/d₂ = 4/3 is K(c) (the charm multiplier from F.5), not h(2).

Deps: O.1 (face graph edges). Verified S178.

## X.70 (S178): Face graph degrees [THM-arith]

deg(1) = 1, deg(2) = 2 = d₁, deg(3) = 3 = d₂, deg(6) = 4 = d₁².

Convention: self-loop excluded from degree count. deg(f) = f for f < N; deg(N) = N − d₁ = d₁² (self-loop reduces effective degree by d₁−1 from the naïve f).

Deps: O.1 (face graph). Follows from face transition counts.

## X.71 (S178): BV→BV bipartite walk [THM-arith]

Two-step bipartite random walk BV→WV→BV with transition matrix P = BB^T/(d₁d₂), where B is the BV×WV incidence matrix (4×6).

Eigenvalues: {1, (N−1)/N, 1/d₂, 1/N} = {1, 5/6, 1/3, 1/6}. All LD monomials.

Self-return probabilities:
- P(BV₀→BV₀) = (N−1)/N = 5/6 (anchor special: multi-edge {c,p} creates high self-return)
- P(BV_i→BV_i) = 1/d₁ = 1/2 for i ∈ {1,2,3}

**Note:** This is the bipartite random walk (BB^T/6), NOT the σ₁-deterministic walk. The σ₁-walk has different eigenvalues {1, 2/3, −1/3, −2/3}.

Deps: D.2 (BB^T), O.1 (BV structure). Verified S178 (Fraction arithmetic + numpy eigenvalues).

## X.72 (S178): BV h-content symmetry [THM-arith]

h-distributions of BV₂(star) and BV₃(oth) are permutations: both have h-multiset {2/3, 1, 9/4}.

| BV | h-values | avg | prod |
|---|---|---|---|
| BV₀(anc) | {2/3, 2/3, 2} | 10/9 | 8/9 |
| BV₁(idx) | {2/3, 2/3, 1} | 7/9 | 4/9 |
| BV₂(star) | {2/3, 1, 9/4} | 47/36 | 3/2 = d₂/d₁ |
| BV₃(oth) | {2/3, 1, 9/4} | 47/36 | 3/2 = d₂/d₁ |

h-avg(BV₀)/h-avg(BV₁) = (10/9)/(7/9) = 10/7 = |B₁|/L.

Deps: O.1 (BV assignment), G.0b (h values). Verified S178.

## X.73 (S178): Absorption times to anchor BV [THM-arith]

Mean first-passage time of BV bipartite walk (X.71) to BV₀(anchor):

| Start | Absorption time | LD |
|---|---|---|
| BV₁(idx) | 18 | d₁d₂² |
| BV₂(star) | 24 | d₁³d₂ |
| BV₃(oth) | 24 | d₁³d₂ |

Ratio BV₂/BV₁ = d₁²/d₂ = **4/3 = K(c)** (same as cut ratio X.69).
Sum = 66 = N·dim M₁₀. Mean = 22 = d₁·dim M₁₀.

**S178 correction:** Session text stated ratio = h(2) = tan²γ. Correct identification: d₁²/d₂ = K(c). See X.69 correction note.

**K(c) = d₁²/d₂ = 4/3 appears in two independent graph-theoretic incarnations:**
(a) p-cut/q-cut [X.69], (b) absorption time ratio [X.73].
This does NOT equal h(2) = d₂²/d₁² = 9/4.

Deps: X.71 (BV walk), O.1. Verified S178 (Fraction Gaussian elimination).



## X.74–X.90 (S179–S184, audited S185): 17 results

### X.74 [THM-arith]: V.4 → AL signs (ε₂,ε₃) = (+1,−1). Deps: V.4, Catalan.
### X.75 [THM-arith]: L_p(k/2)·e₊(p) = 1/5. Deps: L.4, X.74.
### X.76 [THM-arith]: Z₂ quadratic (d₂y−d₁)(d₁²y−1) = 0 from (⊥)+∏h. Δ = (N−1)². Deps: G.0c.
### X.77 [OBS]: h(6) = L₂(k/2) = d₁/d₂. IF derived → Gap 3 closed. Deps: X.74, X.56.
### X.78 [THM-arith, S185-CORRECTED]: Z₂ discriminator. Both roots pass (⊥) by construction. Discriminator = (2). S185: deleted erroneous NOTE. Deps: G.0c, X.76.
### X.79 [THM-arith]: Z₂ trace (h(1)+4h(2))/12 = 11/12, automatic. Deps: G.0c.
### X.80 [THM-arith]: ℓ₂ = d₁/d₂, ℓ₃ = d₂/d₁, product = 1. Deps: X.74, Catalan.
### X.81 [THM-arith]: L₃ pole at s = d₁² = k/2−1. Deps: LMFDB.
### X.82 [THM-arith]: (⊥) = q-equidistribution (9th reformulation). Deps: G.0c, X.57.
### X.83 [THM-arith, S185-CORRECTED]: L_bad table. s=1: −1/[N·d₂·det(M_lep)] = −1/234. Deps: X.74, LMFDB.
### X.84 [THM-arith]: CRT fixed-point asymmetry. |Fix(S₂)|=1, |Fix(S₃)|=0. Deps: C.7.
### X.85 [THM-arith]: S-orbit classification. 4 flip-flip + 2 FIXED-flip. Deps: X.84, O.1.
### X.86 [THM-arith]: h(N) = d₁·T(N,N). Unique (2,3). Deps: X.48.
### X.87 [THM-arith+comp, S185-CORRECTED]: Rationality uniqueness. 1035 pairs (not 570). Deps: G.0c, C.8.4.
### X.88 [THM-arith]: CRT column equipartition (10th reformulation). Deps: C.7, C.8.6.
### X.89 [THM-arith]: P⁺ Z₂ discriminator (11th reformulation). Deps: X.76, LMFDB P⁺.
### X.90 [THM-arith+comp]: Complete j(t₆). BV cubic, Δ=−972. Deps: W.1, LMFDB.


## X.91 (S186-cont) [THM-arith]: Complete L-factor dictionary for h

L_p(k/2, 6.10.a.a) = (1 + W_p/p)⁻¹. L₂ = d₁/d₂ = 2/3, L₃ = d₂/(d₂−1) = 3/2.

| Face | h(f) | L-factor formula |
|---|---|---|
| 3 (leptons) | 1 | L₂·L₃ |
| 6 (quarks) | d₁/d₂ | L₂ |
| 2 (bosons) | d₂²/d₁² | L₃/L₂ |
| 1 (anchor) | d₁ | L₃(6.10.a.a)/L₃(3.10.a.b) |

In (L₂,L₃) exponents: f=3→(1,1), f=6→(1,0), f=2→(−1,1). All 2×2 exponent submatrices have nonzero det.
h(1) = L₃-transfer requires dim S₁₀^{(+,+)} = 1 (W.8 anchor anomaly).

**X.91a** [THM-arith]: L₂·L₃ = 1 ⟺ consecutive primes. Specific to Catalan.
**X.91b**: tan γ_CKM = L₃/L₂ = d₂²/d₁² (new interpretation of V.4).
**X.91c**: Anchor L-transfer: (d₂+1)/(d₂−1) = d₁. Equivalent to scattering X.56.
**12th formulation of Gap 3:** h(6) = L₂(k/2, 6.10.a.a).

Deps: W.4, W.8, X.74, Catalan.


## X.92 (S187) [THM-comp]: CRT factorization T = T₂ ⊗ T₃

T = T₂ ⊗ T₃ where T_p = [[0,1],[1/p,(p−1)/p]].
det(T_p) = −1/p. Eigenvalues {1, −1/p}. Stationary π_p = (1/(p+1), p/(p+1)).
Full T eigenvalues = products: {1, −1/d₂, −1/d₁, 1/N}.

Eigenvectors (face order {1,2,3,6}):
| λ | CRT type | Vector |
|---|---|---|
| 1 | triv×triv | (1,1,1,1) |
| −1/d₂ | 1×e₃ | (3,3,−1,−1) |
| −1/d₁ | e₂×1 | (2,−1,2,−1) |
| 1/N | e₂×e₃ | (6,−3,−2,1) |

4×4 eigenvector matrix invertible (det = −144).
Extends X.57 with full eigenvector/eigenvalue CRT correspondence.

Deps: O.1, C.7, C.8.5.


## X.92a (S187) [THM-arith]: (⊥) = zero pure-T₃-mode

w = f·h decomposition: d₁³d₂·a = (88, 0, −11, −3) for modes (1, −1/d₂, −1/d₁, 1/N).

**(⊥) ⟺ a(−1/d₂) = 0**: w has zero 1×e₃ component.
3-marginal of w constant = dim M₁₀/d₂ = 11/3.
All nonzero normalized coefficients {88, 11, 3} are LD monomials.

**13th formulation of Gap 3:** w ∈ ker(proj_{1×e₃}).

Deps: X.92, G.0b, G.0c.


## X.92b (S187) [OBS]: Z₂ discrimination in T-basis

Physical d₁³d₂·a = (88, 0, −11, −3): all numerators LD monomials.
Spurious d₁³d₂·a = (88, 0, 34, −18): 34 = 2·17, alien to LD.
Ratio a(1/N)/a(−1/d₁): physical = d₂/dim M₁₀ = 3/11; spurious = −9/17.
Characterization, not derivation. Status [OBS].

Deps: X.92a, G.0c, C.8.12.


## X.93 (S195) [THM-comp]: a_p(6.10.a.a) mod 12 congruence

For all good primes p < 500 (93 primes, 0 violations):

| p mod 12 | a_p mod 12 | LD monomial |
|----------|-----------|-------------|
| 1        | 2         | d₁          |
| 5        | 6         | N           |
| 7        | 8         | d₁³         |
| 11       | 0         | 0           |

Sum of residues = d₁ + N + d₁³ + 0 = 16 = d₁⁴ = |a₂|.

Source: CRT of mod-2 and mod-3 Galois representations.
- mod 3: ρ̄₃ reducible, a_p ≡ 1 + χ₃(p) mod 3.
- mod 2: all a_p even; a_p/2 odd iff p ≡ 1 mod 4 (93 primes, 0 violations).

Verified S201: 13 primes in first 50 coefficients, 0 violations.

Deps: LMFDB 6.10.a.a q-expansion.


## X.94 (S196) [THM-comp]: Discriminant uniqueness — Catalan controls rationality

For X₀(pq) (p < q primes), system (1)+(1')+(⊥)+(∏h) reduces to a quadratic with discriminant D·q² = (q² − p³)² − 4pq(p² − q).

| (p,q)   | q² − p³ | D·q²  | √(D·q²) | h rational? |
|---------|---------|-------|----------|-------------|
| **(2,3)** | **1 (Catalan)** | **25** | **5 = N−1** | **YES** |
| (2,5)   | 17      | 569   | irrational | NO |
| (2,7)   | 41      | 2377  | irrational | NO |
| (3,5)   | −2      | 244   | irrational | NO |
| (5,7)   | −76     | −584  | D < 0    | INCONSISTENT |

**Statement:** Rational h ⟺ (d₁,d₂) = (2,3), i.e. Catalan q² − p³ = 1 (Mihailescu theorem).

For (2,3): two Z₂ solutions, both with ∏h = d₂. Physical: h = (2, 9/4, 1, 2/3). Spurious: h = (2, 9/4, 8/3, 1/4).

Deps: X.57a, A.1, A.2, Mihailescu theorem.


## X.95 (S196) [OBS]: T-spectral decomposition of w — new constraint a_N = −1/d₁³

**Statement.** w = f·h in T-eigenbasis:

w = (dim M₁₀/d₂)·v₁ − (dim M₁₀/(d₁³d₂))·v_p − (1/d₁³)·v_N

| Coefficient | Value | LD expression |
|------------|-------|--------------|
| a₁ | 11/3 | dim M₁₀/d₂ |
| a_q | 0 | (⊥) |
| a_p | −11/24 | −dim M₁₀/(d₁³d₂) |
| a_N | −1/8 | −1/d₁³ |

**Key new constraint: a_N = −1/d₁³** [5 equivalent forms]. LINEAR in h. On (⊥)-family: uniquely selects physical h (no Z₂). ∏h = d₂ follows from (⊥) + a_N = −1/d₁³.

Gap 3 decomposed into (A) derive (⊥) [13 formulations] + (B) derive a_N = −1/d₁³ [5 formulations, new]. (A)+(B) → unique h, no Z₂.

Deps: X.92, X.92a, G.0c, X.54.


## X.96 (S198) [THM-arith]: Anchor R_eff triangle theorem

**Statement.** R_eff(c)/R_eff(u) = d₁/d₂, where c = σ₁(p) = σ₀(p), u = σ₀⁻¹(p), R_eff grounded at anchor p.

**Proof (5 steps).**
1. σ₁(p) = c AND σ₀(p) = c (Anchor multi-edge D.1). Weight d₁ = 2.
2. c has exactly 2 neighbors: p (weight 2) and u (weight 1). Triangle {p,c,u}.
3. t is cut vertex: σ₀ preserves BV orbits; only (u,t) crosses BV boundary.
4. Schur complement: L_eff = [[3,−1],[−1,2]], R(c) = 2/5 = d₁/(N−1), R(u) = 3/5 = d₂/(N−1).
5. R(c)/R(u) = 2/(d₁+1) = d₁/d₂ [Catalan: d₂ = d₁+1].

Z_φ pattern: R(c) = d₁/(N−1), R(u) = d₂/(N−1), R(t) = d₁³/(N−1). All pairwise ratios LD monomials.

Verified S198+S201: Fraction exact, O.1 MCT 12/12, Kirchhoff = 1875 = d₂·(N−1)⁴.

Deps: O.1, D.1, BV structure, Catalan.


## X.96a (S198) [THM-arith]: σ₁-pair |ΔR|

| σ₁-pair       | |ΔR|  | LD expression |
|----------------|--------|---------------|
| (u,t) bridge   | 1      | d₂−d₁        |
| (c,p) multi    | 2/5    | d₁/(N−1)     |
| (b,μ) interior | 3/5    | d₂/(N−1)     |
| (d,e) interior | 3/5    | d₂/(N−1)     |
| (s,W) far-end  | 0      | —             |
| (τ,H) far-end  | 0      | —             |

All nonzero values LD monomials. Deps: X.96.


## X.96b (S198) [THM-arith]: Kirchhoff(Schreier) = d₂·(N−1)⁴ = 1875

det(L_red) = 1875 = 3·5⁴. Deps: O.1, Cayley graph.


## X.97 (S199–S200) [DER]: Trace formula derivation of h — GAP 3 CLOSURE

**Statement.** h = (d₁, d₂²/d₁², 1, d₁/d₂) follows from the dessin X₀(6) in 6 steps, with 1 selection step (k = 10).

**Proof (X.97 chain).**

**Step 1 [THM, Path A].** X₀(6) passport → ν₂ = ν₃ = 0.

**Step 2 [THM-comp, W.4].** Newform decomposition: S₁₀(Γ₀(6)) = V₂ ⊕ V₃ᵃ ⊕ V₃ᵇ ⊕ V₆. dim = 2+2+2+1 = 7. Unique level-6 newform (forced by dimension).

**Step 3 [THM-comp + THM-arith].** Oldform AL traces:
- V₂: Q=2 divides M=2 → W₂ = w₂·Id. Tr(W₂|V₂) = 2·(−1) = −2.
  [w₂(2.10.a.a) = −1 verified by independent construction from Eisenstein products, S200/S201.]
- V₃: Q=2 coprime to M=3 → W₂ off-diagonal (Atkin-Li). Tr = 0 for each.

**Step 4 [THM-arith].** Subtraction: w₂(6.10.a.a) = Tr(W₂|S₁₀) − Tr(V₂) − Tr(V₃) = −1 − (−2) − 0 = **+1**.
Similarly w₃(6.10.a.a) = −1 (level-3 oldforms cancel: 2(−1) + 2(+1) = 0).
Cross-check: w₆ = w₂w₃ = −1 (Fricke-odd). ε = (−1)⁵(−1) = +1 (rank 0). ✓

**Step 5 [THM-arith].** L-factors at central point:
L₂(k/2) = (1 + w₂/2)⁻¹ = (3/2)⁻¹ = 2/3 = d₁/d₂.
L₃(k/2) = (1 − 1/3)⁻¹ = 3/2.
h(6) = L₂ = d₁/d₂. h(3) = L₂·L₃ = 1. h(2) = L₃/L₂ = d₂²/d₁². h(1) = d₁.

**Step 6 [THM-arith].** All constraints verified: (⊥) Σf²h = 44, (2) h(3)+2h(6) = 7/3, ∏h = d₂.

**Selection step:** k = 10 (motivated by dim M₁₀ = 11 = rank(Φ−Lℓ), S.12 barrier).

**Status: [DER].** 1 selection step. All other steps [THM], [THM-arith], or [THM-comp].

**3 independent cross-checks (S200, verified S201):**
- Path A: 60+ multiplicativity tests (0 violations), X.93 mod-12 (13 primes, 0 violations).
- Path B: 2.10.a.a constructed from Eisenstein products without LMFDB. a₂=16, a₃=−156 confirmed exact.
- Path C: end-to-end chain w₂=+1, w₃=−1 → L₂=2/3, L₃=3/2 → h. All 5 constraints ✓.

**14th formulation of Gap 3 (S198):** h(6) = R_eff(σ₁(p),p) / R_eff(σ₀⁻¹(p),p) [THM-arith graph identity, OBS link to h].

Deps: O.1, A.1, W.4, X.91, V.4, X.56.

1. **Gap 3: CLOSED for discrete content (S100). Ring OPEN at G (S110).** (3a) Form α/(2π): 4D Weyl [THM, G.3/S29]. (3b) Universality: ring closure excludes edge-local coupling (100% spread vs 0.002% ring precision) [DER+MOTIVATED, M.7/S100]. (3c) Value 1/α ≈ 137.036: from H.1 [DER, H.1/S105]. (3d) EM identification: EW operator T₃−d₂|Q| = −ℓ/2 [THM, G.8/S32]. **S110 correction:** Ring is not a contraction mapping (|F'| = 9.84 >> 1). G requires nuclear input μ_G = (3μ + μ_n − B_d/m_e)/4, not derivable from H.2. G is a prediction given nuclear data, not a ring-closure condition. Hierarchy split: L1 (α, μ) closed; L1b (G) open. **S119–S121 note:** Cuspal regulators (§R) extract ln d₁, ln d₂ as K₂-periods of X₀(6) but do NOT produce α/(2π). Baker's theorem + PSLQ (11 tests, 80 digits) rule out ℚ-linear relation to any Dirichlet L-values. Regulators and coupling live in different transcendence classes. **S125–S132 note:** 28 DFT dead directions (§S.10, X.21) confirm the structural barrier: α/(2π) is not derivable from Mon/cipher algebra. The action principle must come from outside dessin combinatorics. **S134–S137 note:** NCG provides Ω = 36/π [DEF] as clean NCG interpretation of coupling (T.1), but δK = (α/2π)(Φ−Lℓ) remains outside spectral action: heat kernel diagonal DEAD (X.22, 68% off-diagonal), det variation DEAD (X.23, r=−0.06). M_opt ∈ ℂ[Mon] constructively defined (T.8) with DDT eigenvalues = LD monomials (T.6); physical principle for min ||a||² OPEN (T.9). Genus 0 forces additive form [DER] (U.4), upgrading from [MOT/discrete selection]. **Revised discrete-selection count:** 1 postulate (Γ₀(6)) + 1 theorem (D₀, G.5) + 1 derivation (additive form, U.4) + 1 motivated (K_d=√2, EWSB). Previous "4 discrete selections" overcounted.
   **S139–S141 note:** 11 additional dead directions (#30–39b, X.29–X.32), total cumulative **44 dead** (including S145 #43–44). Edge-level modular invariants (E₂, E₄, E₆, η at coset τ-points) contain no per-particle information beyond (n, ℓ, K). F.1 is honest LO rule (8/10 improved, R² = 0.68, RMS_resid/RMS_obs = 0.54). Exact mass correction requires non-additive f(n, ℓ, K) — reformulated Gap 3. **Live directions:** DDT/M_opt physical principle (T.8–T.9): DDT eigenvalues = LD monomials, w ∈ (1/56)ℤ¹², diag = Φ−Lℓ exact; what selects M_opt? **S145 update:** Eisenstein g_k (dim M₂ = 3) tested — analytically realizes CRT but r = 0.52 vs δK, DEAD (X.34). M_opt blocks → CKM/PMNS also DEAD (X.35). Sole live direction: DDT/M_opt physical principle.
   **S149 note:** 3 additional dead directions (#46–48, X.37–X.39): δK from UST joint (r=0.60, class-level only), Z₄ charges on P¹ (σ₁ fixed-point-free), Φ−Lℓ as Eisenstein on cosets (rank 11 vs dim 3). Total cumulative **48 dead**. UST joint probabilities (V.8) and hitting times (V.9) confirm dessin structure but do not resolve within-cycle σ∞-order. S.10 barrier persists.
   **S151/S153 note:** Rank barrier theorem [THM-arith, S.12]: dim M_k < rank(Φ−Lℓ) = 11 for k < 10. ALL weight < 10 modular form approaches to δK structurally precluded (Class A barrier). First admissible weight = 10 where dim M₁₀ = 11 — already an LD fundamental (Tr(L·C_n) = −11). Gap 3 has no live internal directions and no modular-form-on-cosets direction below weight 10. External: spectral theory of Γ₀(6)\ℍ, action principle, or weight-10 structure. Cumulative **50 dead**.
   **S156 note:** E₂ⁿ·fₖ at τ=i DEAD for ALL n ≥ 1, ALL even k [THM-arith, X.42]. Universal identity |E₂(i)+Δ_e| = E₂(i) → pair ratio purely imaginary. Single theorem closes infinite family. Class H barrier. Cumulative **51+ dead**.
   **S157 note:** Elliptic fixed point collapse [THM-arith, X.43]: S·i=i collapses cosets (0:1)↔(1:0) → 11 distinct points. Anchor 192/7 ≠ quark 45/7 → inconsistent at ALL weights. At τ=ρ: only 4 distinct points. Class I barrier (new hard class). Cumulative **52 dead**.
   **S158 note:** Weight-10 at 3 non-CM τ₀ (X.45a): 10/12 fit sub-percent, only {p,c} fails (97–99.9% of residual). S-constraint [OBS]: f(Sτ₀) = τ₀¹⁰f(τ₀) removes 1 DOF. Pointer to non-pointwise.
   **S159 note:** 6.10.a.a period polynomial P⁺ = pure LD monomials (W.5). P⁻ ∝ L·dim M₁₀ = 77 (W.6). Form-specific, not face-level. Non-pointwise territory productive.
   **S160 note:** Double coset Γ₀(6)\SL₂(ℤ)/Γ₀(6) = 4 = σ₀(6) [THM-arith]. Class I′ barrier: bi-invariant functionals ≤ 4 values. Coset-twisted Petersson DEAD #54. Cumulative **54+ dead**.
   **S161 note:** E₂·f₁₀ at τ₀≠i: partial match (93–99.1%), τ₀-dependent. Direction 🟢 #3 → 🟡 SOFT DEAD. Class H broken at τ₀≠i confirmed.
   **S162 note:** Gap 3 reformulated: not "where does α come from" (H.1 answers) but "why product form δK = α·(Φ−Lℓ)?" (G.5 explicit: postulated). Barrier classes: **10** (6 hard Gap 3: A, B, H, I, I′, sign + 4 guards: C, D, F, G). Open directions: 6 (🟢 #1,2,4,5,6,7) — #3 demoted to 🟡.
   **S166 note:** Unique elliptic σ₁-pair {p,c} [THM-arith, I.9j]: L=±S, |Tr|=0, only elliptic linking among 6 pairs. Null-space ≥98% on {p,c}. S158 anchor dominance upgraded [OBS]→[THM-arith+THM-comp]. M₂(Γ(6)) eval rank=12 at generic τ₀ → DEAD #56 (Class C). Direction 🟢 #4 → 🔴 DEAD. Cumulative **56+ dead**.
   **S168 note:** NLO mass rule G.0b: δK = h(F_{σ₁})·(α/2π)(Φ−Lℓ), h=(d₁,d₂²/d₁²,1,d₁/d₂). R²=0.89 (vs 0.68), 0 free params, 10/10 signs. h(2)=tan γ_CKM [THM V.4]. ∏h=d₂. All ratios (d₁,d₂)-monomial. Triple constraint: unique 1/625. Scramble p=0.004 (LEE-corrected). Explains G.6 (d₁-multiplier) and n=3 anomaly. X.47: additive formula without face(σ₁) structurally dead. **Gap 3 reformulated: derive h(f) = (d₁, d₂²/d₁², 1, d₁/d₂) from dessin.**
   **S169 note:** σ₁ face Markov chain spectrum = μ(d)/d [THM-arith X.48]. h derivable from constraints (G.0c): (1) V.4, (1') e₋ cross-ratio X.56, (⊥) v_{d₂}-suppression X.49 [OBS], (2) scattering X.50 [OBS]. h spectral decomposition: all coefficients LD monomials, h·f ⊥ v_{d₂} [OBS X.49]. Scattering identification: ⟨π,h⟩ = Π₊₋/Π₋₊ at s=d₁, specific to (2,3) [OBS X.50]. Extremal principle X.51 [THM-arith] on (⊥)-restricted family. New dead (reformulated Gap 3): 2 (X.52 ω-at-cusps #57, X.53 UST-per-face #58). Cumulative **58+ dead**.
   **S170 note:** Character formula [THM-arith X.54]: d₁³fh = d₂³−L·χ₂−χ₃−d₂·χ₂χ₃. Set identity X.54b: d₁fh ∈ {d₁², d₂², N, d₁³}, ∏=j(i)=1728, Σ=d₂³. T upper triangular in AL basis [THM-arith X.54c]. Arithmetic chain X.55: Catalan → |B₁|=(N−1)d₁ → Π₊₋/Π₋₊=d₂²/d₁³ [THM-arith]. Specific to (2,3): falsified for 5 other prime pairs.
   **S171 note:** **[CORRECTION]** G.0c DOF 1→2-param. (⊥) independent [OBS]. X.56 [THM-arith]: scattering closed forms.
   **S172–S174 (consolidated S175, 1 correction + 1 clarification):** **X.57** [THM-arith]: T = T^(p)⊗T^(q), 6 levels, ‖v_d‖²_π=d. **X.57a** [THM-arith]: (⊥)⟺(2) mod Catalan, G.0c: 3+Catalan, 1 [OBS]. **X.58** [THM-arith]: Π₊₋=−1/K=−1/40. **X.58a** [THM-arith, S175-corrected]: v_q = u_{++}+d₁u_{+-} (not minus). **X.58b** [THM-arith]: [T,Φ/λ]≠0. **X.59** [THM-arith]: (⊥)⟺ratio=−ι(d₂)=−d₁. **X.59a/b** [THM-arith]: dim M₁₀ in all AL projections; u_{+-}=u_{-+}⟺(1). **X.60** [THM-arith]: q-dirt = T^(p)⊗(T^(q)−I). S174 imprecise: σ₁ ∉ N(Γ₀(6)), W₂ used as q-blind reference; math unaffected. **X.60a/b** [THM-arith]: v_q spectral shift (unique stat→decay); (⊥)⟺R=d₂. **[OBS]**: autonomous vs coupled q-oscillation. 6.10.a.a: u_{+-} sector, |a₃/a₂|^{1/2}=h(d₁), weight 10. **DEAD:** (a) 13 functionals, T_h trivial [S172]; (b) Selberg diagonal cusp-blind [S173]; (d) partial [S172]. **Remaining Gap 3:** 1 [OBS]. Derive ANY of {h(d₂)=1, h(N)=d₁/d₂, (⊥), (2), ratio=−ι(d₂), R=d₂}. **Open:** (b') off-diagonal [low], (c) Langlands/6.10.a.a [untried], (e) σ₁ selection [partial]. Open 🟢: #1 Maass, #2 weight≥12 non-CM, #5 L-values, #6 trace formula, #7 action principle (5 remaining).
   **S176–S177 note:** Layer 8 = information geometry of dessin: 13 results (C.8.1–C.8.4, X.61–X.67). Key for Gap 3: spectral sum rule Σf²h=Σn=44 [THM-arith, C.8.3] provides new constraint for h-uniqueness. Cubic (3c−2)(45c²−29c−2)=0 [THM-arith, C.8.4]: unique positive LD-monomial root c=d₁/d₂ from 4 constraints (V.4+∏h+C.8.3+X.50). Face equicorrelation 192=d₁⁶d₂ [THM-arith, C.8.2]. Tr(A²)=K=40 unique to X₀(6) [THM-arith, 6 levels, S177]. All Tr(A³)=N(N−1), Tr(A⁴)=d₁⁵L also unique to X₀(6). (σ₁σ₀)³ fixes anchor+leptons, Σn=dim M₁₀. S177 verified all 13 results independently from O.1; found 1 text error (L8.11 "both n=ℓ" → only W in orbit 2).
   **S178 note:** 16 new results (L8.14–L8.29 → C.8.5–C.8.12, X.68–X.73), all [THM-arith/math/comp]. T₁=T₀ general theorem for all dessins (C.8.5). w=h·f spectral table: c₃(w)=0=(⊥), c₁c₆=−c₂ (7th reformulation of Gap 3). Precise (⊥) clarification: c₃(h·f)=0, NOT c₃(h)=0 (C.8.8). q-balance: (⊥) = conditional independence of 3-divisibility and f·h in edge measure (C.8.11). Constraint landscape: (⊥)+(2) → unique h without ∏h; Gap 3 = derive 2 of 3 [OBS] (C.8.12). Face graph: Tutte T(d₁,d₂)=index²=144 (38th path, new cluster: graph-polynomials, X.68). BV bipartite walk eigenvalues all LD monomials (X.71). Absorption times = d₁d₂², d₁³d₂ (X.73). **CORRECTION:** L8.24/L8.29 session text erroneously identified p-cut/q-cut = 4/3 as h(2) = tan²γ_CKM. Actual: 4/3 = d₁²/d₂ = K(c) ≠ h(2) = 9/4. VERIFY-BEFORE-CORRECT applied (S178 audit). Cumulative dead: **58+** (no new dead).
   **S185 note (audit of S179–S184):** 17 results X.74–X.90 verified (15 [THM-arith], 1 [THM-arith+comp], 1 [OBS]). 3 errors corrected (X.78 NOTE deleted, X.83 label, X.87 count). 6 tautologies identified. 11 equivalent formulations. Bridge problem: (−1/d₂)=−1 → derangement → ε₃=−1 → [GAP] → (⊥). All but last arrow [THM]. Cumulative dead: **58+**.
   **S186 note:** AL sector structure W.8 [THM-comp, erratum S200]. Tr(W_Q) = −1 at k=10 from W.4. General claim (all k) FALSE: k=4 counterexample (S200). dim(+,+) = 1 (anchor anomaly). h = AL transition cost, not multiplicative on (ℤ/2)². 6.10.a.a in lepton sector (+,−).
   **S186-cont note:** X.91 L-factor dictionary [THM-arith]. All 4 h-values via bad Euler factors of 6.10.a.a. L₂·L₃ = 1 (Catalan). tan γ = L₃/L₂. Anchor transfer requires dim(+,+) = 1. **12th formulation:** h(6) = L₂(k/2, 6.10.a.a). 6 dead direct-derivation approaches.
   **S187 note:** X.92 T = T₂⊗T₃ [THM-comp]: full CRT eigenvector correspondence. X.92a (⊥) = zero 1×e₃ mode [THM-arith]: d₁³d₂·a = (88, 0, −11, −3), all LD monomials. X.92b Z₂ alien 17 [OBS]. **13th formulation:** w ∈ ker(proj_{1×e₃}). 2 more dead approaches (T-spectral, character alignment). T-structure insufficient (T independent of W_p). Cumulative dead: **66+**.
   **Remaining Gap 3 (S188):** 1 [OBS]. **13 equivalent formulations.** Derive ANY ONE. Sub-directions: (c1) Eichler-Selberg USED; **(c2) h(6)=L₂ CENTRAL** (8 dead attempts); (c3) CRT+AL ENRICHED (T=T₂⊗T₃, (⊥)=zero 3-mode, T insufficient); (c4) Z₂ SUBORDINATE (alien 17); (c5) rationality ACTIVE; (c6) ramification EXPLORED. Open 🟢: #1 Maass, #2 weight≥12, #5 L-values, **#6 trace formula → USED (S199–S200, X.97)**, #7 action principle.
   **S195 note:** X.93 mod-12 congruence [THM-comp]. X.91 pair-product table and intertwining matrix [THM-arith]. L-factor decomposition (reformulation, not derivation). Dead #68 (face heat kernel), #69 (Sym² L), #70 (scattering Φ ratios). Cumulative dead: **70+**.
   **S196 note:** X.94 discriminant uniqueness [THM-comp]: rational h ⟺ Catalan. X.95 T-spectral w decomposition [OBS]: a_N = −1/d₁³ (new constraint). Gap 3 → (A) derive (⊥) + (B) derive a_N. Monomiality search: 20 LD-smooth solutions, physical unique with ∏h = d₂. BV w-sum structure [OBS]. Dead: **72+**.
   **S197 note:** NNLO residual structure [OBS]. NNLO/NLO ≈ 1/d₂. Generation hierarchy. R_eff ERRATUM (S198). Qualitative 3-layer picture.
   **S198 note:** X.96 anchor R_eff triangle theorem [THM-arith]. R(c)/R(u) = d₁/d₂. X.96a σ₁-pair |ΔR| [THM-arith]. X.96b Kirchhoff = d₂(N−1)⁴ [THM-arith]. 14th formulation of Gap 3. SIGMA0-FROM-O1 barrier established.
   **S199 note:** Phase A: isoperimetric scan on (⊥)-family [DEAD #73]. ~75 functionals tested; 1D linear family structurally forbids extremal principle. Phase B: X.97 trace formula chain [DER, conditional on 2 ⚠]. Complete derivation modulo 2 trace formula evaluations.
   **S200 note:** X.97 ⚠₁ and ⚠₂ CLOSED. Independent construction of 2.10.a.a (Eisenstein product method, no LMFDB). W.8 erratum: general claim FALSE (k=4 counterexample via 6.4.a.a). W.8 downgrade [THM-arith]→[THM-comp]. LMFDB dim S₂ discrepancy flagged. **Gap 3: [OBS] → [DER].** Dead: **73+**.
   **S201 note (verification session):** Full independent verification of S199–S200. ⚠₂ re-derived (Fraction exact quadratic, 2 roots: Eisenstein a₃=19684 vs cusp a₂=16). W.8 erratum re-verified (6.4.a.a η-product q-expansion, 14 terms). X.97 chain end-to-end (6 steps, all constraints). Multiplicativity (60 tests, 0 violations). X.93 mod-12 (13 primes, 0 violations). LMFDB dim S₂ = 0 confirmed (genus 0, conductor 36 not 6). Companion patch applied.

   **S202–S203 note:** S202 L-function BUG (wrong prefactor) → S203 corrected. Periods: Ω⁺ 0.00379→20.974, Ω⁻ 0.01652→2.700. "Period inconsistency"→ARTIFACT. S203-prev a₀=37 WRONG (correct −5 already in K.1, GREP-BEFORE-COMPUTE violated). "P₄ incompletely determined" WRONG (full P₄ since S31). K.1b ramification identities C.9a–i. K.3 Klein (ℤ/2)² fixed points. W.9 corrected period table. N.3 QTC reduction 2→1. X.98 geometric functional + cos² algebraic DEAD #74. Dead: **74+**.
2. **Gap 9: [DER+MOTIVATED] (S99–S100). S116 structural. S190–S194 upgrades. S204–S205: CR values. S207–S217: Gap 9(γ₂) attack, all values [DER].** Schur complement L_eff gives exact rational PMNS (I.11–I.14): sin²θ₁₃(Schur) = 1/26 (−29σ, insufficient alone). Heat kernel at t = √5/2 gives all 3 angles within 2σ (I.17, [CONJ]). Representation-theoretic derivation (I.26): irrep localization → moment theorem → P₁=1, P₂=5 → t = √P/d₁ [DER]. S₃ polarization (I.27): w₊/w₋ = d₂/L for φ-pair (26th path), Σλ·w₊ = |B₁|, Pythagorean identity t₂²−t₁² = 1. Spectral anatomy (I.18–I.24): φ-pair dominates θ₁₃ at 38%. **S116 correction: PMNS has 3 independent root gaps** (not 2): (α) CONJ I.14-ID [Mν, Leff]=0, (β) CONJ I.3-ID M_lep→PMNS, (γ) split S205 into (γ₁) structural [DONE via X.102] + (γ₂) operator identification. Independence of α,β proved by [M_lep,L_eff]≠0 (I.29). **Layers:** Layer 0: char(L) → Q₁,Q₂ [THM]. Layer 1: P₁=1, P₂=5 from moments [THM]. Layer 1b: P₂−P₁ = d₁² [THM]. Layer 2: t=√P/d₁ [DER]. Layer 3: HK PMNS → Σ|pull|=4.52 (NuFIT 6.0 IC19) [CONJ, I.17]. **CR values (S204):** sin²θ₁₂=4/13 [DER], sin²θ₂₃=81/145 [DER], sin²θ₁₃=2/91 **[DER]**. Σ|pull|=0.27 (IC19). **Two-scale structure (S205):** CR(θ₁₂,θ₂₃) at t≈1/d₁, CR(θ₁₃) at t≈√5/2. f(L) insufficient (T.3); need operator in ⟨L,σ∞⟩ (T.5: dim=50). **Remaining (post-S217):** (a) CONJ I.14-ID (Lagrangian origin); (b) Operator M: (b,c,d) degree>128, not derived (technical); (c) F2 selection principle; (d) ~~Channel rule~~ **CLOSED (X.130)**; (e) CP phase δ_CP not addressed. ≥90 dead directions.
   **S147 bridge:** Modular flavor symmetry (Li-Liu-Ding, arXiv:2108.02181) gives sin²θ₁₂ = 1/3 at τ = i (trimaximal). LD correction: 4/13 − 1/3 = −1/(d₂·det M_lep). Formal framework for bridge: finite Langlands for PSL₂(ℤ/6ℤ). Status: OPEN.
   **S151 note (verified S152):** V₂-free zone in cusp forms (k ≤ 6) established [THM-comp/arith]. Fusion table [THM-arith, S.11] gives algebraic V₂ blocking rules. HK V₂ = 6.4% (I.9g.3) is purely Eisenstein — no cuspidal partner below weight 8. Selection rule [OBS]: newform 6.4.a.a has ker Φ(f₄,·) aligned with Eisenstein V₃ direction. Finite Langlands bridge V₂ ↔ automorphic requires weight ≥ 8.
   **S153 note:** Correct Φ−Lℓ irrep decomposition [THM-arith, G.0a]: V₃ dominant (36%), V₂ = 20.9%, V₁ = 14.4%, V₆ = 28.7%. A₄-standard representation dominates δK, not S₃-standard. Σ(Φ−Lℓ) = −d₁⁸d₂/L.
   **S189–S194 structural mechanism:** mu-tau breaking traced to boson circuit (I.9g.8-I.9g.9): A^k|_lep has exact mu-tau symmetry for k<=3, first breaking at k=4 caused by 2 extra tau-only 4-step walks through the boson sector (sigma1(tau)=H). Resistance distances (I.9g.10): R(e,mu)=1, R(e,tau)=82/75, R(mu,tau)=67/75, total asymmetry 1/(N-1). Chain k_break -> P_phi -> t (I.9g.12): boson circuit length 2*d1 -> spectral bridge D.8b -> phi-pair product = det(M^{mu,tau}) = N-1 = 5 -> t=sqrt(5)/2. Status **[DER]** (S193/S194 spectral bridge). Systematic scan: NO zero-parameter operator gives chi^2 < 200 -> Gap 9 gamma genuine. Phi-pair self-duality (I.9g.13): 1/lambda_+ + 1/lambda_- = 1.
   **S207–S217 Gap 9(γ₂) attack:** X.103 28-dim family (tautological universality). X.104 NO-GO ℤ[Mon]. X.108 resultant formula 2/91. X.109 P_face transform, (1,1,1)-obstruction. X.110 Catalan bridge (unique (2,3)). Face-cyclotomic duality X.110a. Irreps blind (X.111-X.113a). Circulant obstruction + rationality–μτ theorem (X.115-X.117): ℚ[Mon]→θ₁₃=0, irrational coefficients required. Operator M=σ₁+b(σ₀+σ₀⁻¹)+c(σ∞+σ∞⁻¹)+d·I exists with exact CR-PMNS (X.118a), two families F1/F2 (X.119), PSLQ null degree>128 (X.119d). Seesaw anatomy: Gram identity (X.122), anchor invisibility (X.123), mediator triangle, UST all rational (X.UST). Unified face-pair construction (X.128): CR→θ₁₂,θ₂₃; Res→θ₁₃; assignment forced. Index formula sin²θ₁₃=index/(N·∏Φ₃)=2/91 (X.129). GN=PMNS denominators (X.129a). θ₁₃ upgraded [CONJ]→[DER]. Dead #75–90. F2 uniquely viable by mass hierarchy (37.5 vs 33.5, only 12% off).

3. **n-formula offsets = −d₁, −1** [OBS]. Slopes [THM] via F.3a. Offsets absorbed into g→n step but origin in ramification indices remains [OBS].
4. **K-cipher: RESOLVED by ε-η architecture (F.6–F.7b-K).** Remaining: (a) analytical product constraint F.7c, (b) d-quark EWSB exception origin.
5. **IR term of α: [DER + 1 bit empirical] (S103+S108+S123, was [FITTED]→[DER cond.]→[DER+1 bit]).** Form A: IR = (π/36)·(j+N)/(j+L). 5-step chain: 4 steps [THM] + Σ=−χ via O(N) = W₆-odd Grothendieck factor (H.1i [THM], S123). Atkin-Lehner provides exactly 2 candidates (binary): W₆-odd (α⁻¹ = 137.035999202, −1.2σ CODATA) vs W₆-even (137.035948904, +2394σ dead). Selection of odd = 1 bit empirical at ≈2400σ. Form B (paper v5.5) DEAD at 10.5σ. Paper v6 must use Form A. Remaining gap: W₆-odd selection not derived (analogy W_N ↔ spacetime parity is verbal, not proven — X.20 DEAD).
6. **cos²(1/(Nπ)): RESOLVED [DER] (S105–S106).** QTC 12-step chain derives cos² from covering geometry. 42/42 checks. Two standard physics inputs (perturbativity, Born interpretation). See §N. Was [MOT] with 9 dead approaches before QTC.
7. **λ = d₂²/K — RESOLVED (S138, §V.4).** Transfer current theorem identifies P(edge ∈ UST) = tree-level lattice propagator. λ = P_triple = d₂²/K [DER via V.4]. Physical bridge: dessin = lattice (L0 content), no new postulate.
8. **μ-τ breaking → quantitative θ₁₃.** Schur complement (I.11) provides exact mechanism: σ₁(τ)=H breaks μ-τ with parameter 7/55. **S189: structural origin traced** — boson circuit (I.9g.9) creates 2 extra 4-step self-returns for τ at A⁴ (I.9g.8). Breaking 7/55 = L/((N−1)·dim M₁₀) (I.9g.11). Resistance asymmetry R(e,τ)−R(μ,τ) = 1/(N−1) (I.9g.10). Chain k_break→P_φ→t (I.9g.12). Heat kernel at t=√5/2 corrects to experiment. **S190–S194: t derived** [DER] via spectral bridge (D.8b); ν₁↔ν₂ swap forced [DER] via Laplacian solar bound. I.9g.12 gap closed.
9. **d₁-multiplier mechanism** (bridge [THM], mechanism EXPLAINED by G.0b S168: face(σ₁) ∈ {1,2} → h ≈ d₁).
10. **Σn=44, ℓ-equipartition, BV sums** → combinatorial derivation.
11. **Scattering matrix identifications (L.5).** 1/α₃ = 40 = Kirchhoff [THM M.3]. s = d₁ [MOTIVATED], not derived.
12. **Kirchhoff = |P³(𝔽_{d₂})| = 1/α₃(d₁)** [THM M.3]. Projective-space dimension 2d₁−1 = 3 unexplored.
13. **φ-zero structural role** [THM D.6]. Z_φ = {p,c,u,t}. Golden hierarchy 1:φ:φ² with norm √|B₁|. 4/13 = full interference [CONFIRMED]. Open: physical meaning of Z_φ, connection to forced spanning-tree edges (E.8).
14. **PMNS spectral anatomy** [OBS I.23–I.24]. e-μ democracy broken by exactly 2 sectors (λ=1, λ=4) with ratios d₁², d₂². M = 20·Q_φ satisfies M² = L(K₃) (I.20). D_τ-duality links two discriminants (I.21). Open: derive these from first principles.
15. **FN charges q = (L−n)/2** [OBS, S143]. Linear change of variable: half-integer Froggatt-Nielsen charges from LD n-formula. Numerator L = LD invariant. Half-integrality nonstandard for U(1)_FN; possible SU(2)/double-cover connection unsubstantiated. Not promoted.

### Y.16: Coherence Map of Weak Points (S116, computational)

29 weak sections (OBS/CONJ/MOT/ALIVE-WEAK/dual) decompose into **7 independence classes + 12 isolates**.

**Class α: CONJ I.14-ID chain** (3 sections: I.14, I.17, I.22)
Root gap: [Mν, Leff] = 0. Cascade = 2 (I.14 → I.17 → I.22).

**Class β: CONJ I.3-ID chain** (2 sections: I.3, I.5)
Root gap: M_lep eigenvectors = PMNS columns. Cascade = 1.
**Independent of α:** [M_lep, L_eff] ≠ 0 [THM-arith, I.29].

**Class γ: Heat kernel** (2 sections: I.9, I.9a)
Gap: t = 1/d₁ identification. Supported by I.6 [THM].

**Class δ: K-cipher** (3 sections: F.5, F.5e, F.8) — **RESOLVED** by F.7b-K [THM].

**Class ε: δK structure** (2 sections: G.10, G.6) — G.6 now **explained by G.0b** (S168: face(σ₁) mechanism). G.10 remains spectrally isolated.

**Class ζ: Peripheral** (5 sections: B.5, L.5, I.2, I.24, I.9d)
Single weak link each, no cascade potential.

**Isolates** (7): G.7, I.1, I.4, I.23, A.3, M.4, M.5. **(S138 update: E.2–E.6 reclassified from isolates to derived cluster via V.4 UST framework.)**

**Strong hubs:** I.6 [THM] supports 3 weak sections. O.1 [THM-comb] anchors F and I sectors. D.5 [THM] supplies M_lep.

**Leverage budget:** 3 root gaps (α, β, γ) control 4 downstream sections. Remaining 22 require individual mechanisms.

**Fiedler partition** (λ₂ = 2.83): PMNS + K-cipher core is one topological blob (not further separable). G.10/G.6 genuinely disconnected. CKM (E.2–E.6) now connected to dessin via UST framework (V.4, S138); no longer fully isolated.


## X.98 (S202–S203): Canonical geometric functional for α⁻¹ — DEAD

### X.98a: Geometric invariants of Γ₀(6)\ℍ (S202)
8 candidates tested, ALL DEAD:
1. Faltings δ: genus 0 → undefined.
2. Arakelov ω·ω: genus 0 → deg K = −2 (topological constant).
3. Arakelov-Green G(i,i): τ=i not Heegner [X.17, P.1]. DEAD.
4. det'(Δ): expressible via ζ'(−1), L'(0,χ) → Baker+PSLQ [S119]. DEAD.
5. Selberg Z(s): = det'(Δ) × cuspal factors → same obstruction. DEAD.
6. Systole = 2 log(4+√(d₁⁴−1)) ≈ 4.127. LD monomial: d₁⁴−1 = 15 = (N−1)·d₂. Not α⁻¹.
7. Volume = 4π. Trivial.
8. Spectral gap λ₁ ≈ 26.16. Not α⁻¹.

**Conclusion:** No single geometric invariant of X₀(6) equals α⁻¹. The unique canonical number within an order of magnitude is E₂(i) = 432/π ≈ 137.51 = BULK (H.1a).

### X.98b: Automorphic periods of 6.10.a.a (S202, corrected S203)
PSLQ nulls (40 digits, 1000 q-coefficients, functional equation verified):
- sin²(1/(6π)) ∉ ℚ-span{1, Ω⁺, Ω⁻, L(f,5)}
- α⁻¹ ∉ ℚ-span{1, Ω⁺, Ω⁻, L(f,5), E₂(i)}
Root cause: Lindemann-Weierstrass vs algebro-geometric transcendence classes. See W.9.

### X.98c: cos² from algebraic ℙ¹ (S203)
Fubini-Study angle between [1:t₆(i)] and Fricke-even eigenspace [1:6√2]:
cos²(θ_FS) = 0.9867 ≠ cos²(1/(6π)) = 0.9972. Δ = 1.05%.
Root cause: cos²(1/(Nπ)) requires π from vol(Γ₀(6)\ℍ) = 4π (Gauss-Bonnet, analytic). Fubini-Study sees only algebraic ℙ¹ structure.
**QTC (§N) confirmed as correct bridge between arithmetic and analytic.**

Dead: #74 (combined).


## X.99 (S204) [THM-arith]: Φ₃ cyclotomic chain

Φ₃(x) = x²+x+1 evaluated on Catalan chain {1, d₁, d₂}: Φ₃(1) = d₂ = 3, Φ₃(d₁) = L = 7, Φ₃(d₂) = det(M_lep) = 13.

**Recurrence:** d₁·Φ₃(d₁) − 1 = Φ₃(d₂), i.e. (d₁−2)(d₁²+2d₁+2) = 0 → d₁ = 2 unique. **Path 41** to N=6 (cluster #2, ramification/cyclotomic).

### X.99a [THM-arith]: Pell relation
d₂² − 2d₁² = 1 (fundamental Pell solution for √2). M_lep eigenvalue center = (d₂²−1)/2 = d₁² exactly.

### X.99b [THM-arith]: char(M_lep) all-LD-monomial
char(M_lep) = x³ − d₂²x² + d₂Lx − Φ₃(d₂) = (x−1)(x² − (d₂²−1)x + Φ₃(d₂)). Quadratic disc = 4d₂.

### X.99c [THM-arith]: Resolvent root factorization
Rational root of Q₄ resolvent = −4320 = −N³ · d₁²(N−1). 20 = scaling factor of Q_φ (I.20).

### Additional identities [THM-arith]
Tr(M_lep²) = d₂ · det(M_lep) = 39. d₁⁶ + 1 = (N−1) · det(M_lep) = 65.

Deps: A.1, D.5, C.9d.


## X.100 (S204) [THM-arith / DER]: Cross-ratio → sin²θ₁₂

CR(−index, 0; −d₂², −d₁³) = d₁/d₂ = 2/3. Four-tuple: j=0 rational root (−12) + 3 non-anchor cusps (0, −9, −8). **sin²θ₁₂ = CR²/(1+CR²) = 4/13.** Identification tan θ₁₂ = CR: [DER], upgrades I.2 [CONJ→DER]. See I.2 for full details, pulls, anharmonic orbit, h-factor connections.

### X.100 cross-ratio table (S204) [THM-arith]
All 15 four-tuples from 6 special points {∞, 0, −6, −8, −9, −12}: values {9/8(×1), 4/3(×3), 3/2(×4), 2(×4), 3(×2), 4(×1)}. Every value an LD monomial (d₁^a·d₂^b). 0/15 alien.

Deps: C.9f, K.5, E.2, V.4.


## X.101 (S204) [DER]: Cross-ratio → sin²θ₂₃

CR(∞, 0; −d₁³, −d₂²) = d₂²/d₁³ = 9/8. Four-tuple: all 4 cusps of X₀(6) (maximally canonical). **sin²θ₂₃ = d₂⁴/(d₂⁴+d₁⁶) = 81/145 = 0.55862.** See I.5 for full details, identities, pulls.

### X.101a [THM-arith]: d₂⁴ + d₁⁶ = index² + 1 = 145 ⟺ d₁ = 2. Path 43.

Deps: W.1, A.1, X.100.


## X.102 (S205) [THM-arith]: Two-metric mixing formula

Same 4 cusps in TWO coordinate systems give TWO mixing angles:

- **ℍ-boundary coordinates:** cusps at {∞, 0, 1/2, 1/3}. CR(∞, 0; 1/2, 1/3) = (1/3)/(1/2) = **2/3 = tan θ₁₂**.
- **Hauptmodul t₆-coordinates:** cusps at {∞, 0, −9, −8}. CR(∞, 0; −d₂², −d₁³) = **9/8 = tan θ₂₃**.

Bridge: ramification with CRT-dual exponents.

### X.102a [THM-arith]: Cross-exponent structure
t(cusp w=d_p) = −d_p^{d_{ι(p)}} where ι = CRT duality (L.3). |t_lep| = d₂^{d₁} = 9, |t_bos| = d₁^{d₂} = 8.
- Product: |t_lep|·|t_bos| = 72 = |Mon| (W.1).
- Difference: d₂^{d₁} − d₁^{d₂} = 1 (Catalan). **Path 44** (CRT + Catalan).

### X.102b [THM-arith]: Product rule
tan(θ₁₂)·tan(θ₂₃) = (d₁/d₂)·(d₂²/d₁³) = d₂/d₁² = **3/4 = reg(ω)_boson** (U.1 connection).
tan(θ₁₂)·tan(θ₂₃)/reg(ω)_quark = (3/4)/(5/12) = **9/5 = λ₂(L_eff)** (I.12 connection).

### X.102c [THM-arith]: Monomial lattice
Exponents in (d₁,d₂)-lattice: θ₁₂ ↔ (1,−1), θ₂₃ ↔ (−3,2). det[(1,−1),(−3,2)] = −1 → **θ₁₂ and θ₂₃ generate full ℤ²**. γ_CKM dependent: tan γ = (d₂/d₁)² has exponent (−2,2) = −2·(1,−1).

### X.102d [THM-arith]: h-factors as mixing tangents
h(6) = tan(θ₁₂) = d₁/d₂. h(2) = tan(γ_CKM) = d₂²/d₁². h(1) = tan(γ)/tan(θ₂₃) = d₁. h(3) = 1. Distortion: tan(θ₂₃)/tan(θ₁₂) = d₂³/d₁⁴ = 27/16 (ramification).

### X.102e [OBS]: Hyperbolic crossing angle
Unique cusp geodesic intersection in ℍ gives sin² = d₁³/d₂² = 8/9, tan = 2√2 = d₁^{d₂/d₁} (irrational LD monomial). 1 − 8/9 = 1/d₂². Not a PMNS angle; complement of Catalan inverse.

Deps: X.100, X.101, U.1, I.12, G.0b.

**Cumulative dead through S206: 74+ directions.** (S207+ results follow.)

---

## X.103 (S208–S211) [THM-comp]: 28-dim family of CR-PMNS operators

dim(ℂ[Mon]_sym|_lep) = 6 (full Sym₃). Off-diag condition: rank 3. Family dimension = 6−3 = 3. ⚠ Eigenvector universality TAUTOLOGICAL (ℂ[Mon]_sym|_lep = full Sym₃). All 28-dim members give sin²θ₁₃=2/91 automatically. X.103a: Tr|_lep=8=d₁³, off-diag sum=66=N·dim M₁₀, M(μ,τ)=12=index. X.103b face traces: anchor=22=d₁·dim M₁₀, boson=4=d₁², lepton=8=d₁³, quark=10=|B₁|, Σ=44=Σn. Deps: O.1, I.11.

## X.104 (S209) [THM-arith]: NO-GO ℤ[Mon]
K_PMNS = ℚ(√182, √25810), [K:ℚ]=4. K_PMNS ∩ K_spectrum = ℚ. CR-PMNS eigenvectors NOT in ℤ[Mon] (require irrational coefficients). Deps: I.12, I.14.

## X.107 (S209) [THM-arith]: e-row Φ₃
|U_e1|²=801/1183, |U_e2|²=356/1183, |U_e3|²=2/91. Sum=1 ✓. 1183=L·det_M². Deps: I.14, D.5.

## X.108 (S209) [THM-arith]: Resultant formula for sin²θ₁₃
sin²θ₁₃ = Res(P_face,Φ₁)/Res(P_face,Φ₃) = 2/91. P_face=(x−d₁)(x−d₂), Φ_d cyclotomic. 5 equivalent formulations: (i) Res ratio, (ii) d₁/(Φ₃(d₁)·Φ₃(d₂)), (iii) d₁/(L·det_M), (iv) sin²θ₁₂/(d₁·L), (v) chain (1/N)·(d₁²/L)·(d₂/det_M). Status: [CONJ] → **[DER]** (X.129 index formula + X.130 channel rule). Deps: X.110a, X.99, X.130.

## X.109 (S210) [THM-arith]: P_face transform
P_face^T·L_eff·P_face eigenvalues = L_eff×91 = L_eff×(L·det_M). All |U|² LD monomials. |U_e3|²=1/(d₁L)=1/14. **ERRATUM:** P^T·L·P (not P^{-T}·L·P^{-1}). X.109a: [L_eff,(P+P^T)/2]=0, commutator entries 42,90,48 (LD monomials). X.109b [THM-arith]: L_eff·(1,1,1)=0 but CR-PMNS does NOT have (1,1,1) as eigenvector — the (1,1,1)-obstruction. X.109c: alien primes 89=L·det_M−d₁, 29=N²−N−1. Deps: I.11, I.12, X.110a.

## X.110 (S209) [THM-arith]: Catalan bridge
d₁²+d₂²=13=Φ₃(d₂). Equivalently d₁²=d₂+1. Unique for (d₁,d₂)=(2,3) among primes. Connects sin²θ₁₂=d₁²/Φ₃(d₂) to sin²θ₁₃=d₁/(Φ₃(d₁)·Φ₃(d₂)). X.110a [THM-arith]: face-cyclotomic duality Res(Φ₁)=d₁, Res(Φ₂)=index, Res(Φ₃)=L·det_M, Res(Φ₆)=d₂·L. Product=(d₁⁶−1)(d₂⁶−1). X.110b: Tr(P_face(σ∞)|_boson)=14=d₁·L, sin²θ₁₃=sin²θ₁₂/14. X.110c: det(lep block)=182=d₁·L·det_M. P†P|_lep: {4,91,91}. Deps: A.1, D.5, X.99.

## X.111–X.113a (S212) [THM-comp]: Irreps blind to PMNS
X.111: W₆∉Mon (0/72 elements W₆-like). X.112: Sym² traces Tr(Sym²(Frob_2))=−d₁⁸, Tr(Sym²(Frob_3))=−d₁·d₂⁸. X.113: P_{V₃}|_lep=(3I−J)/12 (S₃-symmetric). X.113a: ALL P_ρ|_lep ∈ span{I,J} — irreps BLIND to PMNS. Angles from specific Mon-element coefficients, not representation theory. Dead #81–83. Deps: O.1.

## X.115 (S213) [THM-comp]: Circulant Sandwich Phase Theorem
p=aI+bC+cC² gives |U_e3|²(φ)∈[0,2/3]. P_face→|U_e3|²=1/14 at φ=−33°. CR-value 2/91 at φ≈177°. X.115a [THM-comp]: sandwich obstruction — |U_e1|²=1/3 for ALL circulant sandwiches. CR-PMNS needs 0.677 → DEAD #85. Deps: I.12.

## X.117 (S213) [THM-arith]: Rationality–μτ Theorem
M∈ℚ[Mon]_sym with CR-PMNS ⟹ λ₁=λ₂ ⟹ sin²θ₁₃=0. √(91/2) irrational in CR-PMNS. 13195=5·7·13·29=L·∏GN_lep. Physical: ℚ[Mon]=tree level (θ₁₃=0), ℝ\ℚ=loop level (θ₁₃=2/91). Deps: X.103, X.104.

## X.118a (S214) [THM-comp]: 3-parameter exact CR-PMNS
M=σ₁+b(σ₀+σ₀⁻¹)+c(σ∞+σ∞⁻¹)+d·I. Solutions exist. Two families F1, F2 with identical eigenvectors=CR-PMNS. Deps: O.1.

## X.119 (S214) [THM-comp]: Two Solution Families

| | b | c | d | eigenvalues |
|---|---|---|---|---|
| F1 | 2.565 | 2.603 | −2.506 | (−8.805, −0.583, −0.462) |
| F2 | 1.795 | −2.153 | −0.265 | (−0.760, +0.074, +0.144) |

X.119a: M|_lep=(d−c)I+cJ (σ₁|_lep=0, σ₀|_lep=0, (σ∞+σ∞⁻¹)|_lep=J−I). All PMNS from Schur correction M_lr·M_rr⁻¹·M_rl. X.119b: M_lr 9 nonzero entries, anchor columns ALL ZERO. X.119c: symbolic Schur — det(M_rr) degree 9 (154 terms), N entries degree 10. X.119d: PSLQ null at degree≤128, |coeff|<10³⁰ — minimal polynomial degree>128. X.119g: near-monomial hits marginal (2–3σ above random). Deps: O.1, X.118a.

## X.120–X.126 (S215) [THM-arith/comp]: Seesaw Anatomy

**X.120** 4+ real solutions. F2 uniquely viable by mass hierarchy: Δm²₃₁/Δm²₂₁=37.5 (exp 33.5, 12% off). Other roots: 51.1, 6.5, 611 — all excluded.

**X.121** [RECLASSIFIED S217 as TAUTOLOGY]: Cancellation theorem Σ_cr(i,j)=c·v_i·v_j is consequence of M_ll=(d−c)I+cJ + off-diag(M_eff)=0. Not independent content.

**X.122** [THM-arith] Gram Identity: S₁·S₁ᵀ=I, S₀·S₀ᵀ=2I, S₁·S₀ᵀ=C=σ∞|_lep. Root cause: σ₁·σ₀·σ∞=id on full dessin.

**X.123** [THM-arith] Anchor Invisibility + Mediator Triangle: S₁,S₀ zero on anchor columns {c,u,p}. Mediators: e↔τ via d, τ↔μ via H, μ↔e via b.

**X.124** [THM-arith] Boson Contact: v_bos=(0,2,1). |⟨v_bos,ν₃⟩|²/|v_bos|²=4628/5075≈91.2%. Both alien primes (89,29) appear.

**X.125** [THM-comp] Anchor Portal: det(anchor block)=−0.40 for F2 → massive Schur correction (1611%).

**X.126** [THM-comp] Channel Decomposition: σ₀ dominance 94.6% for F2. Quark channel 66%. Boson most CR-diagonal.

ERRATUM (S217): **v=U_CR^T·(1,1,1)=(0.695, 0.363, 1.544)** [V-S217]. Basic S215 version (0.050, 1.730, 0.066) FALSE. ||v||²=3 exactly.

Deps: O.1, X.119, I.11, I.12.

## X.UST (S215) [THM-comp]: UST Edge Probabilities

Weighted Kirchhoff=1875=d₂·(N−1)⁴. 17 edges, all P(edge) rational with denominators d₂^a·(N−1)^b. Bridge u↔t: P=1. e-μ democracy: P(e↔d)=P(μ↔b)=19/25. Shared mediator triangle: each lepton pair shares exactly 1 REST neighbor. Anchor {c,u,p} uncoupled from all leptons. Deps: O.1, D.4.

## X.128 (S216) [THM-comp]: Unified Face-Pair Construction

4 face types × 6 pairs. Two channels: CR (projective, tan θ) and Res (arithmetic, sin²θ).

| Pair | Channel | Value | Angle | Status |
|---|---|---|---|---|
| (2,3) boson–lepton | CR 5pt | tan=2/3→4/13 | θ₁₂ | [DER] |
| (2,3) boson–lepton | CR 4cusp | tan=9/8→81/145 | θ₂₃ | [DER] |
| (1,3) anchor–lepton | Res | 2/91 | θ₁₃ | [DER] |
| (2,6) boson–quark | Res | 4/7 | Schur corr. | [THM-arith] |

θ₁₃ chain: sin²θ₁₃=(1/N)·(d₁²/L)·(d₂/det_M)=2/91 — traverses ALL 4 face types. Uniqueness: Catalan d₁²+d₂²=Φ₃(d₂) only for (2,3) among 10 semiprimes N≤35. Assignment forced: 4/13 unreachable from Res, 2/91 unreachable from CR (Dead #78, 0/378). 17 invariants in PMNS range, unique 1σ match. Deps: X.100, X.101, X.108, X.110, X.110a, K.5.

## X.129 (S217) [THM-arith]: Index Formula for sin²θ₁₃

**sin²θ₁₃ = [SL₂(ℤ):Γ₀(N)] / (N·∏_{p|N} Φ₃(p)) = index/(N·L·det_M) = 12/546 = 2/91.**

Euler product: sin²θ₁₃ = ∏_{p|N} Φ₂(p)/(p·Φ₃(p)) = (3/14)·(4/39) = 2/91. Tautologically equivalent to index formula via index=N·∏Φ₂(p)/p.

**X.129a** [THM-arith]: GN(e,τ,μ)=(29,13,5) → PMNS denominators. 13=GN(τ), 145=GN(μ)·GN(e), 91=L·GN(τ). Convention-independent (set-level). Mechanism: all leptonic cosets have c=d₁, Catalan d₁²+d₂²=Φ₃(d₂)=GN(τ).

**X.129b** [THM-arith]: ∏GN_lep=1885=universal denominator for sin²θ_i·cos²θ_j products (s₁₂²c₂₃²=256/1885=d₁⁸/∏GN, etc). L·∏GN=13195=X.117 rationality denominator.

**X.129c** [THM-arith]: Unified cyclotomic table.

|  | p=d₁=2 | p=d₂=3 |
|---|---|---|
| Φ₂(p)=p+1 | 3 | 4 |
| Φ₃(p)=p²+p+1 | 7=L | 13=det_M |
| Φ₄(p)=p²+1 | 5=N−1 | 10=|B₁| |

Catalan bridge: Φ₂(d₂)=d₂+1=d₁²=4. Separately: Φ₄(d₁)=d₁²+1=N−1=5.

sin²θ₁₂=Φ₂(d₂)/Φ₃(d₂)=4/13 (single-prime). tan θ₂₃=Φ₂(d₁)²Φ₄(d₂)/(Φ₄(d₁)Φ₂(d₂)²)=90/80=9/8 (cross-prime, (2,3)-specific). sin²θ₁₃=∏Φ₂(p)/(p·Φ₃(p))=2/91 (Euler product). Φ₂ in ALL three. sin²θ₁₃/sin²θ₁₂=1/(d₁L)=1/14.

**X.129d** [THM-arith]: tan θ₂₃ = Π₊₋/Π₋₊ in cyclotomic form. Reformulation of X.101/X.50/L.4.

Deps: X.99, X.108, X.110, L.4, Q.3.

## X.130 (S218) [DER]: Channel Rule Theorem

**Statement:** The mapping face-pair invariant → PMNS angle is unique. Each angle accessible from exactly 1 channel; parametrization (tan vs sin²) forced.

**Proof:**
(a) **Forced assignment** [THM-comp]: θ₁₂=4/13 unreachable from any Res ratio or Res²/(1+Res²). θ₁₃=2/91 unreachable from any CR²/(1+CR²) (Dead #78, 0/378). θ₂₃=81/145 unreachable from any Res ratio. No freedom in channel→angle mapping.
(b) **CR → tan** [THM-math]: CR = ratio on ℙ¹. PMNS unitarity (sin²+cos²=1) forces ratio → tan θ → sin²=CR²/(1+CR²). Pythagoras, not Born rule.
(c) **Res → sin²** [forced]: Res(Φ₁)/Res(Φ₃) = 2/91 matches |U_e3|² by direct numerical comparison. Alternative parametrization tan=2/91 gives sin²=0.0005 (40σ off) — excluded.

**Physics input:** PMNS unitarity only. **Born rule not used** — LD computes numbers, experiment measures numbers; Born rule is experimentalists' tool for extracting |U|² from oscillation data, not an LD postulate.

**Consequence:** Channel rule removes the last caveat from I.4. θ₁₃ now on identical footing with θ₁₂, θ₂₃. All three [DER] with same identification step: «face-pair invariants of X₀(6) = PMNS angles.»

Deps: X.128, X.100, X.101, X.108, Dead #78.

## Dead #75–90 (S209–S216)

| # | Direction | Session |
|---|---|---|
| 75 | Mixed Schur P(σ∞)+h.c. | S209 |
| 76 | Modified propagator (two-scale) | S209 |
| 77 | V₃ irrep projection | S209 |
| 78 | CR scan for θ₁₃ (0/378) | S210 |
| 79 | P_face as base change | S211 |
| 80 | [L_eff, P_face] → CR-PMNS | S211 |
| 81 | W₆ equivariance | S212 |
| 82 | V₃ → direct PMNS | S212 |
| 83 | Irrep projectors → PMNS | S212 |
| 84 | p(σ∞)|_lep → CR-PMNS | S213 |
| 85 | Circulant sandwich | S213 |
| 86 | Real-solution uniqueness | S215 |
| 87 | Weighted Gram X.122 | S215 |
| 88 | Anti-symmetry b·c<0 selector | S216 |
| 89 | LD-point eigenvalues = monomials | S216 |
| 90 | LD-point sign pattern = F2 | S216 |

**Cumulative dead: 90+ directions.**

### Findings [OBS] (S217)

**Finding 1** (mediator n ↔ angle): n(d)=1→θ₁₃(min), n(b)=5→θ₁₂(mid), n(H)=6→θ₂₃(max). Σn(med)=12=index. Rank correlation on 3 items, p=1/6. [OBS]

**Finding 2** (GN neighbor sums, CW convention): ΣGN(REST neighbors of e)=24=d₁³d₂, τ=28=d₁²L, μ=40=Kirchhoff. **Convention-dependent** (CCW: 48, 40, 28). [OBS, CW-dependent]

### PMNS Pulls (NuFIT 6.0 IC19 NO, verified S206)

| Angle | Value | Pull | Status |
|---|---|---|---|
| sin²θ₁₂ | 4/13 | −0.06σ | [DER] |
| sin²θ₂₃ | 81/145 | +0.16σ | [DER] |
| sin²θ₁₃ | 2/91 | −0.06σ | [DER] |

**Σ|pull| = 0.27. 0 free parameters.** (S217 log reports 0.75 using NuFIT 5.x values — corrected here per S206 audit.)


---

# Z. CORRECTIONS LOG

| What | Was | Now | Session |
|------|-----|-----|---------|
| Σℓ | 42 | **39** | S43 |
| √2-knockout | 14σ, ×200 | **8.4σ, ×100.7** | S42 |
| Σn | 40 | **44** | S57 |
| Line graph | 3-regular, 18 edges | **NOT 3-regular, 17 edges** | S64 |
| α formula | "0.001 ppb" | **BULK ~600 ppm, IR fitted** | S54 |
| Row monotonicity | postulate | **FALSE** | S60 |
| genus(Γ₀(21)) | 1.67 | **1** | S66 |
| δG | −30.3 ppm | **−34.7 ppm** (at μ_G=1835.697) | S66 |
| IR norm form | "derivation" | **repackaging** | S67 |
| **IR formula** | **Form B: 1−1/j+11/j²** | **Form A: (j+N)/(j+L) = 1734/1735** | **S102** |
| **α⁻¹ value** | **137.035999084 (Form B)** | **137.035999202 (Form A)** | **S102** |
| **"HF selects CODATA"** | **c₂=11 argument** | **INVALIDATED (Form B dead)** | **S102** |
| **cos² status** | **[MOT] (9 dead)** | **[DER] (QTC 12-step chain)** | **S105–S106** |
| **IR status** | **[FITTED]** | **[DER conditional on Σ=−χ]** | **S103** |
| **τ=i selection** | **postulate** | **[THM] via E₂*=0** | **S101** |
| **μ_G description** | **"H.2 at NLO truncated"** | **nuclear masses: (3μ+μ_n−B_d/m_e)/4** | **S110** |
| **Ring status** | **"contraction mapping, 3 iter"** | **forward prediction + Newton; \|F'\| = 9.84 >> 1** | **S110** |
| **G status** | **"ring closure, not independent"** | **prediction given nuclear data; ring open at G** | **S110** |
| **Hierarchy L1** | **L1: α, μ, G** | **L1: α, μ (closed); L1b: G (open, nuclear input)** | **S110** |
| **T₃(H)** | **0** | **−1/2** | **S68** |
| CKM | FAILED 0/4 | **OBS 4/4** | S72 |
| ρ = L(f₁)/L(f₂) | ≈1.051 | **≈1.389** | S71 |
| ρ ≈ √C | SPEC | **DEAD** | S71 |
| σ²(B) | OBS | **THM** | S73 |
| Kirchhoff=40 | OBS | **THM** | S73 |
| n-formula slopes (d₂→up, d₁→down) | OBS | **THM** (F.3a Isospin Theorem) | S74 |
| λ = 9/40 mechanism | OBS with mechanism (S74) | **THM** (Residual Tree Theorem) | S75 |
| ℓ source | SM quantum numbers (external) | **Dessin: F(e)+S(e)** [DER] | S76 |
| Gap 3 scope | 4 external inputs (n,Φ,ℓ,α) | **1 external input (α/(2π) only)** | S76 |
| P₄ in G.9 | (t+3)²(t²+12t+24) [WRONG] | **(t+12)(t³+252t²+3888t+15552)** [CORRECTED same session] | S76 |
| G.9 R-residues | {+6,+3,+3} non-uniform | **{+3,+3,+3,+3} = +d₂ uniform** | S76 |
| θ₂₃ lower octant prediction | paper v4 prediction (3) | **WRONG — removed** (no LD candidate gives lower octant) | S77 |
| sin²θ₁₂ mechanism | K-ratio ansatz only | + heat kernel double-transversality [THM] + 4.6 ppm relative [OBS] | S77–S78 |
| f(M_lep) → 4/13 | untested | **DEAD** (no-go, 25 variants, μ-τ forces {0, 0.789, 1}) | S77 |
| G deviation | −30.3 ppm (paper v4) | **−35 ppm** (with CODATA α) | S77 |
| m_d/m_u pulls | −0.04σ PDG, +0.27σ FLAG (paper v4) | **−0.5σ PDG, +1.3σ FLAG** | S77 |
| G.2 BVP condition | "iff 1+d₂=d₁²" (false equivalence) | **d₁+d₂=5** (D⁴ fixed); 1+d₂=d₁² separate (Residual Tree) | S78 |
| I.9 ppm | 1.4 ppm (absolute) | **4.6 ppm (relative)** | S78 |
| I.9 heat kernel | exp(−L/(2d₁)) | **exp(−L/d₁)** | S78 |
| σ-pull convention | mixed (theory−exp in some places) | **(exp−theory)/σ** unified | S78 |
| Σω'(Q₄)=39 | [THM numerical] (S81) | **[THM]** (SymPy exact) | S82 |
| Σω'(all)=54 | [THM numerical] (S81) | **[THM]** (SymPy exact) | S82 |
| CRT-биекция | [THM, 12/12] (S82) | **[THM, 36/36, unique]** (all 36 dessins give same grid) | S83 |
| (n,ℓ,K,face) multiset | implicit | **[THM, 36/36]** dessin-invariant | S83 |
| Unified K(x₂,x₃) | open question | **DEAD** (CRT-irreducibility: v₃≠f(x₃)) | S83 |
| D.4 Laplacian eigenvalues | σ²=5→√5, σ²=1→√21 (swapped) | **σ²=5→√21, σ²=1→√5** | S83 audit |
| K-cipher structure | face-type primary (F.5) | **σ₁-partnership primary** (F.5a/b/d: BV(σ₁) is main variable) | S84 |
| K-cipher open directions | Mon-irreps, stabilisers open | **DEAD** (Mon transitive, |Stab|=6 ∀e, K not class function) | S84 |
| S84 σ₁-map | u↔c swapped in transfer | **Corrected**: σ₁(u)=t, σ₁(c)=p. F.5a/b/d tables rebuilt from verified edge table | S84 verification |
| E.8 spanning tree labels | forced={c,t}, multi-edge={u,p} | **forced={u,t}, multi-edge={c,p}** (u on bridge WV₁, {c,p} on multi-edge WV₀) | S85 |
| SC matrix col order | bos(2)↔lep(3) transposed in Φ₆/λ summary | **Corrected**: anc,bos,lep,qrk ordering throughout | S86 (E1) |
| v₃ d-quark qualifier | "Quarks: v₃=−1" without EWSB exception | **"Quarks (K≠√2): v₃=−1; d-quark (EWSB): v₃=0"** | S86 (E2) |
| SC cusp table ℓ-column | ambiguous (values don't match per-particle ℓ) | **Column removed**; ℓ is per-particle, not per-sector | S86 (E3) |
| μ anomaly status | "Two anomalous: d and μ" | **μ NOT anomalous** (F.7b formula absorbs it); only d-quark structurally exceptional | S87 (E4) |
| K-cipher item Y.4 | F.5a primary, sp bit open | **RESOLVED by ε-η architecture** (F.6–F.7b-K: label-free, constructive) | S87 |
| S51 Schreier spectrum | {0,2,3,4,6,7} | **OBSOLETE** — replaced by I.6 Cayley spectrum (12×12, 8 distinct eigenvalues) | S77/S89 |
| K.1 P₃ typo | "P₃ coefficients" | **R₃ coefficients** | pre-existing |
| C.1 convention | implicit | **σ₁·σ₀·σ∞ = id** (explicit) | S90 |
| t* for 4/13 | "close gap?" | **UNCLOSABLE**: t* transcendental (PSLQ deg ≤ 8 NULL) | Flavor |
| φ-pair role | assumed relevant | **0.015% contribution** — irrelevant; √21-pair dominant (18.8%) | Flavor |
| I.9d pull signs | +0.8σ, −2.0σ, +1.4σ (theory−exp) | **−0.8σ, +2.0σ, −1.4σ** ((exp−theory)/σ convention) | Flavor audit |
| σ∞ convention | σ₀·σ₁·σ∞=id (S90 initial) | **σ₁·σ₀·σ∞=id** | S90/S91 |
| φ-zero set | {p,c,t} (S90 initial) | **{p,c,u,t}** (u also zero) | S90 |
| A.3 path count | 20 | **≥24** (add moonshine, cross-duality, Schur disc, Schur eigvecs) | S92–S97 |
| Kirchhoff bridge | THM D.4 only (graph) | + THM M.3 (= 1/α₃(d₁) = |P³(𝔽₃)|) | S95 |
| Gap 3 status | MOTIVATED (G.9 ω) | MOTIVATED+++ (G.10 + M.1–M.5 Eisenstein) | S91/S95 |
| Contour shift | untested | DEAD (M.6: single pole at s=1) | S95 |
| h_int∝Φ hypothesis | open | **DEAD** (S90: no proportionality) | S90 |
| Any Schreier op→n | open | **DEAD** (S91: σ∞ invisible to L_Sch) | S91 |
| sin²θ₁₃ | 0.006 (t=1/2 tree-level) | **0.022 at t=√5/2** [CONJ] | S97+ |
| Gap 9 (PMNS) | I.9d ε-perturbation only | + Schur complement (I.11–I.14) + heat kernel PMNS (I.17) | S97/S97+ |
| S97.6 interpolation | [OBS] α=1/|B₁| | **OBSOLETE** — replaced by pure HK t=√5/2 | S97+ |
| t derivation | open | **DEAD** (~25 functionals, none within ±0.05 of √5/2) | S97++ |
| S97/S97+/S97++ pull signs | (theory−exp)/σ in session logs | **Flipped to (exp−theory)/σ** in companion (I.14, I.17, X.11, Y.2) | S97++ audit |
| **I.3 status** | [THM] | **[THM-arith / CONJ]**: eigenvectors [THM], PMNS identification [CONJ] | **S98 audit** |
| **I.14 status** | [THM] | **[THM-arith / CONJ]** + Robustness Lemma I.14-R: gap = [M_ν, L_eff]=0 | **S98 audit** |
| **I.22 status** | [THM] | **[THM-math / CONJ]**: eigvec-eigval identity (Thompson 1966) [THM-math], θ₁₃ interpretation [CONJ] | **S98 audit** |
| **M.4 status** | [THM] | **[OBS]**: Δn ≠ ramification (verified: quarks {2,2,3,4,6}, leptons {1,3}) | **S98 audit** |
| **M.4 quark Δn** | {0,1,1,2,2} (sorted-order error) | **{2,2,3,4,6}** (verified: σ∞ cycle c→t→d→s→b→u) | **S98 verification** |
| **M.3 status** | [THM] | **[THM-arith / OBS]**: 40=40=40 each [THM-arith], bridge [OBS] | **S98 audit** |
| **G.8 dependencies** | C.1, C.3, F.3a | + **SM_QN** (boson ℓ values require T₃, \|Q\|) | **S98 audit** |
| **F.2 dependencies** | δK formula (§G) | + **EMP_masses** (sign(δK_obs) from empirical masses) | **S98 audit** |
| **New section I.25** | — | **Identification Hierarchy**: 3-layer logic frame, robustness lemma, closure criteria | **S98 audit** |
| **A.3 path count** | ≥24 | **≥26** (add irrep localization, S₃ polarization) | **S99+S100** |
| **Gap 3 status** | MOTIVATED+++ | **CLOSED** (3a,3c,3d [THM]; 3b [DER+MOTIVATED]) | **S100** |
| **Gap 9 status** | CONJ only | **[DER+MOTIVATED]**, ≥38 dead, 3-layer structure | **S99+S100** |
| **I.9d S₃ weights** | φ-pair = 2:3 (S99 non-orthonormal basis) | **3:7 = d₂:L** (corrected S100) | **S100 [CORRECTED]** |
| **det(L\|_{std⊗V})** | (not stated) | **75 = 3·5²** | **S100** |
| **det'(L_eff)** | (not stated) | **45/11 = d₂²(N−1)/(2N−1)** | **S100** |
| **Neutrino predictions** | (not stated) | **m₁=0, NO, Σmν=0.059 eV** [PRED] | **S100** |
| **Ring universality** | (not stated) | Edge spread 100% vs ring 0.002% → [DER+MOTIVATED] M.7 | **S100** |
| **I.17 exp values** | NuFIT 5.x (0.570±0.020) | + **NuFIT 6.0 table** (IC19 and IC24+SK) + **octant prediction** [PRED] | **S101 audit** |
| **I.4 exp source** | "NuFIT" (unspecified) | **NuFIT 5.x** (explicit) | **S101 audit** |
| **I.26.4 justification** | "dimensional analysis" | **"scale matching"** (all quantities dimensionless) | **S101 audit** |
| **I.28.4 DESI 3σ** | "F-C in 3σ tension with floor" | **Clarified**: 3σ from Bayesian Σm_{ν,eff} analysis, not direct F-C vs floor | **S101 audit** |
| **γ_CKM exp** | **65.98°±4.0° (−0.015σ)** | **(62.8±2.6)° LHCb 2025 (−1.25σ)**. Now max-pull CKM. | **S109** |
| **Σ=−χ status** | **[MOT]** | **[DER conditional on weight=level]** (S108: 3a-3e chain) | **S108** |
| **α overall** | **~75%** | **~80%** (Σ=−χ upgrade) | **S108** |
| **CKM χ²/dof** | **0.40** | **1.96** (γ dominates) | **S109** |
| **σ₁ full map** | (ut)(cp)(be)(dH)(sμ)(Wτ) implicit | **(ut)(cp)(bμ)(de)(sW)(τH)** unique, MCT 12/12 | **S112** |
| **σ∞ full cycle** | not explicitly recorded | **(cubsdt)(eτμ)(WH)(p)** type (6,3,2,1) | **S112** |
| **σ₀ full orbits** | not explicitly recorded | **(cup)(bte)(sμH)(dWτ)** type (3⁴) | **S112** |
| **I.6 Aut(G)** | (W↔H)(e↔b)(s↔μ)(τ↔d), "minimal breaking word" | **(c↔p) only, \|Aut\|=2** (multi-edge endpoints) | **S112** |
| **I.3 σ₁(e) text** | "S-partners are quarks (s and b)" | **"(d and b)"**: σ₁(e)=d, σ₁(μ)=b | **S113** |
| **F.5/F.5b formula** | δ(e, pre_anc) in quark/S=anc branch | **δ(σ₁(e), anchor)**: c=σ₁(anchor), not pre_anchor | **S113** |
| **F.5e mechanism** | "pre_anchor +1" | **"σ₁(c)=anchor term"** | **S113** |
| **E.8 boundary pairs** | {d⊕H} × {W⊕τ} | **{s⊕W} × {τ⊕H}** (WV_E and WV_F, both star—oth) | **S113** |
| **E.8 interior** | {b, e, μ, s} | **{b, μ, d, e}** (WV_C and WV_D) | **S113** |
| **pre_anchor identity** | c (conflated with σ₁(anchor)) | **u** = σ₀⁻¹(p); σ₁(p) = c is a different edge | **S113** |
| **D.1 proof text** | σ₀(σ₁(x))=x in Forward/Reverse | **σ₀⁻¹(σ₁(x))=x** (MCT: σ∞=σ₀⁻¹·σ₁). m=1 unaffected | **S115** |
| **F.5 table** | truncated after 7/11 rows | **11/11 complete** (e,τ,μ,W,H added) | **S115** |
| **K.1 disc(R₃)** | "R₃ (cubic)" | **"R₃ (scaled: R₃(12s)/12³)"**. Raw disc = −2¹⁴·3¹¹ | **S115** |
| **H.3 G_pred** | 6.67410 × 10⁻¹¹ (rounded up) | **6.67407 × 10⁻¹¹** (exact computation, δG = −35 ppm consistent) | **S115** |
| **F.5 status** | [OBS] | **[THM]** (subsumed by F.7b-K constructive derivation) | **S116** |
| **F.5e status** | [OBS] | **[THM-arith]** (arithmetic on derived K) | **S116** |
| **F.8 status** | [OBS] | **[THM-arith/OBS]** (Σn from F.3; Σℓ partial) | **S116** |
| **PMNS root gap count** | 2 (I.14-ID, I.17) | **3** (I.14-ID, I.3-ID, I.17 independent). Proved: [M_lep, L_eff] ≠ 0 (I.29) | **S116** |
| **A.3 path count** | ≥30 | **≥31** (add d₁+(N−1)²=d₂³ from I.29) | **S116** |
| **H.1d pull signs (all 6)** | +1.2σ/−4.3σ/−0.4σ/−10.9σ/+2.4σ/−5.3σ (theory−exp) | **−1.2σ/+4.3σ/+0.4σ/+10.9σ/−2.4σ/+5.3σ** ((exp−theory)/σ). Root cause: S102 creation pre-dates S97++ sign audit. χ² sign-blind → not caught in S115. | **S118** |
| **H.1d "Rb Parker 2018"** | Parker 2018 = Rb | **Parker 2018 = Cs** (Science 360:191). **Rb = Morel 2020** (Nature 588:61). | **S118** |
| **H.1d χ²(B)** | 165.6 | **166.2** (= 4.33² + 10.91² + 5.33²) | **S118** |
| **Notation table α⁻¹** | 137.035999084 (CODATA 2018) | **137.035999177(21) (CODATA 2022)** | **S118** |
| **New §P.1** | — | **Heegner obstruction** [THM-arith]: τ=i, τ=ρ not Heegner on X₀(6). Complementary inertness. D=−8 first Heegner, t²−72t−648=0. Kudla+Arakelov DEAD for α. | **S118** |
| **New §R** | — | Cuspal regulators R.1–R.9 | **S119–S121** |
| **R.1 ∫η(t₆,t₆+8)** | not computed | **[THM]**: −2π ln 2, analytical proof via Bloch-Wigner + cuspal phases | **S120** |
| **R.2 ∫η(t₆,t₆+9)** | not computed | **[THM]**: −2π ln 3, analytical proof, same method | **S120** |
| **R.3 general formula** | not stated | **[THM] for 2 cases, [THM-arith] by pattern**: ∫η = −2π ln(w_c), mechanism = e_c cancellation | **S120** |
| **R.5 third symbol** | not computed | **[THM]**: ∫η(t₆+8, t₆+9) = 0 on finite paths (Catalan: \|d₂²−d₁³\|=1) | **S121** |
| **R.6 real paths** | not stated | **[THM]**: ∫η = 0 on real-t₆ paths (d(arg)=0 for real functions) | **S121** |
| **R.7 uniqueness** | not stated | **[THM]**: R.3 mechanism unique to N=6 (ν₂=ν₃=0 = Path A) | **S121** |
| **R.8 K₂ structure** | not stated | **[RESOLVED]**: rk K₂=3, effective=2, = #{lattice generators} | **S121** |
| **R.9 regulator table** | not stated | **60% resolved**: Classes A+B [THM], Class C [OPEN, deferred] | **S121** |
| **Brunault / L-functions** | OPEN | **DEAD forever** — PSLQ NULL (11 tests, 80 digits) + Baker independence | **S121** |
| **A.3 path count** | ≥31 | **≥32** (add cuspal regulators, cluster 2) | **S120** |
| **New §Q** | — | Cayley–Hecke bridge: Q.1–Q.3 | **S122** |
| **Q.1 trace formula** | not computed | **[THM-comb]**: Tr(A·T_p^{left})=(p+1)−2χ₋₃(p), unique N=6 | **S122** |
| **Q.1 decomposition** | Tr(σ₁·T)=2 (session WRONG) | **Tr(σ₁·T)=(p+3−4χ)/3, Tr(σ₀·T)=(p−χ)/3** | **S122 audit** |
| **Q.2 formula** | Tr(A²)=3ψ+4#{fix σ∞} (session WRONG) | **Tr(A²)=3ψ+2ν₃+4** [THM], verified 12 levels | **S122 audit** |
| **Q.2 N=21** | #{fix σ∞}=2 (session WRONG) | **#{fix σ∞}=1 always; ν₃=2 for N=21** | **S122 audit** |
| **Q.3 Gaussian norms** | not computed | **[THM]**: E₂(γ(i))=(c²+d²)·3/π, 12 norms, Σ=132 | **S122** |
| **A.3 path count** | ≥32 | **≥33** (add Q.1, cluster 9: Cayley×Hecke) | **S122** |
| **Spectral theory** | PRELIMINARY NULL | **CONFIRMED NULL** (full Φ(s) scan, Z(s), geodesics) | **S122** |
| **New H.1i** | — | **[THM]**: Grothendieck splitting f_* O = O ⊕ O(−1)^{11}, Atkin-Lehner binary | **S123** |
| **H.1c step (3)** | [DER cond. on weight=level] | **[DER + 1 bit empirical]**: W₆-odd from Grothendieck, ≈2400σ confirmed | **S123** |
| **H.1g IR row** | [DER conditional] | **[DER + 1 bit]**: binary selection, ∞→2 candidates | **S123** |
| **DEAD: W_N=parity** | not tested | **DEAD**: W_N acts on τ (modular), P acts on spacetime, no bridge | **S123** |
| **New §F.7d** | — | **[THM-arith]**: Global n-polynomial, 10 terms, 12/12, unique minimal | **S127** |
| **New §F.7e** | — | **[THM-arith]**: Global ℓ-polynomial, 5 terms, 12/12. Bosons from η₁ bit | **S127** |
| **New §F.7f** | — | **[THM-comb]**: ε-η algebra completeness, rank 12 = full diagonal | **S125** |
| **G.8 status** | [DER] (SM_QN for bosons) | **[THM-arith]**: F.7e gives ALL ℓ from ε-η. SM_QN dependency REMOVED | **S127** |
| **F.8 Σℓ status** | Σℓ partial (bosons need SM_QN) | **Σℓ fully from ε-η [THM, F.7e]** | **S127** |
| **New §S** | — | Cipher operator C_sym, σ₁-blocks, traces, irreps, V₂ eigenbasis (DFT S125–S132) | **S125–S132** |
| **A.3 path count** | ≥33 | **≥35** (add reciprocal cusp S.1, V₂ cipher det S.7) | **S125, S131** |
| **V₃ char poly sign** | x³−62x−60 (S131 session log) | **x³−62x+60** (correct: constant = +d₁²d₂(N−1) = +60) | **S131 [ERRATA]** |
| **28 DFT dead** | — | D1–D28: no operator eigenvalues=n, no Mon/cipher→α/(2π). Structural barrier confirmed | **S125–S131** |
| **rank ⟨L,σ∞⟩ diagonal** | 11 (S134 WRONG) | **12** (full non-commutative algebra needed) | **S135** |
| **S134 structural barrier** | "Φ−Lℓ ∉ ⟨L,σ∞⟩" | **Φ−Lℓ ∈ ⟨L,σ∞⟩ = ℂ[Mon]** (S134 used commutative sub-algebra only) | **S135** |
| **Σ(56·w)** | −312 (S135 WRONG) | **−256 = −d₁⁸** (analytical: 56·Σtarget/24) | **S138** |
| **f₀ = 36/π status** | [THM] (S134) | **[DEF]** (repackaging of BULK=432/π) | **S135 critique** |
| **a₄ = 132 uniqueness** | [THM] (S134) | **[OBS]** (σ² circularity: only proven for N=6) | **S135 critique** |
| **"4 discrete selections"** | 4 (G.0) | **1 postulate + 1 THM + 1 DER + 1 MOT** (U.4 upgrades additive form) | **S137** |
| **CKM status E.2–E.6** | [OBS]×4 | **[OBS→DER via V.4]** (UST framework, χ²/dof=0.66) | **S138** |
| **Y.15 CKM isolates** | E.2–E.6 fully isolated | **Connected to dessin via V.4** (UST framework) | **S138** |
| **A.3 path count** | ≥35 | **≥37** (add palindromic UST #36, complementarity #37) | **S138** |
| **CKM χ²/dof (E.2)** | **1.96 (dof=1)** | **0.66 (dof=3)**: (d₁,d₂) are model constants, not fit params | **S142** |
| **V.4 dof** | **dof=1 (line 4992)** | **dof=3** (consistent with χ²/dof=0.66 on same page) | **S142** |
| **S115 χ²/dof** | **1.95** | Stale: pre-S138 value with old pulls. Current = **0.66** | **S142** |
| **S139 BV denoms** | D={1,3,14,26}, Σ=44 | **N_ω={1,3,7,13}, Σ=24=d₁·index** (factor-2 bug) | **S140** |
| **S139 r=0.91** | [OBS] | **DEAD** (LEE: canonical r=−0.08) | **S140** |
| **S140 RMS_resid/RMS** | 0.80 ("86% unexplained") | **0.54** (S140 wrongly included anchor e) | **S141** |
| **S140 improved count** | 6/9 | **8/10** (counting error) | **S141** |
| **F.1 status (G.0)** | exact mass formula | **LO rule** (signs+orders, not magnitudes; R²=0.68) | **S140–S141** |
| **S140 Q.3 ref** | "Σ_WV=48 = Q.3" | **WRONG ref**: Q.3=132 (all 12 cosets), 48=WV only | **S142** |
| **η-product characters** | f_A, S, f_B ∈ M₂(Γ₀(6)) trivial char. | **Non-trivial character** (orders 4, 2, 4 under T: τ→τ+1). True basis: Eisenstein G_d = E₂(τ)−d·E₂(dτ), d∈{2,3,6} | **S144** |
| **Dead count** | 39 (S141) → 42 (S144) | **44** (+Eisenstein g_k #43, M_opt blocks #44) | **S145** |
| **S148 draft 3×3 spec** | {1, 4, 5} | **{d₁±√d₂, N−1} = {2±√3, 5}** (trace 9≠10) | **S148** |
| **S148 draft CRT §2.4** | "τ↔μ swap" | **columns only; rows completely different** | **S148 audit** |
| **S147 monomial** | −d₁/(d₂·det M_lep) | **−1/(d₂·det M_lep) = −1/39** | **S148 audit** |
| **S147 HK(e,e;1/2)** | 0.374 | **0.3265** (degenerate eigenspace double-count) | **S148 audit** |
| **Dead count** | 44 | **45** (+naive HK–modular form bridge) | **S148** |
| **S149 I.9h table** | 10/12 labels wrong | **Corrected** (root cause: (0,1)=p not c, since T∈Γ₀(6) fixes identity coset) | **S149 review** |
| **S149 V.9.4 draft** | "minimum commute time C=36" | **FALSE**: min C = 72/5 for {c,p}. C=36 for exactly 3 pairs (rank 24–26/66) | **S149 review** |
| **S149 V.8.5 draft** | "λ=1/5 spans interior {b,μ,d,e}" | **FALSE**: 4D eigenspace mixes interior and boundary (bdy coefficients ±0.41) | **S149 review** |
| **S149 V.9.1 1044** | "LD monomial" | **FALSE**: 1044=2²·3²·29, prime 29 not LD | **S149 review** |
| **S149 V.10.4 draft** | "11/12 unique syndromes" | **10 of 12** unique; c and p collide; 11 distinct syndrome values | **S149 review** |
| **Dead count** | 45 | **48** (+δK from UST joint #46, Z₄ charges #47, Φ−Lℓ as Eisenstein #48) | **S149** |
| **S152 n-vector** | Hardcoded qn dict with 7/12 wrong n-values (d=4,p=0,e=3,τ=2,μ=5,W=3,H=2) | **ANNULLED: S.7.6, G.0a from S152 patch.** n must be DERIVED from monodromy via F.7. n=2 impossible in LD (valid: {0,1,3,4,5,6,7}). | **S153 forensic audit** |
| **S152 sin²(V₂)=1/13** | Claimed sin²(V₂(n),V₂(ℓ))=1/det(M_lep) | **FALSE.** Correct: sin²=972/2821. Root cause: wrong n-vector. | **S153** |
| **S152 V₂ dominates Φ−Lℓ** | Claimed V₂=39.1%, V₃=1.3% | **FALSE.** Correct: V₃=36.0% dominant, V₂=20.9%. | **S153** |
| **S152 Σ(Φ−Lℓ)≈−α⁻¹** | Claimed −960/7≈−137.14 | **FALSE.** Correct: −768/7≈−109.71=−d₁⁸d₂/L. | **S153** |
| **S152 ⟨n⟩=det(M)/4** | Claimed Σn=39, ⟨n⟩=13/4 | **FALSE.** Correct: Σn=44, ⟨n⟩=11/3. | **S153** |
| **S152 σ₁-pair diffs=K,d₁²L,d₂L** | Claimed 40,28,21 | **FALSE.** Only (c,p) diff=−d₂L survives. | **S153** |
| **S151 M₄ table** | Eisenstein percentages listed without τ₀ | **Marked τ₀-dependent** (cusp form percentages τ₀-independent; Eisenstein not) | **S152 verification** |
| **H.5 G_pred** | 6.67410 × 10⁻¹¹ | **6.67407 × 10⁻¹¹** (H.3 corrected S115, H.5 missed) | **S153.1** |
| **V.4 J pull** | +0.16σ | **−0.15σ** (sign error, convention (exp−theory)/σ) | **S153.1** |
| **I.1 vs I.28** | Both active, no cross-ref; I.28.2 [PRED] | **Cross-refs added; I.28.2 → [CONJ cond. I.14-ID]** | **S153.1** |
| **E.6 χ² formula** | 0.15² | **0.13²** (0.15 = R_b² value, not pull) | **S153.1** |
| **V.4 R_b pull** | +0.15σ | **+0.13σ** (not reproducible from E.5 data) | **S153.1** |
| **Q.3 ↔ I.9h** | Two (c,d) tables without convention label | **Convention note added to both; T=σ∞ vs T⁻¹=σ∞ equivalent** | **S156** |
| **E₂ⁿ CHECK 26** | "likely dead, not proven" for n≥2 | **[THM-arith]: DEAD for all n≥1 via \|A_e\|=E₂(i) identity** | **S156** |
| **S156 CHECK 27** | Σ Im×12 = 42 = LN noted as coincidence | **Convention-dependent (42 or 26); dropped as non-invariant** | **S156** |
| **S155 erratum** | n(e) = 3 in handoff | **n(e) = 0; pair sum (d,e) = −484/7 not −376/7** | **S156** |
| **Dead count** | 50 | **51+** (+E₂ⁿ·fₖ infinite family, Class H barrier) | **S156** |
| **n(p) = 0 in S157 draft** | S157 draft code | **n(p) = 4, ℓ(p) = 0, Φ−Lℓ(p) = 192/7** | **S157** |
| **Rank-12 at τ₀=0.3+0.8i** | S161 | **Numerical artifact: worst \|q\|~0.77–0.81, residual 10⁻¹⁵ = Class C tautology** | **S161** |
| **"Gap 3: CLOSED" unqualified** | pre-S162 | **Sub-gaps (3a)–(3d) closed; product form δK=α·(Φ−Lℓ) remains [POSTULATED/G.5]** | **S162** |
| **Dead count** | 51+ | **54+** (added X.43 Class I, X.45a non-CM, X.45b Petersson/double coset) | **S162** |
| **Barrier classes** | 8 (A–H) | **10** (6 hard Gap 3: A, B, H, I, I′, sign + 4 guards: C, D, F, G) | **S162** |
| **X.45a anchor dominance** | [OBS] (3 τ₀ points) | **[THM-arith + THM-comp]** (I.9j elliptic linking + null-space concentration) | **S166** |
| **Direction 🟢 #4** | Γ₁(6)/Γ(6) forms — OPEN | **🔴 DEAD #56** M₂(Γ(6)) rank=12 at generic τ₀ → Class C | **S166** |
| **G.6 d₁-multiplier** | [OBS], mechanism OPEN | **Mechanism EXPLAINED by G.0b** (face(σ₁) ∈ {1,2} → h ≈ d₁) | **S168** |
| **F.1 LO R²** | 0.68 (best available) | **NLO G.0b: R²=0.891**, 0 free params, h=(d₁,d₂²/d₁²,1,d₁/d₂) | **S168** |
| **Dead count** | 54+ | **56+** (added X.46 M₂(Γ(6)) #56, X.47 structural barrier) | **S168** |
| **Open 🟢 directions** | 6 (#1,2,4,5,6,7) + 1 🟡 (#3) | **5** (#1,2,5,6,7) + 1 🟡 (#3). #4 DEAD. | **S166** |
| **Gap 3 h-derivation** | h postulated (G.0b [OBS]) | **G.0c: 3+Catalan → unique h** [DER cond.]. (1)+(1') [THM], ONE of {(⊥),(2)} [OBS]. | **S169–S175** |
| **h(1) origin** | unknown | **h(1) = d₁ = e₋(d₁)/e₋(d₂)** [THM-arith X.56] via Catalan | **S171** |
| **G.0c DOF** | 1-param (S169, wrong) | **3+Catalan** (S172). (⊥)⟺(2) mod Catalan. 2 [OBS]→1. | **S172** |
| **X.49 ⊥ status** | automatic (S170, wrong) | **Independent [OBS]**: 6(3t−s) ≠ 0 on full family | **S171 correction** |
| **Dead count** | 56+ | **58+** (added X.52 ω-cusps #57, X.53 UST-per-face #58) | **S169** |
| **Tensor factorization** | — | **T = T^(p) ⊗ T^(q)** [THM-arith X.57]. 6 levels verified | **S172** |
| **CRT duality** | — | (⊥) ⟺ ratio = −ι(d₂) [THM-arith X.59] | **S173** |
| **q-dirt, spectral shift** | — | X.60, X.60a [THM-arith]. v_q unique stat→decay | **S174** |
| **Directions (a)(b)** | Open | **DEAD**: (a) 13 functionals; (b) Selberg diag cusp-blind | **S172/S173** |
| **L8.11 commutator text** | "both n=ℓ particles in orbit 2" | **one n=ℓ (W) in orbit 2; s in orbit 1** | **S176/S177** |
| **Tr(A²)=K status** | [OBS] (N=6 only) | **[THM-arith, unique to X₀(6)]**: 6 levels tested, only N=6 matches | **S177** |
| **Layer 8** | — | C.8.1–C.8.12 + X.61–X.73: 29 results, all verified S177/S178 | **S176–S178** |
| **X.78 NOTE** | "(⊥) fails spurious" | **DELETED** — both Z₂ roots pass (⊥) by construction | **S185** |
| **X.83 label** | −1/(N·Σℓ) | **−1/[N·d₂·det(M_lep)] = −1/234** | **S185** |
| **X.87 pair count** | 570 | **1035 = C(46,2)** | **S185** |
| **X.91 exponent |det|** | "Any 2×2 has \|det\|=1" | **"Any 2×2 has nonzero det"** (\|det\|∈{1,2}) | **S188** |
| **X.92 eigvec matrix** | "Any 2×2 has \|det\|≠0" | **"V invertible (det = −144)"** | **S188** |
| **D.8 containment** | [OBS] | **[THM-arith]** via spectral bridge D.8b | **S193/S194** |
| **I.9g.12 chain** | [OBS→DER cond.] | **[DER]**: spectral bridge closes P_φ=det(M^{μτ}) gap | **S193/S194** |
| **I.17 swap** | 1 bit (free choice) | **forced [DER]** by Laplacian solar bound | **S190/S192** |
| **I.17 t** | motivated, not derived | **[DER]** via I.9g.12 chain | **S189/S193** |
| **I.17 params** | 1+1bit | **0** (t [DER], swap forced) | **S190–S194** |
| **I.28.2 item 1 (m₁=0)** | [CONJ cond. I.14-ID] | **KILLED**: forced swap → f(0)=0 unphysical under NO | **S192** |
| **R14 polynomials** | "one cubic governs all" | **4 different polynomials** (degree 2–5), common root d₁=2 | **S193** |
| **X.109 ERRATUM** | P^{-T}·L·P^{-1} | **P^T·L·P** | **S210** |
| **v = U_CR^T·(1,1,1)** | S215 basic: (0.050, 1.730, 0.066) | **FALSE. Correct: (0.695, 0.363, 1.544)** [V-S217] | **S217** |
| **I.4 sin²θ₁₃** | [CONJ] | **[DER]** via X.129 + X.130. Channel rule **closed**. | **S217/S218** |
| **X.121** | [THM-comp] independent | **TAUTOLOGY** of off-diag=0 condition | **S217** |
| **S217 Catalan bridge** | "Φ₂(d₂)=Φ₄(d₁)=d₁²=4" | **FALSE: Φ₄(d₁)=5≠4.** Correct: Φ₂(d₂)=d₁²=4, Φ₄(d₁)=N−1=5 | **S217 audit** |
| **S216/S217 pulls** | Σ\|pull\|=0.68/0.75 (NuFIT 5.x) | **Σ\|pull\|=0.27** (NuFIT 6.0 IC19, S206-verified) | **S217 audit** |


*Assembled: 2026-03-15, updated S217 (2026-04-02). S217 audit: 4 errata corrected (E1–E4).*
*Sources: paper v5.5, session logs S42–S100, S125–S146, S151–S153, S153.1, S156–S162, S166, S168–S217, Claude memory.*
*S88–S89: Independent verification of I.6/I.9 (Python/scipy ab initio).*
*S90: φ-zero theorem [THM], golden hierarchy [THM], h_int∝Φ DEAD.*
*S91: Partial fractions G.10 [MOTIVATED], face trace K.8 [THM], Schreier no-go [DEAD].*
*S92: P₄ Catalan K.7 [THM], inter-cuspal distances K.7a [THM].*
*S93: Companion integration (11 patches, 3 errors fixed).*
*S94: Moonshine K.9 [THM]: T_{6E}=t₆+5, 21st path, cluster 6 (sporadic).*
*S95: Section M (scattering splitting M.1–M.6). Cross-duality 22nd path. Kirchhoff=|P³(𝔽₃)|.*
*S97: Schur complement I.11–I.14. sin²θ₁₃(Schur) = 1/26. Eigenvectors = LD monomials. 23rd–24th paths.*
*S97+: Σ self-energy I.15, P₂₁ projector I.16, heat kernel PMNS at t=√5/2 [CONJ] I.17. Interpolation OBSOLETE.*
*S97++: Spectral projectors I.18–I.24. φ-pair structure, Q_φ²=L(K₃), D_τ duality, sin²θ₁₃ factorization. ~25 functionals for t DEAD.*
*S98: THM audit — 7 marker corrections (I.3, I.14, I.22, M.3, M.4, G.8, F.2). Robustness Lemma I.14-R. Identification Hierarchy I.25. M.4 downgraded [OBS].*
*S99: Irrep localization I.26 [THM], moment derivation I.26.2 [THM], CRT coupling I.26.3 [THM-arith], t=√P/d₁ prescription I.26.4 [DER]. 25th path. 13 dead directions.*
*S100: S₃ polarization I.27 [THM-arith], 26th path. Pythagorean identity P₂−P₁=d₁² [THM]. Gap 3 CLOSED (M.7 ring universality [DER+MOTIVATED]). Neutrino predictions I.28 [PRED]: m₁=0, NO, Σmν=0.059 eV. S99 φ-weight CORRECTED 2:3→3:7. ≥38 dead directions cumulative.*
*S101 audit: I.17 NuFIT 6.0 update (IC19/IC24 pulls, octant prediction). I.4 exp source annotated. I.26.4 "dimensional analysis"→"scale matching". I.28.4 DESI tension clarified. 4 Z-log entries added.*
*S101: E₂(i) identification H.1a [THM]. E₂* variational H.1f [THM]: replaces τ=i postulate, 27th path.*
*S102: j+N factorization [THM], 28th path. Form B DEAD (χ²=165.6 vs 7.3). Fricke product t₆(i)·t₆(i/6)=72 [THM]. IR structural mismatch (log vs rational) confirmed.*
*S103: IR chain 5 steps [DER conditional on Σ=−χ]. dim M_N=L from Path A [THM]. Eisenstein identity g_c(i)=E₂(i)−w_c [THM].*
*S104: 137=index·Σ(1/K) [THM], 29th path. Self-duality BULK·IR_coeff=index [OBS]. Fourier phases at cusps disproven (KR12). |d₁−d₂|=1 iff d₁=2 [THM], 30th path (lemma, not independent). BB^T eigenvalues = D.3 restatement (not new). 6 dead cos² approaches.*
*S105: QTC v2.2 created. cos² upgraded [MOT]→[DER] via 12-step chain (78/78 checks). 3 DEAD approaches added (#7-9). Alternative scan: best unified 8.7 ppb vs Form A 0.03 ppb.*
*S106: QTC directions 1-4 explored (Fricke distance, φ(d₁)=1/(2π), sheets, IR). Caveats C1-C3 strengthened. Fricke distance N.6 [THM], d₁=2 degeneracy N.7 [THM], dimension matching N.5 [THM]. 42/42 final checks. Companion integration.*
*S110: μ_G description CORRECTED (nuclear masses, not H.2 truncation). Ring NOT contraction (|F'|=9.84). G prediction OPEN (requires nuclear data). H.3a G-elasticity [THM]: 222/101. Hierarchy L1→L1+L1b. CLOSURE-TEST workflow rule added.*
*S107: Bootstrap invariant F(N)=B²·lnB/M: N=6 unique with 10⁴³ separation [THM-analytic]. Γ₀ family privilege [THM-computational]. N.1 (amplification identity) = tautology. N.3 (Banach) DEAD per S110. Paths 31-32 not independent → A.3 stays ≥30.*
*S108: Isospectrality X₀(6)↔X₀(11) [THM-computational] kills STM. det'(L)=N²(N−1)⁴ uniquely N=6. Σ=−χ upgraded [MOT]→[DER cond. on weight=level]. VMF saddle at τ=i [THM]. α overall →~80%.*
*S109: ω DEAD for per-particle Φ(n). All operator-diagonal DEAD (dim ℝ¹²=12 tautology). Graph automorphism [OBS→CORRECTED S112]. γ_CKM updated: (62.8±2.6)° LHCb 2025, pull −1.25σ. GREP-BEFORE-COMPUTE rule.*
*S112: Unique monodromy proven (1/480 candidates). σ₁ map CORRECTED: (bμ)(de)(sW)(τH). Aut(G)=(c↔p), |Aut|=2. σ₀-orbit invariants [THM-arith]. σ₁-pair n-sums [OBS].*
*S113: Companion audit — 7 errors patched (1 formula F.5b, 6 text/labels). §O.1 added (monodromy SSoT). E.8 boundary/interior relabeled. MCT rule established. 0 theorems affected.*
*S114: Tier-1 programmatic audit — 11 critical nodes, 11 PASS. 2 text-level issues (D.1 σ₀↔σ₀⁻¹, F.5 table truncation), 1 minor ambiguity (K.1 disc label). 0 theorems affected. Full chain σ₀,σ₁,σ∞ → α⁻¹ independently verified.*
*S115: Tier-2 verification — E.8 CKM (5 pulls ✓, χ²/dof=1.95), I.17 PMNS (NuFIT 6.0 6/6 ✓), K.9 Moonshine (16 coefficients ✓), H.2–H.3 (μ₀,μ,G ✓; G_pred CORRECTED 6.67410→6.67407), QTC (cos²,BULK,α⁻¹,Fricke ✓). 3+1 patches applied. Meta-audit: DAG ✓ (0 cycles), 73 [THM] — 0 inflation, Z-log S112–S113 complete.*
*S116: Coherence map (Y.15): 29 weak → 7 classes + 12 isolates. Commutator [M_lep,L_eff]≠0 (I.29) [THM-arith]: 55·C=[[0,30,37],[−30,0,−7],[−37,7,0]], orthogonal decomposition A₁⊥A₂. tan(2θ)=√2/5, sin²(2θ)=d₁/d₂³=2/27 [THM-arith]. 67-cancellation in eigenbasis. PMNS root gaps: 3 (not 2). 31st path: d₁+(N−1)²=d₂³. Status patches: F.5→[THM], F.5e→[THM-arith], F.8→[THM-arith/OBS].*
*S118: H.1d pull sign audit — all 6 signs CORRECTED (root cause: S102 creation in old convention, S97++ audit did not cover H.1d). Attribution CORRECTED: Rb=Morel 2020, Cs=Parker 2018. CODATA 2022 adopted: α⁻¹=137.035999177(21), Form A pull −5.6σ→−1.2σ. Heegner obstruction P.1 [THM-arith]: τ=i not Heegner on X₀(6) (complementary inertness), D=−8 first Heegner, Kudla+Arakelov DEAD for α. +2 dead (X.17).*
*S119: Cuspal regulators discovered numerically (Colab A100, 50-digit). ∫η(t₆,t₆+8)=−2πln2 [OBS, 0.0 ppm]. Categories/K₂/C*-algebra directions DEAD.*
*S120: Analytical proof of R.1–R.3 [THM]. Method: Bloch-Wigner vanishing on ℝ + cuspal phase arg(t₆)=−2π/e_c + ramification cancellation. 32nd path confirmed (cluster 2: ramification/j-geometry).*
*S121: Closed 4/5 open questions from S120. Brunault/L-function route DEAD (Baker + PSLQ 11 tests). R.3 uniqueness proven (ν₂=ν₃=0 ⟺ N=6 = Path A). K₂ structure: rk=3, effective=2. New vanishing theorems R.5 (Catalan ln|1|=0), R.6 (real-path d(arg)=0). Regulator table 60% complete (Classes A+B proven, Class C deferred).*
*S122: Cayley–Hecke bridge Q.1–Q.3. Q.1 [THM-comb]: Tr(A·T_p^{left})=(p+1)−2χ₋₃(p), unique N=6, 33rd path (cluster 9). Q.2 [THM]: Tr(A²)=3ψ+2ν₃+4 (corrected from session's 3ψ+4#{fix σ∞}); at N=6 gives 40=Kirchhoff. Q.3 [THM]: E₂(γ(i))=(c²+d²)·3/π, 12 Gaussian norms, Σ=132=index·dim M₁₀. Session decomposition errors corrected: Tr(σ₁·T_p)≠2, #{fix σ∞}≠2 at N=21. 4 dead: ‖[A,T]‖→α (0.9≠0.001), PMNS from A↔T (A|_lep=0), ΔT₅ vs δK (null), continuous spectral theory (confirmed null).*
*S123: Grothendieck splitting H.1i [THM]. f_* O = O ⊕ O(−1)^{11}. Atkin-Lehner: W₆-odd O(−1)^N vs W₆-even O⊕O(−1)^{N−1}. Binary IR selection: odd (α⁻¹=137.035999202, −1.2σ) vs even (137.035948904, +2394σ dead). Upgrade: [DER cond. on weight=level] → [DER + 1 bit empirical (W₆-odd, ≈2400σ)]. Overall ~80% unchanged. DEAD: W_N=spacetime parity (different spaces, verbal analogy only).*
*S125–S131 (DFT): Cipher operator C_sym and representation theory. ε-η global polynomials (n: 10 terms, ℓ: 5 terms). C_sym construction, σ₁-blocks (10/12 evals LD), trace identities (Tr(L·C_n)=−dim M₁₀). Projector traces, pairing theorem. Irrep decomposition V_perm=V₁⊕V₂⊕V₃⊕V₆ (dims=Div(N)). L+C_sym generate full 50-dim image. V₂ det=−31 (35th path). V₃ char poly x³−62x+60. Reciprocal cusp theorem (34th path). 28 dead directions (D1–D28). Gap 3 structural barrier confirmed: α/(2π) not from Mon/cipher algebra. Errata: V₃ constant sign +60 (not −60).*
*S132: V₂ cipher matrix in L-eigenbasis [THM-arith]. C_n|_{V₂} = (L/d₁)·[[1,(N−1)√d₂/L],[(N−1)√d₂/L,−1]]. tan(2θ)=5√3/7, sin²(2θ)=75/124. Level repulsion: bare gap d₁ → dressed gap 2√31.*
*S134: NCG Lagrangian. f₀=36/π≡Ω [DEF] (repackaging BULK/index). a₄=132=index·dim M₁₀ [OBS] (σ² circularity). S_LD full Lagrangian [DER], δK postulated. Heat kernel diagonal DEAD [THM]: 68% off-diagonal in L-basis, r=0.52. det variation DEAD: r=−0.06. Extended resolvent (L+aP∞+bP∞²+c·diag(w)+m²)⁻¹: R²=0.59 [ALIVE-WEAK]. S134 rank ⟨L,σ∞⟩ = 11 WRONG (corrected S135→12).*
*S135: Burnside-monodromy δK-operator. rank ⟨L,σ∞⟩ diag = 12 CORRECTS S134 (was 11). W≡H unique commutative degeneracy; splitter L·σ∞²·L (depth 4, Δ=−1). ⟨L,σ∞⟩ = ℂ[Mon], dim=50 [THM]. DDT eigenvalues = {d₁(×6), N(×2), d₁³(×3), d₁²N(×1)} [THM-arith]. w=DDT⁻¹·target ∈(1/56)ℤ¹² [THM-arith]. Σ(56w) = −312 WRONG (corrected S138→−256). M_opt: a(g)=Σ_{Fix(g)} w(k), symm, 7M_opt rational [THM]. Heat equation DEAD (R²=0.37). Physical principle for min ∥a∥² OPEN.*
*S137: Belyi connection. reg(ω) = LD monomials at 3 finite cusps: {5/12, −4/3, 3/4} [THM-arith]. Sum rules: Σw^k·reg at k=−1,0,1,2,3 = {0,−1/N,0,N,N|B₁|} [THM-arith]. Ramification duality reg(lep)·reg(bos)=−1 [THM-arith]. Genus 0 → additive δK forced [DER]. Face sums Σn, Σℓ = LD monomials [THM-arith]; boson Σ(Φ−Lℓ) = 89/7 (89 prime!). KK on M⁴×ℙ¹ DEAD (4 kills). "4 discrete selections" overcounted → 1 postulate + 1 THM + 1 DER + 1 MOT.*
*S138: UST framework. Edge probabilities {1, 1/2, 4/5, 7/10} = 4 LD monomials, palindromic ΔP = {1/5, 1/10, 1/5} [THM-comb]. P(boundary triple) = d₂²/K = 9/40, all 8 equal [THM-comb]. CKM: λ=P_triple, A²=9/13, tanγ=9/4, R_b²=3/20, χ²/dof=0.66 [DER]. sin²θ₁₂(PMNS) = ΔP/(ΔP+P_triple) = 4/13, A²+sin²θ₁₂=1 [THM-arith]. μ-τ breaking: σ₁(τ)=H (boundary), unique [THM-comb]. Physical bridge: transfer current theorem [DER]. Σ(56w) CORRECTED −312→−256=−d₁⁸. HK C₆→CKM DEAD, Schur up-dn→CKM DEAD. ≥37 paths.*
*S139: Coset norms Q.4 [THM-arith]: N_ω(BV)={1,3,7,13}, Σ=24; N_i(WV)={1,2,5,10,13,17}, Σ=48. Ratio=d₁. ERRATA: D={1,3,14,26} factor-2 bug (corrected S140). Belyi arc r=0.91 LEE artifact (corrected S140). 3 dead (#30-32). Ramification Φ = S30d confirmed.*
*S140: S139 corrections (BV denoms, r=0.91). F.1 LO diagnosis: 8/10 improved, ×1.84, RMS=1.49%, R²=0.68, RMS_resid/RMS_obs=0.54. τ/μ worsens. Φ_exp not function of n alone (spread up to 33). 4 dead (#33-36). ERRATA: "0.80"/"86%" included anchor e (corrected S141), "6/9" counting error.*
*S141: Paper v6 review (5 point edits). Edge-level modular scan: 3936+ tests, all below F.1. 4 dead (#37-39b). Structural barrier: geometry→(n,ℓ,K) but NOT→δK without dynamics. Live: DDT/M_opt, Eisenstein gₖ (dim M₂=3, untested). ≥37 paths confirmed.*
*S142: Audit of S139–S141. 7 errors traced and resolved. χ²/dof CORRECTED: 1.96(dof=1)→0.66(dof=3). Memory blocks #20,#29 corrected. 8 companion patches applied. New §Q.4 (coset norms). G.0 LO addendum. X.29–X.32 (dead #30–39b). Z-log: 10 entries.*
*S143: SM↔LD bridge. RG running → LD = IR theory (pole masses optimal). FN charges q=(L−n)/2 half-integer [OBS]. Fritzsch texture Cabibbo = 0.0495 (internal tension with UST 0.0506). Mon ≅ S₃×A₄ = 72 (known, not new). η-products f_A, S, f_B character issue identified. τ* = i·ln(μ)/π proposed then critiqued. 3 dead (#40–42).*
*S144: τ* critique finalized [DEAD]. η-quotient R-identity W.1 [THM-arith]: R = [(η₂η₃)/(η₁η₆)]¹² = (t₆+d₂²)(t₆+d₁³)/t₆. Catalan via modular function (path #38 = #20 alt). CM point t₆²=|Mon|. CRT irrep analysis C.7b: ℓ rank-1 (factorizes), K rank-2 (irreducible). η-product characters CORRECTED (order 4,2,4 not trivial). Cumulative: 42 dead.*
*S145: Eisenstein g_k DEAD #43 (r=0.52, CRT analytically realized but no δK; X.34). M_opt blocks→CKM/PMNS DEAD #44 (|V_ud|=0.82, sin²θ₁₂=0.088; X.35). R(w) at cusp widths: {90,55,44,35}, ΣR=224=d₁⁵L, differences={35,11,9}={N²−1,dimM₁₀,d₂²} [THM-arith; W.2]. det(L_rr)=R(d₁)·(N−1)²=1375, Tr(55·L_eff,nonzero)=ΣR=224 [THM-arith; W.2]. R'(−d₂²)·R'(−d₁³)=−1/|Mon| [THM-arith]. Three K_d=√2 characterizations [CONJ]. σ₁-pair ℓ-sums added to table. Cumulative: 44 dead.*
*S146: (s,W) self-duality [THM-arith; W.3]: unique n=ℓ pair, 7(Φ−Lℓ) common factor −13=−det(M_lep), ratio=d₁. {n,K} minimal complete identifier from F.1 ingredients [THM-comb; F.9]: Φ−Lℓ resolves 65/66≡(n,ℓ), sole collision (u,d) resolved by K. σ₁-pair Σℓ: quark={N,d₂,|B₁|}, cross={|B₁|,d₂²,d₁³}. Latin square 3×3 on uniqueness classes [OBS]. "Informational inversion" claim tested and rejected: n dominates at 60/66, shared tree/loop; α/(2π) value irrelevant for identification (any c≠0 works).*
*S147 (corrected S148): Modular flavor symmetry bridge. 6/6 structural matches with Li-Liu-Ding (arXiv:2108.02181): Mon=Γ₆, CRT=S₃×T', dim M₁=3, τ=i, m₁=0, μ-τ [THM-comp]. sin²θ₁₂: modular forms give 1/3 (trimaximal at τ=i); LD gives 4/13; difference = −1/(d₂·det M_lep) = −1/39 [THM-arith]. LD better by 2.1σ, JUNO 8.5σ. HK irrep decomposition [THM-comp]: V₁=0.0833, V₃=0.1385, V₂=0.0196, V₆=0.0851, total=0.3265 (NOT 4/13; 4/13 from DT restriction I.9). Y⁽⁶⁾₆ᵢᵢ ratio = −√d₂ [OBS]. t-interpolation: 1/3→4/13→1/3 as t: 0→1/d₁→∞. Naive bridge w_ρ≠|Y_ρ|² DEAD #45. Formal: finite Langlands for PSL₂(ℤ/6ℤ). 3 errors corrected by S148 audit (monomial, HK double-count, CRT retraction).*
*S148: BV-projection of Cayley Laplacian. σ₀-erasure Π·L=Π·(I−σ₁) [THM-arith]: quotient depends on σ₁ only. Π·L·Πᵀ: char poly λ(λ−1)(λ−d₁²)(λ−(N−1)), all LD monomials [THM-arith]. spec(ΠLΠᵀ)⊂spec(L) despite non-equitable partition [OBS]. Eig(3)⊥BV (×2), Eig(5)⊥BV (×3): dim ker(Π)∩spec=N−1=5 [THM-comp]. Non-anchor 3×3: spec={d₁±√d₂, N−1}, trace=d₂², det=N−1 [THM-comp; CORRECTS draft {1,4,5}]. Two independent √d₂ channels — NOT Gap 9. Canonical CRT: unique normal S₃ and A₄; face block-diagonal [THM-comp]. Canonical↔companion: columns τ↔μ, rows different [OBS; CORRECTS draft]. Workflow: IRREP-PROJECTOR, MONOMIAL-CHECK, SUM-PARTS=WHOLE. Cumulative: 45 dead, ≥37 paths.*
*S149: UST joint probabilities V.8 [THM-comb]: 5 pair types, all LD monomials; conditionals numerator dim M₁₀=11 (int↔bdy), d₂²=9 (bdy cross). Transfer current derives V.2 palindrome [THM-arith]. Covariance eigenvalues {1/2, 3/10, 1/5, 2/25, 0}, top 3 eigenvectors = E.8 boundary choices. Hitting times V.9 [THM-comp]: 6 classes reproduce golden hierarchy D.6–D.7 exactly, h(p→u)=d₂, h(p→t)=index, c uniquely symmetric. Kemeny κ=511/20, √21-sector=15=|P³(𝔽₂)|. C=∏wᵢ=36 for exactly 3 pairs. Dessin as [12,3,2] code V.10 [THM-comb]: k=β₁=3=d₂, d=2 from Anchor; codewords=E.8 choices; σ∞ resolves; syndrome=dessin address (c,p collision only). P¹ coset table I.9h [THM-arith/OBS]: S=σ₁, T=σ∞ standard; |j(γ,i)|²=|j(γS,i)|² (CM); min norms {1,d₁,N−1,|B₁|,det M_lep} forced by level. 3 dead (#46–48): δK from UST joint (r=0.60, X.37), Z₄ charges on P¹ (σ₁ fpf, X.38), Φ−Lℓ as Eisenstein (rank 11 vs dim 3, X.39). S149 draft corrections: 10/12 table labels wrong (p↔c root), C=36 not minimum, λ=1/5 not interior-only, c²+d² overclaim, 1044=29·36 not LD. Cumulative: 48 dead, ≥37 paths.*

*S151 (verified S152): f₄ = η₁²η₂²η₃²η₆² ∈ S₄(Γ₀(6)) lives in V₆ (100%, 5 τ₀ points) [THM-comp]. Hadamard fusion table on V_perm = 10 exact rational rules [THM-arith, S.11]. Key: V₆⊙V₂ = no V₂, V₆⊙V₆ → V₂ rank 2. Weight-6 cusp forms V₂-free [THM-comp]; V₂ appears at weight 8 via f₄² (31.7% CM, 28.7% generic) [THM-comp]. Selection rule [OBS]: ker Φ(f₄,·) ∩ V₃ aligned with Eisenstein direction. M₄ Eisenstein percentages τ₀-dependent (corrected). Cumulative dead unchanged at 49 (S150).*
*S152: Independent verification of all 6 S151 results confirmed (mpmath 50 digits + Fraction). NEW S152 results (S.7.6 sin²=1/13, G.0a V₂-dominant) computed with hardcoded n-vector containing 7/12 errors → ALL S152-new results ANNULLED by S153 forensic audit. Root cause: n=2 entered for τ and H, impossible in LD. ℓ-values correct 12/12.*
*S153: Forensic audit of S152. Three-way comparison (monodromy-derived vs companion vs S152): companion correct 12/12, S152 wrong 7/12 in n. Correct Φ−Lℓ irrep decomposition [THM-arith]: V₃=36.0% dominant, V₂=20.9%, V₁=14.4% (Σ=−d₁⁸d₂/L), V₆=28.7%. Rank barrier theorem S.12 [THM-arith]: weight k<10 structurally cannot reproduce Φ−Lℓ (dim M_k < rank 11). Weight-4 regression r=0.65 (DEAD #50, X.41). Barrier taxonomy file created (7 classes, A–G). Workflow rules: DERIVE-NOT-HARDCODE, VERIFY-BOTH, BARRIER-CHECK. Cumulative: 50 dead.*
*S153.1: Companion-wide consistency audit. 5 patches: (B.1) H.5 G_pred 6.67410→6.67407 (H.3 corrected S115, H.5 missed); (B.2) V.4 J pull +0.16σ→−0.15σ (sign error); (B.3) I.1↔I.28 cross-ref added, I.28.2 [PRED]→[CONJ cond. I.14-ID]; (B.4) E.6 χ² 0.15²→0.13² (R_b² value confused with pull); (B.5) V.4 R_b pull +0.15σ→+0.13σ. 5 workflow rules: PROPAGATION-CHECK, SIGN-CHECK, VALUE-VS-PULL, PREDICTION-XREF, CONVENTION-SPEC. 0 theorems affected.*
*S156: E₂ⁿ·fₖ ratio test + full audit. Universal E₂-modulus identity |E₂(i)+Δ_e|=E₂(i) [THM-arith]: (1−2c²/N)²+4c²d²/N²=1. E₂ⁿ·fₖ at τ=i DEAD for ALL n≥1, ALL even k [THM-arith]: pair ratio purely imaginary (i·tan nφ). Convention-independent. Q.3↔I.9h reconciled: T=σ∞ vs T⁻¹=σ∞ both valid, convention notes added. CHECK 27 dropped (convention-dependent). S155 erratum: n(e)=0 not 3. Class H barrier added. Cumulative: 51+ dead.*
*S157: Elliptic fixed point collapse [THM-arith]: S·i=i, S∉Γ₀(6) → cosets (0:1),(1:0) map to same point. 12→11 distinct ℍ-points at τ=i; 4 at τ=ρ. Anchor (192/7) ≠ quark (45/7) → inconsistent at ALL weights. Class I barrier. n(p)=4 correction verified. Cumulative: 52 dead.*
*S158: Weight-10 pointwise at 3 non-CM τ₀. 10/12 fit sub-percent; {p,c} anchor pair systematic failure (97–99.9% of residual). S-constraint [OBS]: f(−1/τ₀)=τ₀¹⁰f(τ₀) removes 1 DOF. "Laser pointer" to non-pointwise. Cumulative: 53 dead (one direction, 3 tests).*
*S159: S₁₀(Γ₀(6)) newform decomposition [THM-comp, PARI/GP]: 7=2+4+1, 4 rational orbits. 6.10.a.a unique at level 6: a₂=−d₁⁴, a₃=d₂⁴, W₂=+1, W₃=−1 (Fricke-odd). Period polynomial P⁺(u)=−N³u³+d₁d₂Lu²−Lu+1, root u=1/N, disc=−143=−13·11. P⁻ middle coefficients ∝ L·11=77. L-value algebraic parts: dim M₁₀=11 in all odd ratios (convention-dependent). Non-pointwise territory productive. [VERIFIED LMFDB S163]*
*S160: Double coset Γ₀(6)\SL₂(ℤ)/Γ₀(6) = 4 = σ₀(N) [THM-arith]. Class I′ barrier: bi-Γ₀(6)-invariant functional ≤ 4 values, kills coset-twisted Petersson (DEAD #54). Cumulative: 54+ dead.*
*S161: E₂·f₁₀ quasi-modular at τ₀≠i: Class H broken (|W| spread 89–128%). target/|W|² 30–45% better than plain M₁₀. SVD: 99.1% captured at best τ₀, residual ~1%. Direction 🟢 #3 → 🟡 SOFT DEAD.*
*S162: DDT/M_opt structural confirmations (T.6–T.8 re-derived, not independently verified to [THM]). Gap 3 reformulated: "why product δK=α·(Φ−Lℓ)?" Φ−Lℓ formula re-confirmed: Σ=−768/7=−d₁⁸d₂/L.*
*S166: M₂(Γ(6)) eval rank=12 → DEAD #56 Class C [THM-comp, DUAL-COMPUTE]. Unique elliptic σ₁-pair {p,c} [THM-arith, I.9j]: L=±S, |Tr|=0, only elliptic linking among 6 pairs. Null-space ≥98% on {p,c} at all generic τ₀ [THM-comp, DUAL-COMPUTE]. Geometric cause: S elliptic → minimal d_hyp. n(p)=n(c)=d₁² unique: Φ cancels, diff = d₂L ∈ ℤ. Zero-residual τ₀ exists for any target (codimension, not LD-specific). S158 anchor dominance upgraded: [OBS]→[THM-arith+THM-comp]. Direction 🟢 #4 → 🔴 DEAD. Cumulative dead: 56+.*
*S168: Empirical δK scan (20+ forms). Doublet test: n=3 (s/μ) ℓ-splitting WRONG SIGN — root cause of R²=0.68. face(σ₁) identified as hidden variable. NLO rule G.0b: δK = h(F_{σ₁})·(α/2π)(Φ−Lℓ), h=(d₁,d₂²/d₁²,1,d₁/d₂). R²=0.89 (vs 0.68), 0 free params, 10/10 signs. h(2)=tan γ_CKM [THM V.4]. ∏h=d₂. All ratios (d₁,d₂)-monomial. Triple constraint: unique 1/625. Scramble p=0.004 (LEE-corrected). Explains G.6 (d₁-multiplier) and n=3 anomaly. X.47: additive formula without face(σ₁) structurally dead. Gap 3 reformulated: derive h(f) from dessin. [OBS S168].*
*S169: σ₁ face Markov chain spectrum = μ(d)/d [THM-arith X.48]. h derivable from constraints (G.0c): (1) V.4, (2) scattering X.50 [OBS], (⊥) v_{d₂}-suppression X.49 [OBS], (E) extremal X.51 [THM-arith]. h spectral decomposition: all coefficients LD monomials, h·f ⊥ v_{d₂} [OBS X.49]. p-adic weight cross-duality: Σf·v₂(h) = d₂, Σf·v₃(h) = −d₁ [OBS]. Scattering identification: ⟨π,h⟩ = Π₊₋/Π₋₊ at s=d₁, specific to (2,3) [OBS X.50]. New dead (reformulated Gap 3): 2 (X.52 ω-at-cusps #57, X.53 UST-per-face #58). Σh·f²=44=Σn. Σh·f=d₂³/d₁.*
*S170: Character formula [THM-arith X.54]: d₁³fh = d₂³−L·χ₂−χ₃−d₂·χ₂χ₃. Coefficients {d₂³,−L,−1,−d₂}, sum=d₁⁴. CRT partial factorization X.54a: v₃=0 branch uses Φ₃(d₂)=13, v₃=1 branch uses Φ₃(d₁)=L. Set identity X.54b: d₁fh∈{d₁²,d₂²,N,d₁³}, ∏=j(i)=1728, Σ=d₂³. T upper triangular in AL basis [THM-arith X.54c]: off-diagonal all LD monomials, flag structure. Cyclotomic link X.54d: Φ₃(p) in both h-coefficients and scattering differences. Arithmetic chain X.55: Catalan→|B₁|=(N−1)d₁→Π₊₋/Π₋₊=d₂²/d₁³ [THM-arith]. Specific to (2,3): falsified for 5 other prime pairs.*
*S171: **[CORRECTION]** S169 G.0c miscounted DOF: (1)+(2) → 2-parameter family h(s,t) = (s, 9/4, (9−s−6t)/3, t), NOT 1-parameter. The parametrization h(t)=(3t,9/4,3−3t,t) implicitly assumes h₁=d₂h₆. S170 correction of X.49 REVERSED: h·f ⊥ v_{d₂} is NOT automatic for (1)+(2); it is an independent [OBS] constraint equivalent to h(1)=d₂·h(6). Extremal principle X.51 works on (⊥)-restricted subfamily but physical point is NOT extremal on full (1)+(2) space (∇P≠0, max=27/8>d₂). **[NEW]** Scattering closed forms X.56 [THM-arith]: e₊(p)=(p+1)/[p(p²+1)], e₋(p)=−1/[p(p+1)]. Cross-prime ratios: e₊(d₁)/e₊(d₂)=h(2)=tan γ, e₋(d₁)/e₋(d₂)=h(1)=d₁. X.50 decomposed: Π₊₋/Π₋₊ = h(2)/h(1). Z₂ ambiguity: quadratic 6h₆²−7h₆+2=(3h₆−2)(2h₆−1) gives 2 LD-monomial solutions, discriminated by Σhf²=Σn (44 vs 41) and h·f ⊥ v_{d₂} (0 vs −3). Revised G.0c: 4 linear constraints {(1),(1'),(⊥),(2)} → unique h, no extremal needed. Remaining Gap 3: derive (⊥) or (2) from dessin. Cumulative dead: 58+.*
*S172–S174 (consolidated S175, logic-audited, 1 correction (X.58a sign) + 1 clarification (X.60 framing)): 10 [THM-arith] (X.57–X.60b), 1 [OBS]. Tensor factorization X.57: T=T^(p)⊗T^(q), verified 6 levels (N=6,10,14,15,21,35), eigenbasis=per-prime products, ‖v_d‖²=d. Catalan equivalence X.57a: (⊥)⟺(2) mod d₂²−d₁³=1, falsified 5 pairs. G.0c DOF: 4→3+Catalan, 2[OBS]→1[OBS]. Kirchhoff X.58: Π₊₋=−1/K=−1/40. Basis X.58a: v_q=u_{++}+d₁u_{+-} (S175 corrected sign; S173 had minus). Non-commutativity X.58b: [T,Φ/λ]≠0. CRT duality X.59: (⊥)⟺ratio=−ι(d₂)=−d₁. dim M₁₀ in all AL projs X.59a. Mixed equality X.59b: u_{+-}=u_{-+}⟺(1). q-dirt X.60 (S175 note: σ₁ ∉ N(Γ₀(6)), W₂ valid as q-blind reference). Spectral shift X.60a: v_q uniquely stat→decay. q-marginal X.60b: (⊥)⟺R=d₂. [OBS]: autonomous vs coupled q-oscillation. 6.10.a.a: u_{+-} sector, |a₃/a₂|^{1/2}=h(d₁). DEAD: direction (a) [13 functionals, T_h trivial similarity], direction (b) [Selberg diagonal cusp-blind], direction (d) [partially]. Also: det(Π·σ₁·Φᵀ)=−(N−1), [A⁻¹QA,T]≠0, Grothendieck (W₂,W₃) decomp, BV×face cross-table. φ'/φ: 137/60 in ++ mode (coincidental).*
*S176–S177: Layer 8 information geometry. C.8.1–C.8.4, X.61–X.67 (13 results). Shannon optimality, equicorrelation 192=d₁⁶d₂, spectral sum Σf²h=44, cubic uniqueness. Tr(A²)=K unique to X₀(6). (σ₁σ₀)³ fixes anchor+leptons.*
*S178: C.8.5–C.8.12, X.68–X.73 (16 results). T₁=T₀ general. Tutte T(d₁,d₂)=144 (38th path). (⊥) clarified: c₃(h·f)=0. Constraint landscape C.8.12. CORRECTION: 4/3=K(c)≠h(2). 58+ dead.*
*S179–S184: X.74–X.90 (17 results). AL signs, L-factors, Z₂ quadratic, CRT fixed points, rationality, j(t₆).*
*S185: Audit of S179–S184. 3 errors (X.78 NOTE, X.83 label, X.87 count). 6 tautologies. 11 formulations.*
*S186: AL sector structure W.8 [THM-comp, erratum S200]. Tr(W_Q)=−1 at k=10 from W.4. General claim FALSE (k=4 counterexample). dim(+,+)=1. 6.10.a.a in lepton sector.*
*S186-cont: X.91 L-factor dictionary [THM-arith]. Gap 3 → h(6)=L₂. 12th formulation. 6 dead approaches.*
*S187: X.92 T=T₂⊗T₃ [THM-comp]. X.92a (⊥)=zero 3-mode [THM-arith]. X.92b Z₂ alien 17 [OBS]. 13th formulation. 66+ dead.*
*S188: Audit of S186–S187. 2 minor errors corrected (|det| claims). 1 false finding retracted (spectral gap: different definitions). VERIFY-BEFORE-CORRECT expanded. Companion patch assembled + verified.*

*S189: DESSIN PRIMACY established as BARRIER-level principle (A.0). I.9g.8–I.9g.13 (6 new sections): A^k|_lep mu-tau hierarchy [THM-comp], boson circuit mechanism [THM-comp], resistance distances [THM-arith], L_eff breaking decomposition [THM-arith], k_break→P_phi→t chain [OBS→DER cond.], phi-pair self-duality [THM-arith]. Spectral decomposition of mu-tau breaking [RECORD]. h-weighted Schur→TBM [OBS]. Systematic PMNS operator scan: 0 viable zero-param (Gap 9 gamma genuine). 3 dead variants (A^4 in L_eff basis, M_lep↔L_eff rotation, h-weighted HK). GitHub audit: LD-supplementary 10 commits, LD-explorer 16 commits deployed. Log numbering: I.9g.6-I.9g.11 in session logs → renumbered I.9g.8-I.9g.13 in companion (collision with existing I.9g.6-7). Verified: all computational claims independently reproduced (0 errors in 2 logs).*

*S190: Audit of S189 results + new derivations. R1: monodromy fixed, L_eff verified [THM-arith]. R2: mu-tau symmetric partners — two distinct objects clarified (L_avg ≠ isospectral, L_TBM isospectral but sin²θ₁₂=2/3). R2 error caught by DUAL-COMPUTE-NEW (FORMULA-WITHOUT-PRECONDITION). R3: sin²θ₁₃ rotation factorization (2/3)·(3/52)=1/26 [THM-arith]. R4: h-weighted Schur→TBM downgraded [OBS-approx]. R5: k_break=2d₁ [OBS→DER]. R6: Laplacian solar bound — any 3×3 Laplacian has |U_e1|²=1/3, forced ν₁↔ν₂ swap [THM-arith+exp, DER]. DUAL-COMPUTE-NEW workflow established. 67+ dead.*

*S191: Audit of S190. All results confirmed (R1-R5 ✓). R6 corrections: "25/26=1−s" downgraded to remark (tautology); forced swap scope clarified; I.28.2↔forced swap tension flagged as OPEN.*

*S192: Overlap matrix G [THM-arith], eigenvector dilation ×13 [THM-arith], rotation angle identity L²+d₂=d₁²·det_M (unique d₁=2) [THM-arith], full Schur PMNS with forced swap (all 9 entries LD monomials) [THM-arith], unitarity identity L²+d₁·det_M=d₂·(N-1)² [THM-arith], I.28.2 m₁=0 KILLED by forced swap [DER], R6 table erratum (4/13→0.290 at HK), det_M spectral archaeology (det_M=(Δ₁+Δ₂)/2, minor(μ,τ)=disc_φ) [THM-arith], spectral containment spec(L_bip)\{d₁}⊂spec(L_Cayley) [THM-comp]. t bipartite interpretation [DER cond.]. 40th path to (2,3). R14 polynomial claims — 3/4 incorrect (factorizations incomplete). 67+ dead.*

*S193: Audit of S192 — R14 polynomial erratum corrected (4 different polynomials, not one cubic). Spectral bridge identity BB^T+ΠLΠ^T=2d₂I₄ [THM-arith] — Πσ₁Π^T enters with opposite signs, cancels in sum. Analytical proof of spectral containment via bridge + M_8 restriction + char(L) factorization [THM-arith]. Cascade upgrades: R11 [THM-comp→THM-arith], R12 [DER cond.→DER], I.9g.12 [DER cond.→DER]. Independent HK computation confirmed sin²θ₁₂(swap)≈0.290.*

*S194: Independent verification of S193 — P1 (spectral bridge, 3 methods: direct sum, BB^T decomposition from monodromy, ΠLΠ^T decomposition from monodromy, all Fraction arithmetic), P2 (char(L) factorization sympy exact, char(A₈) factorization match, x²−5x+5 via M₈ confirmed, x²−5x+1 from char(L), ker B^T exclusion x=2 remainder=540), P3 (cascade logic verified). All confirmed [THM-arith]. Companion integration: D.8 spectral bridge added, containment [OBS→THM-arith], I.9g.12 [DER cond.→DER], I.17 swap forced + t derived (0 free params), I.28.2 m₁=0 KILLED, 40th path added.*

*S195: Gap 3 deep attack via direction #5 (L-values 6.10.a.a). X.93 mod-12 congruence [THM-comp]: a_p mod 12 residues = {d₁, N, d₁³, 0} by CRT. X.91 pair-product table and intertwining matrix (all coefficients LD monomials, Tr=index=12, tautological). L-factor decomposition M_p(1/2)·ι(p)^{δ_p} (reformulation, not derivation). Dead #68 (face heat kernel, Class A), #69 (Sym² L, tautological), #70 (scattering Φ ratios, Class I). Cumulative 70+ dead.*

*S196: Gap 3 analytical study. R1: (⊥) NOT universal (tested 7 dessins X₀(N)). R2/X.94: discriminant uniqueness [THM-comp] — rational h ⟺ Catalan (8 prime pairs verified). R3: linear structure on (⊥)-family (c₁ = 88 = d₁³·dim M₁₀ constant, c_p+d₂c_N=−d₁²(N−1) constant). R4: monomiality search — 20 solutions, physical unique with ∏h=d₂. R5/X.95: T-spectral decomposition of w [OBS] — a_N=−1/d₁³ new constraint (linear, selects without Z₂). R6: BV w-sum {|B₁|, dim M₁₀, 23/2, 23/2}. R7: Fourier of d₁³fh. Gap 3 decomposed: (A) derive (⊥) + (B) derive a_N. 72+ dead.*

*S197: NNLO residual structure. R1: scalar NNLO [DEAD]. R2: face(σ₁) not NNLO organizer. R3: NNLO/NLO ≈ 1/d₂. R4: generation hierarchy RMS ∝ ecc^{3.2}. R5: R_eff values ERRATUM (corrected S198 — σ₀ construction error). R6-R7: qualitative 3-layer picture (LO ramification, NLO involution, NNLO electrical).*

*S198: Gap 3 via Schreier R_eff. Erratum S197 R_eff: Kirchhoff=1875=d₂(N−1)⁴ (not 1125), R_eff corrected by σ₀ hardcode from O.1. X.96 anchor R_eff triangle theorem [THM-arith]: R(c)/R(u)=d₁/d₂. X.96a σ₁-pair |ΔR| table [THM-arith]. X.96b Kirchhoff [THM-arith]. 14th formulation of Gap 3. SIGMA0-FROM-O1 barrier established. Non-Z_φ R_eff contains alien primes (71, 29). Face-averaged R_eff violates (⊥) [DEAD]. 72+ dead.*

*S199: Phase A: isoperimetric scan — ~75 functionals on (⊥)-family. Products, sums, spectral, entropy, character, dessin-mixed, Dirichlet energy. All F'(4)≠0 except tautological (Σf²h=44 constant, (Σfh−27/2)²). Structural diagnosis: 1D linear family → extremal impossible. [DEAD #73]. Phase B: X.97 trace formula chain [DER, conditional on 2 ⚠]. 6-step derivation: passport → ν₂=ν₃=0 → decomposition → subtraction → w₂=+1 → L₂=2/3 → h. Dependencies: O.1, A.1, W.4, X.91, V.4, X.56. 73+ dead.*

*S200: X.97 ⚠₁ and ⚠₂ CLOSED. ⚠₁: Tr(W₂|S₁₀)=−1 verified by W.4 decomposition (−2+0+0+1=−1). ⚠₂: w₂(2.10.a.a)=−1 verified by independent construction of M₁₀(Γ₀(2)) from E₁₀(τ), E₁₀(2τ), E₄·E₆(2τ) — exact Fraction arithmetic, perfect square discriminant 1257062400², 2 roots (Eisenstein a₃=19684, cusp a₂=16 a₃=−156). W.8 erratum: general claim "ν₂=ν₃=0 → Tr(W_Q)=−1 for all k" FALSE. Counterexample: k=4, Tr(W₂|S₄)=+1 from 6.4.a.a (a₂=−2, w₂=+1). Root cause: CM fixed points of W_Q ≠ elliptic fixed points of Γ₀(6); U_{k−2}(0) NEVER vanishes for even k. W.8 downgrade [THM-arith]→[THM-comp]. LMFDB dim S₂ discrepancy flagged: genus 0 → dim S₂=0, not 1. 3 cross-checks (multiplicativity, independent construction, end-to-end chain). **Gap 3: [OBS] → [DER].** 73+ dead.*

*S201 (verification session): Full independent verification of S199–S200. ⚠₂ re-derived (exact quadratic, Eisenstein vs cusp). W.8 erratum re-verified (η-product 6.4.a.a, 14 terms exact). X.97 chain end-to-end (6 steps, all constraints ✓). Path A: 60 multiplicativity tests (0 violations), X.93 mod-12 (13 primes, 0 violations). LMFDB dim S₂ confirmed (genus 0). W.8 root cause verified (Chebyshev U analysis). Companion + index patch applied.*

*S202: Canonical functional on X₀(6) for α⁻¹. 8 geometric candidates ALL DEAD (Faltings inapplicable, Arakelov trivial, Green not Heegner, det'Δ Baker-killed, Selberg same, systole/volume/spectral gap wrong magnitude). Systole = 2 log(4+√(d₁⁴−1)), d₁⁴−1=(N−1)d₂ [THM-arith]. 6.10.a.a periods: PSLQ null (sin² and Ω± in different transcendence classes). L-function BUG (prefactor, corrected S203). Period inconsistency ARTIFACT. Dead #74 (combined functional+PSLQ+cos²). 74+ dead.*

*S203-prev: L-function bug fixed, functional equation verified 60 digits. W.9 period table corrected (Ω⁺≈20.974, Ω⁻≈2.700). Klein (ℤ/2)²: W₃ fixes −N, −index; universal product 72=Mon [THM-arith]. cos² algebraic ℙ¹ DEAD (FS=0.987≠0.997). QTC reduction 2→1 physics input [MOTIVATED]. Q₂/Q₄ CRT decomposition [THM-comp]: P₂ generic↔Q₂, cuspal↔Q₄. Hauptmodul erratum (a₀=37 WRONG, correct −5 already in K.1). 74+ dead.*

*S203: Ramification identities C.9a–i [THM-arith]: ∏(j=0)=432², ∏(j=1728)=−432³, 432 universal (3 appearances), Σ(j=1728)=468=d₁²d₂²·Φ₃(d₂), resolvent −4320=−N³d₁²(N−1), CR=d₁/d₂ and d₁, R₃ pure d₂, Q₄=Mon×LD. S203-prev erratum confirmed (a₀ and P₄). Information capacity ~95%. 74+ dead.*

*S204: Cross-ratio → PMNS. X.99 Φ₃ cyclotomic chain [THM-arith]: Φ₃(1,d₁,d₂)=(d₂,L,det M_lep), recurrence d₁·Φ₃(d₁)−1=Φ₃(d₂) unique d₁=2 (path 41). X.99a Pell d₂²−2d₁²=1 [THM-arith]. X.99b char(M_lep) all-LD-monomial. X.99c resolvent root −4320=−N³d₁²(N−1). X.100 CR→sin²θ₁₂=4/13 [DER]: CR(−12,0;−9,−8)=d₁/d₂, four-tuple canonical (j=0+3 non-anchor cusps), upgrades I.2 [CONJ→DER]. X.100a anharmonic orbit = LD constants [THM-arith]. X.100b h(6)=CR, h(2)=CR⁻² [THM-arith/OBS]. 15 CR table: all LD monomials. X.101 CR→sin²θ₂₃=81/145 [DER]: CR(∞,0;−8,−9)=d₂²/d₁³. X.101a d₂⁴+d₁⁶=index²+1 [THM-arith], path 43. X.101b unified CR table. θ₁₃: 0/15 single CRs work; 2/91 best LD fraction [CONJ]. PMNS (0 free params): Σ|pull|=0.26 (IC19). Paths 41–43. 74+ dead.*

*S205: Two-metric mixing (X.102) + HK vs CR conflict. X.102 [THM-arith]: same cusps in ℍ-boundary (tan θ₁₂=2/3) vs Hauptmodul (tan θ₂₃=9/8). X.102a cross-exponent t(w=d_p)=−d_p^{d_{ι(p)}}, product=|Mon|, diff=1 (Catalan), path 44. X.102b product rule tan θ₁₂·tan θ₂₃=3/4=reg_boson (U.1 link), /reg_quark=9/5=λ₂(L_eff). X.102c monomial lattice generates ℤ². X.102d h=mixing tangents. X.102e hyperbolic crossing sin²=8/9 [OBS]. HK scan: CR(θ₁₂,θ₂₃) at t≈1/d₁, CR(θ₁₃) at t≈√5/2, no single t gives all three. f(L) insufficient (T.3). Two-scale structure [KEY]. Gap 9(γ) split: (γ₁) structural [DONE, X.102] + (γ₂) operator in ⟨L,σ∞⟩ [OPEN]. V.6 erratum: NuFIT 6.0 IC19 sin²θ₁₂=0.307 (not 0.303). 74+ dead.*

*S206 (audit+integration): Full verification of S204–S205 arithmetic (all [THM-arith] PASS). Pull sign audit: S205 honest status table had 3 errors (θ₁₂ CR sign, θ₁₃ HK sign+magnitude, θ₁₂ HK magnitude) — corrected using nu-fit.org verified IC19 values. V.6 pre-existing erratum corrected (0.303→0.307). S204 dataset mixing flagged (JUNO θ₁₂ + IC19 θ₂₃/θ₁₃ → Σ|pull|=0.38; all-IC19 → 0.26). Nearest sin² minor correction (1/65 closer than 1/82). Paths: 41 (#30 alt), 42–44 cluster 2 extensions, total ≥44 in 11 clusters. Companion integration: 14 edits (I.2 [CONJ→DER], I.5 [CONJ→DER], I.17 HK vs CR note, D.5 Φ₃/Pell, C.9f interpretation, G.0b mixing tangents, U.1 product rule, A.3 paths 41–44, Gap 9 γ split, X.99–X.102 new sections, session log). 74+ dead.*

*S207: Gap 9(γ₂) attack begins. Context consolidation of S99–S206 history.*

*S208–S211 (consolidated, audited S217): X.103 28-dim family [THM-comp] (tautological universality). X.103a M_break traces. X.103b face traces. X.104 NO-GO ℤ[Mon] [THM-arith]. X.107 e-row Φ₃. X.108 resultant formula sin²θ₁₃=2/91 (5 formulations) [THM-arith]. X.109 P_face transform [THM-arith, ERRATUM: P^T·L·P]. X.109a Hermitian decomposition. X.109b (1,1,1)-obstruction [THM-arith]. X.109c alien primes. X.110 Catalan bridge d₁²+d₂²=Φ₃(d₂) [THM-arith]. X.110a face-cyclotomic duality [THM-arith]. X.110b boson trace 14=d₁L [THM-arith]. X.110c P_face block structure. Dead #75–80. 80+ dead.*

*S212: X.111 W₆∉Mon [THM-comp]. X.112 Sym² traces [THM-arith]. X.113 P_{V₃}|_lep=(3I−J)/12 [THM-comp]. X.113a all P_ρ|_lep∈span{I,J} — irreps BLIND. Dead #81–83. 83+ dead.*

*S213: X.115 circulant sandwich [THM-comp]. X.115a sandwich obstruction (|U_e1|²=1/3 always) [THM-comp]. X.117 rationality–μτ: ℚ[Mon]→θ₁₃=0 [THM-arith]. X.118a 3-param exact CR-PMNS [THM-comp]. Dead #84–85. 85+ dead.*

*S214: X.119 two solution families F1/F2 [THM-comp]. X.119a M|_lep=(d−c)I+cJ [THM-comp]. X.119b M_lr sparsity (9 nonzero, anchor zero) [THM-comp]. X.119c symbolic Schur (det degree 9, 154 terms) [THM-comp]. X.119d PSLQ null degree>128 [THM-comp Colab]. 50-digit refinement. 85+ dead.*

*S215: X.120 4+ real solutions, F2 uniquely viable (Δm²ratio=37.5 vs 33.5) [THM-comp]. X.121 cancellation theorem [→TAUTOLOGY S217]. X.122 Gram identity S₁S₁ᵀ=I, S₀S₀ᵀ=2I, S₁S₀ᵀ=C [THM-arith]. X.123 anchor invisibility + mediator triangle [THM-arith]. X.124 boson contact projection 91.2% [THM-arith]. X.125 anchor portal [THM-comp]. X.126 channel decomposition (σ₀ 94.6%) [THM-comp]. X.UST.1–5 [THM-comp]: Kirchhoff=1875=d₂(N−1)⁴, 17 edges all rational, denominators d₂^a(N−1)^b. Dead #86–87. 87+ dead.*

*S216: X.128 unified face-pair construction [THM-comp]: CR→θ₁₂,θ₂₃; Res→θ₁₃; assignment forced. θ₁₃ chain (1/N)(d₁²/L)(d₂/det_M)=2/91 through all 4 face types. Catalan uniqueness (2,3). 17 invariants, unique 1σ. F2 mass hierarchy (37.5 vs 33.5). Dead #88–90 (anti-symmetry, LD-point eigenvalues, sign pattern). 90+ dead.*

*S217 (audit+consolidation+breakthrough): Full verification of S208–S216 (1 erratum: v vector S215 basic FALSE). X.121 reclassified as tautology. X.129 index formula sin²θ₁₃=index/(N·∏Φ₃)=2/91 [THM-arith]. X.129a GN=PMNS denominators [THM-arith]. X.129b ∏GN_lep=1885 universal for sin²·cos² products [THM-arith]. X.129c cyclotomic unification table [THM-arith]. X.129d θ₂₃ cyclotomic form (reformulation). I.4 [CONJ→DER] (X.129+X.130). Findings: mediator n↔angle [OBS], GN neighbor sums [OBS, CW-dependent]. S217 audit (S218): errata E1 (Catalan bridge Φ₄≠Φ₂), E2 (pulls NuFIT 5.x not 6.0), E3 (arithmetic 0.68≠0.75), E4 (universal denom scope). All corrected in this patch. 90+ dead.*
