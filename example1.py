"""
Example of how the class can be used
Track the frequency of the D allele for 100 generations
Let's use parameters such that all mutations are neutral and very frequent
"""

import wrightfisher as wf

pop_example1 = wf.Population(1000, (0.5, 0.5, 0.5, 0.5, 0.5, 0.5), (1, 1, 1, 1))
pop_example1.freqTraj(100)
#wf.plt.show() #might need this if you run from terminal
