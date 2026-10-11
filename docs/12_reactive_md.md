# 12. Reactive molecular dynamics

**Level:** advanced. **Outcomes:** understand bond-order models; design chemical validation rather than relying on element coverage.

## Definition and foundation

Reactive MD propagates atoms using a model that allows bonding environments to change. [ReaxFF](../references.md#van_duin2001) is a prominent fitted reactive force-field family; [Senftle et al.](../references.md#senftle2016) review its development and applications. Other bond-order and learned potentials can also be reactive within their supported domains.

A schematic energy decomposition is

```math
U=U_{\rm bond}(\{BO_{ij}\})+U_{\rm angle}+U_{\rm torsion}
+U_{\rm over/under}+U_{\rm vdW}+U_{\rm Coulomb}+\cdots .
```

Bond orders $BO_{ij}$ depend continuously on geometry and model parameters. This is a conceptual decomposition, not a complete implementation formula. Forces must differentiate all dependencies. ReaxFF parameter files define a particular model; “ReaxFF” alone is not a reproducible force-field specification.

Many implementations equilibrate charges at each step. A typical charge model minimizes an energy involving electronegativities, hardnesses and screened pair interactions subject to total-charge conservation. Convergence tolerance and treatment of distant fragments can affect results. Charge equilibration is not a direct solution of the electronic Schrödinger equation.

## Algorithm and assumptions

Prepare a parameter set covering the relevant elements **and chemistry**, minimize inappropriate contacts, converge charge solving, then integrate with a sufficiently small timestep and appropriate thermal control. Save bond-order or geometry information at intervals fast enough to distinguish persistent products from transient contacts.

The fitted energy surface approximates a selected quantum/experimental training domain. Reactive capability does not certify every oxidation state, coordination number, reaction path or high-temperature condition. Standard fixed-topology force fields cannot generally be substituted when bond changes are central.

## Validation hierarchy

Start with isolated or small-system energetics: structures, binding, dissociation curves, relative products and barriers. Add condensed-phase structure, density and transport where relevant. Then compare the specific reaction network against independent electronic-structure information. Check charge artifacts, energy conservation, parameter file version and timestep.

Heating a system until reactions occur can reveal possible pathways but does not establish ambient rates. Accelerated temperature changes mechanisms and entropic weighting. A visually plausible product is not proof of a correct barrier.

## Applications, resources and scale

Combustion-like chemistry, oxidation, decomposition and solid–liquid reactions are plausible application classes when the parameterization supports them. The original hydrocarbon ReaxFF paper demonstrates a specific chemistry; transferring its claims to oxides or aqueous interfaces would be unjustified.

LAMMPS includes reactive models subject to installed packages. CP2K and other engines support particular classical/reactive workflows. Verify charge-solver and force-field compatibility. Neighbor searches, many-body interactions and iterative charges cost more than simple LJ; smaller timesteps increase step counts. Workstation pilots and CPU/GPU cluster production are reasonable planning categories, with acceleration depending on the exact styles. Spatial/temporal reach is model- and implementation-dependent.

## Analysis and uncertainty

Define a bond with threshold **and persistence**, inspect threshold sensitivity, track atom conservation and charge, construct species/event counts, and distinguish transient recrossings. Species definitions based only on one distance can misclassify thermal fluctuations. Reaction rates require stationary conditions, enough independent events and an appropriate kinetic model.

Chemical model error often dominates statistical error. Compare selected event geometries and competing channels with DFT, or use enhanced sampling for barriers. Do not report narrow event-count error bars as total predictive uncertainty.

## Guided exercise

Design validation for water dissociation at an oxide surface. List at least three small reference reactions, two condensed-phase checks and a false-positive reaction diagnostic.

**Checkpoint:** include dissociation/recombination energetics, proton-transfer barriers, adsorption configurations, bulk/surface hydration structure, and persistence/recrossing checks. Element coverage is only a first filter.

**Sources:** [ReaxFF foundation](../references.md#van_duin2001), [review](../references.md#senftle2016). See [validation decision trees](22_validation_common_mistakes.md).
