# 13. Coarse-grained molecular dynamics

**Level:** intermediate → advanced. **Outcomes:** understand mapping, effective interactions and the loss of dynamical information.

## Definition and physical foundation

Coarse graining replaces selected atomistic degrees of freedom by fewer sites. A bead can represent several atoms, a monomer or another collective unit. It increases accessible length/time scales by reducing particle count and smoothing fast degrees of freedom, at the cost of detail and often transferability.

[Kremer–Grest](../references.md#kremer1990) provides a bead-spring polymer-melt example; [Martini](../references.md#marrink2007) and [Martini 3](../references.md#souza2021) illustrate broader chemically motivated mappings. These models have different targets and should not be mixed merely because both use beads.

## Mapping and effective free energy

For atomistic coordinates $\mathbf r$ and mapping $\mathbf R=M(\mathbf r)$, define the mapped canonical probability by integrating out hidden variables:

```math
e^{-\beta W(\mathbf R)}\propto
\int e^{-\beta U(\mathbf r)}
\delta[M(\mathbf r)-\mathbf R]\,d\mathbf r .
```

$W$ is an effective free energy at the specified state, not generally a transferable pair potential. It can depend on temperature, density and composition and contains many-body effects. Approximating it by simple bonded and pair terms sacrifices some representability.

For an isolated coordinate with a stated measure, $W=-k_BT\ln p+C$. In a dense fluid, directly using $-k_BT\ln g(r)$ as a pair potential ignores mediated many-body correlations. Iterative Boltzmann inversion, force matching and relative-entropy approaches optimize different objectives.

## Algorithms and assumptions

Choose a mapping, identify target observables, fit or select compatible interactions, simulate, and compare against held-out atomistic or experimental information. Validate density, structure and thermodynamics beyond the fitting target. If restoring atomistic detail, backmapping requires extra structural reconstruction and relaxation; lost coordinates cannot be uniquely recovered.

A polymer bead-spring Hamiltonian can combine excluded-volume pair interactions and finite-extensible nonlinear elastic bonds. Such bonds prevent arbitrary extension but do not model a particular chemical bond vibration. Chain crossing and entanglement preservation depend on the interaction parameters and timestep.

## Time, resources and software

Eliminating degrees of freedom changes friction and memory. A smoother potential often speeds motion, but a single time-rescaling factor need not correct all observables, temperatures or compositions. Rigorous projected dynamics can include memory kernels and stochastic terms. Ordinary Newtonian propagation under a fitted $W$ is a modeling choice.

Laptop bead models are useful teaching systems; large polymer/membrane assemblies can benefit from GPUs and clusters. Fewer sites can reduce cost and permit larger timesteps, but actual savings require benchmarks. LAMMPS, GROMACS and OpenMM support appropriate coarse-grained models with compatible parameters.

## Applications and analysis

For polymer melts, measure chain size, end-to-end relaxation, Rouse modes, segment MSD and entanglement-sensitive quantities. For membranes, assess area, thickness, composition structure and diffusion. Do not infer atom-specific hydrogen bonds from beads that have no such resolution.

The Kremer–Grest study addresses dynamics across chain-length regimes in its model; its conclusions are not a universal calibration of chemical-polymer timescales. Martini applications establish useful organization patterns within a defined mapping and parameterization, not all-atom reaction chemistry.

## Guided exercise

Map groups of consecutive atoms in a polymer trajectory to centers of mass. Compare the mapped RDF and chain radius of gyration with a proposed bead model. If both agree but diffusion does not, identify two explanations.

**Checkpoint:** equilibrium targets do not determine friction/memory or a universal kinetic mapping. Check chain topology, density, temperature, and slow relaxation as well as the lost bath degrees of freedom.

**Sources:** [Kremer–Grest](../references.md#kremer1990), [Martini](../references.md#marrink2007), [Martini 3](../references.md#souza2021), [Frenkel–Smit](../references.md#frenkel2023).
