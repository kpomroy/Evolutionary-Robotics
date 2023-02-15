import constants as c
import numpy as np
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from robot import ROBOT
from world import WORLD
import time

class SIMULATION:
    def __init__(self):
        self.world = WORLD()
        self.robot = ROBOT()

        physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        #set gravity
        p.setGravity(0,0,-9.8)

        #read in the robot body to robotId object
        self.robotId = p.loadURDF("body.urdf")

        #prepare to simulate sensors
        pyrosim.Prepare_To_Simulate(self.robotId)

         #create floor
        self.planeId = p.loadURDF("plane.urdf")

        #read in the world described in box.sdf
        p.loadSDF("world.sdf")

    #deconstructor
    def __del__(self):
        p.disconnect()

    def run(self):
        #loop to keep simulated environment open
        for i in range(c.steps):
            #print (i)
            
            p.stepSimulation()
            time.sleep(1/1000)

'''
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
                '''

    