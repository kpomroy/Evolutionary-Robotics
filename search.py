from parallelHillClimber import PARALLEL_HILL_CLIMBER
import os

os.system("rm finalProject/fitness/quadrupedFitness.csv")
for i in range(5):
    phc = PARALLEL_HILL_CLIMBER()
    phc.Evolve()
    phc.Show_Best(i)