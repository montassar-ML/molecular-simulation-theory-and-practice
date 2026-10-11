# Case B — Solid-state molecular dynamics

**Level:** intermediate. **Resources:** laptop CPU; core Python requirements, optional ASE.  
**Execution:** short LJ solid and ASE/EMT copper runs executed. They are diagnostic, not converged thermophysical predictions.

## Objectives and theory

Build an FCC lattice, distinguish vibration from diffusion, examine temperature dependence and understand why a potential must suit the bonding. A crystal's atoms fluctuate around sites; a short plateau in MSD does not by itself prove long-time stability. Thermal expansion requires equilibrium pressure/volume treatment, not simply measuring motion in a fixed cell.

Two complementary models are supplied: an original force-shifted LJ FCC solid and an optional copper crystal using ASE's EMT calculator. LJ is a generic solid; EMT includes a many-body metallic description with its own limited domain.

## Run the reduced-unit solid

From repository root:

```bash
python -m scripts.run_lj --phase solid --equil 1000 --steps 4000 --out outputs/solid
python -m scripts.analyze_lj outputs/solid/trajectory.npz
```

Default: 108 particles, $\rho^*=0.95$, preparation target $T^*=0.15$, $r_c=2\sigma$, $\Delta t^*=0.004$. The file structure matches [Case A](../01_lennard_jones/README.md). Compare `--temperature 0.15` and `--temperature 0.30` with independent output paths and enough preparation. Do not infer a melting point from two short runs.

## Optional copper example

```bash
python -m pip install ase
python tutorials/02_solid_state_md/run_ase_copper.py --out outputs/copper
```

The script builds 108 copper atoms at an illustrative lattice parameter 3.6 Å, uses ASE EMT, prepares with Langevin dynamics and switches to 1 fs NVE production. Outputs: `copper.traj`, `thermo.csv`, `run_manifest.json`. Record the installed ASE version. A fixed 3.6 Å lattice is a starting assumption, not an optimized 300 K lattice parameter. The package may report temperature with a degree count that differs from a center-of-mass-constrained estimator; compare kinetic energy using explicit conventions.

## Analysis and convergence

Plot total energy versus time, temperature, lattice displacement distribution, RDF and cell-size dependence. For copper, read the ASE trajectory and calculate displacements relative to reference sites after removing collective translation. Check atom identity and periodic images before assigning site motion.

Vary timestep at constant duration, lattice parameter/pressure treatment, temperature, cell size and sampling length. A structural classifier can help distinguish FCC, defect and disordered environments, but threshold sensitivity matters. Thermal expansion and mechanical stability require stress/volume evidence.

## Interpretation and troubleshooting

Unstable lattice: inspect potential applicability, volume, integration and initial velocities. Excess drift: test timestep and force consistency. Apparent melting can be finite-size superheating or poor preparation; an abrupt visual disordering is not a thermodynamic coexistence calculation.

**Exercise:** compare solid and liquid MSDs at the same number of saved frames. Explain why equal frame counts do not mean equal independent information. For the metal, propose validation against lattice, elastic or defect data outside the fitting target.

**Literature:** [Daw–Baskes EAM](../../references.md#daw1984) explains metallic many-body modeling; it is not the source of ASE EMT parameters. Cite [ASE](../../references.md#larsen2017) for the executed tool and its [EMT documentation](https://ase.gitlab.io/ase/ase/calculators/emt.html) for the calculator. [Statistical uncertainty](../../docs/18_uncertainty_convergence.md).
