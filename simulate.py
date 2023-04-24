from simulation import SIMULATION
import createBody
import sys
import os

try:
    directOrGUI = sys.argv[1]
except:
    directOrGUI = "GUI"

try:
    solutionID = sys.argv[2]
except:
    solutionID = 0

os.system('python3 createBody.py')

simulation = SIMULATION(directOrGUI, solutionID)

simulation.Run()
simulation.Get_Fitness()
#print("FINISHED")
