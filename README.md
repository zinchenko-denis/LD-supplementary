# LD Framework — Supplementary Materials

Computational verification and interactive dashboard for:

**"Discrete Scale Invariance and the Particle Mass Spectrum: A Number-Theoretic Framework"**
Denis D. Zinchenko
Paper DOI: [10.5281/zenodo.19046582](https://doi.org/10.5281/zenodo.19046582)

## Verification Notebook

`LD_verification.sage` — 82 independent checks of all numerical claims in the paper.

**Usage:**

    sage LD_verification.sage

**Requirements:** SageMath >= 9.5, NumPy

**Key feature — Blind Prediction Mode (Section 18):**
Starting from only two inputs (electron mass + N=6), the notebook computes
all 12 particle masses ab initio and compares with PDG 2024.
No experimental mass data enters the computation chain.
Result: 10 predictions, RMS = 1.49%, all within 3%.

## Output

    82 PASSED / 0 FAILED / 82 TOTAL
    *** ALL CHECKS PASSED ***

## Interactive Dashboard

`dashboard/` — React/TypeScript visualization of all LD predictions.
12 tabs: Constants, Dessin, B1 Set, Mass Spectrum, delta-K, CKM, alpha, Neutrinos, Gravity, Tests, Status.

## License

MIT

## Citation

    @misc{zinchenko2026ld,
      author = {Zinchenko, Denis D.},
      title = {Discrete Scale Invariance and the Particle Mass Spectrum},
      year = {2026},
      doi = {10.5281/zenodo.19046582},
      publisher = {Zenodo}
    }
