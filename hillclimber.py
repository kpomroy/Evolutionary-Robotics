import constants as c
import copy
from solution import SOLUTION

class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()
        

    def Evolve(self):
        self.parent.Evaluate()
        for currentGeneration in range(0, c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate()
        self.Print()
        self.Select()
        

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        print("self.parent.fitness: " + str(self.parent.fitness))
        print("self.child.fitness: " + str(self.child.fitness))
        if(self.parent.fitness > self.child.fitness):
            self.parent = self.child
            print("parent replaced by child")

    def Print(self):
        print("")
        print("Parent fitness: " + str(self.parent.fitness) + " Child fitness: " + str(self.child.fitness))
        print("")