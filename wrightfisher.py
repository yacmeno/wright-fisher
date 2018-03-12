# -*- coding: utf-8 -*-
"""
Wright-Fisher simulations with 4 alleles.
Selection, drift and mutations are considered.
This code is adapted to a project of mine and is not a 'general' WF model,
for example, not all possible mutations are considered.

I am interrested in studying the decay/disappearance of a genotype (D) 
that starts fixed in a population. The D genotype can mutate to 3 other 
different genotypes (E, A and F). And the mutants can mutate according to the
following scheme: F to A, F to E, A to F and A to E.

A generation is described as the population went through a round of mutation,
drift and selection. 
"""

import numpy as np
import matplotlib.pyplot as plt

class Population:
    """
    Instantiate as example_pop = population(N, murates, fitnesses) 
    where N is an integer and murates/fitnesses are tuples
    The indexes of the tuples are important and must be given like this:
        (muE, muA, muF, muFA, muFE, muAE)
        (wD, wE, wA, wF)
    The initial genotype D can mutate to 3 possible genotypes with rates mui
    The 3 mutants can mutate to another genotype with rates muij
    """
    def __init__(self, N, murates, fitnesses):
        """ 
        The initial population starts with the D genotype fixed
        The elements in murates are the mutations per genes per generation
        The elements in fitnesses is the relative fitnesses of the 4 genotypes 
        such that wD = 1 and wi = 1 + si where si is the selection coefficient
        which can be positive or negative
        """
        self.N = N
        self.murates = murates
        self.fitnesses = fitnesses
        self.pop = {'ND' : self.N, 'NE' : 0, 'NA' : 0, 'NF' : 0}
    
    def mutate(self):
        """
        The number of mutants in each generation is determined by sampling a 
        random number from a poisson distribution with mean equal to the
        mutation rate. Thus, mutation rates are mutations per gene per
        generation.
        
        The if conditions make sure we don't end up with negative individuals
        """
         #D that mutates to the other 3
        if self.pop['ND'] != 0:
            newE = np.random.poisson(self.murates[0], 1)
            if newE[0] > self.pop['ND']:
                newE[0] = self.pop['ND']
            self.pop['ND'] -= newE[0]
            self.pop['NE'] += newE[0]
        if self.pop['ND'] != 0:
            newA = np.random.poisson(self.murates[1], 1)
            if newA[0] > self.pop['ND']:
                newA[0] = self.pop['ND']
            self.pop['ND'] -= newA[0]
            self.pop['NA'] += newA[0]
        if self.pop['ND'] != 0:
            newF = np.random.poisson(self.murates[2], 1)
            if newF[0] > self.pop['ND']:
                newF[0] = self.pop['ND']
            self.pop['ND'] -= newF[0]
            self.pop['NF'] += newF[0]
        #The other 3 mutants that mutate
        if self.pop['NF'] != 0:
            newFA = np.random.poisson(self.murates[3], 1)
            if newFA[0] > self.pop['NF']:
                newFA[0] = self.pop['NF']
            self.pop['NF'] -= newFA[0]
            self.pop['NA'] -= newFA[0]
        if self.pop['NF'] != 0:
            newFE = np.random.poisson(self.murates[4], 1)
            if newFE[0] > self.pop['NF']:
                newFE[0] = self.pop['NF']
            self.pop['NF'] -= newFE[0]
            self.pop['NE'] += newFE[0]
        if self.pop['NA'] != 0:
            newAE = np.random.poisson(self.murates[5], 1)
            if newAE[0] > self.pop['NA']:
                newAE[0] = self.pop['NA']
            self.pop['NA'] -= newAE[0]
            self.pop['NE'] += newAE[0]

        
    def driftsel(self):
        """
        This method applies the forces of drift and selection to the population
        Both forces are coupled in a multinomial sampling with probability values (pvals)
        given by the frequency of each genotype weighted by its fitness such that
        each genotype has probability (Ni/N)wi/sum((Ni/N)wi)
        """
        frequencies = [self.pop['ND']/self.N, self.pop['NE']/self.N,
                       self.pop['NA']/self.N, self.pop['NF']/self.N] #cannot use [Ni/N for Ni in list(pop.values)]
        unweighted_pvals = [self.fitnesses[i]*frequencies[i] for i in range(len(self.fitnesses))] 
        pvals = [unweighted/sum(unweighted_pvals) for unweighted in unweighted_pvals]
        np.random.multinomial(self.N, pvals)
        newSizes = np.random.multinomial(self.N, pvals) #returns array[ND, NE, NA, NF]
        self.pop['ND'] = newSizes[0]
        self.pop['NE'] = newSizes[1]
        self.pop['NA'] = newSizes[2]
        self.pop['NF'] = newSizes[3]
    
    def evolve(self, g):
        """
        This will apply the rounds of mutations, drift, and selection g times,
        which represents the number of generations forward
        """
        for generation in range(g):
            self.mutate()
            self.driftsel()
            
    def freqTraj(self, nGen):
        """
        Plotting method to get the allele frequency trajectory 
        after nGen generations. In this project I focus on the D genotype decay
        but you can add arguments to plt.plot() to track any of the four alleles
        """
        x_axis = [i for i in range(nGen)]
        ND_history = [] 
        NE_history = []
        NA_history = []
        NF_history = []
    
        for generation_step in range(nGen):
            self.evolve(1)
            ND_history.append(self.pop['ND'])
            NE_history.append(self.pop['NE'])
            NA_history.append(self.pop['NA'])
            NF_history.append(self.pop['NF'])
        
        return plt.plot(x_axis, ND_history)


