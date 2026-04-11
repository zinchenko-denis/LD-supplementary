# LD Verification Suite — Architecture

## Принципы

1. **Python 3.10+**, без Sage — воспроизводимо на любой машине
2. **Exact arithmetic**: `fractions.Fraction` для рациональных, `sympy` для алгебраических
3. **Модульность**: один файл = одна секция companion, запускается независимо
4. **Единый runner**: `python run_all.py` прогоняет всё, считает PASS/FAIL
5. **Каждый check ссылается** на companion секцию (O.1, D.5, X.129 etc.)
6. **Ноль внешних данных** — все константы hardcoded с источником (CODATA/PDG/NuFIT)

## Зависимости

```
numpy       # числовые вычисления
sympy       # символьная алгебра, char poly
fractions   # stdlib — exact Fraction arithmetic
```

Без scipy, без mpmath, без sage. Только стандартный стек.

## Структура файлов

```
LD-supplementary/
├── LD_proof_companion.md          # (existing)
├── LD_verification.sage           # (existing, legacy)
├── verify/
│   ├── __init__.py
│   ├── run_all.py                 # Entry point: imports all, runs, prints summary
│   ├── framework.py               # check(), section(), summary(), constants
│   │
│   ├── t0_foundation.py           # A.1: N=6 uniqueness (3 filters)
│   │                              # B.1-B.5: B₁ set, Hecke orbit, |B₁|=10
│   │
│   ├── t1_monodromy.py            # O.1: σ₁, σ₀, σ∞ definitions
│   │                              # MCT: σ₁·σ₀·σ∞ = id (12/12)
│   │                              # |Mon|=72, |Aut|=2, BV compositions
│   │                              # σ₁-pair table (n+n', ℓ+ℓ')
│   │
│   ├── t2_quantum_numbers.py      # F.3: n from eccentricity (quark/lepton formulas)
│   │                              # F.7d: global n-polynomial (10 terms, 12/12)
│   │                              # F.7e: global ℓ-polynomial (5 terms, 12/12)
│   │                              # F.7b-K: K-reconstruction (11/11 + √2)
│   │                              # F.7f: ε-η algebra completeness (rank 12)
│   │                              # G.8: ℓ from dessin (no SM input)
│   │
│   ├── t3_spectrum.py             # I.6: char(L_Cayley) factorization
│   │                              # D.2: BB^T uniqueness
│   │                              # D.5: M_lep eigenvalues d₁² ± √d₂, det=13
│   │                              # D.4: Kirchhoff = 40
│   │                              # D.6: φ-zero theorem Z_φ = {p,c,u,t}
│   │                              # D.7: golden hierarchy 1:φ:φ²
│   │                              # D.8: BV-quotient spec, σ₀-erasure
│   │                              # D.8b: spectral bridge BB^T + ΠLΠ^T = 2d₂·I₄
│   │
│   ├── t4_ckm.py                  # E.8: Residual Tree Theorem (3 layers, d₂²=9)
│   │                              # V.1: UST edge probabilities (4 types)
│   │                              # V.3: P_triple = 9/40
│   │                              # V.4: Wolfenstein λ, A, γ, R_b
│   │                              # V.6: CKM-PMNS complementarity A²+sin²θ₁₂=1
│   │                              # Pulls vs PDG 2024 + LHCb 2025
│   │
│   ├── t5_pmns.py                 # I.2/X.100: sin²θ₁₂ = 4/13 from CR
│   │                              # I.5/X.101: sin²θ₂₃ = 81/145 from CR
│   │                              # I.4/X.108/X.129: sin²θ₁₃ = 2/91 (index formula)
│   │                              # X.110: Catalan bridge d₁²+d₂² = Φ₃(d₂)
│   │                              # X.110a: face-cyclotomic resultants
│   │                              # X.129a: GN = PMNS denominators
│   │                              # Pulls vs NuFIT 6.0 IC19 NO
│   │
│   ├── t6_mass_formula.py         # G.1: sign window (k=3 unique)
│   │                              # G.2: BVP well-posedness (d₁+d₂=5)
│   │                              # G.3: Weyl 4D uniqueness
│   │                              # F.1: LO δK, R², 10/10 signs
│   │                              # G.0b: NLO h-factors, R²=0.89
│   │                              # G.0c: h derivation (4 constraints → unique)
│   │                              # C.8.3: Σf²h = Σn = 44
│   │                              # C.8.4: cubic uniqueness
│   │
│   ├── t7_alpha_mu_G.py           # H.1: α⁻¹ Form A = 137.035999202
│   │                              # H.1a: BULK = 432/π
│   │                              # H.1f: E₂*(τ=i) variational
│   │                              # H.2: μ₀ = 6π⁵, C = 10/9
│   │                              # H.3: G_pred = 6.67407e-11
│   │                              # H.3a: G-elasticity 222/101
│   │
│   ├── t8_gap3_closure.py         # X.97: trace formula chain (6 steps)
│   │                              # W.4: S₁₀ decomposition 2+2+2+1=7
│   │                              # X.91: L-factor dictionary
│   │                              # X.54: character formula d₁³fh
│   │                              # X.57: tensor factorization T = T₂⊗T₃
│   │                              # X.48: face Markov chain eigenvalues μ(d)/d
│   │
│   ├── t9_information.py          # C.8.1: Shannon H = log₂(12)
│   │                              # C.8.2: equicorrelation 192 = d₁⁶d₂
│   │                              # C.8.3: Σf²h = 44
│   │                              # V.10: dessin as [12,3,2] code
│   │                              # K.9: Moonshine T_{6E} = t₆ + 5
│   │
│   ├── t10_weinberg.py            # X.219: sin²θ_W = 3/13 = d₂/det_M
│   │                              # Tower C₂ = 13/12, gen ratio 1/d₁²
│   │                              # Unified det_M = 13 denominator
│   │                              # NLO correction (N-1)/d₂ = 5/3
│   │                              # Pull vs PDG 2024
│   │
│   ├── t11_cp_phase.py            # X.218: |sinδ| = 1 (cross-term irrationality)
│   │                              # X.224: sinδ = -1 (canonical ℍ orientation)
│   │                              # J² = 2⁹·3⁶·89²/(5²·7³·13⁵·29²)
│   │                              # Full |U|² matrix (9 rational entries)
│   │                              # 4-gear structure {5, 7, 13, 29}
│   │
│   ├── t12_cr_master.py           # X.225: Resultant degree 42 = N·L
│   │                              # X.226: GCD(R₁₃, R₂₃) = 1
│   │                              # CR = master equation, M = scaffolding
│   │                              # Cross-ratio arithmetic verification
│   │                              # Channel rule X.130 (forced assignment)
│   │
│   └── t13_tower.py               # X.183: f₁ = 1/55 = 1/((N-1)·dim_M₁₀)
│                                  # X.188/X.200/X.205: Tower levels n=0,1,2,3
│                                  # X.202: Fricke ★★★
│                                  # X.228: N=6 = max{genus 0 ∩ φ(N)≤2}
│
│   ├── t14_directed.py            # X.256: A_dir = σ₁+σ₀, χ = x²(x+1)(x−2)·q₃·q₅
│   │                              # X.263: Golden bridge q₅ = q_φ·q₃ − d₂
│   │                              # X.259: Old/new decomposition, 15 genus-0 levels
│   │                              # Discriminants: −59, 46901 (both prime)
│   │
│   ├── t15_golden_bridge.py       # X.267: Ω₃ = σ₁−σ₀ → eigenvalues {0,−φ,1/φ}
│   │                              # X.272: Tr(Ω₃^k) = (−1)^k L_k (Lucas)
│   │                              # X.268: [A₃,Ω₃] maximally nilpotent
│   │                              # X.275: N=6 unique (golden uniqueness)
│   │
│   └── t16_crt_unification.py     # X.280: L = 3I − A_dir − σ₀⁻¹ on V₆^{ex}
│                                  # X.281: C eigenvalues = {3, 6/5, 8/11}
│                                  # det(C) = 144/55 = index²/f₁⁻¹
│                                  # Tower corrections: 7/4, 169/150
│                                  # X.187: Fermat filtration (W₂=+1 → HALT)
│                                  # JUNO confirmation (+0.17σ)
│
├── README.md                      # (update with verification instructions)
└── requirements.txt               # numpy, sympy
```

## framework.py — ядро

```python
from fractions import Fraction
import sys

PASS = FAIL = 0

# ── LD constants (immutable) ──
d1, d2 = 2, 3
N = d1 * d2            # 6
index = (d1+1)*(d2+1)  # 12
L = N + 1              # 7
B1_size = 10
K_Kirchhoff = 40
Mon_order = 72
prod_w = 1*2*3*6       # 36
j_i = 1728             # j(τ=i)
dim_M10 = 11

# ── Experimental (CODATA 2022 / PDG 2024 / NuFIT 6.0 IC19 NO) ──
m_e = 0.51099895       # MeV
mu = 1836.15267343
g = mu ** 0.25
alpha_inv_CODATA = 137.035999177  # ± 0.000000021
alpha_inv_Rb = 137.035999206      # ± 0.000000011

# NuFIT 6.0 IC19 NO
sin2_12_exp, sin2_12_sig = 0.307, 0.012
sin2_23_exp, sin2_23_sig = 0.561, 0.015
sin2_13_exp, sin2_13_sig = 0.02195, 0.00054

# PDG 2024
lambda_exp, lambda_sig = 0.22497, 0.00070
A_exp, A_sig = 0.839, 0.011
gamma_exp, gamma_sig = 62.8, 2.6  # degrees, LHCb 2025
Rb_exp, Rb_sig = 0.389, 0.010

def check(name, condition, detail=""):
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"  ✓ {name}")
    else:
        FAIL += 1
        print(f"  ✗ {name}  {detail}")

def section(title):
    print(f"\n{'─'*65}")
    print(f"  {title}")
    print(f"{'─'*65}")

def summary():
    total = PASS + FAIL
    print(f"\n{'═'*65}")
    print(f"  TOTAL: {PASS}/{total} passed", end="")
    if FAIL: print(f"  *** {FAIL} FAILED ***")
    else: print(f"  — ALL CLEAR")
    print(f"{'═'*65}")
    return FAIL == 0
```

## Пример: t5_pmns.py

```python
from framework import *
import math

def run():
    section("5. PMNS MIXING ANGLES (X.100, X.101, X.108, X.129)")
    
    # X.100: sin²θ₁₂ from cross-ratio
    CR_12 = Fraction(d1, d2)  # 2/3
    sin2_12 = CR_12**2 / (1 + CR_12**2)  # = 4/13
    check("X.100: sin²θ₁₂ = 4/13",
          sin2_12 == Fraction(4, 13))
    
    # X.101: sin²θ₂₃ from cross-ratio  
    CR_23 = Fraction(d2**2, d1**3)  # 9/8
    sin2_23 = CR_23**2 / (1 + CR_23**2)  # = 81/145
    check("X.101: sin²θ₂₃ = 81/145",
          sin2_23 == Fraction(81, 145))
    
    # X.129: index formula
    Phi3_d1 = d1**2 + d1 + 1  # 7 = L
    Phi3_d2 = d2**2 + d2 + 1  # 13 = det M_lep
    sin2_13 = Fraction(index, N * Phi3_d1 * Phi3_d2)
    check("X.129: sin²θ₁₃ = index/(N·∏Φ₃) = 2/91",
          sin2_13 == Fraction(2, 91))
    
    # X.110: Catalan bridge
    check("X.110: d₁² + d₂² = Φ₃(d₂)",
          d1**2 + d2**2 == Phi3_d2)
    
    # Pulls
    pull_12 = (sin2_12_exp - float(sin2_12)) / sin2_12_sig
    pull_23 = (sin2_23_exp - float(sin2_23)) / sin2_23_sig
    pull_13 = (sin2_13_exp - float(sin2_13)) / sin2_13_sig
    
    check(f"PMNS θ₁₂ pull = {pull_12:+.2f}σ (within 1σ)",
          abs(pull_12) < 1)
    check(f"PMNS θ₂₃ pull = {pull_23:+.2f}σ (within 1σ)",
          abs(pull_23) < 1)
    check(f"PMNS θ₁₃ pull = {pull_13:+.2f}σ (within 1σ)",
          abs(pull_13) < 1)
    
    sum_pull = abs(pull_12) + abs(pull_23) + abs(pull_13)
    check(f"PMNS Σ|pull| = {sum_pull:.2f} < 1.0",
          sum_pull < 1.0)
    
    # CKM-PMNS complementarity V.6
    A2 = Fraction(d2**2, d1**2 + d2**2)  # 9/13
    check("V.6: A²(CKM) + sin²θ₁₂(PMNS) = 1",
          A2 + sin2_12 == 1)

if __name__ == "__main__":
    run()
    summary()
```

## Метрики (v1728)

| Tier | Секция companion | Checks | Статус |
|------|-----------------|--------|--------|
| t0 | A.1, B.1-B.5 | 35 | v8 (unchanged) |
| t1 | O.1 | 17 | v8 (unchanged) |
| t2 | F.3-F.7 | 58 | v8 (unchanged) |
| t3 | I.6, D.2-D.8 | 34 | v8 (unchanged) |
| t4 | E.8, V.1-V.6 | 26 | v8 (unchanged) |
| t5 | X.100-X.129 | 29 | v8 (unchanged) |
| t6 | G.0-G.8 | 22 | v8 (unchanged) |
| t7 | H.1-H.3 | 15 | v8 (unchanged) |
| t8 | X.97, W.4, X.48 | 31 | v8 (unchanged) |
| t9 | C.8, K.9, V.10 | 23 | v8 (unchanged) |
| t10 | X.219 | 15 | **NEW v1728** |
| t11 | X.218, X.224 | 25 | **NEW v1728** |
| t12 | X.225, X.226 | 15 | **NEW v1728** |
| t13 | X.183, X.202, X.228 | 28 | **NEW v1728** |
| t14 | X.256, X.263 | 34 | **NEW S300** |
| t15 | X.267, X.272, X.275 | 39 | **NEW S300** |
| t16 | X.280, X.281 | 58 | **NEW S300** |
| **Total** | | **508** | 290 v8 + 87 v1728 + 131 S300 |

## Запуск

```bash
cd LD-supplementary/verify
python run_all.py          # все тесты
python t5_pmns.py          # только PMNS
python t3_spectrum.py      # только спектр
```

## Принцип DUAL-COMPUTE

Каждое число вычисляется двумя способами где возможно:
- `Fraction` (exact) + `numpy` (float) → `assert` совпадение
- Альтернативная формула → `assert` совпадение с первой
