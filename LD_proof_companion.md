# LD PROOF COMPANION
# Version: post-S116 (2026-03-22, coherence map + commutator theorem + 3 status patches)
# Author: Denis D. Zinchenko
# Assembled by: Claude (from session logs S42–S100, paper v5.5, context files)
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
| α⁻¹ | 137.035999084 | Fine structure constant (CODATA 2018) |

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

| WV | σ₁-pair | BV—BV | Role | n+n' |
|----|---------|-------|------|:----:|
| A | {u, t} | anc—idx | **Bridge** (FORCED in all spanning trees) | 8 = d₁³ |
| B | {c, p} | anc—anc | **Multi-edge** (one per spanning tree) | 8 = d₁³ |
| C | {b, μ} | idx—star | Interior | 8 = d₁³ |
| D | {d, e} | idx—oth | Interior (contains √2 anomaly) | 1 |
| E | {s, W} | star—oth | **Far-end** (competing pair) | 9 = d₂² |
| F | {τ, H} | star—oth | **Far-end** (competing pair) | 10 = |B₁| |

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


## [OBS/DER] A.3: ≥31 paths to (d₁, d₂) = (2, 3)
Source: Compiled S73 §11, updated S99–S116

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

No other pair survives more than 4 tests.

### Independence analysis (8 clusters)
Not all 30 paths are fully independent. They cluster into ~8 groups sharing common inputs:

| Cluster | Paths | Shared input |
|---------|-------|-------------|
| **Pure number theory** | 1, 2, 5, 20, 30 | Properties of N=6 as integer |
| **Ramification/j-geometry** | 3, 8, 10, 15, 16, 17, 18, 27, 28 | j-map structure, ν₂=ν₃=0 |
| **B₁ algebra** | 4, 6, 7, 11, 12, 29 | Generator lattice ⟨2,3⟩, K-cipher |
| **L-functions** | 9 | η-product Hecke relations |
| **Physical data** | 13, 14, 19 | Empirical masses or CKM |
| **Sporadic groups** | 21 | Monster representation theory |
| **Automorphic (scattering)** | 22 | Scattering matrix of Γ₀(6) |
| **Effective Laplacian** | 23, 24, 25, 26, 31 | Schur complement / Cayley graph |

Within each cluster, paths share assumptions and could fail together. Between clusters, failure modes are independent. Conservative count: **~8 independent lines of evidence**, not 30.


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

## [THM] D.5: Leptonic block M_lep
Source: S73 §4

M_lep = 3×3 non-anchor submatrix of BB^T. Eigenvalues: 4+√3, 4−√3, 1.

**det(M_lep) = 13 = d₁²+d₂².** ← PMNS denominator.

**μ-τ symmetry [THM]:** PMP = M (P swaps rows 2,3). Proof: (BB^T)₁₂ = (BB^T)₁₃ = 1, (BB^T)₂₂ = (BB^T)₃₃ = 3. ∎

Tree level: sin²θ₁₃ = 0, sin²θ₂₃ = 1/2.

Leptonic Kirchhoff = N−1 = 5. Full/leptonic = d₁³ = 8.


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


# E. CKM

## [DEAD] E.1: 10 dead graph approaches (S72 §1)
All give inverted hierarchy. Key insight: relevant variable is |Δg|, not graph distance.

## [OBS] E.2: λ = d₂²/Kirchhoff = 9/40 = 0.22500
Source: S72 §3. PDG: 0.22497±0.00070, δ = **−0.04σ**.

Compact: λ = d₂²/[2d₁²(d₁+d₂)].

## [OBS] E.3: A = d₂/√(d₁²+d₂²) = 3/√13 = 0.83205
Source: S72 §4. PDG: 0.839±0.011, δ = **+0.63σ**.

A = cos θ₁₂(PMNS). CKM-PMNS link.

## [OBS] E.4: γ = arctan(d₂²/d₁²) = arctan(9/4) = 66.04°
Source: S72 §5. Exp: (62.8 ± 2.6)° (LHCb combination, Nov 2025), δ = **−1.25σ**. Previous: 65.98°±4.0° (−0.015σ). Now max-pull CKM parameter.

## [OBS] E.5: R_b² = N/Kirchhoff = 3/20 = 0.15
Source: S72 §6. Exp: 0.15088±0.007, δ = **+0.13σ**.

Identity: R_b² = λ·d₁/d₂ (only 3 independent parameters).

## [OBS] E.6: Full CKM (9 elements, Sage-verified)
Source: S72 §7. Max deviation: |V_td| at 1.11%. J = 3.095×10⁻⁵ (**−0.12σ**).

| Parameter | LD | Exp | σ-pull |
|-----------|-----|-----|--------|
| λ | 9/40 | 0.22497±0.00070 | −0.04 |
| A | 3/√13 | 0.839±0.011 | +0.63 |
| γ | arctan(9/4) | (62.8±2.6)° (LHCb 2025) | **−1.25** |
| R_b² | 3/20 | 0.15088±0.007 | +0.13 |
| J | 3.095×10⁻⁵ | (3.08±0.13)×10⁻⁵ | −0.12 |

### Degree-of-freedom count
All 4 Wolfenstein parameters are functions of (d₁, d₂) only (K = |B₁|·d₁² follows from d₁, d₂). Inputs: 2 numbers. Outputs: 4 parameters. But R_b² = λ·d₁/d₂ is a **constraint**, not an independent prediction. Effective: **3 independent predictions from 2 inputs, dof = 1**. χ²/dof = (0.04² + 0.63² + 1.25²)/1 = 1.96. Acceptable (p = 0.16), but γ now dominates. If CKMfitter indirect (66.3°) preferred over LHCb direct, pull drops to +0.1σ.

## [THM→OBS] E.7: Chain anchor → Cabibbo
```
σ∞ 1-cycle → Anchor Lemma [THM] → m=1 → BB^T unique [THM]
→ σ²={N,N−1,d₁,1} [THM] → Kirchhoff=40 [THM] → λ=d₂²/K [OBS]
```
Every step except the physical identification is proven. λ = d₂²/K is a graph theorem (E.8, Residual Tree Theorem). The sole remaining gap: λ_Wolfenstein = d₂²/K [OBS — physics identification].


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


## [THM-arith/OBS] F.8: BV-level sums
Source: S87
Status: [THM-arith/OBS] (Σn from F.3 [THM]; Σℓ partial — bosons need SM_QN; was [OBS] pre-S116)

| BV | Edges | Σℓ | = | Σn | = |
|----|-------|:---:|:-:|:---:|:-:|
| anc | c, u, p | 6 | N | 9 | d₂² |
| idx | b, t, e | 13 | d₁²+d₂² | 12 | index |
| star | s, μ, H | 11 | dim M₁₀ | 12 | index |
| oth | d, W, τ | 16 | d₁⁴ | 11 | dim M₁₀ |

Totals: Σℓ = 46, Σn = 44 = d₁²·dim M₁₀.

F.7c product dichotomy: product = d₂N² ⟺ BV\_idx = {b, t, e}. Status: [OBS].


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
Observation (2 data points). Bridge is [THM]. Mechanism: OPEN (possibly related to the double ramification at n = e² node).


## [OBS] G.7: W anomaly
Source: S43
Status: [OBS]

### Statement
δK_pred(W) = −1.29%, δK_obs(W) = −0.04%. Ratio = 32×. The W boson is the unique particle where |δK_obs| ≈ 0 while |δK_pred| is substantial.

Interpretation: gauge protection — the W mass receives SM radiative corrections that cancel most of the "bare" δK predicted by the formula. This is expected: gauge boson masses are protected by gauge symmetry in a way fermion masses are not. The formula predicts the "pre-protection" value.


## [DER] G.8: EW operator ℓ from dessin
Source: S76
Status: [DER]
Dependencies: C.1 (dessin), C.3 (uniqueness 36/36), F.3a (σ₁-sector dichotomy); **SM_QN** (T₃, |Q| for boson ℓ values only)
Verified: Sage (8/8 dessins × 12/12 edges)
Replaces: G.4 [DER] (which derived ℓ from SM quantum numbers; now ℓ derived from dessin itself)

### Dependency note (S98 audit)
Fermion ℓ values (quarks: d₂=3, leptons: L=7, anchor: 0) are derived purely from face sizes — **no SM input**. Boson ℓ values (H: 1, W: 6) require SM quantum numbers (T₃, |Q|) via ℓ = −2(T₃−d₂|Q|). The σ₁-dichotomy determines **which** boson is H vs W [THM-comb], but not their ℓ **values** without SM_QN.

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
| ℓ(e) | face(e) + face(σ₁(e)) | **[DER] (G.8)** |
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
Status: BULK [DER via QTC, §N], IR [DER conditional on weight=level, S103+S108]
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
(3) Self-energy Σ = −χ(O(N)) = −L [DER conditional on weight=level, S108]:
  (3a) Hodge bundle ω on ℙ¹ = X₀(6) has deg(ω) = index/12 = 1 [THM].
  (3b) ω^⊗N = O(N). Sections = M_N(Γ₀(6)), dim = N+1 = L = 7 [THM: Riemann-Roch].
  (3c) O(N) is UNIQUE line bundle on ℙ¹ with χ = L: n+1 = L has unique solution n = N [THM].
  (3d) Action S[φ] = ∫_{ℙ¹} |∂̄φ|² ω_FS, unique gauge-invariant second-order action [DER].
  (3e) 1-loop: Σ = −[a₂ in heat kernel of ∂̄*∂̄ on O(N)] = −ind(∂̄) = −χ(O(N)) = −L [DER: index theorem].
  Sign: QFT convention G⁻¹_dressed = G⁻¹_bare − Σ = j − (−L) = j + L.
(4) Fricke W_N: tadpole shift = N [THM].
(5) Dyson resummation: G_dressed = (j+N)/(j+L) [DER from 1–4].

**Remaining caveat:** The identification "field lives in O(N)" is equivalent to "weight = level." Self-referential but unique: O(N) is the only line bundle on ℙ¹ with χ = L, and O(N) = ω^⊗N = weight-N modular forms. Weaker than full Gap 3 resolution, but stronger than the former [MOT] ansatz. Status: [DER conditional on weight=level].

Factorizations: j(i)+N = 1734 = N·17² = N·(index+d₁+d₂)² [THM, S102, 28th path]. j(i)+L = 1735 = 5·347 (347 prime, no LD structure).

### H.1d: Form B death [THM, S102]

**Paper v5.5 uses Form B (WRONG).** Paper formula: IR = (π/36)·(1 − 1/j + 11/j²) with c₂ = dim M₁₀ = 11. This is a Taylor approximation that does not equal any exact closed form precisely.

Form B exact: IR_B = (π/36)·(j+|B₁|)/(j+dim M₁₀) = (π/36)·1738/1739.
α⁻¹(B) = 137.035999086. α⁻¹(A) = 137.035999202. Separation: 10.5σ_Rb.

| Measurement | α⁻¹(exp) ± σ | Pull A | Pull B |
|---|---|---|---|
| CODATA 2022 | 137.035999177(21) | +1.2σ | −4.3σ |
| Rb Parker 2018 | 137.035999206(11) | −0.4σ | −10.9σ |
| ae Fan 2023 | 137.035999166(15) | +2.4σ | −5.3σ |
| χ² (3 meas.) | | 7.3 | 165.6 |

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
| IR = (j+N)/(j+L) | [DER conditional] | 4 steps [THM] + Σ=−χ [DER cond. on weight=level, S108] |
| π/36 = 1/(index·E₂) | [THM] | self-duality |
| Form A vs B | [THM] | B dead at 10.5σ |

Overall α formula: ~80% [THM/DER], up from ~75% at S107. Σ=−χ upgraded [MOT]→[DER cond.] (S108). Remaining gap: weight=level identification (self-referential but unique).

### H.1h: VMF — saddle at τ=i [THM, S108]

h(τ) = −log(y^{1/2}|η(τ)|²) has E₂*(τ)=0 as Euler-Lagrange equation [THM]. τ=i is a **saddle point** (not minimum): Hessian eigenvalues 1/4 ± π²E₄(i)/36 ≈ +0.649, −0.149, Morse index 1 [THM]. h is SL₂(ℤ)-invariant → descends to X(1) → **cannot select Γ₀(6)** [structural barrier]. No Γ₀(6)-specific functional with E₂*=0 as EL equation was found (5 attempts DEAD). Constrains future VMF attempts: any variational principle for τ=i must break SL₂(ℤ)-invariance.


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
- G_pred = 6.67410 × 10⁻¹¹, δG = −35 ppm (CODATA 2018).
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


## [CONJ] I.2: sin²θ₁₂ = 4/13 = 0.30769
Source: S8 (original ansatz), Paper §8 Conj 8.1
Status: [CONJ]

### Origin
tan θ₁₂ = K₁/K₂ = (1/3)/(1/2) = 2/3. Then sin²θ₁₂ = tan²/(1+tan²) = (4/9)/(1+4/9) = 4/13.

Equivalently: sin²θ₁₂ = d₁²/(d₁²+d₂²) = 4/13.

### Experimental test
JUNO (November 2025, arXiv:2511.14593): sin²θ₁₂ = 0.3092 ± 0.0087.
- LD (4/13 = 0.30769): **+0.17σ** ✓
- TBM (1/3 = 0.33333): **−2.8σ** ✗

### Status upgrade attempt (S73)
det(M_lep) = 13 = d₁²+d₂² (§D.5). This connects the denominator 13 to the leptonic block of BB^T. sin²θ₁₂ = d₁²/det(M_lep) = 4/13 [DER cond.].

**BUT:** BB^T eigenvectors give θ₁₂ = 0.211 (WRONG, −7.7σ). The K-ratio ansatz tan = 2/3 gives the correct value, but is not derived from M_lep. The det = 13 observation connects denominators, but eigenvectors don't match.

**Honest verdict:** sin²θ₁₂ = 4/13 remains a [CONJ]. Source = K-ratio ansatz. Mass matrix absent (Gap 9).


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


## [CONJ] I.4: sin²θ₁₃ candidates
Source: S73 §3
Status: [CONJ]

From scan of ~50,000 expressions over Γ₀(6) invariant pool:

| Candidate | Formula | Value | Pull (NuFIT 5.x: 0.02203±0.00056) |
|-----------|---------|-------|-----|
| A | d₁³/(d₂·dim²M₁₀) = 8/363 | 0.022039 | **−0.016σ** |
| B | d₁/(L·(d₁²+d₂²)) = 2/91 | 0.021978 | **+0.093σ** |

Candidate B preferred: 91 = 7·13 = L·det(M_lep). Gives sin²θ₁₃ = sin²θ₁₂/(d₁·L) = (4/13)/14. Transparent hierarchy: θ₁₂ ≫ θ₁₃ by factor d₁·L = 14.


## [CONJ] I.5: sin²θ₂₃
Source: Paper §8, S73, corrected S77

Tree-level from μ-τ symmetry: sin²θ₂₃ = 1/2. Exp: 0.570 ± 0.016 → **+4.4σ**.

The candidate 13/24 = 0.5417 (from |SL₂(F₃)| = 24) is **post-hoc** [S77]: 6 competing ratios from LD invariants fall in the same range (N/dim M₁₀, K/|Mon|, etc.). Not unique.

**CORRECTION (S77):** Paper v4 prediction "θ₂₃ lower octant" is **WRONG**. No LD candidate gives lower octant: 1/2 = maximal, 13/24 = 0.5417 = upper, heat kernel = 0.556 = upper. Paper v5: remove from falsification map, add to known tensions.

μ-τ breaking source: σ₁(τ) = H (§I.3). Quantitative correction requires Gap 9.


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
| **t=√5/2 (this)** | **−0.03σ** | **+1.19σ** | **−1.74σ** | **2.96** | **1 (t) + 1 bit (swap)** |

### Self-criticism
**LEE:** ~50 LD-motivated t candidates tested; at ~50 trials, ≥1 falling within 0.4% of optimum expected ~10–20% of the time. **Swap:** ν₁↔ν₂ is a discrete choice (1 bit) not accounted in pulls. Without swap: θ₁₂ misses by 30σ. **Honest significance:** ~1–2σ after LEE correction. **Counterargument:** disc_φ is the privileged invariant of the same Laplacian — reduces effective trials, but hard to formalize.

### Status
[CONJ] — t motivated but not derived. Upgrade requires extremum of a natural functional at t=√5/2, or trace formula derivation. ~25 functionals tested, all DEAD (see X.11).


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
  t = √5/2 (heat kernel parameter)
  ν₁ ↔ ν₂ swap
  Physical content: finite diffusion time on dessin determines PMNS corrections.
  Status: t motivated (disc_φ = 5), not derived (~25 functionals DEAD, X.11).

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
| Heat kernel (I.17) | 0.022 | −0.03σ | 1+1bit |

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

### I.28.2 Structural predictions [PRED]

1. **m₁ = 0** (lightest neutrino massless).
   Basis: zero eigenvalue of L_eff is structural (Laplacian property: row sums = 0).

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
[PRED] — predictions are structural consequences of m₁=0 (from L_eff null mode) + NO (from eigenvalue ordering) + experimental oscillation parameters. LD does not predict Δm² values themselves; these come from NuFIT 6.0. The LD content is the prediction m₁=0 and NO.


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
- (γ) CONJ I.17: t = √5/2

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

## [THM] K.2: Q₆ factorisation
F₁₂ = Q₆². f₁ roots ratio = 2+√3. Discriminants purely {2,3}.

## [THM] K.3: Atkin-Lehner
W₂: −8(t+9)/(t+8). W₃: −9(t+8)/(t+9). W₆: 72/t. j∘W₂≠j.

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
| off-diag numerators | 7, 13, 91 | |P²(𝔽₂)|, |P²(𝔽₃)|, product |

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



# Y. OPEN QUESTIONS

1. **Gap 3: CLOSED for discrete content (S100). Ring OPEN at G (S110).** (3a) Form α/(2π): 4D Weyl [THM, G.3/S29]. (3b) Universality: ring closure excludes edge-local coupling (100% spread vs 0.002% ring precision) [DER+MOTIVATED, M.7/S100]. (3c) Value 1/α ≈ 137.036: from H.1 [DER, H.1/S105]. (3d) EM identification: EW operator T₃−d₂|Q| = −ℓ/2 [THM, G.8/S32]. **S110 correction:** Ring is not a contraction mapping (|F'| = 9.84 >> 1). G requires nuclear input μ_G = (3μ + μ_n − B_d/m_e)/4, not derivable from H.2. G is a prediction given nuclear data, not a ring-closure condition. Hierarchy split: L1 (α, μ) closed; L1b (G) open.
2. **Gap 9: [DER+MOTIVATED] (S99–S100). S116 structural analysis.** Schur complement L_eff gives exact rational PMNS (I.11–I.14): sin²θ₁₃(Schur) = 1/26 (−29σ, insufficient alone). Heat kernel at t = √5/2 gives all 3 angles within 2σ (I.17, [CONJ]). Representation-theoretic derivation (I.26): irrep localization → moment theorem → P₁=1, P₂=5 → t = √P/d₁ [DER]. S₃ polarization (I.27): w₊/w₋ = d₂/L for φ-pair (26th path), Σλ·w₊ = |B₁|, Pythagorean identity t₂²−t₁² = 1. Spectral anatomy (I.18–I.24): φ-pair dominates θ₁₃ at 38%. **S116 correction: PMNS has 3 independent root gaps** (not 2): (α) CONJ I.14-ID [Mν, Leff]=0, (β) CONJ I.3-ID M_lep→PMNS, (γ) CONJ I.17 t=√5/2. Independence of α,β proved by [M_lep,L_eff]≠0 (I.29). **Layers:** Layer 0: char(L) → Q₁,Q₂ [THM]. Layer 1: P₁=1, P₂=5 from moments [THM]. Layer 1b: P₂−P₁ = d₁² [THM]. Layer 2: t=√P/d₁ [DER]. Layer 3: PMNS at t₁,t₂ → Σ|p|=2.96 (NuFIT 5.x) but 4.52 (NuFIT 6.0 IC19) / 9.65 (IC24+SK, θ₂₃=7.9σ) [CONJ, I.17]. **Irreducible gap:** linearity of f(P) at 2 points; ν₁↔ν₂ swap (1 bit). ≥38 dead directions (X.12–X.13). **Remaining:** (a) derive linearity or accept [DER]; (b) derive ν₁↔ν₂ swap; (c) Lagrangian origin.
3. **n-formula offsets = −d₁, −1** [OBS]. Slopes [THM] via F.3a. Offsets absorbed into g→n step but origin in ramification indices remains [OBS].
4. **K-cipher: RESOLVED by ε-η architecture (F.6–F.7b-K).** Remaining: (a) analytical product constraint F.7c, (b) d-quark EWSB exception origin.
5. **IR term of α: [DER conditional] (S103+S108, was [FITTED]).** Form A: IR = (π/36)·(j+N)/(j+L). 5-step chain: 4 steps [THM] + Σ=−χ [DER cond. on weight=level, S108]. Form B (paper v5.5) DEAD at 10.5σ. Paper v6 must use Form A. Remaining gap: weight=level self-referential identification (unique but not derived from deeper principle).
6. **cos²(1/(Nπ)): RESOLVED [DER] (S105–S106).** QTC 12-step chain derives cos² from covering geometry. 42/42 checks. Two standard physics inputs (perturbativity, Born interpretation). See §N. Was [MOT] with 9 dead approaches before QTC.
7. **λ = d₂²/K — graph identity proven, physics gap remains.** Bridge from spanning-tree fraction to sin θ_C.
8. **μ-τ breaking → quantitative θ₁₃.** Schur complement (I.11) provides exact mechanism: σ₁(τ)=H breaks μ-τ with parameter 7/55. Heat kernel at t=√5/2 corrects to experiment. Open: derive t.
9. **d₁-multiplier mechanism** (bridge [THM], mechanism OPEN).
10. **Σn=44, ℓ-equipartition, BV sums** → combinatorial derivation.
11. **Scattering matrix identifications (L.5).** 1/α₃ = 40 = Kirchhoff [THM M.3]. s = d₁ [MOTIVATED], not derived.
12. **Kirchhoff = |P³(𝔽_{d₂})| = 1/α₃(d₁)** [THM M.3]. Projective-space dimension 2d₁−1 = 3 unexplored.
13. **φ-zero structural role** [THM D.6]. Z_φ = {p,c,u,t}. Golden hierarchy 1:φ:φ² with norm √|B₁|. 4/13 = full interference [CONFIRMED]. Open: physical meaning of Z_φ, connection to forced spanning-tree edges (E.8).
14. **PMNS spectral anatomy** [OBS I.23–I.24]. e-μ democracy broken by exactly 2 sectors (λ=1, λ=4) with ratios d₁², d₂². M = 20·Q_φ satisfies M² = L(K₃) (I.20). D_τ-duality links two discriminants (I.21). Open: derive these from first principles.

### Y.15: Coherence Map of Weak Points (S116, computational)

29 weak sections (OBS/CONJ/MOT/ALIVE-WEAK/dual) decompose into **7 independence classes + 12 isolates**.

**Class α: CONJ I.14-ID chain** (3 sections: I.14, I.17, I.22)
Root gap: [Mν, Leff] = 0. Cascade = 2 (I.14 → I.17 → I.22).

**Class β: CONJ I.3-ID chain** (2 sections: I.3, I.5)
Root gap: M_lep eigenvectors = PMNS columns. Cascade = 1.
**Independent of α:** [M_lep, L_eff] ≠ 0 [THM-arith, I.29].

**Class γ: Heat kernel** (2 sections: I.9, I.9a)
Gap: t = 1/d₁ identification. Supported by I.6 [THM].

**Class δ: K-cipher** (3 sections: F.5, F.5e, F.8) — **RESOLVED** by F.7b-K [THM].

**Class ε: δK structure** (2 sections: G.10, G.6) — **spectrally isolated** (Fiedler: positive component, separated from PMNS core).

**Class ζ: Peripheral** (5 sections: B.5, L.5, I.2, I.24, I.9d)
Single weak link each, no cascade potential.

**Isolates** (12): E.2–E.6 (CKM), G.7, I.1, I.4, I.23, A.3, M.4, M.5.

**Strong hubs:** I.6 [THM] supports 3 weak sections. O.1 [THM-comb] anchors F and I sectors. D.5 [THM] supplies M_lep.

**Leverage budget:** 3 root gaps (α, β, γ) control 4 downstream sections. Remaining 22 require individual mechanisms.

**Fiedler partition** (λ₂ = 2.83): PMNS + K-cipher core is one topological blob (not further separable). G.10/G.6 genuinely disconnected. CKM (E.2–E.6) fully isolated (zero cross-references to other weak sections).


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


*Assembled: 2026-03-15, updated post-S100 (2026-03-20).*
*Sources: paper v5.5, session logs S42–S100, Claude memory.*
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
