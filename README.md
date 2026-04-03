# LD Framework — Supplementary Materials

Computational verification, proof companion, and supplementary materials for:

**"Discrete Scale Invariance and the Standard Model Mass Spectrum: A Number-Theoretic Framework from X₀(6)"**
Denis D. Zinchenko
Paper DOI: [10.5281/zenodo.19393365](https://doi.org/10.5281/zenodo.19393365)

---

## Proof Companion

`LD_proof_companion.md` — self-contained catalog of all LD results (sessions S42–S217).

**Contents:**
- Every theorem, derivation, observation, and conjecture with epistemic markers:
  `[THM]`, `[DER]`, `[OBS]`, `[CONJ]`, `[DEAD]`
- Full derivation chains with dependencies
- 90+ closed (dead) directions with session references
- Corrections log (Z-log) tracking all errors found and fixed
- Open questions with current status (Gap 9 active, Gap 3 closed)

**Sections:** O (Monodromy) · A (Foundation) · B (B₁ set) · C (Dessin) · D (Spectrum/Kirchhoff) · E (CKM) · F (Mass formula) · G (δK formula) · H (α formula and ring) · I (Neutrinos/PMNS) · J (L-functions) · K (Hauptmodul) · L (Scattering matrix) · M (Selberg/splitting) · N (QTC — cos² derivation) · R (Cuspal regulators) · S (DFT barriers) · T (Operator search) · U (Genus-0 additivity) · V (CKM derived) · W (Modular forms) · X (Dead directions) · Y (Open questions) · Z (Corrections)

---

## Verification Notebook

`LD_verification.sage` — 87 independent checks of all numerical claims in the paper.

**Usage:**

```
sage LD_verification.sage
```

**Requirements:** SageMath >= 9.5, NumPy

**Output:**

```
87 PASSED / 0 FAILED / 87 TOTAL
*** ALL CHECKS PASSED ***
```

---

## Interactive Dashboard

See: [zinchenko-denis.github.io/LD-explorer](https://zinchenko-denis.github.io/LD-explorer/)

---

## License

MIT

## Citation

```
@misc{zinchenko2026ld,
  author = {Zinchenko, Denis D.},
  title = {Discrete Scale Invariance and the Standard Model Mass Spectrum:
           A Number-Theoretic Framework from $X_0(6)$},
  year = {2026},
  doi = {10.5281/zenodo.19393365},
  publisher = {Zenodo}
}
```
