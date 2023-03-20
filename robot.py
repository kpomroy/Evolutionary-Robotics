import constants as c
from motor import MOTOR 
import numpy as np
import os
import pybullet as p
import pybullet_data
from pyrosim.neuralNetwork import NEURAL_NETWORK
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR

class ROBOT:
    def __init__(self, solutionID):
        #read in the robot body to robot object
        self.robot = p.loadURDF("body.urdf")

        #prepare to simulate sensors
        pyrosim.Prepare_To_Simulate(self.robot)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

        self.nn = NEURAL_NETWORK("brain" + str(solutionID) + ".nndf")

        #delete brainID.nndf
        os.system("rm brain" + str(solutionID) + ".nndf")
        
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

        for neuronName in self.nn.Get_Neuron_Names():

            if self.nn.Is_Motor_Neuron(neuronName):

                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName.encode('ASCII')].Set_Value(self.robot, desiredAngle)

    def Think(self):
        
        self.nn.Update()
        #self.nn.Print()

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robot,0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        fitnessOut = open("fitness.txt", "w")
        fitnessOut.write(str(xCoordinateOfLinkZero))
        fitnessOut.close()
        
