import math
import numpy as np
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import random
import time

PI = math.pi

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
backLegSensorValues = np.zeros(500)
frontLegSensorValues = np.zeros(500)

#loop to keep simulated environment open
for i in range(500):
    p.stepSimulation()
    time.sleep(1/100)

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
        targetPosition = random.uniform(-PI/2, PI/2),
        maxForce = 50)

    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_FrontLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = random.uniform(-PI/2, PI/2),
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