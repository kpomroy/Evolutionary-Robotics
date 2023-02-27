import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        #create empty array for sensor values
        self.values = np.zeros(c.steps)

    def Get_Value(self, time):
        self.values[time] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        if (time == c.steps-1):
            print (self.values)

    def Save_Values(self):
        sensorData= open("data/" + self.linkName + ".npy", "wb")
        np.save(sensorData, self.values)
        sensorData.close()