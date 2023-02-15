from simulation import SIMULATION


simulation = SIMULATION()
simulation.run()

""" import constants as c
import numpy as np
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time



#create vectors of sensor values
backLegSensorValues = np.zeros(c.steps)
frontLegSensorValues = np.zeros(c.steps)

#back leg sinusoidal target angles vector (motor command vector)
backLegTargetAngles = np.zeros(c.steps)
backLegRadianValues = np.linspace(0, 2*np.pi, num = c.steps)
for i in range(c.steps):
    backLegTargetAngles[i] = c.backLegAmplitude*np.sin(c.backLegFrequency*backLegRadianValues[i] + c.backLegPhaseOffset)

#front leg sinusoidal target angles vector (motor command vector)
frontLegTargetAngles = np.zeros(c.steps)
frontLegRadianValues = np.linspace(0, 2*np.pi, num = c.steps)
for i in range(c.steps):
    frontLegTargetAngles[i] = c.frontLegAmplitude*np.sin(c.frontLegFrequency*frontLegRadianValues[i] + c.frontLegPhaseOffset)


#plot sinusoidal values
targetAnglesData = open("data/targetAngleValues.npy", "wb")
np.save(targetAnglesData, backLegTargetAngles)
targetAnglesData.close()

'''
frontLegTargetAnglesData = open("data/frontLegTargetAngleValues.npy", "wb")
np.save(frontLegTargetAnglesData, frontLegTargetAngles)
frontLegTargetAnglesData.close()
exit()
'''



print(backLegSensorValues)
print(frontLegSensorValues)

backLegData= open("data/backLegSensorValues.npy", "wb")
np.save(backLegData, backLegSensorValues)
backLegData.close()

frontLegData = open("data/frontLegSensorValues.npy", "wb")
np.save(frontLegData, frontLegSensorValues)
frontLegData.close()


p.disconnect() """