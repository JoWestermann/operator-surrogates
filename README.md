# Tutorial on Operator Surrogates

This repository provides a self-contained, pedagogical comparison of surrogate modelling approaches for parametric PDEs. The central example is a one-dimensional parametric diffusion problem whose coefficient field is drawn from a log-normal random field; a secondary example covers the Lotka-Volterra predator-prey ODE. Three surrogate families are implemented and compared: sparse-grid (Smolyak) interpolation, PCA-Net (a feedforward network operating in a PCA-reduced latent space), and the Fourier Neural Operator (FNO). The central goal is to understand the cost-accuracy trade-off of the different surrogate architectures.

## Notebooks

- **`0_Diffusion.ipynb`**: Introduces the parametric diffusion problem and defines `Grid` and `Diffusion`, the latter implementing a finite-difference solver used throughout as the ground-truth operator.
- **`1_Representation.ipynb`**: Defines the input encoder `Encoder` (log-normal field via a truncated sine-series expansion) and the PCA-based output decoder `Decoder` (analysis/synthesis via empirical PCA modes).
- **`2_Interpolation.ipynb`**: Builds a Smolyak sparse-grid interpolant over the encoded parameter domain using the `smolyax` library. Studies convergence as a function of the number of quadrature nodes and the coefficient decay rate.
- **`3_PCANet.ipynb`**: Trains `FFN`, a fully connected network mapping encoded inputs to encoded outputs in the PCA latent space. Studies convergence as a function of training set size.
- **`4_FNO.ipynb`**: Trains `FNO`, a Fourier Neural Operator that maps the full diffusion-coefficient field directly to the solution field without PCA compression.
- **`5_Comparison.ipynb`**: Compares the cost-accuracy trade-off of all three surrogates, considering data generation, training or setup, and online evaluation as separate cost contributions.
- **`6_IVP.ipynb`**: Applies sparse-grid interpolation and feedforward networks to approximate the solution of the Lotka-Volterra initial value problem, a finite-dimensional problem that requires no encoder or decoder.

### Notebook Imports

All Python classes are defined inline in the notebook where the corresponding methods are first discussed, so the code and its explanation always appear together. When a later notebook needs to reuse a class, the relevant code cells are marked with `#EXPORT`. `importer.py` provides `import_notebook(path, globals())`, which reads the target notebook, executes only the `#EXPORT`-marked cells, and makes the resulting names available in the caller's namespace.

## Installation and Usage

Navigate to the repository root. 

Optionally, create a virtual environment:

```bash
python -m venv .venv && source .venv/bin/activate
```

Install the necessary dependencies:

```bash
pip install -r requirements.txt
```

Launch jupyter lab to explore the notebooks:

```bash
jupyter lab
```
