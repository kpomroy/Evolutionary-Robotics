import os as os
from parallelHillClimber import PARALLEL_HILL_CLIMBER

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()

'''
for i in range(5):
    os.system("python3 generate.py")
    os.system("python3 simulate.py")
'''