# Wright-Fisher simulations
Simulations to analyze evolution of a simplified haploid population.
For more details about Wright-Fisher simulations or population genetics, see :
* https://bit.ly/2Lf3FWc (PDF)
* https://bit.ly/2OQsBpp (PDF)
* https://fla.st/2nUg1tJ (PDF)
* https://bit.ly/2wi1CLx (Youtube video)
* https://bit.ly/2PqDgYM (Youtube playlist)

The ressources go into much more detail than what I used to create this repo.

This is a customized Wright-Fisher model. I used it to analyze specific hypothetical populations with:
* 4 possible alleles at a locus of interest (D, E, A, F)
* Discrete time steps (generations)
* At t=0, allele D is fixed and can mutate to E, A or F
* Mutants E, A and F can mutate between each others with a custom pattern

Evolutionary forces considered are mutation, drift and selection. They are modeled as:

* Mutation: random number from a poisson distribution with mutation rate as mean
* Drift + selection: coupled as a weighted(selection coefficient), normalized(so sum of frequencies stays 1), multinomial sampling(4 outcomes/alleles).


