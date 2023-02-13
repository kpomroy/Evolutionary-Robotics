import constants as c
import numpy as np
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time



physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

#set gravity
p.setGravity(0,0,-9.8)
 #create floor
planeId = p.loadURDF("plane.urdf")

#read in the world described in box.sdf
p.loadSDF("world.sdf")

#read in the robot body to robotId object
robotId = p.loadURDF("body.urdf")

#prepare to simulate sensors
pyrosim.Prepare_To_Simulate(robotId)

#create vectors of sensor values
backLegSensorValues = np.zeros(c.steps)
frontLegSensorValues = np.zeros(c.steps)

#back leg sinusoidal target angles vector (motor command vector)
backLegTargetAngles = np.zeros(c.steps)
backLegRadianValues = np.linspace(0, 2*np.pi, num = c.steps)
for i in range(c.steps):
    backLegTargetAngles[i] = c.backLegAmplitude*np.sin(c.backLegFrequency*backLegRadianValues[i] + c.backLegPhaseOffset)

#front legsinusoidal target angles vector (motor command vector)
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

#loop to keep simulated environment open
for i in range(c.steps):
    p.stepSimulation()
    time.sleep(1/1000)

    #create backleg touch sensor at each iteration of loop
    #save to backLegSensorValues array
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")

    #create frontleg touch sensor
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    #create motors for joints
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_BackLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = backLegTargetAngles[i],
        maxForce = 50)

    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_FrontLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = frontLegTargetAngles[i],
        maxForce = 50)

print(backLegSensorValues)
print(frontLegSensorValues)

backLegData= open("data/backLegSensorValues.npy", "wb")
np.save(backLegData, backLegSensorValues)
backLegData.close()

frontLegData = open("data/frontLegSensorValues.npy", "wb")
np.save(frontLegData, frontLegSensorValues)
frontLegData.close()


p.disconnect()