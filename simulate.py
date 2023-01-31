import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np

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

#create vector of sensor values
backLegSensorValues = np.zeros(100)


#loop to keep simulated environment open
for i in range(100):
    p.stepSimulation()
    time.sleep(1/60)

    #create backleg touch sensor at each iteration of loop
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    
outfile = open("data/BackLeg.npy", "w")
np.save(outfile)
outfile.close()
print(backLegSensorValues)

p.disconnect()