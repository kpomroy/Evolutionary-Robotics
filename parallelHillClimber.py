import constants as c
import copy
import os
from solution import SOLUTION

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        self.nextAvailableID = 0
        self.parent = {}
        for i in range (c.populationSize):
            self.parent[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1
        

    def Evolve(self):
        for i in range(c.populationSize):
            self.parent[i].Start_Simulation("DIRECT")
        for i in range(c.populationSize):
            self.parent[i].Wait_For_Simulation_To_End()

        #self.parent.Evaluate("GUI")
        for currentGeneration in range(0, c.numberOfGenerations):
            #if(currentGeneration == 0):
            self.Evolve_For_One_Generation()


    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        # self.child.Evaluate("DIRECT")
        # self.Print()
        # self.Select()
        

    def Spawn(self):
        self.children = {}
        for i in range (len(self.parent)):
            self.children[i] = copy.deepcopy(self.parent[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1
        

    def Mutate(self):
        for i in range (len(self.parent)):
            self.children[i].Mutate()

    def Select(self):
        if(self.parent.fitness > self.child.fitness):
            self.parent = self.child

    def Print(self):
        print("")
        print("Parent fitness: " + str(self.parent.fitness) + " Child fitness: " + str(self.child.fitness))
        print("")

    def Show_Best(self):
        pass
        #self.parent.Evaluate("GUI")