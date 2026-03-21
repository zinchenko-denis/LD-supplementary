# LD Framework — Supplementary Materials

Computational verification, proof companion, and interactive dashboard for:

**"Discrete Scale Invariance and the Particle Mass Spectrum: A Number-Theoretic Framework"**
Denis D. Zinchenko
Paper DOI: [10.5281/zenodo.19150365](https://doi.org/10.5281/zenodo.19150365)

---

## Proof Companion

`LD_proof_companion.md` — self-contained catalog of all LD results (sessions S42–S106).

**Contents:**
- Every theorem, derivation, observation, and conjecture with epistemic markers:
  `[THM]`, `[DER]`, `[OBS]`, `[CONJ]`, `[DEAD]`
- Full derivation chains with dependencies
- 150+ closed (dead) directions with session references
- Corrections log (Z-log) tracking all errors found and fixed
- Open questions with current status

**Sections:** A (Foundation) · B (B₁ set) · C (Dessin) · D (Spectrum/Kirchhoff) · E (CKM) · F (Mass formula) · G (δK formula) · H (α formula and ring) · I (Neutrinos/PMNS) · J (L-functions) · K (Hauptmodul) · L (Scattering matrix) · M (Selberg/splitting) · N (QTC — cos² derivation) · X (Dead directions) · Y (Open questions) · Z (Corrections)

---

## Verification Notebook

`LD_verification.sage` — 87 independent checks of all numerical claims in the paper.

**Usage:**

```
sage LD_verification.sage
```

**Requirements:** SageMath >= 9.5, NumPy

**Key feature — Blind Prediction Mode (Section 18):**
Starting from only two inputs (electron mass + N=6), the notebook computes
all 12 particle masses ab initio and compares with PDG 2024.
No experimental mass data enters the computation chain.
Result: 10 predictions, RMS = 1.49%, all within 3%.

## Output

```
87 PASSED / 0 FAILED / 87 TOTAL
*** ALL CHECKS PASSED ***
```

---

## Interactive Dashboard

`dashboard/` — React/TypeScript visualization of all LD predictions.
12 tabs: Constants, Dessin, B₁ Set, Mass Spectrum, δK, CKM, α, Neutrinos, Gravity, Tests, Status.

---

## License

MIT

## Citation

```
@misc{zinchenko2026ld,
  author = {Zinchenko, Denis D.},
  title = {Discrete Scale Invariance and the Particle Mass Spectrum:
           A Number-Theoretic Framework},
  year = {2026},
  doi = {10.5281/zenodo.19150365},
  publisher = {Zenodo}
}
```
