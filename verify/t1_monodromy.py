"""Tier 1: Monodromy verification (O.1)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from framework import *

def compose(perm_a, perm_b):
    """Compose two permutations: (a∘b)(x) = a(b(x))."""
    return {x: perm_a[perm_b[x]] for x in perm_b}

def run():
    section("1. MONODROMY — O.1")

    # MCT: σ₁ · σ₀ · σ∞ = id
    product = compose(SIGMA1, compose(SIGMA0, SIGMA_INF))
    all_fixed = all(product[x] == x for x in PARTICLES)
    check("O.1 MCT: σ₁·σ₀·σ∞ = id (12/12)", all_fixed,
          f"failures: {[x for x in PARTICLES if product[x] != x]}")

    # σ∞ cycle type = (6, 3, 2, 1)
    def cycle_lengths(perm):
        visited = set()
        lengths = []
        for x in perm:
            if x not in visited:
                length = 0
                y = x
                while y not in visited:
                    visited.add(y)
                    y = perm[y]
                    length += 1
                lengths.append(length)
        return sorted(lengths, reverse=True)

    check("σ∞ cycle type = (6,3,2,1)", cycle_lengths(SIGMA_INF) == [6, 3, 2, 1])
    check("σ₁ cycle type = (2⁶)", cycle_lengths(SIGMA1) == [2]*6)
    check("σ₀ cycle type = (3⁴)", cycle_lengths(SIGMA0) == [3]*4)

    # BV compositions from σ₀
    def orbit(perm, start):
        result = set()
        x = start
        while x not in result:
            result.add(x)
            x = perm[x]
        return result

    bv0 = orbit(SIGMA0, 'c')
    bv1 = orbit(SIGMA0, 'b')
    bv2 = orbit(SIGMA0, 's')
    bv3 = orbit(SIGMA0, 'd')

    check("BV0 (anchor) = {c, u, p}", bv0 == {'c', 'u', 'p'})
    check("BV1 (index)  = {b, t, e}", bv1 == {'b', 't', 'e'})
    check("BV2 (star)   = {s, mu, H}", bv2 == {'s', 'mu', 'H'})
    check("BV3 (other)  = {d, W, tau}", bv3 == {'d', 'W', 'tau'})

    # Mon order: |⟨σ₁, σ₀⟩| = 72
    seen = set()
    queue = [SIGMA1, SIGMA0]
    identity = {x: x for x in PARTICLES}
    group = {tuple(sorted(identity.items()))}
    frontier = [SIGMA1, SIGMA0]
    # BFS to generate group
    elements = [identity]
    for _ in range(200):
        new_elements = []
        for g in elements:
            for gen in [SIGMA1, SIGMA0]:
                h = compose(g, gen)
                key = tuple(sorted(h.items()))
                if key not in group:
                    group.add(key)
                    new_elements.append(h)
        elements = new_elements
        if not elements:
            break

    check(f"|Mon| = |⟨σ₁, σ₀⟩| = 72", len(group) == Mon_order,
          f"got {len(group)}")

    # σ₁-pairs
    sigma1_pairs = []
    seen_pairs = set()
    for x in PARTICLES:
        y = SIGMA1[x]
        pair = tuple(sorted([x, y]))
        if pair not in seen_pairs:
            seen_pairs.add(pair)
            sigma1_pairs.append(pair)

    check("6 σ₁-pairs", len(sigma1_pairs) == 6)

    # Anchor = unique σ∞ fixed point
    fixed = [x for x in PARTICLES if SIGMA_INF[x] == x]
    check("Unique σ∞ fixed point = p (anchor)", fixed == ['p'])

    # σ₁-pair n-sums
    expected_n_sums = {
        ('u', 't'): 8,   # d₁³
        ('c', 'p'): 8,   # d₁³
        ('b', 'mu'): 8,  # d₁³
        ('d', 'e'): 1,
        ('s', 'W'): 9,   # d₂²
        ('H', 'tau'): 10, # |B₁|
    }
    for pair, expected in expected_n_sums.items():
        n_sum = PARTICLE_DATA[pair[0]][0] + PARTICLE_DATA[pair[1]][0]
        check(f"σ₁-pair {{{pair[0]},{pair[1]}}} Σn = {expected}",
              n_sum == expected, f"got {n_sum}")

if __name__ == "__main__":
    run()
    summary()
