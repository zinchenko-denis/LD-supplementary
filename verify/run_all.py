#!/usr/bin/env python3
"""LD Verification Suite — run all tiers.

Usage:
    python run_all.py          # all tiers
    python run_all.py t5       # only PMNS
    python run_all.py t1 t5    # monodromy + PMNS
"""
import sys, os, importlib

sys.path.insert(0, os.path.dirname(__file__))
import framework

TIERS = [
    ('t0_foundation',      'Foundation: N=6, B₁ (A.1, B.1–B.5)'),
    ('t1_monodromy',       'Monodromy O.1'),
    ('t2_quantum_numbers', 'Quantum numbers (F.3–F.7)'),
    ('t3_spectrum',        'Spectrum D.2–D.8, I.6'),
    ('t4_ckm',            'CKM E.8, V.1–V.4'),
    ('t5_pmns',            'PMNS angles (X.100–X.129)'),
    ('t6_mass_formula',    'Mass formula G.0–G.8'),
    ('t7_alpha_mu_G',      'α, μ, G (H.1–H.3)'),
    ('t8_gap3_closure',   'Gap 3 closure X.97'),
    ('t9_information',    'Information geometry C.8, K.9'),
    ('t10_weinberg',      'Weinberg angle X.219'),
    ('t11_cp_phase',      'CP phase, |U|², Jarlskog X.218/X.224'),
    ('t12_cr_master',     'CR = master equation X.225/X.226'),
    ('t13_tower',         'Tower structure X.183/X.202/X.228'),
    ('t14_directed',      'Directed operators X.256/X.263'),
    ('t15_golden_bridge', 'Golden bridge + Lucas X.267/X.272'),
    ('t16_crt_unification', 'CRT grand unification X.280/X.281'),
]

def main():
    print("=" * 65)
    print("  LD VERIFICATION SUITE")
    print(f"  Companion: S295+, 17 tiers (t0–t16)")
    print(f"  Paper: v1728_draft_S295, DOI 10.5281/zenodo.19520240")
    print("=" * 65)

    # Filter tiers if args given
    if len(sys.argv) > 1:
        requested = set(sys.argv[1:])
        tiers = [(m, d) for m, d in TIERS if any(r in m for r in requested)]
    else:
        tiers = TIERS

    for module_name, description in tiers:
        try:
            mod = importlib.import_module(module_name)
            mod.run()
        except ImportError as e:
            print(f"\n  [SKIP] {description} — {e}")
        except Exception as e:
            print(f"\n  [ERROR] {description} — {e}")
            framework.FAIL_COUNT += 1

    framework.summary()
    sys.exit(0 if framework.FAIL_COUNT == 0 else 1)

if __name__ == "__main__":
    main()
