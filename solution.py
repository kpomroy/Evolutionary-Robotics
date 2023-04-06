import constants as c
import numpy as numpy
#from generate import Create_World
import os as os
import pyrosim.pyrosim as pyrosim
import random
import time

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        #create matrix of weights between 0 and 1
        self.weights = numpy.zeros(shape = (c.numSensorNeurons,c.numMotorNeurons))
        for i in range(c.numSensorNeurons):
            for j in range(c.numMotorNeurons):
                self.weights[i][j] = numpy.random.rand()
        #scale weights to be between -1 and 1
        self.weights = self.weights * 2 - 1


    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " 2&>1 &")

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)
        fitnessFile = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(fitnessFile.read())
        #print(self.fitness)
        fitnessFile.close()
        os.system("rm fitness" + str(self.myID) + ".txt")
        

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[5,5,.5] , size=[1,1,1])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")

        #torso
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[2,1,1])


        #front leg
        pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [-1,0,1], jointAxis = "0 1 0")

        pyrosim.Send_Cube(name="FrontLeg", pos=[-0.5,0,0] , size=[1,0.2,0.2])


        #front lower leg
        pyrosim.Send_Joint(name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", position = [-1,0,0], jointAxis = "0 1 0")

        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])


        #left front leg
        pyrosim.Send_Joint(name = "Torso_LeftFrontLeg" , parent= "Torso" , child = "LeftFrontLeg" , type = "revolute", position = [-.5,-0.5,1], jointAxis = "1 0 0")

        pyrosim.Send_Cube(name="LeftFrontLeg", pos=[0,-0.5,0] , size=[0.2,1,0.2])

        #left front lower leg
        pyrosim.Send_Joint(name = "LeftFrontLeg_LeftFrontLowerLeg" , parent= "LeftFrontLeg" , child = "LeftFrontLowerLeg" , type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")

        pyrosim.Send_Cube(name="LeftFrontLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])

        #left back leg
        pyrosim.Send_Joint(name = "Torso_LeftBackLeg" , parent= "Torso" , child = "LeftBackLeg" , type = "revolute", position = [0.5,-0.5,1], jointAxis = "1 0 0")

        pyrosim.Send_Cube(name="LeftBackLeg", pos=[0,-0.5,0] , size=[0.2,1,0.2])

        #left back lower leg
        pyrosim.Send_Joint(name = "LeftBackLeg_LeftBackLowerLeg" , parent= "LeftBackLeg" , child = "LeftBackLowerLeg" , type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")

        pyrosim.Send_Cube(name="LeftBackLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])

        #back leg
        pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1,0,1], jointAxis = "0 1 0")

        pyrosim.Send_Cube(name="BackLeg", pos=[0.5,0,0] , size=[1,0.2,0.2])

        #back lower leg
        pyrosim.Send_Joint(name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", position = [1,0,0], jointAxis = "0 1 0")

        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])


        #right front leg
        pyrosim.Send_Joint(name = "Torso_RightFrontLeg" , parent= "Torso" , child = "RightFrontLeg" , type = "revolute", position = [-.5,0.5,1], jointAxis = "1 0 0")

        pyrosim.Send_Cube(name="RightFrontLeg", pos=[0,0.5,0] , size=[0.2,1,0.2])


        #right front lower leg
        pyrosim.Send_Joint(name = "RightFrontLeg_RightFrontLowerLeg" , parent= "RightFrontLeg" , child = "RightFrontLowerLeg" , type = "revolute", position = [0,1,0], jointAxis = "1 0 0")

        pyrosim.Send_Cube(name="RightFrontLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])

        #right back leg
        pyrosim.Send_Joint(name = "Torso_RightBackLeg" , parent= "Torso" , child = "RightBackLeg" , type = "revolute", position = [.5,0.5,1], jointAxis = "1 0 0")

        pyrosim.Send_Cube(name="RightBackLeg", pos=[0,0.5,0] , size=[0.2,1,0.2])

        #right back lower leg
        pyrosim.Send_Joint(name = "RightBackLeg_RightBackLowerLeg" , parent= "RightBackLeg" , child = "RightBackLowerLeg" , type = "revolute", position = [0,1,0], jointAxis = "1 0 0")

        pyrosim.Send_Cube(name="RightBackLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1, linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2, linkName = "BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 3, linkName = "FrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 4, linkName = "FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 5, linkName = "RightFrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 6, linkName = "RightFrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 7, linkName = "LeftFrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 8, linkName = "LeftFrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 9, linkName = "RightBackLeg")
        pyrosim.Send_Sensor_Neuron(name = 10, linkName = "RightBackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 11, linkName = "LeftBackLeg")
        pyrosim.Send_Sensor_Neuron(name = 12, linkName = "LeftBackLowerLeg")

        pyrosim.Send_Motor_Neuron( name = 13, jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 14, jointName = "FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 15, jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 16, jointName = "BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 17, jointName = "Torso_RightFrontLeg")
        pyrosim.Send_Motor_Neuron( name = 18, jointName = "RightFrontLeg_RightFrontLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 19, jointName = "Torso_LeftFrontLeg")
        pyrosim.Send_Motor_Neuron( name = 20, jointName = "LeftFrontLeg_LeftFrontLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 21, jointName = "Torso_RightBackLeg")
        pyrosim.Send_Motor_Neuron( name = 22, jointName = "RightBackLeg_RightBackLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 23, jointName = "Torso_LeftBackLeg")
        pyrosim.Send_Motor_Neuron( name = 24, jointName = "LeftBackLeg_LeftBackLowerLeg")

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+c.numSensorNeurons , weight = self.weights[currentRow][currentColumn])

        pyrosim.End()

    def Mutate(self):
        randRow = random.randint(0,c.numSensorNeurons-1)
        randCol = random.randint(0,c.numMotorNeurons-1)
        self.weights[randRow][randCol] = random.random() * 2 - 1
  
    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID