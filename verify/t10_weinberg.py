"""Tier 10: Weinberg Angle (X.219) — sin²θ_W = 3/13.

Derivation:
  EW generators: SU(2)_L has 3, U(1)_Y has 1 → ratio 1/d₁² = 1/4.
  Tower coefficient C₂ = det_M/index = 13/12 (PMNS level).
  sin²θ_W = (1/d₁²)/C₂ = (1/4)/(13/12) = 3/13.

Companion: X.192 (scan), X.219 (derivation).
Paper v1728: §XIV (Electroweak Mixing), Theorem (Weinberg angle).
"""

from framework import *

def run():
    section("10a. WEINBERG ANGLE — TREE LEVEL (X.219)")

    # EW generator ratio
    gen_ratio = Fraction(1, d1**2)  # 1/4
    check("X.219: EW generator ratio = 1/d₁² = 1/4",
          gen_ratio == Fraction(1, 4))

    # Tower C₂
    C2 = C_tower[2]
    check("X.219: C₂ = det_M/index = 13/12",
          C2 == Fraction(det_M_lep, index))

    # sin²θ_W
    sin2_W = gen_ratio / C2
    check("X.219: sin²θ_W = (1/d₁²)/C₂ = 3/13",
          sin2_W == Fraction(3, 13))
    check("X.219: sin²θ_W = d₂/det_M = 3/13",
          sin2_W == Fraction(d2, det_M_lep))

    # Unified denominator: det_M = 13 appears in θ₁₂, θ_W, θ₁₃
    sin2_12 = Fraction(d1**2, d1**2 + d2**2)  # 4/13
    sin2_13 = Fraction(d1, L * det_M_lep)     # 2/91
    check("Unified denom: sin²θ₁₂ = 4/13 has denom 13",
          sin2_12.denominator == 13)
    check("Unified denom: sin²θ_W = 3/13 has denom 13",
          sin2_W.denominator == 13)
    check("Unified denom: sin²θ₁₃ = 2/91 = 2/(7·13)",
          sin2_13 == Fraction(2, 91) and 91 % 13 == 0)
    check("Unified denom: 13 = Φ₃(d₂) = det M_lep",
          det_M_lep == 13)

    section("10b. WEINBERG ANGLE — TOWER CROSS-LEVEL (X.219)")

    # At n=1 (response level): sin²θ_W(n=1) = (1/d₁²)/C₁ = 9/40 = λ_CKM
    C1 = C_tower[1]
    sin2_W_n1 = gen_ratio / C1
    lambda_CKM = Fraction(d2**2, K_Kirchhoff)  # 9/40
    check("X.219 n=1: sin²θ_W(n=1) = (1/d₁²)/C₁ = 9/40",
          sin2_W_n1 == Fraction(9, 40))
    check("X.219 n=1: sin²θ_W(n=1) = λ_CKM",
          sin2_W_n1 == lambda_CKM)

    # cos²θ_W = 10/13
    cos2_W = 1 - sin2_W
    check("cos²θ_W = 10/13",
          cos2_W == Fraction(10, 13))

    section("10c. PULL vs EXPERIMENT (PDG 2024)")

    # Tree-level: 3/13 = 0.23077 vs MS-bar 0.23122.
    # At tree level, radiative corrections not included → deviation expected.
    exp_val, exp_sig = EXP_EW['sin2_thetaW_MSbar']
    dev_pct = (float(sin2_W) - exp_val) / exp_val * 100
    check(f"Tree-level dev = {dev_pct:+.3f}% (< 0.2%)",
          abs(dev_pct) < 0.2)

    # NLO correction: sin²θ_W = (3/13)(1 + (5/3)·α/(2π))
    alpha = 1.0 / alpha_inv_CODATA
    f_NLO = Fraction(N - 1, d2)  # 5/3
    sin2_W_NLO = float(sin2_W) * (1 + float(f_NLO) * alpha / (2 * math.pi))
    p_NLO = pull(sin2_W_NLO, exp_val, exp_sig)
    check(f"NLO correction factor = (N-1)/d₂ = 5/3 = {float(f_NLO):.4f}",
          f_NLO == Fraction(5, 3))
    check(f"NLO value = {sin2_W_NLO:.8f} (≈ exp {exp_val})",
          abs(sin2_W_NLO - exp_val) < 0.0001)
    check(f"Pull vs PDG (NLO) = {p_NLO:+.2f}σ (|pull| < 1)",
          abs(p_NLO) < 1)


if __name__ == "__main__":
    run()
    summary()
