import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        #create empty array for sensor values
        self.values = np.zeros(c.steps)

    def Get_Value(self, time):
        #create touch sensor at each iteration of loop
        #save to this.values array
        self.values[time] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        print(time)
        if (time == 999):
            print (self.values)
        