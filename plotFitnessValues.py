import constants as c
from cProfile import label
import numpy as np
from collections import OrderedDict
import matplotlib.pyplot as matplotlib

#quadruped
quadruped = {}
quadFitnessValues = np.load('finalProject/fitness/quadruped0.npy')
#print(quadFitnessValues)

#hexapod 1
hex1FitnessValues = np.load('finalProject/fitness/hexapod10.npy')
#print(hex1FitnessValues)

#hexapod 2
hex20FitnessValues = np.load('finalProject/fitness/hexapod20.npy')
print(hex20FitnessValues)
hex21FitnessValues = np.load('finalProject/fitness/hexapod21.npy')
print(hex21FitnessValues)
'''
hex22FitnessValues = np.load('finalProject/fitness/hexapod22.npy')
hex23FitnessValues = np.load('finalProject/fitness/hexapod23.npy')
hex24FitnessValues = np.load('finalProject/fitness/hexapod24.npy')
hex25FitnessValues = np.load('finalProject/fitness/hexapod25.npy')
hex26FitnessValues = np.load('finalProject/fitness/hexapod26.npy')
hex27FitnessValues = np.load('finalProject/fitness/hexapod27.npy')
hex28FitnessValues = np.load('finalProject/fitness/hexapod28.npy')
hex29FitnessValues = np.load('finalProject/fitness/hexapod29.npy')
'''

#octopod 1
oct1FitnessValues = np.load('finalProject/fitness/octopod10.npy')
#print(oct1FitnessValues)

#octopod 2
oct20FitnessValues = np.load('finalProject/fitness/octopod20.npy')
oct21FitnessValues = np.load('finalProject/fitness/octopod21.npy')
oct22FitnessValues = np.load('finalProject/fitness/octopod22.npy')
oct23FitnessValues = np.load('finalProject/fitness/octopod23.npy')
oct24FitnessValues = np.load('finalProject/fitness/octopod24.npy')
oct25FitnessValues = np.load('finalProject/fitness/octopod25.npy')
oct26FitnessValues = np.load('finalProject/fitness/octopod26.npy')
oct27FitnessValues = np.load('finalProject/fitness/octopod27.npy')
oct28FitnessValues = np.load('finalProject/fitness/octopod28.npy')
oct29FitnessValues = np.load('finalProject/fitness/octopod29.npy')

#STORE MEANS
#quadruped
meanQuad = np.mean(quadFitnessValues, axis = 0)

#hexapod 1
meanHex1 = np.mean(hex1FitnessValues, axis = 0)

#hexapod 2
meanHex20 = np.mean(hex20FitnessValues, axis = 0)
meanHex21 = np.mean(hex21FitnessValues, axis = 0)
'''
meanHex22 = np.mean(hex22FitnessValues, axis = 0)
meanHex23 = np.mean(hex23FitnessValues, axis = 0)
meanHex24 = np.mean(hex24FitnessValues, axis = 0)
meanHex25 = np.mean(hex25FitnessValues, axis = 0)
meanHex26 = np.mean(hex26FitnessValues, axis = 0)
meanHex27 = np.mean(hex27FitnessValues, axis = 0)
meanHex28 = np.mean(hex28FitnessValues, axis = 0)
meanHex29 = np.mean(hex29FitnessValues, axis = 0)
'''
#octopod 1
meanOct1 = np.mean(oct1FitnessValues, axis = 0)

#octopod 2
meanOct20 = np.mean(oct20FitnessValues, axis = 0)
meanOct21 = np.mean(oct21FitnessValues, axis = 0)
meanOct22 = np.mean(oct22FitnessValues, axis = 0)
meanOct23 = np.mean(oct23FitnessValues, axis = 0)
meanOct24 = np.mean(oct24FitnessValues, axis = 0)
meanOct25 = np.mean(oct25FitnessValues, axis = 0)
meanOct26 = np.mean(oct26FitnessValues, axis = 0)
meanOct27 = np.mean(oct27FitnessValues, axis = 0)
meanOct28 = np.mean(oct28FitnessValues, axis = 0)
meanOct29 = np.mean(oct29FitnessValues, axis = 0)


print("mean quad")
print(meanQuad)
print("mean hex1")
print(meanHex1)
print("mean hex20")
print(meanHex20)
print("mean hex21")
print(meanHex21)
print("mean oct1")
print(meanOct1)
print("mean oct20")
print(meanOct20)

# average the means from different runs

#hex2
'''
meanHex2All = np.zeros(c.numberOfGenerations)
for i in range(c.numberOfGenerations):
   meanHex2All[i] = (meanHex20[i] + meanHex21[i] + meanHex22[i] + meanHex23[i] + meanHex24[i] + meanHex25[i] + meanHex26[i] + meanHex27[i] + meanHex28[i] + meanHex29[i])/10

print("mean hex2 all")
print(meanHex2All)
'''
meanOct2All = np.zeros(c.numberOfGenerations)
for i in range(c.numberOfGenerations):
   meanOct2All[i] = (meanOct20[i] + meanOct21[i] + meanOct22[i] + meanOct23[i] + meanOct24[i] + meanOct25[i] + meanOct26[i] + meanOct27[i] + meanOct28[i] + meanOct29[i])/10

print("mean Oct2 all")
print(meanOct2All)

matplotlib.plot(meanQuad, label = "quadruped", linewidth = 1)
matplotlib.plot(meanHex1, label = "hexapod1", linewidth = 2.5) 
#matplotlib.plot(meanHex2All, label = "hexapod2", linewidth = 2.5)
matplotlib.plot(meanOct1, label = "octopod1", linewidth = 4)
matplotlib.plot(meanOct2All, label = "octopod2", linewidth = 4)

matplotlib.xlabel("Generation")
matplotlib.ylabel("Average Fitness")
matplotlib.title("Average fitness over 10 runs")



handles, labels = matplotlib.gca().get_legend_handles_labels()
by_label = OrderedDict(zip(labels, handles))
matplotlib.legend(by_label.values(), by_label.keys())

#add legend to plot
#matplotlib.legend()

#show plot
matplotlib.show()