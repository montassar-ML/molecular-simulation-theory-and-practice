# Start here

Start with a scientific question: a structure, a thermodynamic average, a transport coefficient, a reaction pathway or a rate. Different questions require different methods and evidence.

## Choose an entry path

| Background | First reading | First practical activity |
|---|---|---|
| New to molecular simulation | Chapters 1–5 and conventions | Notebook 1, then LJ Case A |
| Experimental scientist | Chapters 2, 17, 18 and application guide | Inspect LJ plots and write what each can establish |
| Existing MD user | Ensembles, thermostats, uncertainty and validation | Audit one of your analysis conventions |
| DFT/materials researcher | BOMD/CPMD, GCMC, enhanced sampling and MLIPs | CP2K input audit and method-selection protocol |

## Your first session

1. Read [units and conventions](docs/CONVENTIONS.md).
2. Install core dependencies following [README](README.md#quick-start).
3. Run the unit tests, then [Case A](tutorials/01_lennard_jones/README.md).
4. Open its diagnostic figure and distinguish raw observations from unverified interpretations.
5. Explain why an RDF can be computed from equilibrium MC but diffusion generally cannot.

Core Python exercises require no license or institutional computer. Optional engines are installed separately from their official sources.

## Notebooks and Google Colab

There are six [notebooks](notebooks/README.md). They import the repository's transparent utility code, so retain the complete folder structure. In Colab, upload the ZIP, extract it, change the working directory to its top-level folder, install `requirements-dev.txt` and open/run notebook cells with that directory available. No published GitHub clone URL is assumed before you publish this repository.

The delivered notebooks include recorded outputs from socket-free execution of their Python cells. Standard Jupyter-kernel startup was blocked in the build environment; the [report](VALIDATION_REPORT.md) distinguishes this from a full interactive-kernel test.

## What is a good result?

A successful program exit is only the beginning. A good exercise submission states the Hamiltonian and ensemble, shows a diagnostic, estimates relevant uncertainty and explains one limitation. The course intentionally does not supply a numerical answer to “the correct diffusion coefficient” for a short toy run.

Proceed through [the roadmap](LEARNING_ROADMAP.md), using the chapter exercises and [checklist](CHECKLIST.md).
