from parallelHillClimber import PARALLEL_HILL_CLIMBER
import os

os.system("rm finalProject/fitness/octopod1Fitness.csv")
for i in range(2):
    phc = PARALLEL_HILL_CLIMBER()
    phc.Evolve()
    phc.Show_Best(i)