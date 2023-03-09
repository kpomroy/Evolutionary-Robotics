import numpy as numpy
from generate import Create_World
import os as os
import pyrosim.pyrosim as pyrosim
import random

class SOLUTION:
    def __init__(self):
        #create matrix of weights between 0 and 1
        self.weights = numpy.zeros(shape = (3,2))
        for i in range(3):
            for j in range(2):
                self.weights[i][j] = numpy.random.rand()
        #scale weights to be between -1 and 1
        self.weights = self.weights * 2 - 1

    def Evaluate(self):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("python3 simulate.py DIRECT")
        fitnessFile = open("fitness.txt", "r")
        self.fitness = fitnessFile.read()
        fitnessFile.close()
        

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[-2,2,0.5] , size=[1,1,1])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")

        pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[1,1,1])

        pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1,0,1])

        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5] , size=[1,1,1])

        pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2,0,1])

        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5] , size=[1,1,1])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")

        pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1, linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2, linkName = "FrontLeg")

        pyrosim.Send_Motor_Neuron( name = 3, jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4, jointName = "Torso_FrontLeg")

        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+3 , weight = self.weights[currentRow][currentColumn])

        pyrosim.End()

    def Mutate(self):
        randRow = random.randint(0,2)
        randCol = random.randint(0,1)
        self.weights[randRow][randCol] = random.random() * 2 - 1
  
