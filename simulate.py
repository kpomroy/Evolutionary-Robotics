import pybullet as p
import time
import pybullet_data

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

#loop to keep simulated environment open
for i in range(5000):
    p.stepSimulation()
    time.sleep(1/60)

p.disconnect()