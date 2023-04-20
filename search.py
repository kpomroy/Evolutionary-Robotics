from parallelHillClimber import PARALLEL_HILL_CLIMBER
import time

for i in range(5):
    phc = PARALLEL_HILL_CLIMBER()
    phc.Evolve()
    phc.Show_Best(i)