from cProfile import label
import numpy as np
from collections import OrderedDict
import matplotlib.pyplot as matplotlib

iteration = 0

quadFitnessValues = np.load('finalProject/fitness/quadruped0.npy')
hex1FitnessValues = np.load('finalProject/fitness/hexapod10.npy')
print(quadFitnessValues)
hex2FitnessValues = np.load('finalProject/fitness/hexapod20.npy')
print(quadFitnessValues)
oct1FitnessValues = np.load('finalProject/fitness/octopod10.npy')
print(quadFitnessValues)
oct2FitnessValues = np.load('finalProject/fitness/octopod20.npy')
print(quadFitnessValues)

meanQuad = np.mean(quadFitnessValues, axis = 0)
meanHex1 = np.mean(hex1FitnessValues, axis = 0)
meanHex2 = np.mean(hex2FitnessValues, axis = 0)
meanOct1 = np.mean(oct1FitnessValues, axis = 0)
meanOct2 = np.mean(oct2FitnessValues, axis = 0)
print("mean quad")
print(meanQuad)
print("mean hex1")
print(meanHex1)
print("mean hex2")
print(meanHex2)
print("mean oct1")
print(meanOct1)
print("mean oct2")
print(meanOct2)

for i in range(10):
   matplotlib.plot(meanQuad, label = "quadruped", linewidth = 1)
   matplotlib.plot(meanHex1, label = "hexapod1", linewidth = 2.5) 
   matplotlib.plot(meanHex2, label = "hexapod2", linewidth = 2.5)
   matplotlib.plot(meanOct1, label = "octopod1", linewidth = 4)
   matplotlib.plot(meanOct2, label = "octopod2", linewidth = 4)

matplotlib.xlabel("Generation")
matplotlib.ylabel("Average Fitness")



handles, labels = matplotlib.gca().get_legend_handles_labels()
by_label = OrderedDict(zip(labels, handles))
matplotlib.legend(by_label.values(), by_label.keys())

#add legend to plot
#matplotlib.legend()

#show plot
matplotlib.show()