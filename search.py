from parallelHillClimber import PARALLEL_HILL_CLIMBER
import os

os.system("rm finalProject/fitness/octopod1Fitness.csv")
for i in range(1):
    phc = PARALLEL_HILL_CLIMBER(i)
    phc.Evolve()
    phc.Show_Best(i)