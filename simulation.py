import constants as c
import motor
import numpy as np
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from robot import ROBOT
from world import WORLD
import time

class SIMULATION:
    def __init__(self, directOrGUI):
        self.directOrGUI = directOrGUI
        if (directOrGUI == "DIRECT"):
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        #set gravity
        p.setGravity(0,0,-9.8)

        self.world = WORLD()
        self.robot = ROBOT()

    #deconstructor
    def __del__(self):
        p.disconnect()

    def Run(self):
        #loop to keep simulated environment open
        for t in range(c.steps):
            #print(t)
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Think()
            self.robot.Act(t)
            if (self.directOrGUI == "GUI"):
                time.sleep(1/10000)

    def Get_Fitness(self):
        self.robot.Get_Fitness()