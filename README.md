# LD Framework — Supplementary Materials

Computational verification, proof companion, and supplementary materials for:

**"1728: The Standard Model from X₀(6)"**
Denis D. Zinchenko
Paper DOI: [10.5281/zenodo.19520240](https://doi.org/10.5281/zenodo.19520240)

---

## Proof Companion

`LD_proof_companion.md` — self-contained catalog of all LD results (sessions S42–S295).

**Contents:**
- Every theorem, derivation, observation, and conjecture with epistemic markers:
  `[THM]`, `[DER]`, `[OBS]`, `[CONJ]`, `[DEAD]`
- Full derivation chains with dependencies
- 117+ closed (dead) directions with session references
- Corrections log (Z-log) tracking all errors found and fixed
- Open questions with current status (Gap 9 partially closed, Gap 3 closed)
- Independence ledger: 18 Tier A predictions

**Sections:** O (Monodromy) · A (Foundation) · B (B₁ set) · C (Dessin) · D (Spectrum) · E (CKM) · F (Mass formula) · G (δK formula) · H (α, μ, G) · I (PMNS) · J (L-functions) · K (Hauptmodul) · L (Scattering) · M (Selberg) · N (QTC) · R (Regulators) · S (DFT) · T (Operator) · U (Genus-0) · V (CKM derived) · W (Modular forms) · X (Results X.1–X.281) · Y (Open) · Z (Corrections)

---

## Verification Suite (Python)

`verify/` — **508 independent checks** across 17 tiers, covering every numerical claim in the paper, using exact arithmetic.

**Usage:**

```bash
cd verify
pip install numpy sympy
python run_all.py          # all 17 tiers (508 checks)
python run_all.py t5       # only PMNS
python run_all.py t10 t11  # Weinberg angle + CP phase
```

**Requirements:** Python 3.10+, NumPy, SymPy. No SageMath needed.

**Output:**

```
508 PASSED / 0 FAILED — ALL CLEAR ✓
```

**Tiers:**

| Tier | Section | Description | Checks |
|------|---------|-------------|-------:|
| t0 | A.1, B.1–B.5 | N=6 uniqueness, B₁ set, bootstrap | 35 |
| t1 | O.1 | Monodromy σ₁·σ₀·σ∞ = id, Mon order 72 | 17 |
| t2 | F.3–F.7 | Quantum numbers n, ℓ, K from dessin | 58 |
| t3 | D.2–D.8, I.6 | Spectrum, Kirchhoff, φ-zero, spectral bridge | 34 |
| t4 | E.8, V.1–V.6 | CKM: UST → Wolfenstein, pulls vs PDG 2025 | 26 |
| t5 | X.100–X.130 | PMNS angles from cross-ratios, NuFIT 6.1 IC23 | 29 |
| t6 | G.0–G.8 | Mass formula: LO+NLO, sign window, h derivation | 22 |
| t7 | H.1–H.3 | α⁻¹, μ = 6π⁵(…), G prediction | 15 |
| t8 | X.97, W.4, X.48 | Gap 3 closure: trace formula chain | 31 |
| t9 | C.8, K.9, V.10 | Information geometry, Moonshine, linear code | 23 |
| t10 | X.219 | **sin²θ_W = 3/13**, tower C₂, unified denom 13 | 15 |
| t11 | X.218, X.224 | **\|sinδ\|=1, sinδ=−1**, \|U\|² matrix, J² | 25 |
| t12 | X.225, X.226 | **CR = master equation**, resultant deg 42=N·L | 15 |
| t13 | X.183, X.202, X.228 | **Tower structure**, JUNO, N=6 maximality | 31 |
| t14 | X.256, X.263 | **Directed operators**, isospectrality breaking | 27 |
| t15 | X.267, X.272 | **Golden bridge** q₅ = q_φ·q₃ − 3, Lucas | 29 |
| t16 | X.280, X.281 | **CRT grand unification**, Schur spectral | 34 |
| | | **Total** | **508** |

Tiers t10–t13 cover v1728 additions (CP violation, Weinberg angle, tower, CR master).
Tiers t14–t16 cover directed operators, golden bridge, and CRT unification (S288–S291).

---

## Verification Notebook (SageMath, legacy)

`LD_verification.sage` — 90 independent checks (SageMath implementation, paper v8).

```bash
sage LD_verification.sage
```

---

## Interactive Dashboard

See: [zinchenko-denis.github.io/LD-explorer](https://zinchenko-denis.github.io/LD-explorer/)

---

## License

MIT

## Citation

```bibtex
@misc{zinchenko2026ld,
  author = {Zinchenko, Denis D.},
  title = {1728: The Standard Model from $X_0(6)$},
  year = {2026},
  doi = {10.5281/zenodo.19520240},
  publisher = {Zenodo}
}
```
