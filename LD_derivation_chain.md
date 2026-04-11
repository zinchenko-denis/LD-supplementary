# LD Derivation Chain — 18 Tier A Outputs

**From a single dessin d'enfant to 18 independent predictions at 0 continuous parameters.**

Every chain starts from the monodromy triple (σ₁, σ₀, σ∞) of the unique
dessin of X₀(6) — verified by 508/508 computational checks.

---

## Root: The Dessin

```
A_F = ℂ ⊕ ℍ ⊕ M₃(ℂ)
   ↓  (d₁, d₂) = (2, 3)
N = d₁·d₂ = 6
   ↓  Theorem 4.2–4.4: UNIQUE
Γ₀(6), genus 0, index 12, cusps = {∞, 0, 1/2, 1/3}
   ↓  Belyi theorem
Dessin d'enfant: 4 BV + 6 WV + 12 edges
   ↓  Theorem 5.3: UNIQUE (O.1)
Monodromy: σ₁·σ₀·σ∞ = id,  |Mon| = 72 = d₁³·d₂²
```

---

## Block I: Masses and Couplings (8 outputs)

### 1. α⁻¹ = 137.035999202  [DER cond.]
```
Dessin → cusps → E₂*(τ) at τ = i
  → j(i) = 1728 = index³
  → QTC chain (12 steps, N.3–N.5)
  → cos²(1/(Nπ)) [DER, 2 physics inputs]
  → α⁻¹ = (j + N)/(j + L) · (d₁²π/d₂) · cos²(1/(Nπ)) · W₆-sign
W₆-odd: α⁻¹ = 137.035999202 (−1.2σ)
W₆-even: excluded at ~2400σ
```
Pull: −1.2σ CODATA 2022. Companion: H.1.

### 2. μ = mₚ/mₑ = 1836.153  [DER]
```
Dessin → Hauptmodul t₆ → L-function 6.10.a.a
  → μ₀ = 6π⁵ (structural: N·(N−1)! in π)
  → NLO: C₁ = 10/9 = |B₁|/(|B₁|−1)
  → μ = μ₀ · C₁ · (1 + NNLO)
```
Pull: < 0.001 ppm. Companion: H.2.

### 3–12. Ten particle masses  [OBS → DER]
```
Dessin → σ∞ cycles → face(e) → (ε, η) architecture (F.6–F.7)
  → n(e), ℓ(e), K(e) for each particle
  → m(e) = mₑ · μ^{n/4} · K(e)
  → NLO: δK from h-weighted face Markov chain (X.97, G.0b)
```
LO: R² = 0.89 (10 masses). NLO: 15/16 hadronic observables ≤ 1.7σ.

### 13. sin²θ_W = 3/13  [DER, 1 identification]
```
Dessin → d₁² = 4 = dim(SU(2)_L)
  → generator ratio 1/d₁² = 1/4
  → tower C₂ = 13/12 = det_M/index
  → sin²θ_W = (1/d₁²)/C₂ = 3/13 = 0.23077
  → NLO: (3/13)(1 + (5/3)α/(2π)) = 0.23122
```
Pull: +1.9σ PDG 2024 (NLO). Companion: X.219.

---

## Block II: CKM (4 outputs)

### 14. λ_CKM = 9/40 = 0.22500  [DER]
```
Dessin → bipartite graph (4 BV × 6 WV)
  → BB^T spectrum: {1, 2, 5, 6}
  → Kirchhoff K = 40 (matrix tree theorem)
  → UST ensemble → Residual Tree Theorem (E.8)
  → λ = 9/40
```
Pull: −0.04σ. Companion: V.1.

### 15. A_CKM = 3/√13 = 0.83205  [DER]
```
UST → P_triple / (ΔP + P_triple)
  → A = √(d₂/det_M) = 3/√13
```
Pull: +0.63σ. Companion: V.2.

### 16. γ_CKM = arctan(9/4) = 66.04°  [DER]
```
UST → arctan(P_triple / ΔP)
  → γ = arctan(d₂²/d₁²) = arctan(9/4)
```
Pull: −1.25σ. Companion: V.3.

### 17. R_b = √(3/20) = 0.38730  [DER]
```
UST → √(N/K) = √(6/40) = √(3/20)
```
Pull: +0.17σ. χ²/dof = 0.65 (4 parameters). Companion: V.4.

---

## Block III: PMNS + δ (4 outputs)

### 18. sin²θ₁₂ = 4/13 = 0.30769  [DER]
```
Dessin → Hauptmodul → cusps → cross-ratio (X.100)
  → Tower: (1/d₂)/C₂ = (1/3)/(13/12) = 4/13
  → VC: δ-products → same value (X.240)
  Three independent paths → same fraction.
```
Pull: +0.17σ JUNO 2025. TBM (1/3) excluded at −2.8σ. Companion: X.100.

### 19. sin²θ₂₃ = 81/145 = 0.55862  [DER]
```
Cross-ratio: CR(1/3, 0; 1/2, ∞) = 81/145
  → d₂⁴/(d₂⁴ + d₁⁶) = 81/(81+64) = 81/145
  → Catalan: d₂² > d₁³ (9 > 8) → upper octant
```
NuFIT 6.1: inside 3σ. Companion: X.101.

### 20. sin²θ₁₃ = 2/91 = 0.02198  [DER]
```
Index formula: sin²θ₁₃ = index/(N·∏Φ₃) = 12/(6·91) = 2/91
  → 91 = 7·13 = L·det_M
  → Tower correction from tree-level 1/26: ratio L/d₁² = 7/4
```
Pull: +0.90σ. Companion: X.129.

### 21. sinδ = −1 (δ = 270°)  [DER, 1 identification]
```
|sinδ| = 1 [THM-arith, X.218]:
  Cross-term in |U_μ1|² has odd prime exponents (2¹¹, 7¹)
  → cos δ = 0 forced by rationality of |U|² matrix
sinδ = −1 [DER, X.224]:
  Hermitian perturbation iε·A from canonical ℍ orientation
  → sign fixed, same epistemic class as O.1
```
NuFIT 6.0: δ = 197°, consistent at ~1.5σ from 270°. Companion: X.224.

---

## Cross-Sector Consistency

These are not 18 independent fits — they are consequences of ONE object:

1. **Pythagorean bridge:** A²(CKM) + sin²θ₁₂(PMNS) = 1, because both denominators = 13 = det M_lep from independent chains.

2. **Shared prime 13:** sin²θ₁₂ = 4/13, sin²θ_W = 3/13, sin²θ₁₃ = 2/(7·13). All from Φ₃(d₂) = d₂² + d₂ + 1.

3. **Kirchhoff unification:** K = 40 = q₃(2)·q₅(2) (directed spectrum) = det(L')/12 (matrix tree) = UST count (CKM source).

4. **Tower coherence:** The SAME tower coefficients C_n give both sin²θ₁₂ (at n=2) and sin²θ_W (at n=2) and λ_CKM (at n=1, as 9/40 = sin²θ_W(n=1)).

---

## Verification

All 18 outputs verified by:
- `verify/` suite: 508/508 checks from monodromy to observables
- `LD_verification.sage`: 91/91 independent Sage checks
- Dual-compute: Fraction arithmetic + numpy cross-validation
- GPT 5.3 triple audit (S270): mathematician PASS

---

*Version: S300. Companion: S291. Paper: v1728. 0 continuous free parameters. 0 circular dependencies.*
