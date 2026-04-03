"""LD Verification Framework — core constants, check/section/summary."""

from fractions import Fraction
import math

# ═══════════════════════════════════════════════════════════════
#  LD CONSTANTS (immutable, from companion §Notation)
# ═══════════════════════════════════════════════════════════════

d1, d2 = 2, 3
N = d1 * d2                    # 6
index = (d1 + 1) * (d2 + 1)   # 12
L = N + 1                      # 7
B1_size = 10
K_Kirchhoff = 40
Mon_order = 72
Aut_order = 2
prod_w = 1 * 2 * 3 * 6        # 36
j_i = 1728                     # j(τ = i)
dim_M10 = 11                   # dim M₁₀(Γ₀(6))

# Cyclotomic at primes
Phi2_d1 = d1 + 1               # 3
Phi2_d2 = d2 + 1               # 4
Phi3_d1 = d1**2 + d1 + 1       # 7 = L
Phi3_d2 = d2**2 + d2 + 1       # 13 = det M_lep
det_M_lep = Phi3_d2            # 13

# ═══════════════════════════════════════════════════════════════
#  MONODROMY — Single Source of Truth (O.1)
# ═══════════════════════════════════════════════════════════════

PARTICLES = ['c', 'u', 'b', 's', 'd', 't', 'e', 'tau', 'mu', 'W', 'H', 'p']
P = {name: i for i, name in enumerate(PARTICLES)}

# σ∞ = (c u b s d t)(e τ μ)(W H)(p)
SIGMA_INF = {
    'c': 'u', 'u': 'b', 'b': 's', 's': 'd', 'd': 't', 't': 'c',
    'e': 'tau', 'tau': 'mu', 'mu': 'e',
    'W': 'H', 'H': 'W',
    'p': 'p'
}

# σ₁ = (u t)(c p)(b μ)(d e)(s W)(τ H)
SIGMA1 = {
    'u': 't', 't': 'u',
    'c': 'p', 'p': 'c',
    'b': 'mu', 'mu': 'b',
    'd': 'e', 'e': 'd',
    's': 'W', 'W': 's',
    'tau': 'H', 'H': 'tau'
}

# σ₀ = (c u p)(b t e)(s μ H)(d W τ)
SIGMA0 = {
    'c': 'u', 'u': 'p', 'p': 'c',
    'b': 't', 't': 'e', 'e': 'b',
    's': 'mu', 'mu': 'H', 'H': 's',
    'd': 'W', 'W': 'tau', 'tau': 'd'
}

# ═══════════════════════════════════════════════════════════════
#  PARTICLE DATA (verified S211, companion Table 1)
# ═══════════════════════════════════════════════════════════════

PARTICLE_DATA = {
    #       n   ℓ   K            face  Fσ₁
    'e':   (0,  7,  1,           3,    3),
    'u':   (1,  3,  Fraction(2,3), 6,  6),
    'd':   (1,  3,  None,        6,    3),     # K = √2 (EWSB)
    'mu':  (3,  7,  Fraction(3,4), 3,  6),
    's':   (3,  3,  Fraction(2,3), 6,  2),
    'p':   (4,  0,  1,           1,    1),
    'c':   (4,  3,  Fraction(4,3), 6,  1),
    'tau': (4,  7,  2,           3,    2),
    'b':   (5,  3,  Fraction(2,3), 6,  3),
    'W':   (6,  6,  2,           2,    6),
    'H':   (6,  1,  3,           2,    3),
    't':   (7,  3,  Fraction(2,3), 6,  6),
}

# h-factor table (G.0b)
H_FACTOR = {1: 2, 2: Fraction(9, 4), 3: 1, 6: Fraction(2, 3)}

# ═══════════════════════════════════════════════════════════════
#  EXPERIMENTAL DATA (sources in comments)
# ═══════════════════════════════════════════════════════════════

# CODATA 2022 (α⁻¹)
m_e_MeV = 0.51099895
mu_ratio = 1836.15267343
g_base = mu_ratio ** 0.25
alpha_inv_CODATA = 137.035999177   # ± 0.000000021
alpha_inv_Rb = 137.035999206       # ± 0.000000011

# NuFIT 6.0 IC19 NO
EXP_PMNS = {
    'sin2_12': (0.307, 0.012),
    'sin2_23': (0.561, 0.015),
    'sin2_13': (0.02195, 0.00054),
}

# PDG 2024 + LHCb 2025
EXP_CKM = {
    'lambda': (0.22497, 0.00070),
    'A':      (0.839, 0.011),
    'gamma':  (62.8, 2.6),       # degrees, LHCb 2025
    'Rb':     (0.389, 0.010),
    'J':      (3.08e-5, 0.13e-5),
}

# Masses (MS-bar at 2 GeV for quarks, pole for others) — MeV
EXP_MASS = {
    'e': 0.51099895, 'u': 2.16, 'd': 4.67, 'mu': 105.6584, 's': 93.4,
    'p': 938.27208, 'c': 1270, 'tau': 1776.86, 'b': 4180,
    'W': 80377, 'H': 125100, 't': 172690,
}

# ═══════════════════════════════════════════════════════════════
#  TEST FRAMEWORK
# ═══════════════════════════════════════════════════════════════

PASS_COUNT = 0
FAIL_COUNT = 0

def check(name: str, condition: bool, detail: str = ""):
    """Register a pass/fail check."""
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        print(f"  ✓ {name}")
    else:
        FAIL_COUNT += 1
        print(f"  ✗ {name}  {detail}")

def section(title: str):
    """Print section header."""
    print(f"\n{'─' * 65}")
    print(f"  {title}")
    print(f"{'─' * 65}")

def summary() -> bool:
    """Print summary and return True if all passed."""
    total = PASS_COUNT + FAIL_COUNT
    print(f"\n{'═' * 65}")
    if FAIL_COUNT:
        print(f"  RESULT: {PASS_COUNT}/{total} passed — {FAIL_COUNT} FAILED")
    else:
        print(f"  RESULT: {PASS_COUNT}/{total} passed — ALL CLEAR ✓")
    print(f"{'═' * 65}")
    return FAIL_COUNT == 0

def pull(theory: float, exp_val: float, exp_sig: float) -> float:
    """Compute (exp - theory) / σ."""
    return (exp_val - theory) / exp_sig
