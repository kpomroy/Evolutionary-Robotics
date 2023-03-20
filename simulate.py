from simulation import SIMULATION
import sys

try:
    directOrGUI = sys.argv[1]
except:
    directOrGUI = "GUI"

try:
    solutionID = sys.argv[2]
except:
    solutionID = 0

simulation = SIMULATION(directOrGUI, solutionID)

simulation.Run()
simulation.Get_Fitness()
#print("FINISHED")
