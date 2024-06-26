# Wright-Fisher simulations
## Overview
Simulations to analyze evolution of a simplified haploid population.
For more details about Wright-Fisher simulations or population genetics, see :
* [Tutorial on Theoretical Population Genetics, Joe Felsenstein
](https://web.archive.org/web/20221001021120/https://evolution.gs.washington.edu/gecco.pdf) (PDF)
* [Pop Gen 1, Taylor](https://web.archive.org/web/20181030051958/http://www2.hawaii.edu/~taylor/z652/PopGen1.pdf) (PDF)
* https://fla.st/2nUg1tJ (PDF, dead link 🤷)
* [Evolution in Finite Population, Jeff Gore](https://www.youtube.com/watch?v=KLrPm-BEEOI) (Youtube video)
* [Statistical Physics of Biological Evolution, J Krug](https://www.youtube.com/watch?v=XSdg2U_TYyY&list=PLMxUX2BDY1G1p_925tb9zVTjar6bRYLjs) (Youtube playlist)

The ressources go into much more detail than what I used to create this repo.

This is a customized Wright-Fisher model. I used it to analyze specific hypothetical populations with:
* 4 possible alleles at a locus of interest (D, E, A, F)
* Discrete time steps (generations)
* At t=0, allele D is fixed and can mutate to E, A or F
* Mutants E, A and F can mutate between each others with a custom pattern

Evolutionary forces considered are mutation, drift and selection. They are modeled as:

* Mutation: random number from a poisson distribution with mutation rate as mean
* Drift + selection: coupled as a weighted(selection), normalized(so sum of frequencies stays 1), multinomial sampling(4 outcomes/alleles).

## Use code
I suggest using anaconda and jupyter-notebook.

Import the main class from ```wrightfisher.py``` to instantiate a population and track the changes over time through the class methods. The files ```example1.py``` and ```example2.py``` are use cases.

Instantiating the class requires: population size, mutation rates tuple and selection coefficient tuple (in the form of (1 + s)). The tuples indexes are important and should be given in a certain order.

Example:
clone the repo > go to the directory > $pip3 install numpy matplotlib > open jupyter-notebook
```python3
import wrightfisher as wf

N = 10000
murates = (1, 1, 1, 1, 1, 1) # (muE, muA, muF, muFA, muFE, muAE)
fitnesses = (1, 1, 1, 1) # (wD, wE, wA, wF) all neutral in this case

#Plot frequency trajectory for 100 generations
pop_instance1 = wf.Population(N, murates, fitnesses)
pop_instance1,freqTraj(100)

#Evolve population for 100 generations and see details
pop_instance2 = wf.Population(N, murates, fitnesses)
pop_instance2.evolve(100)
print(pop_instance2.pop['ND']), pop_instance2.pop['NA'], pop_instance2.pop['NE'], pop_instance2.pop['NF'])
```
