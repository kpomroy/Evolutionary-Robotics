import constants as c
import copy
import os
from solution import SOLUTION

class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        self.nextAvailableID = 0
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
            if(self.parents[i].fitness > self.children[i].fitness):
                self.parents[i] = self.children[i]

    def Print(self):
        print("")
        for i in self.parents:
            print(str(i) + "Parent fitness: " + str(self.parents[i].fitness) + " Child fitness: " + str(self.children[i].fitness))
        print("")

    def Show_Best(self):
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

        for i in range(c.populationSize * (c.numberOfGenerations+1)):
            if(i != bestSolution.myID):
                os.system("rm brain" + str(i) + ".nndf")

    def Evaluate(self, solutions):
        for i in range(c.populationSize):
            solutions[i].Start_Simulation("DIRECT")
        for i in range(c.populationSize):
            solutions[i].Wait_For_Simulation_To_End()
    