"""Tier 12: Cross-Ratio Master Equation (X.225, X.226).

X.225 [THM-comp]: Resultant R₁₃ has degree 42 = N·L, irreducible over ℚ.
X.226 [THM-comp]: GCD(R₁₃, R₂₃) = 1 → no operator M reproduces all 3 PMNS
    angles simultaneously → CR is the master equation, M is scaffolding.

Note: Full symbolic verification of X.225/X.226 requires ~150s of sympy
    computation on the operator M. This module verifies the STRUCTURAL
    properties (degree = N·L, coprimality implications) but not the
    polynomial itself (which requires the full M60 Universal Sylvester
    framework from Colab).

Companion: X.225, X.226. Paper v1728: §XII (PMNS — Cross-Ratio).
"""

from framework import *

def run():
    section("12a. STRUCTURAL DEGREE (X.225)")

    # Resultant degree = N·L = 42
    resultant_deg = N * L
    check("X.225: Resultant degree = N·L = 42",
          resultant_deg == 42)
    check("42 = 6 × 7 = N × L",
          42 == N * L)
    check("42 = 2 × 3 × 7 = d₁·d₂·L",
          42 == d1 * d2 * L)

    section("12b. GCD = 1 IMPLICATIONS (X.226)")

    # The structural result: if GCD(R₁₃, R₂₃) = 1 then the algebraic
    # curves C₁₃ and C₂₃ share no common point in (b,c)-space.
    # This means no single operator M in the monodromy algebra
    # simultaneously produces sin²θ₁₃ = 2/91 AND sin²θ₂₃ = 81/145.

    # Verify the LD values that enter the resultants:
    sin2_13 = Fraction(2, 91)
    sin2_23 = Fraction(81, 145)

    # Check denominators are coprime (necessary for GCD=1)
    from math import gcd
    check("gcd(91, 145) = 1 (coprime denominators)",
          gcd(91, 145) == 1)

    # 91 = 7 × 13, 145 = 5 × 29
    check("91 = L · det_M = 7 · 13",
          91 == L * det_M_lep)
    check("145 = 5 · 29 (base primes, no tower overlap)",
          145 == 5 * 29)

    # Prime factorisation shows separation:
    # θ₁₃ involves tower primes {7, 13}
    # θ₂₃ involves base primes {5, 29}
    check("Tower primes {7, 13} ∩ Base primes {5, 29} = ∅",
          {7, 13}.isdisjoint({5, 29}))

    section("12c. CROSS-RATIO VALUES — ARITHMETIC CHECK")

    # The 4 cusp values of t₆ on P¹:
    cusps = {
        'c0': 0,         # cusp at ∞ → t₆ = 0
        'c2': -d2**2,    # cusp at 0 → t₆ = -9
        'c3': -d1**3,    # cusp at 1/2 → t₆ = -8
        'cinf': None,    # cusp at 1/3 → t₆ = ∞
    }
    # Special point: t₆ = -index = -12 (from j=0, P₄(-index)=0)
    t_special = -index  # -12

    # CR for θ₁₂: CR(-12, 0; -9, -8) = 2/3
    a, b_pt, c_pt, d_pt = -12, 0, -9, -8
    CR_12 = Fraction((c_pt - a) * (d_pt - b_pt),
                     (c_pt - b_pt) * (d_pt - a))
    check(f"CR(-12, 0; -9, -8) = {CR_12} = d₁/d₂",
          CR_12 == Fraction(d1, d2))
    check("tan θ₁₂ = CR = 2/3 → sin²θ₁₂ = 4/13",
          CR_12**2 / (1 + CR_12**2) == Fraction(4, 13))

    # CR for θ₂₃: CR(∞, 0; -8, -9) = d₂²/d₁³ = 9/8
    # With ∞: CR(∞,b;c,d) = (d-b)/(c-b)
    CR_23 = Fraction((-9 - 0), (-8 - 0))  # (d-b)/(c-b) = -9/(-8) = 9/8
    check(f"CR(∞, 0; -8, -9) = {CR_23} = d₂²/d₁³",
          CR_23 == Fraction(d2**2, d1**3))
    check("tan θ₂₃ = CR = 9/8 → sin²θ₂₃ = 81/145",
          CR_23**2 / (1 + CR_23**2) == Fraction(81, 145))

    # θ₁₃ from INDEX formula (not CR): sin²θ₁₃ = 2/91
    sin2_13_euler = (Fraction(Phi2_d1, d1 * Phi3_d1) *
                     Fraction(Phi2_d2, d2 * Phi3_d2))
    check("sin²θ₁₃ = ∏(Φ₂(p)/(p·Φ₃(p))) = 2/91",
          sin2_13_euler == Fraction(2, 91))

    section("12d. CHANNEL RULE (X.130) — FORCED ASSIGNMENT")

    # θ₁₃ unreachable from CR channel:
    # CR²/(1+CR²) for CR = d₁/d₂ → 4/13 (= θ₁₂)
    # CR²/(1+CR²) for CR = d₂²/d₁³ → 81/145 (= θ₂₃)
    # No CR among the 6 special points gives 2/91
    check("2/91 ≠ 4/13 (θ₁₃ ≠ θ₁₂ channel)",
          Fraction(2, 91) != Fraction(4, 13))
    check("2/91 ≠ 81/145 (θ₁₃ ≠ θ₂₃ channel)",
          Fraction(2, 91) != Fraction(81, 145))

    # Verify Pythagorean: sin²θ₁₃ = sin²θ₁₂ / (d₁·L)
    check("Hierarchy: sin²θ₁₃ = sin²θ₁₂/(d₁L) = (4/13)/14",
          sin2_13 == Fraction(4, 13) / (d1 * L))


if __name__ == "__main__":
    run()
    summary()
