# Case E — Small water Born–Oppenheimer MD

**Level:** advanced. **Resources:** CP2K with its basis/pseudopotential data; multicore workstation or cluster recommended.  
**Status:** **unexecuted teaching inputs**. Geometry generation was checked; no CP2K SCF, optimization or MD result is claimed.

## Objectives and model

Understand electronic force generation, SCF consistency, basis/grid convergence and why short AIMD cannot establish liquid transport.

The original generator places eight water molecules with deterministic randomized orientations in a 6.214 Å periodic cubic cell. This is an ordered starting configuration at approximately liquid-like number density, **not an equilibrated liquid**. The tiny cell is for input mechanics and convergence exercises.

The prepared input uses GPW PBE, GTH-PBE pseudopotentials, DZVP-MOLOPT-SR-GTH bases, 400 Ry density cutoff, 60 Ry relative cutoff, $10^{-7}$ SCF tolerance, Gamma-point sampling, classical nuclei, 0.5 fs steps and CSVR temperature control. These are explicit starting settings to test, not universally converged recommendations. Dispersion is deliberately omitted to keep the initial Hamiltonian transparent; quantitative water studies must justify functional and dispersion together.

## Prepare and execute when CP2K is available

From this tutorial directory:

```bash
python prepare.py
cp2k.psmp -i minimize.inp -o minimize.out
python extract_last_xyz.py water8_relax-pos-1.xyz water8_relaxed.xyz
cp2k.psmp -i water.inp -o water.out
```

Use the actual executable/MPI launcher for your installation. Ensure `BASIS_MOLOPT` and `GTH_POTENTIALS` are available through the configured CP2K data path or explicit correct paths. Basis/pseudopotential files are not redistributed.

Inspect optimization convergence before extracting a frame; the extractor does not assert convergence. The optimizer's trajectory filename follows standard CP2K project output conventions but should be checked in your run. Archive the original and relaxed coordinates separately. No completed calculation should be overwritten.

## Expected structure and interpretation

Inputs: `prepare.py`, `water8.xyz` after generation, `minimize.inp`, `water.inp`. User-generated outputs include logs, trajectory, energy and restart files. MD production length in the starter is only 200 steps = 0.1 ps. Treat it as a syntax/numerical diagnostic, not equilibrated liquid water.

Check each SCF convergence, electronic iteration counts, minimum separations, energy and temperature. Compare forces on fixed snapshots across cutoff, relative cutoff, basis and SCF tolerances before longer MD. Test 0.5 and 0.25 fs at equal simulated duration. For an NVE diagnostic remove thermostatting consistently and start from a prepared state.

## Analysis, cost and convergence

Plot potential/kinetic/total energy, temperature, SCF iterations and force differences. Larger cells and longer trajectories are necessary for meaningful RDFs, diffusion and hydrogen-bond statistics. A short cell's smooth RDF is not reliable bulk structure.

Measure elapsed electronic work and memory on this exact build. More atoms mean more basis functions, grids and matrix work, not only more pair distances. GPUs accelerate selected CP2K libraries and kernels; no speedup is assumed. [Resource worksheet](../../COMPUTATIONAL_RESOURCES.md).

**Troubleshooting:** missing basis names require compatible installed data; poor SCF convergence requires diagnosing electronic guesses, geometry and solver settings, not silently accepting failed steps. Heating can arise from electronic force noise or timestep error. A different functional may change water structure even when every numerical test passes.

**Exercise:** prepare a table separating fixed-geometry force convergence, NVE numerical drift, structural sampling and model accuracy. Which of these can the 0.1 ps input test?

**Literature:** [Quickstep](../../references.md#vandevondele2005), [CP2K](../../references.md#kuhne2020), [DFT water perspective](../../references.md#michaelides2016), [official AIMD tutorial](https://www.cp2k.org/exercises:common:aimd).
