"""Tier 6: Mass formula — LO, NLO, signs, h-derivation (G.0–G.8)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from framework import *
from fractions import Fraction
import math

def Phi(n):
    """Φ(n) = n³(1 − n/L)."""
    return n**3 * (1 - n / L)

def run():
    section("6a. SIGN WINDOW AND BVP (G.1, G.2)")

    # G.1: k=3 unique integer in sign window
    alpha = 1 / alpha_inv_CODATA
    for particle in PARTICLES:
        n, ell = PARTICLE_DATA[particle][0], PARTICLE_DATA[particle][1]
        if particle == 'p':
            continue  # anchor: ℓ=0, always positive
        delta_pred = Phi(n) - L * ell
        # We just check signs are correct — need experimental δK
        # Sign of δK_pred comes from Φ(n) − Lℓ

    # Count signs correct at k=3 (unique)
    # Particles with known sign of δK_obs
    SIGN_OBS = {
        'u': -1, 'd': -1, 's': -1, 'c': +1, 'b': +1, 't': -1,
        'mu': -1, 'tau': -1, 'W': -1, 'H': +1,
    }
    signs_ok = 0
    for p_name, obs_sign in SIGN_OBS.items():
        n, ell = PARTICLE_DATA[p_name][0], PARTICLE_DATA[p_name][1]
        pred_sign = 1 if Phi(n) - L * ell > 0 else -1
        if pred_sign == obs_sign:
            signs_ok += 1
    check(f"G.1: 10/10 signs correct at k=d₂=3", signs_ok == 10)

    # Check k=2 and k=4 fail
    for k_test in [2, 4]:
        ok = 0
        for p_name, obs_sign in SIGN_OBS.items():
            n = PARTICLE_DATA[p_name][0]
            ell = PARTICLE_DATA[p_name][1]
            phi_k = n**k_test * (1 - n / L)
            pred_sign = 1 if phi_k - L * ell > 0 else -1
            if pred_sign == obs_sign:
                ok += 1
        check(f"G.1: k={k_test} gives {ok}/10 signs (not 10/10)", ok < 10)

    # G.2: BVP well-posedness d₁+d₂=5
    check("G.2: d₁+d₂ = 5 (BVP D⁴ well-posedness)", d1 + d2 == 5)
    check("G.2: BVP boundary conditions = d₂+(d₁-1) = 3+1 = 4 = d₁²",
          d2 + (d1 - 1) == d1**2)

    # ═══════════════════════════════════════════════════════════
    section("6b. NLO h-FACTORS (G.0b)")

    # h-factor values
    h = {1: Fraction(2), 2: Fraction(9, 4), 3: Fraction(1), 6: Fraction(2, 3)}

    check("G.0b: h(1) = d₁ = 2", h[1] == d1)
    check("G.0b: h(2) = d₂²/d₁² = 9/4", h[2] == Fraction(d2**2, d1**2))
    check("G.0b: h(3) = 1", h[3] == 1)
    check("G.0b: h(6) = d₁/d₂ = 2/3", h[6] == Fraction(d1, d2))

    # Key identities
    prod_h = h[1] * h[2] * h[3] * h[6]
    check(f"G.0b: ∏h = {prod_h} = d₂ = 3", prod_h == d2)

    sum_f2h = sum(Fraction(f**2) * h[f] for f in [1, 2, 3, 6])
    check(f"C.8.3: Σf²h = {sum_f2h} = Σn = 44", sum_f2h == 44)

    check("V.4: h(2) = tan γ_CKM = d₂²/d₁²",
          h[2] == Fraction(d2**2, d1**2))

    # ═══════════════════════════════════════════════════════════
    section("6c. NLO PERFORMANCE (G.0b)")

    # Compute δK for each particle
    alpha_val = 1 / alpha_inv_CODATA
    NLO_pred = {}
    LO_pred = {}
    for p_name in PARTICLES:
        n, ell, K, face, fs1 = PARTICLE_DATA[p_name]
        if p_name == 'p':
            continue
        phi_val = Phi(n)
        lo = alpha_val / (2 * math.pi) * (phi_val - L * ell)
        nlo = float(h[fs1]) * lo
        LO_pred[p_name] = lo * 100   # percent
        NLO_pred[p_name] = nlo * 100

    # Observed δK (from companion G.0b table)
    DK_OBS = {
        'u': -3.14, 'd': -1.28, 's': -2.26, 'c': 1.52, 'b': 2.08, 't': -1.58,
        'mu': -1.71, 'tau': -5.31, 'W': -0.05, 'H': 3.84,
    }

    # R² computation
    obs_vals = [DK_OBS[p] for p in DK_OBS]
    mean_obs = sum(obs_vals) / len(obs_vals)
    ss_tot = sum((v - mean_obs)**2 for v in obs_vals)

    ss_res_nlo = sum((DK_OBS[p] - NLO_pred[p])**2 for p in DK_OBS)
    ss_res_lo = sum((DK_OBS[p] - LO_pred[p])**2 for p in DK_OBS)

    r2_nlo = 1 - ss_res_nlo / ss_tot
    r2_lo = 1 - ss_res_lo / ss_tot

    check(f"G.0b: R²(NLO) = {r2_nlo:.3f} > 0.85", r2_nlo > 0.85)
    check(f"G.0b: R²(LO) = {r2_lo:.3f} ≈ 0.68", abs(r2_lo - 0.68) < 0.05)
    check(f"G.0b: NLO improves over LO (R² {r2_nlo:.2f} > {r2_lo:.2f})", r2_nlo > r2_lo)

    # Signs NLO (same as LO since h > 0)
    nlo_signs = sum(1 for p in DK_OBS
                    if (NLO_pred[p] > 0) == (DK_OBS[p] > 0))
    check(f"G.0b: NLO signs {nlo_signs}/10", nlo_signs == 10)

    # ═══════════════════════════════════════════════════════════
    section("6d. h DERIVATION CONSTRAINTS (G.0c)")

    # 4 constraints → unique h
    # (1) h(2) = d₂²/d₁² [THM, V.4]
    check("G.0c(1): h(2) = 9/4 from V.4", h[2] == Fraction(9, 4))

    # (1') h(1) = d₁ [THM-arith, X.56]
    check("G.0c(1'): h(1) = 2 from X.56", h[1] == Fraction(d1))

    # (⊥) c₃(h·f) = 0 ⟺ h(1) = d₂·h(6)
    check("G.0c(⊥): h(1) = d₂·h(6)", h[1] == d2 * h[6])

    # (2) ⟨π,h⟩ = d₂²/d₁³ = 9/8
    pi_h = sum(Fraction(f) * h[f] for f in [1, 2, 3, 6]) / index
    check(f"G.0c(2): ⟨π,h⟩ = {pi_h} = d₂²/d₁³",
          pi_h == Fraction(d2**2, d1**3))

    # Catalan consistency: (⊥)+(2) require d₂²−d₁³=1
    check("G.0c: Catalan consistency d₂²−d₁³ = 1", d2**2 - d1**3 == 1)

    # C.8.4: cubic uniqueness
    # (3c-2)(45c²-29c-2) = 0 at c = h(6) = 2/3
    c = h[6]
    cubic = (3 * c - 2) * (45 * c**2 - 29 * c - 2)
    check(f"C.8.4: cubic at h(6)=2/3 → {cubic} = 0", cubic == 0)

if __name__ == "__main__":
    run()
    summary()
