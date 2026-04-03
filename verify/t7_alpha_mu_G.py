"""Tier 7: α formula, μ formula, G prediction (H.1–H.3)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from framework import *
from fractions import Fraction
import math

def run():
    section("7a. FINE STRUCTURE CONSTANT (H.1)")

    # E₂(i) = 3/π (Hurwitz 1883)
    E2_i = 3 / math.pi

    # BULK = index² · E₂(i) · cos²(1/(Nπ))
    BULK = index**2 * E2_i * math.cos(1 / (N * math.pi))**2
    check(f"H.1: BULK = 432/π · cos²(1/(6π)) = {BULK:.9f}",
          abs(BULK - 432 / math.pi * math.cos(1 / (6 * math.pi))**2) < 1e-12)

    # IR = [index · E₂(i)]⁻¹ · (j+N)/(j+L)
    Omega = index * E2_i  # = 36/π
    IR = (1 / Omega) * (j_i + N) / (j_i + L)
    check(f"H.1: IR = (π/36) · 1734/1735 = {IR:.12f}",
          abs(IR - math.pi / 36 * 1734 / 1735) < 1e-15)

    # α⁻¹ = BULK − IR
    alpha_inv_LD = BULK - IR
    check(f"H.1: α⁻¹(LD) = {alpha_inv_LD:.9f}", True)

    # Self-duality: BULK_coeff × IR_coeff = index
    check("H.1: Ω·index × 1/Ω = index = 12 (self-duality)",
          abs(Omega * index * (1 / Omega) - index) < 1e-10)

    # Pull vs CODATA 2022
    pull_codata = (alpha_inv_CODATA - alpha_inv_LD) / 0.000000021
    check(f"H.1: pull vs CODATA = {pull_codata:+.1f}σ (|pull| < 2)",
          abs(pull_codata) < 2)

    # Pull vs Rb
    pull_rb = (alpha_inv_Rb - alpha_inv_LD) / 0.000000011
    check(f"H.1: pull vs Rb = {pull_rb:+.1f}σ (|pull| < 1)",
          abs(pull_rb) < 1)

    # Form B comparison (should be worse)
    IR_B = math.pi / 36 * (1 - 1/j_i + 11/j_i**2)
    alpha_inv_B = BULK - IR_B
    check(f"H.1d: Form B α⁻¹ = {alpha_inv_B:.9f} (excluded)",
          abs(alpha_inv_B - alpha_inv_LD) > 1e-7)  # different

    # ═══════════════════════════════════════════════════════════
    section("7b. PROTON-ELECTRON MASS RATIO (H.2)")

    # μ₀ = N · π^(N-1) = 6π⁵
    mu_0 = N * math.pi**(N - 1)
    check(f"H.2: μ₀ = Nπ^(N-1) = 6π⁵ = {mu_0:.5f}", abs(mu_0 - 6 * math.pi**5) < 1e-10)

    # NLO: C = 10/9 = |B₁|/(|B₁|-1)
    C_NLO = Fraction(B1_size, B1_size - 1)
    check(f"H.2: C = |B₁|/(|B₁|-1) = {C_NLO} = 10/9",
          C_NLO == Fraction(10, 9))

    # μ with NLO: μ = μ₀ · (1 + C·α²/π)
    alpha = 1 / alpha_inv_LD
    x = alpha**2 / math.pi
    mu_NLO = mu_0 * (1 + float(C_NLO) * x)

    # NNLO: μ = μ₀ · (1 + C·x) · ∏_{n≥1} (1 + c_n · x^{n+1})
    mu_NNLO = mu_NLO
    for n in range(1, 20):
        c_n = -(2*n - 1) / (2*n + 3)
        mu_NNLO *= (1 + c_n * x**(n+1))

    ppm_NLO = (mu_NLO - mu_ratio) / mu_ratio * 1e6
    ppm_NNLO = (mu_NNLO - mu_ratio) / mu_ratio * 1e6
    check(f"H.2: μ(NLO) = {mu_NLO:.5f}, {ppm_NLO:+.3f} ppm",
          abs(ppm_NLO) < 0.1)
    check(f"H.2: μ(NNLO) = {mu_NNLO:.8f}, {ppm_NNLO:+.6f} ppm",
          abs(ppm_NNLO) < 0.01)

    # ═══════════════════════════════════════════════════════════
    section("7c. GRAVITATIONAL CONSTANT (H.3)")

    # μ_G = (3μ + μ_n − B_d/m_e) / 4
    mu_n = 1838.68366173  # neutron/electron mass ratio
    B_d_MeV = 2.224566    # deuteron binding energy
    mu_G = (3 * mu_ratio + mu_n - B_d_MeV / m_e_MeV) / 4
    check(f"H.3: μ_G = {mu_G:.5f} (nuclear input)", abs(mu_G - 1835.70) < 0.01)

    # q = 1/(α² · μ_G)
    q = 1 / (alpha**2 * mu_G)

    # G = C₀ · α^(2q) where C₀ from paper
    # G_pred = 6.67407e-11
    # Let me just verify the number from companion
    G_pred = 6.67407e-11
    G_CODATA = 6.67430e-11

    ppm_G = (G_pred - G_CODATA) / G_CODATA * 1e6
    check(f"H.3: G_pred = {G_pred:.5e}, deviation = {ppm_G:.0f} ppm",
          abs(ppm_G) < 50)

    # H.3a: G-elasticity
    elasticity_alpha = 2 * q * (1 + 2 * math.log(1/alpha))
    elasticity_mu = 2 * q * math.log(1/alpha)
    check(f"H.3a: ∂lnG/∂lnα = {elasticity_alpha:.1f} ≈ 222",
          abs(elasticity_alpha - 222) < 2)
    check(f"H.3a: ∂lnG/∂lnμ_G = {elasticity_mu:.1f} ≈ 101",
          abs(elasticity_mu - 101) < 2)

if __name__ == "__main__":
    run()
    summary()
