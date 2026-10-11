# Validation report

**Release:** 0.1.0 · **Date:** 11 October 2026 · **Scope:** educational source archive prepared for review and subsequent GitHub publication.

The supplied checks support the correctness of specific algorithms, file relationships and short execution paths. They do **not** establish converged material properties, experimental agreement, production-engine equivalence or independent human peer review. No live GitHub publication is claimed.

## Completed checks

| Area | Result | Evidence and limits |
|---|---|---|
| Numerical utilities | **14 tests passed** | Force gradients, force-cutoff continuity, pair-force balance, Verlet reversibility, timestep error, RDF normalization, ballistic MSD, known diffusion slope, AR(1) correlation, blocking, ideal GCMC, KMC occupations, analytical WHAM and disconnected-overlap rejection, and resource arithmetic. Several checks share one test method. |
| Python syntax | **Passed** | All bundled Python source parsed, including original engine drivers. Parsing an optional driver does not execute its engine. |
| Notebooks | **6 notebooks, 19 code cells executed without error** | Fresh Python namespace per notebook; stdout and figures retained in the notebook files. [Execution record](validation/executed_notebooks/execution_report.json). |
| Notebook transport | **Environment-dependent; not validated** | Standard Jupyter kernel attempts encountered local socket-binding restrictions. The explicit `inprocess` runner executed the Python cells without Jupyter messaging. Interactive kernel behavior and the GitHub Actions job remain to be checked in a normal environment. |
| Documentation | **Offline checks passed** | Local file links, reference anchors, README navigation, fenced blocks and TeX brace balance. Exact current counts are in [repository checks](validation/repository_checks.json). |
| Math parsing | **411 expressions parsed without errors** | 50 display and 361 inline expressions parsed with KaTeX 0.16.22. [Machine record](validation/math_parsing.json). This is syntax validation, not a live GitHub rendering test. |
| Scientific equations | **Algebraic and dimensional review completed** | [Equation review](EQUATION_REVIEW.md) separates analytic reasoning, numerical evidence and untested theory. Sources accompany the relevant equations. |
| Bibliography | **76 BibTeX records parsed; 75 DOI identities audited** | Authors, titles, venues, dates and available volume/page/article metadata checked through Crossref and selected publisher records. One textbook entry uses publisher metadata without a DOI. [Metadata audit](data/reference_audit.json). |
| External resource URLs | **36 HTTP successes; 1 access restriction** | 37 unique non-DOI Markdown URLs checked. Oxford's book page returned HTTP 403; its live reachability was not confirmed. DOI metadata verification is separate from publisher-page accessibility. [URL record](validation/external_links.json). |
| Figures | **12 original teaching figures generated and visually inspected** | Editable SVG, PNG previews and [generator](scripts/make_figures.py). Analytic/schematic curves are labeled. Actual-run diagnostic plots were also inspected. |
| Third-party assets | **Source/modified hashes checked** | Pinned RASPA3 source commit, MIT notice, modifications and bundled hashes are recorded in [provenance](data/THIRD_PARTY_PROVENANCE.json). |

## Executed tutorials and exact scope

| Case | Executed configuration | What this establishes |
|---|---|---|
| A — LJ liquid | 108 particles; reduced density 0.75; preparation target temperature 1.2; timestep 0.004; 500 preparation and 1,000 NVE production steps; seed 2026 | Force-shifted Python run and energy, temperature, RDF, MSD and VACF analysis complete. Four reduced production time units are insufficient to assert a converged transport coefficient. |
| B — LJ solid | 108 FCC particles; reduced density 0.95; preparation target temperature 0.15; timestep 0.004; 500 preparation and 1,000 NVE steps | Short vibrational/structural diagnostics complete. No phase diagram, melting point or thermal expansion is measured. |
| B — copper/ASE | ASE 3.29.0; 108 Cu atoms; EMT; lattice parameter 3.6 Å; target 300 K; timestep 1 fs; 100 preparation and 300 production steps | Calculator/integrator/trajectory path complete. EMT is explicitly identified; this is not an EAM validation or an equilibrium lattice determination. |
| C — water/NaCl | OpenMM 8.6.1 CPU, 2 threads; 883 waters and 4 ions, 2,653 atoms; nominal 3 nm initial box; nominal 0.15 M salt request; 300 K/1 bar preparation; 250 NPT preparation and 500 fixed-cell NVE steps; timestep 2 fs | Preparation, constraints, PME, production and analysis complete. Actual composition is discrete. The final production PDB records the final preparation cell. A 1 ps production run does not converge electrolyte structure, diffusion or experimental density. |
| D — ideal-gas GCMC | Analytical Poisson-limit unit test and notebook sampler | Number-distribution acceptance factors and rejected-state sampling are checked for the ideal model. This does not validate atomistic MFI adsorption. |
| E — water geometry | Original 8-water, 24-atom ordered configuration generated; CP2K sections statically checked | Geometry preparation and section balance complete. The starting geometry is not an equilibrated liquid and has not been relaxed by CP2K. |
| F — umbrella/WHAM | 13 double-well windows; 20,000 attempted MC steps/window, including 4,000 burn steps/window; seed 2026; WHAM converged numerically in 267 iterations | Toy point estimate, histogram overlap and comparison with the analytic one-dimensional potential generated. Estimator iteration convergence is not statistical convergence or a molecular rate measurement. |

Small retained outputs under `validation/` make these execution claims inspectable. Run manifests state model, settings and limitations. Short wall times in LJ manifests describe this particular diagnostic execution; they are not portable hardware benchmarks. Machine-specific OpenMM checkpoints and serialized force-field parameter files are omitted from the distributable evidence; the original driver regenerates them from the installed, named force field.

## Unexecuted examples and static-input checks

- **LAMMPS:** `tutorials/01_lennard_jones/in.lammps` is an **unexecuted teaching input**. Its potential-shifted cutoff differs from the Python force-shifted model, as documented. No cross-engine numerical agreement is claimed.
- **RASPA3:** the MFI methane input is an **unexecuted teaching input**. JSON parsing, provenance and the seed keyword in the pinned source were checked. The force-field file explicitly sets a 12 Å cutoff. The public orthorhombic unit cell is 20.022 × 19.899 × 13.383 Å; doubling each axis gives a shortest length of 26.766 Å, exceeding twice the cutoff. ASE parsed 96 Si and 192 O in the unit cell, with a CIF space-group interpretation warning. This parser result does not certify the engine's symmetry expansion or a completed simulation. Inspect the RASPA3 startup structure and recognized input settings before production.
- **CP2K:** `minimize.inp` and `water.inp` are **unexecuted teaching inputs**. Balanced sections and generated geometry were checked; basis-file availability, executable schema, SCF convergence, geometry relaxation and dynamics were not. The PBE setup deliberately omits dispersion, with that model limitation stated in the tutorial.
- **MLIP:** Case G is a guided model-audit exercise. No model weights, learned-force trajectory or training result is bundled or claimed.
- **Other methods:** the reactive MD, coarse-graining, CPMD and PIMD chapters teach theory and protocol design; they are not represented as completed engine calculations. No viscosity or thermal-conductivity trajectory analysis was executed.

## Reproduce the checks

From the extracted repository root, use a clean Python environment:

```bash
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -v
python scripts/check_repository.py
python scripts/run_notebooks.py --mode inprocess --output outputs/notebook_check
```

Use the default notebook `--mode kernel` to test full Jupyter execution when local kernels/sockets are available. The optional `--external` checker performs fresh URL requests and reports access restrictions separately. Install optional engine packages according to the case READMEs. [requirements-tested.txt](requirements-tested.txt) records the numerical package versions used here; it is not a guarantee of compatibility on every operating system. [Environment metadata](validation/environment.json) provides the recorded Python/platform versions.

The exact short engine commands were:

```bash
python -m scripts.run_lj --phase liquid --equil 500 --steps 1000 --out validation/liquid_smoke
python -m scripts.analyze_lj validation/liquid_smoke/trajectory.npz
python -m scripts.run_lj --phase solid --equil 500 --steps 1000 --out validation/solid_smoke
python -m scripts.analyze_lj validation/solid_smoke/trajectory.npz
python tutorials/02_solid_state_md/run_ase_copper.py --equil 100 --steps 300 --out validation/copper_smoke
python tutorials/03_water_electrolyte/run_openmm.py --equil 250 --steps 500 --out validation/water_smoke --platform CPU --threads 2
python tutorials/03_water_electrolyte/analyze.py validation/water_smoke
python -m scripts.free_energy --steps 20000 --burn 4000 --out validation/free_energy_smoke
```

Before regenerating retained evidence, copy it or choose another output directory. Engine trajectories can differ across builds, platforms and random-number implementations even with the same seed; numerical and statistical comparison is more meaningful than requiring identical binary files.

## Literature and interpretation boundaries

The [source review](SOURCE_REVIEW.md) explains how official educational resources informed the course structure. The [application chapter](docs/21_research_applications.md) distinguishes primary applications, foundational methods and reviews, and does not invent capacities, rates, diffusion constants or speedups. Bibliographic discrepancies, including online/print years and the Gravelle article number, are recorded rather than silently conflated.

The documented checks distinguish **algorithmic correctness, numerical convergence, statistical convergence, model accuracy and experimental agreement**. The last four are system-specific investigations, not consequences of a passing unit-test suite. The [scientific checklist](CHECKLIST.md) remains a worksheet for future users rather than a claim that every research criterion has been met by the short examples.

## Archive and publication checks

The deliverable contains source, licensed public teaching assets, modest diagnostic outputs and original figures. It excludes credentials, private research data, installed software, external binaries and pretrained weights. Contact placeholders remain exactly as requested. [GITHUB_RELEASE.md](GITHUB_RELEASE.md) supplies the proposed description, topics and first commit message. Review and human scientific feedback are appropriate before using this course as an authoritative research protocol.
