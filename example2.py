"""
For my project, I am interested in seeing how the fitnesses of the mutants
affect the loss of the D allele. For example, let's see the distribution of how many 
generations it takes for the D allele to reach 80% of its initial frequency with
neutral mutations (you could then choose different fitness values to see how the
distribution changes)

Ideally, I would choose 0% (allele loss). But with realistic parameters, like
mutation rates of order 10e-5, the simulation is very long.
"""

import wrightfisher as wf

N = 10000
murates = (1, 1, 1, 1, 1, 1)
fitnesses = (1, 1, 1, 1)
nSamples = 1000 #number of populations
nb_generations =[] #it will store how many generations it took for each population

populations = [wf.Population(N, murates, fitnesses) for i in range(nSamples)]

for sample in populations:
    sample_generations = 0
    while sample.pop['ND'] > N*0.8:
        sample.evolve(1)
        sample_generations += 1
    nb_generations.append(sample_generations)

wf.plt.xlabel('Number of generations before D decays to 0.8N')
wf.plt.ylabel('Number of populations')
wf.plt.hist(nb_generations) #very basic histogram without any parameters
wf.plt.show() #to see the plot if you run this in a terminal
