import constants as c
from motor import MOTOR 
import numpy as np
import pybullet as p
import pybullet_data
from pyrosim.neuralNetwork import NEURAL_NETWORK
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR

class ROBOT:
    def __init__(self):
        #read in the robot body to robot object
        self.robot = p.loadURDF("body.urdf")

        #prepare to simulate sensors
        pyrosim.Prepare_To_Simulate(self.robot)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

        self.nn = NEURAL_NETWORK("brain.nndf")
        
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, time):
        for sensorName in self.sensors:
            self.sensors[sensorName].Get_Value(time)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, time):
        for motorName in self.motors:
            self.motors[motorName].Set_Value(self.robot, time)

    def Think(self):
        self.nn.Update()
        self.nn.Print()