# Case A — Lennard-Jones liquid

**Level:** beginner → intermediate. **Resources:** laptop, Python/NumPy/SciPy/Matplotlib, no external engine.  
**Execution:** Python short run executed; see [validation](../../VALIDATION_REPORT.md). The optional LAMMPS variant is an **unexecuted teaching input**.

## Objectives and model

Connect forces and integration to structure and dynamics. Diagnose energy conservation, temperature, RDF normalization, unwrapping and diffusion regimes.

The original Python model contains 108 equal-mass LJ particles from a 3×3×3 FCC construction at $\rho^*=0.75$, preparation target $T^*=1.2$, periodic cubic boundaries and **force-shifted** cutoff $r_c=2\sigma$. Reduced units set $\epsilon=\sigma=m=k_B=1$. BAOAB Langevin preparation fixes the center-of-mass momentum subspace; velocity Verlet advances NVE production. There is no tail correction. These choices define a teaching fluid, not an asserted experimental argon model.

Read [MD](../../docs/02_classical_md.md), [potentials](../../docs/03_force_fields.md) and [analysis](../../docs/17_trajectory_analysis.md).

## Prepare and run

From repository root after installing `requirements.txt`:

```bash
python -m scripts.run_lj --equil 1000 --steps 4000 --out outputs/lj
python -m scripts.analyze_lj outputs/lj/trajectory.npz
```

The default production is $4000\times0.004=16$ reduced time units. Initial FCC order must relax before interpreting a fluid; inspect preparation and increase its length when needed. The seed is recorded. Use separate output directories for independent runs.

Outputs: `trajectory.npz` (unwrapped positions, velocities, thermo, box, saved interval, preparation trace), `thermo.csv`, `run_manifest.json`, `rdf.csv`, `dynamics.csv` and diagnostic SVG/PNG. The [notebook](../../notebooks/02_lj_structure_and_dynamics.ipynb) runs a smaller example directly.

## Validation and expected plots

1. Check conservation of total momentum and finite-difference forces using the unit tests.
2. Compare $\Delta t=0.004$ and $0.002$ at equal physical duration and initial seed; change step counts accordingly.
3. Plot NVE energy per particle and temperature; do not impose an NVT constant-temperature expectation on NVE.
4. Plot finite-$N$ RDF with the proper ideal reference, then compare independent blocks.
5. Plot MSD on linear and logarithmic axes; identify ballistic, caged and possible diffusive intervals.
6. Compare cell sizes and independent seeds before quoting bulk transport.

A structured RDF and bounded energy are qualitative expectations of an appropriate run, **not supplied numerical acceptance targets**. Do not fit the entire MSD blindly. There is no automatically “correct” diffusion coefficient in this repository. For longer runs, choose and report a fit interval and apply the estimator independently to blocks/replicas.

## Troubleshooting and interpretation

Large drift: verify force/cutoff consistency, timestep and initial contacts. A flat MSD from wrapped positions is an analysis error. Remaining lattice order can reflect inadequate equilibration or conditions, not necessarily a code failure. The all-pairs Python engine scales poorly; move larger simulations to an optimized engine after reproducing the Hamiltonian.

The optional `in.lammps` uses **potential-shifted** `lj/cut`, whose force discontinuity and Hamiltonian differ from the Python force-shifted model. It is a separate demonstration, not a cross-code energy match. With LAMMPS installed:

```bash
lmp -in tutorials/01_lennard_jones/in.lammps
```

Run in an empty working directory if you want to isolate LAMMPS outputs.

**Exercise submission:** one conservation plot, one RDF, one MSD, a timestep comparison, a replica/block uncertainty plan and a paragraph stating which physical claims remain unresolved.

**Literature:** [Verlet](../../references.md#verlet1967), [Rahman](../../references.md#rahman1964), [Gravelle tutorials](../../references.md#gravelle2025). Our inputs and algorithms are original.
