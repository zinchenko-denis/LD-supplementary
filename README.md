# LD Framework — Supplementary Materials

Computational verification, proof companion, and supplementary materials for:

**"1728: The Standard Model from $X_0(6)$"**
Denis D. Zinchenko

- Paper v1728 (published 12 April 2026):
  [DOI 10.5281/zenodo.19520240](https://doi.org/10.5281/zenodo.19520240)
- Paper v9 (current snapshot): DOI to be assigned on Zenodo deposit.

> **Snapshot note.** This repository carries the public companion
> snapshot synchronised to the most recent paper release. Live work
> (working database, session journals, lessons learned, ongoing
> derivations) is maintained in a separate private repository and
> is not mirrored here.

---

## Proof Companion

`LD_proof_companion.md` — self-contained catalog of all LD results,
theorems, derivations, observations, conjectures, and closed (DEAD)
directions cited in the paper.

**Status markers used throughout:**

`[THM]`, `[THM-arith]`, `[THM-comb]`, `[THM-comp]` — verified;
`[DER]`, `[DER cond.]` — derived (≤1 selection step from a theorem,
optionally under a stated condition);
`[OBS]` — pattern without proof;
`[CONJ]` — conjecture (e.g. headline X.247c);
`[DEAD]` — closed direction (kept as part of the falsification record).

Star ratings ★1–★5 indicate confidence within each status class.

**Internal session markers** of the form `Source: SNNN` or
`post-SNNN` are preserved as a provenance trail: any claim can be
traced to the session that introduced or last modified it.

**Sections** (top-level):
O (Monodromy) · A (Foundation) · B (B₁ set) · C (Dessin) ·
D (Spectrum) · E (CKM) · F (Mass formula) · G (δK formula) ·
H (α, μ, G) · I (PMNS) · J (L-functions) · K (Hauptmodul) ·
L (Scattering) · M (Selberg) · N (QTC) · R (Regulators) ·
S (DFT) · T (Operator) · U (Genus-0) · V (CKM derived) ·
W (Modular forms) · X (Results X.1–X.4xx) · Y (Open) ·
Z (Corrections).

---

## Verification Suite (Python, v1728-era)

`verify/` — 508 independent checks across 17 tiers, using exact
arithmetic (no SageMath dependency).

**Usage:**

```bash
cd verify
pip install numpy sympy
python run_all.py          # all 17 tiers (508 checks)
python run_all.py t5       # only PMNS
python run_all.py t10 t11  # Weinberg angle + CP phase
```

**Requirements:** Python 3.10+, NumPy, SymPy.

**Scope.** The current verify suite was prepared for paper v1728
(published April 2026). It covers every numerical claim of v1728
across the tier table below. Tiers covering new v9 material will
be added with the v9 verification update; until then, this suite
is the authoritative cross-check of all v1728 numerical results
that are carried unchanged into v9.

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
| t10 | X.219 | sin²θ_W = 3/13, tower C₂, unified denom 13 | 15 |
| t11 | X.218, X.224 | \|sin δ\|=1, sin δ=−1, \|U\|² matrix, J² | 25 |
| t12 | X.225, X.226 | CR = master equation, resultant deg 42=N·L | 15 |
| t13 | X.183, X.202, X.228 | Tower structure, JUNO, N=6 maximality | 31 |
| t14 | X.256, X.263 | Directed operators, isospectrality breaking | 27 |
| t15 | X.267, X.272 | Golden bridge q₅ = q_φ·q₃ − 3, Lucas | 29 |
| t16 | X.280, X.281 | CRT grand unification, Schur spectral | 34 |
|      |              | **Total**                                | **508** |

---

## Verification Notebook (SageMath, legacy)

`LD_verification.sage` — 90 independent checks
(SageMath implementation, paper v8 baseline). Kept for reference.

```bash
sage LD_verification.sage
```

---

## Reviewer FAQ

`LD_reviewer_FAQ.md` — answers to common reviewer questions
(23 entries, v1728-era; carried into v9 unchanged where applicable).

---

## Derivation Chain Summary

`LD_derivation_chain.md` — high-level summary of the derivation
DAG: from N=6 uniqueness through mass formula, α, μ, CKM, and PMNS.

---

## Interactive Dashboard

See [zinchenko-denis.github.io/LD-explorer](https://zinchenko-denis.github.io/LD-explorer/)
for the interactive parameter explorer (v1728-era; v9 update planned).

---

## License

MIT (code and notebooks); CC BY 4.0 (companion text).

## Citation

```bibtex
@misc{zinchenko2026ld,
  author    = {Zinchenko, Denis D.},
  title     = {1728: The Standard Model from $X_0(6)$},
  year      = {2026},
  doi       = {10.5281/zenodo.19520240},
  publisher = {Zenodo}
}
```
