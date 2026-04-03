"""Tier 3: Spectrum — Laplacian, BB^T, Kirchhoff, φ-zero, spectral bridge (D.2–D.8, I.6)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from framework import *
from fractions import Fraction
import numpy as np

def build_adjacency():
    """Build 12×12 adjacency matrix of Cayley graph from generators {σ₁, σ₀, σ₀⁻¹}.
    Multi-edges counted: A[i,j] = number of generators mapping i→j."""
    n = len(PARTICLES)
    A = np.zeros((n, n), dtype=int)
    sigma0_inv = {v: k for k, v in SIGMA0.items()}
    for perm in [SIGMA1, SIGMA0, sigma0_inv]:
        for x in PARTICLES:
            i, j = P[x], P[perm[x]]
            A[i][j] += 1
    return A

def build_biadjacency():
    """Build 4×6 biadjacency matrix B (BV × WV). Returns B and edge labels."""
    # BV indices: BV0={c,u,p}, BV1={b,t,e}, BV2={s,mu,H}, BV3={d,W,tau}
    # WV indices from σ₁-pairs: W0={c,p}, W1={u,t}, W2={b,mu}, W3={s,W}, W4={d,e}, W5={tau,H}
    BV = [{'c','u','p'}, {'b','t','e'}, {'s','mu','H'}, {'d','W','tau'}]
    WV_pairs = [('c','p'), ('u','t'), ('b','mu'), ('s','W'), ('d','e'), ('tau','H')]

    B = np.zeros((4, 6), dtype=int)
    for wi, (a, b_name) in enumerate(WV_pairs):
        for bi, bv_set in enumerate(BV):
            if a in bv_set:
                B[bi][wi] += 1
            if b_name in bv_set:
                B[bi][wi] += 1
    return B

def run():
    section("3a. BIADJACENCY AND BB^T (C.1, D.2, D.5)")

    B = build_biadjacency()

    # C.1: B is 4×6 with sum = 12 = index
    check("C.1: B is 4×6", B.shape == (4, 6))
    check("C.1: sum(B) = 12 = index", B.sum() == index)

    # D.2: BB^T — BV₀ has multi-edge {c,p} → BB^T[0,0] = 5
    BBT = B @ B.T
    BBT_expected = np.array([
        [5, 1, 0, 0],   # BV₀: multi-edge gives 2²+1² = 5
        [1, 3, 1, 1],
        [0, 1, 3, 2],
        [0, 1, 2, 3],
    ])
    check("D.2: BB^T[0,0] = 5 (multi-edge c,p)", BBT[0, 0] == 5)
    check("D.2: BB^T matches companion", np.array_equal(BBT, BBT_expected))
    check("D.2: Tr(BB^T) = 14 = index + d₁", np.trace(BBT) == index + d1)

    # D.5: M_lep = BB^T[1:,1:] (non-anchor 3×3)
    M_lep = BBT[1:, 1:]
    check("D.5: M_lep = [[3,1,1],[1,3,2],[1,2,3]]",
          np.array_equal(M_lep, np.array([[3,1,1],[1,3,2],[1,2,3]])))
    check("D.5: Tr(M_lep) = d₂² = 9", np.trace(M_lep) == d2**2)
    check("D.5: det(M_lep) = 13 = Φ₃(d₂)", int(round(np.linalg.det(M_lep))) == Phi3_d2)

    # M_lep eigenvalues: 1, d₁² ± √d₂ (roots of (x-1)(x²-8x+13))
    eigs = sorted(np.linalg.eigvalsh(M_lep))
    expected_eigs = sorted([1, d1**2 - d2**0.5, d1**2 + d2**0.5])
    check(f"D.5: M_lep eigenvalues ≈ {{1, d₁²±√d₂}} = {{1, 2.27, 5.73}}",
          all(abs(eigs[i] - expected_eigs[i]) < 1e-10 for i in range(3)))

    # μ-τ symmetry
    check("D.5: μ-τ symmetry M_lep(e,μ)=M_lep(e,τ)=1",
          M_lep[0, 1] == 1 and M_lep[0, 2] == 1)
    check("D.5: μ-τ symmetry M_lep(μ,μ)=M_lep(τ,τ)=3",
          M_lep[1, 1] == 3 and M_lep[2, 2] == 3)

    # ═══════════════════════════════════════════════════════════
    section("3b. CAYLEY LAPLACIAN (I.6)")

    A = build_adjacency()
    deg = np.diag(A.sum(axis=1))
    L_cayley = deg - A

    # All vertices have degree 3
    check("I.6: Cayley graph is 3-regular", all(A.sum(axis=1) == 3))

    # Laplacian = 3I - A
    check("I.6: L = 3I - A", np.array_equal(L_cayley, 3 * np.eye(12, dtype=int) - A))

    # Characteristic polynomial factorization
    # char(L) = x(x-1)(x-3)²(x-4)(x-5)³(x²-5x+1)(x²-5x+5)
    eigenvalues = sorted(np.linalg.eigvalsh(L_cayley.astype(float)))

    # Expected: 0, 1, 3, 3, 4, 5, 5, 5, (5±√21)/2, (5±√5)/2
    sqrt21 = 21**0.5
    sqrt5 = 5**0.5
    expected = sorted([0, 1, 3, 3, 4, 5, 5, 5,
                       (5 - sqrt21)/2, (5 + sqrt21)/2,
                       (5 - sqrt5)/2, (5 + sqrt5)/2])

    match = all(abs(eigenvalues[i] - expected[i]) < 1e-10 for i in range(12))
    check("I.6: Cayley spectrum matches char(L) factorization", match)

    # Trace = 12·3/2... no, Tr(L) = sum of eigenvalues = sum of degrees for Laplacian
    check(f"I.6: Tr(L) = 3·12 = 36", int(sum(eigenvalues) + 0.5) == 36)

    # ═══════════════════════════════════════════════════════════
    section("3c. KIRCHHOFF (D.4)")

    # K = 40 is for the BIPARTITE dessin graph (4 BV + 6 WV = 10 vertices)
    # Build bipartite adjacency and Laplacian
    n_bip = 10  # 4 BV + 6 WV
    A_bip = np.zeros((n_bip, n_bip), dtype=int)
    # B[i,j] = edges between BV_i and WV_j. Use B from biadjacency.
    for bi in range(4):
        for wj in range(6):
            if B[bi, wj] > 0:
                A_bip[bi, 4 + wj] = B[bi, wj]
                A_bip[4 + wj, bi] = B[bi, wj]

    deg_bip = np.diag(A_bip.sum(axis=1))
    L_bip = deg_bip - A_bip

    # Matrix Tree Theorem: K = det(L') for any cofactor
    # Remove last row/col (WV₅)
    L_bip_minor = L_bip[:-1, :-1].astype(float)
    K_bipartite = round(np.linalg.det(L_bip_minor))
    check(f"D.4: Kirchhoff(bipartite) = det(L') = {K_bipartite} = 40",
          K_bipartite == K_Kirchhoff)

    # Cross-check via eigenvalues
    eigs_bip = sorted(np.linalg.eigvalsh(L_bip.astype(float)))
    nonzero_bip = [e for e in eigs_bip if e > 0.01]
    K_from_eigs = np.prod(nonzero_bip) / n_bip
    check(f"D.4: Kirchhoff from bipartite spectrum = {K_from_eigs:.1f} = 40",
          abs(K_from_eigs - K_Kirchhoff) < 0.01)

    # Cayley graph Kirchhoff (different: 12-vertex Schreier graph)
    nonzero_cayley = [e for e in eigenvalues if e > 0.01]
    K_cayley = np.prod(nonzero_cayley) / 12
    check(f"X.UST: Kirchhoff(Cayley) = {K_cayley:.0f} = d₂(N−1)⁴ = 1875",
          abs(K_cayley - d2 * (N - 1)**4) < 1)

    # ═══════════════════════════════════════════════════════════
    section("3d. φ-ZERO THEOREM (D.6)")

    # φ-pair: eigenvalues (5±√5)/2
    phi = (1 + sqrt5) / 2
    lam_plus = (5 + sqrt5) / 2   # ≈ 3.618
    lam_minus = (5 - sqrt5) / 2  # ≈ 1.382

    # Find eigenvectors for φ-pair
    evals, evecs = np.linalg.eigh(L_cayley.astype(float))
    # Find indices closest to φ-pair eigenvalues
    idx_minus = min(range(12), key=lambda i: abs(evals[i] - lam_minus))
    idx_plus = min(range(12), key=lambda i: abs(evals[i] - lam_plus))

    v_minus = evecs[:, idx_minus]
    v_plus = evecs[:, idx_plus]

    # Z_φ = {p, c, u, t} — indices
    Z_phi = {P['p'], P['c'], P['u'], P['t']}

    for name in ['p', 'c', 'u', 't']:
        i = P[name]
        check(f"D.6: φ-eigenvector vanishes on {name} (v₋[{name}]={v_minus[i]:.2e})",
              abs(v_minus[i]) < 1e-10)
        check(f"D.6: φ-eigenvector vanishes on {name} (v₊[{name}]={v_plus[i]:.2e})",
              abs(v_plus[i]) < 1e-10)

    # Non-zero on others
    nonzero_count = sum(1 for i in range(12) if i not in Z_phi and abs(v_minus[i]) > 0.01)
    check(f"D.6: φ-eigenvector nonzero on 8 non-Z_φ particles", nonzero_count == 8)

    # D.7: golden hierarchy 1:φ:φ²
    abs_vals = {}
    for name in PARTICLES:
        i = P[name]
        abs_vals[name] = abs(v_minus[i])

    # Three nonzero tiers: {b,e}, {s,tau,W,H}, {d,mu}
    tier1 = [abs_vals['b'], abs_vals['e']]
    tier2 = [abs_vals['s'], abs_vals['tau'], abs_vals['W'], abs_vals['H']]
    tier3 = [abs_vals['d'], abs_vals['mu']]

    # All within each tier should be equal
    check("D.7: |v(b)| = |v(e)| (tier 1)", abs(tier1[0] - tier1[1]) < 1e-10)
    check("D.7: |v(s)| = |v(τ)| = |v(W)| = |v(H)| (tier 2)",
          max(tier2) - min(tier2) < 1e-10)
    check("D.7: |v(d)| = |v(μ)| (tier 3)", abs(tier3[0] - tier3[1]) < 1e-10)

    # Ratios should be 1 : φ : φ²... but which tier is which?
    t1_val = tier1[0]
    t2_val = tier2[0]
    t3_val = tier3[0]
    vals_sorted = sorted([t1_val, t2_val, t3_val])

    ratio_21 = vals_sorted[1] / vals_sorted[0]
    ratio_32 = vals_sorted[2] / vals_sorted[1]
    check(f"D.7: tier ratios ≈ φ = {phi:.6f} (got {ratio_21:.6f}, {ratio_32:.6f})",
          abs(ratio_21 - phi) < 1e-6 and abs(ratio_32 - phi) < 1e-6)

    # ═══════════════════════════════════════════════════════════
    section("3e. SPECTRAL BRIDGE (D.8b)")

    # BB^T + Π·L·Π^T = 2·d₂·I₄
    # Π = 4×12 BV indicator matrix
    BV_sets = [{'c','u','p'}, {'b','t','e'}, {'s','mu','H'}, {'d','W','tau'}]
    Pi = np.zeros((4, 12), dtype=int)
    for bi, bv_set in enumerate(BV_sets):
        for name in bv_set:
            Pi[bi][P[name]] = 1

    PiLPiT = Pi @ L_cayley @ Pi.T
    bridge = BBT + PiLPiT
    expected_bridge = 2 * d2 * np.eye(4, dtype=int)

    check("D.8b: BB^T + Π·L·Π^T = 2d₂·I₄ = 6·I₄",
          np.array_equal(bridge, expected_bridge))

    # σ₀-erasure: Π·L = Π·(I - σ₁)
    sigma1_matrix = np.zeros((12, 12), dtype=int)
    for x in PARTICLES:
        sigma1_matrix[P[x]][P[SIGMA1[x]]] = 1

    PiL = Pi @ L_cayley
    Pi_I_minus_S1 = Pi @ (np.eye(12, dtype=int) - sigma1_matrix)
    check("D.8: σ₀-erasure Π·L = Π·(I₁₂ − σ₁)",
          np.array_equal(PiL, Pi_I_minus_S1))

    # BV-quotient char poly: λ(λ-1)(λ-d₁²)(λ-(N-1))
    PiLPiT_quotient = (Pi @ L_cayley @ Pi.T).astype(float)
    # Normalize: each BV has 3 members, so quotient = PiLPiT / 3? No.
    # Actually quotient Laplacian Q = Π·L·Π^T where Π rows are normalized
    # But companion says char poly of ΠLΠ^T = λ(λ-1)(λ-d₁²)(λ-(N-1))
    q_eigs = sorted(np.linalg.eigvalsh(PiLPiT_quotient))
    expected_q = sorted([0, 1, d1**2, N - 1])
    check(f"D.8: spec(Π·L·Π^T) = {{0, 1, d₁², N-1}} = {{0, 1, 4, 5}}",
          all(abs(q_eigs[i] - expected_q[i]) < 1e-10 for i in range(4)))

if __name__ == "__main__":
    run()
    summary()
