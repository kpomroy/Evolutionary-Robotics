import constants as c
import copy
import numpy as np
import os
from solution import SOLUTION

class PARALLEL_HILL_CLIMBER:

    def __init__(self, iteration):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        #create matrix for fitnesses
        self.fitnessMat = np.zeros(shape = (c.populationSize,c.numberOfGenerations))
        self.nextAvailableID = 0
        self.generation = 0
        self.iteration = iteration
        self.parents = {}
        for i in range (c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1
        

    def Evolve(self):
        self.Evaluate(self.parents)
        #self.parent.Evaluate("GUI")
        for currentGeneration in range(0, c.numberOfGenerations):
            #if(currentGeneration == 0):
            self.Evolve_For_One_Generation()


    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()
        

    def Spawn(self):
        self.children = {}
        for i in self.parents:
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1
        

    def Mutate(self):
        for i in self.parents:
            self.children[i].Mutate()

    def Select(self):
        for i in self.parents:
            self.fitnessMat[i][self.generation] = self.children[i].fitness
            if(self.parents[i].fitness > self.children[i].fitness):
                #replace parent with child if more fit
                self.parents[i] = self.children[i]
                #delete brain file
                deleteID = self.parents[i].myID
                os.system("rm brain" + str(deleteID) + ".nndf")
            else:
                #delete brain file
                deleteID = self.children[i].myID
                os.system("rm brain" + str(deleteID) + ".nndf")
        self.generation+=1

        if(self.generation == c.numberOfGenerations-1):
            np.savetxt('finalProject/fitness/octopod2' + str(self.iteration) + '.txt' ,self.fitnessMat, fmt = '%.4f')

    def Print(self):
        allFitnessFile = open("finalProject/fitness/octopod2Fitness" + str(self.iteration) + ".csv", "a")
        if (os.stat("finalProject/fitness/octopod2Fitness.csv").st_size == 0):
            allFitnessFile.write("Family,Parent,Child\n")
        for i in self.parents:
            allFitnessFile.write(str(i) + "," + str(round(self.parents[i].fitness), 4) + "," + str(round(self.children[i].fitness, 4)) + "\n")
        allFitnessFile.close()

    def Show_Best(self, num):
        #initialize lowest (best) fitness
        bestFitness = self.parents[0].fitness
        bestSolution = self.parents[0]
        for i in self.parents:
            if self.parents[i].fitness < bestFitness:
                bestFitness = self.parents[i].fitness
                bestSolution = self.parents[i]
        bestSolution.Start_Simulation("GUI")

        print("")
        print("Best fitness:", bestFitness)
        print("Best solution ID: " + str(bestSolution.myID))
        print("i: " + str(num))
        print("")
        #move best brain to brains folder to save
        os.system('mv brain' + str(bestSolution.myID) + '.nndf finalProject/brains/octopod2/brain' + str(num) + '.nndf')
        
    def Evaluate(self, solutions):
        for i in range(c.populationSize):
            solutions[i].Start_Simulation("DIRECT")
        for i in range(c.populationSize):
            solutions[i].Wait_For_Simulation_To_End()
    