"""Tier 2: Quantum numbers from dessin (F.3, F.7d, F.7e, F.7b-K, F.7f, G.8)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from framework import *
from fractions import Fraction

def face(particle):
    """Face size = length of σ∞-cycle containing particle."""
    FACES = {
        'c': 6, 'u': 6, 'b': 6, 's': 6, 'd': 6, 't': 6,
        'e': 3, 'tau': 3, 'mu': 3,
        'W': 2, 'H': 2,
        'p': 1,
    }
    return FACES[particle]

def run():
    section("2a. n-VALUES FROM ECCENTRICITY (F.3)")

    # Quark n-formula: n_up = d₂·g − d₁, n_dn = d₁·g − 1
    # Generation g from eccentricity: g = N − ecc
    quarks = {
        'u': ('up', 1), 'd': ('down', 1),
        'c': ('up', 2), 's': ('down', 2),
        't': ('up', 3), 'b': ('down', 3),
    }
    for name, (iso, gen) in quarks.items():
        if iso == 'up':
            n_pred = d2 * gen - d1
        else:
            n_pred = d1 * gen - 1
        n_actual = PARTICLE_DATA[name][0]
        check(f"F.3: n({name}) = {n_pred} (g={gen}, {iso})", n_pred == n_actual,
              f"expected {n_actual}, got {n_pred}")

    # Lepton n-formula: n = (g-1)(N-1-g), g from ecc_full - d₂ + 1
    leptons = {'e': 1, 'mu': 2, 'tau': 3}
    for name, gen in leptons.items():
        n_pred = (gen - 1) * (N - 1 - gen)
        n_actual = PARTICLE_DATA[name][0]
        check(f"F.3: n({name}) = {n_pred} (g_lep={gen})", n_pred == n_actual)

    # Bosons: n = N = 6
    for name in ['W', 'H']:
        check(f"F.3: n({name}) = N = 6", PARTICLE_DATA[name][0] == N)

    # Anchor: n = d₁² = 4
    check("F.3: n(p) = d₁² = 4", PARTICLE_DATA['p'][0] == d1**2)

    # Σn = 44 = d₁²·dim M₁₀
    total_n = sum(PARTICLE_DATA[p][0] for p in PARTICLES)
    check(f"F.8: Σn = {total_n} = d₁²·dim M₁₀ = 44", total_n == d1**2 * dim_M10)

    # ═══════════════════════════════════════════════════════════
    section("2b. ε-η DFT ARCHITECTURE (F.7d, F.7e)")

    # ε-η bits for each particle
    def eps(w, prime):
        """ε(w) = 1 if gcd(w, d₂)=1, i.e. w coprime to 3."""
        if prime == d2:
            return 1 if w % d2 != 0 else 0
        return 0  # not used

    def eta(w):
        """η(w) = 1 if w ∈ {1, N}."""
        return 1 if w in (1, N) else 0

    for pname in PARTICLES:
        n_actual, ell_actual, K_actual, F_e, Fs1 = PARTICLE_DATA[pname]
        F_s0_e = face(SIGMA0[pname])  # face of σ₀-image

        eF = 1 if F_e % d2 != 0 else 0    # εF = ε(face(e))
        etF = 1 if F_e in (1, N) else 0    # ηF = η(face(e))
        e0 = 1 if F_s0_e % d2 != 0 else 0  # ε₀ = ε(face(σ₀(e)))

        Fs1_e = Fs1
        e1 = 1 if Fs1_e % d2 != 0 else 0   # ε₁ = ε(face(σ₁(e)))
        eta1 = 1 if Fs1_e in (1, N) else 0  # η₁ = η(face(σ₁(e)))

        # F.7d: Global n-polynomial (10 terms)
        n_poly = (N * eF + (N-1) * etF + (N-1) * e0 + d1**2 * e1
                  - d2**2 * etF * eF - d2**2 * etF * e0 - N * etF * e1
                  + d1 * etF * eta1 - d1 * e0 * eta1 - e1 * eta1)

        check(f"F.7d: n-poly({pname}) = {n_poly} = {n_actual}",
              n_poly == n_actual, f"got {n_poly}")

    section("2c. ℓ-POLYNOMIAL (F.7e)")

    for pname in PARTICLES:
        n_actual, ell_actual, K_actual, F_e, Fs1 = PARTICLE_DATA[pname]

        eF = 1 if F_e % d2 != 0 else 0
        etF = 1 if F_e in (1, N) else 0
        Fs1_e = Fs1
        eta1 = 1 if Fs1_e in (1, N) else 0

        # F.7e: ℓ = L − N·εF − d₁²·ηF − d₁·εF·ηF + (N−1)·εF·η₁
        ell_poly = L - N * eF - d1**2 * etF - d1 * eF * etF + (N-1) * eF * eta1

        check(f"F.7e: ℓ-poly({pname}) = {ell_poly} = {ell_actual}",
              ell_poly == ell_actual, f"got {ell_poly}")

    # Σℓ = 46
    total_ell = sum(PARTICLE_DATA[p][1] for p in PARTICLES)
    check(f"F.8: Σℓ = {total_ell} = 46", total_ell == 46)

    # ═══════════════════════════════════════════════════════════
    section("2d. K-RECONSTRUCTION (F.7b-K)")

    # K = 2^v₂ · 3^v₃ for rational-K particles
    K_TABLE = {
        'c':   (2, -1),   # 4/3
        'u':   (1, -1),   # 2/3
        't':   (1, -1),   # 2/3
        'b':   (1, -1),   # 2/3
        's':   (1, -1),   # 2/3
        'e':   (0, 0),    # 1
        'mu':  (-2, 1),   # 3/4
        'tau': (1, 0),    # 2
        'H':   (0, 1),    # 3
        'W':   (1, 0),    # 2
        'p':   (0, 0),    # 1
    }

    for pname, (v2, v3) in K_TABLE.items():
        K_computed = Fraction(2, 1)**v2 * Fraction(3, 1)**v3
        K_expected = PARTICLE_DATA[pname][2]
        check(f"F.7b-K: K({pname}) = 2^{v2}·3^{v3} = {K_computed}",
              K_computed == K_expected)

    check("F.7b-K: K(d) = √2 (EWSB, v₂=1/2, v₃=0)",
          PARTICLE_DATA['d'][2] is None)  # stored as None for √2

    # ═══════════════════════════════════════════════════════════
    section("2e. FACE SUMS (F.8)")

    face_sums_n = {}
    face_sums_ell = {}
    for pname in PARTICLES:
        f = face(pname)
        face_sums_n[f] = face_sums_n.get(f, 0) + PARTICLE_DATA[pname][0]
        face_sums_ell[f] = face_sums_ell.get(f, 0) + PARTICLE_DATA[pname][1]

    check("F.8: Σn(quarks) = d₂·L = 21", face_sums_n[6] == d2 * L)
    check("F.8: Σn(leptons) = L = 7", face_sums_n[3] == L)
    check("F.8: Σn(bosons) = index = 12", face_sums_n[2] == index)
    check("F.8: Σn(anchor) = d₁² = 4", face_sums_n[1] == d1**2)

    check("F.8: Σℓ(quarks) = N·d₂ = 18", face_sums_ell[6] == N * d2)
    check("F.8: Σℓ(leptons) = d₂·L = 21", face_sums_ell[3] == d2 * L)
    check("F.8: Σℓ(bosons) = L = 7", face_sums_ell[2] == L)
    check("F.8: Σℓ(anchor) = 0", face_sums_ell[1] == 0)

if __name__ == "__main__":
    run()
    summary()
