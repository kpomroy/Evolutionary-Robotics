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
        # self.Select()
        

    def Spawn(self):
        self.children = {}
        for i in range (len(self.parents)):
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1
        

    def Mutate(self):
        for i in range (len(self.parents)):
            self.children[i].Mutate()

    def Select(self):
        if(self.parent.fitness > self.child.fitness):
            self.parent = self.child

    def Print(self):
        print("")
        for i in range (len(self.parents)):
            print("Parent fitness: " + str(self.parents[i].fitness) + " Child fitness: " + str(self.children[i].fitness))
        print("")

    def Show_Best(self):
        pass
        #self.parent.Evaluate("GUI")

    def Evaluate(self, solutions):
        for i in range(c.populationSize):
            solutions[i].Start_Simulation("DIRECT")
        for i in range(c.populationSize):
            solutions[i].Wait_For_Simulation_To_End()