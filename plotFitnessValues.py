import constants as c
from cProfile import label
import numpy as np
from collections import OrderedDict
import matplotlib.pyplot as matplotlib

#LOAD NPY FITNESS FILES
#quadruped
quad0FitnessValues = np.load('finalProject/fitness/quadruped0.npy')
quad1FitnessValues = np.load('finalProject/fitness/quadruped1.npy')
quad2FitnessValues = np.load('finalProject/fitness/quadruped2.npy')
quad3FitnessValues = np.load('finalProject/fitness/quadruped3.npy')
quad4FitnessValues = np.load('finalProject/fitness/quadruped4.npy')
quad5FitnessValues = np.load('finalProject/fitness/quadruped5.npy')
quad6FitnessValues = np.load('finalProject/fitness/quadruped6.npy')
quad7FitnessValues = np.load('finalProject/fitness/quadruped7.npy')
quad8FitnessValues = np.load('finalProject/fitness/quadruped8.npy')
quad9FitnessValues = np.load('finalProject/fitness/quadruped9.npy')

#hexapod 1
hex10FitnessValues = np.load('finalProject/fitness/hexapod10.npy')
hex11FitnessValues = np.load('finalProject/fitness/hexapod11.npy')
hex12FitnessValues = np.load('finalProject/fitness/hexapod12.npy')
hex13FitnessValues = np.load('finalProject/fitness/hexapod13.npy')
hex14FitnessValues = np.load('finalProject/fitness/hexapod14.npy')
hex15FitnessValues = np.load('finalProject/fitness/hexapod15.npy')
hex16FitnessValues = np.load('finalProject/fitness/hexapod16.npy')
hex17FitnessValues = np.load('finalProject/fitness/hexapod17.npy')
hex18FitnessValues = np.load('finalProject/fitness/hexapod18.npy')
hex19FitnessValues = np.load('finalProject/fitness/hexapod19.npy')

#hexapod 2
hex20FitnessValues = np.load('finalProject/fitness/hexapod20.npy')
hex21FitnessValues = np.load('finalProject/fitness/hexapod21.npy')
hex22FitnessValues = np.load('finalProject/fitness/hexapod22.npy')
hex23FitnessValues = np.load('finalProject/fitness/hexapod23.npy')
hex24FitnessValues = np.load('finalProject/fitness/hexapod24.npy')
hex25FitnessValues = np.load('finalProject/fitness/hexapod25.npy')
hex26FitnessValues = np.load('finalProject/fitness/hexapod26.npy')
hex27FitnessValues = np.load('finalProject/fitness/hexapod27.npy')
hex28FitnessValues = np.load('finalProject/fitness/hexapod28.npy')
hex29FitnessValues = np.load('finalProject/fitness/hexapod29.npy')

#octopod 1
oct10FitnessValues = np.load('finalProject/fitness/octopod10.npy')
oct11FitnessValues = np.load('finalProject/fitness/octopod11.npy')
oct12FitnessValues = np.load('finalProject/fitness/octopod12.npy')
oct13FitnessValues = np.load('finalProject/fitness/octopod13.npy')
oct14FitnessValues = np.load('finalProject/fitness/octopod14.npy')
oct15FitnessValues = np.load('finalProject/fitness/octopod15.npy')
oct16FitnessValues = np.load('finalProject/fitness/octopod16.npy')
oct17FitnessValues = np.load('finalProject/fitness/octopod17.npy')
oct18FitnessValues = np.load('finalProject/fitness/octopod18.npy')
oct19FitnessValues = np.load('finalProject/fitness/octopod19.npy')

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
meanQuad0 = np.mean(quad0FitnessValues, axis = 0)
meanQuad1 = np.mean(quad1FitnessValues, axis = 0)
meanQuad2 = np.mean(quad2FitnessValues, axis = 0)
meanQuad3 = np.mean(quad3FitnessValues, axis = 0)
meanQuad4 = np.mean(quad4FitnessValues, axis = 0)
meanQuad5 = np.mean(quad5FitnessValues, axis = 0)
meanQuad6 = np.mean(quad6FitnessValues, axis = 0)
meanQuad7 = np.mean(quad7FitnessValues, axis = 0)
meanQuad8 = np.mean(quad8FitnessValues, axis = 0)
meanQuad9 = np.mean(quad9FitnessValues, axis = 0)

#hexapod 1
meanHex10 = np.mean(hex10FitnessValues, axis = 0)
meanHex11 = np.mean(hex11FitnessValues, axis = 0)
meanHex12 = np.mean(hex12FitnessValues, axis = 0)
meanHex13 = np.mean(hex13FitnessValues, axis = 0)
meanHex14 = np.mean(hex14FitnessValues, axis = 0)
meanHex15 = np.mean(hex15FitnessValues, axis = 0)
meanHex16 = np.mean(hex16FitnessValues, axis = 0)
meanHex17 = np.mean(hex17FitnessValues, axis = 0)
meanHex18 = np.mean(hex18FitnessValues, axis = 0)
meanHex19 = np.mean(hex19FitnessValues, axis = 0)

#hexapod 2
meanHex20 = np.mean(hex20FitnessValues, axis = 0)
meanHex21 = np.mean(hex21FitnessValues, axis = 0)
meanHex22 = np.mean(hex22FitnessValues, axis = 0)
meanHex23 = np.mean(hex23FitnessValues, axis = 0)
meanHex24 = np.mean(hex24FitnessValues, axis = 0)
meanHex25 = np.mean(hex25FitnessValues, axis = 0)
meanHex26 = np.mean(hex26FitnessValues, axis = 0)
meanHex27 = np.mean(hex27FitnessValues, axis = 0)
meanHex28 = np.mean(hex28FitnessValues, axis = 0)
meanHex29 = np.mean(hex29FitnessValues, axis = 0)

#octopod 1
meanOct10 = np.mean(oct10FitnessValues, axis = 0)
meanOct11 = np.mean(oct11FitnessValues, axis = 0)
meanOct12 = np.mean(oct12FitnessValues, axis = 0)
meanOct13 = np.mean(oct13FitnessValues, axis = 0)
meanOct14 = np.mean(oct14FitnessValues, axis = 0)
meanOct15 = np.mean(oct15FitnessValues, axis = 0)
meanOct16 = np.mean(oct16FitnessValues, axis = 0)
meanOct17 = np.mean(oct17FitnessValues, axis = 0)
meanOct18 = np.mean(oct18FitnessValues, axis = 0)
meanOct19 = np.mean(oct19FitnessValues, axis = 0)

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

'''
print("mean quad0")
print(meanQuad0)
print("mean hex10")
print(meanHex10)
print("mean hex20")
print(meanHex20)
print("mean hex21")
print(meanHex21)
print("mean oct10")
print(meanOct1)
print("mean oct20")
print(meanOct20)
'''

# AVERAGE MEANS FROM DIFFERENT RUNS
#quadruped
meanQuadAll = np.zeros(c.numberOfGenerations)
for i in range(c.numberOfGenerations):
   meanQuadAll[i] = (meanQuad0[i] + meanQuad1[i] + meanQuad2[i] + meanQuad3[i] + meanQuad4[i] + meanQuad5[i] + meanQuad6[i] + meanQuad7[i] + meanQuad8[i] + meanQuad9[i])/10

print("mean quad all")
print(meanQuadAll)

#hexapod 1
meanHex1All = np.zeros(c.numberOfGenerations)
for i in range(c.numberOfGenerations):
   meanHex1All[i] = (meanHex10[i] + meanHex11[i] + meanHex12[i] + meanHex13[i] + meanHex14[i] + meanHex15[i] + meanHex16[i] + meanHex17[i] + meanHex18[i] + meanHex19[i])/10

print("mean hex1 all")
print(meanHex1All)

#hexapod 2
meanHex2All = np.zeros(c.numberOfGenerations)
for i in range(c.numberOfGenerations):
   meanHex2All[i] = (meanHex20[i] + meanHex21[i] + meanHex22[i] + meanHex23[i] + meanHex24[i] + meanHex25[i] + meanHex26[i] + meanHex27[i] + meanHex28[i] + meanHex29[i])/10

print("mean hex2 all")
print(meanHex2All)

#octopod 1
meanOct1All = np.zeros(c.numberOfGenerations)
for i in range(c.numberOfGenerations):
   meanOct1All[i] = (meanOct10[i] + meanOct11[i] + meanOct12[i] + meanOct13[i] + meanOct14[i] + meanOct15[i] + meanOct16[i] + meanOct17[i] + meanOct18[i] + meanOct19[i])/10

print("mean Oct1 all")
print(meanOct1All)

#octopod 2
meanOct2All = np.zeros(c.numberOfGenerations)
for i in range(c.numberOfGenerations):
   meanOct2All[i] = (meanOct20[i] + meanOct21[i] + meanOct22[i] + meanOct23[i] + meanOct24[i] + meanOct25[i] + meanOct26[i] + meanOct27[i] + meanOct28[i] + meanOct29[i])/10

print("mean Oct2 all")
print(meanOct2All)

matplotlib.plot(meanQuadAll, label = "quadruped", linewidth = 1)
matplotlib.plot(meanHex1All, label = "hexapod1", linewidth = 2.5) 
matplotlib.plot(meanHex2All, label = "hexapod2", linewidth = 2.5)
matplotlib.plot(meanOct1All, label = "octopod1", linewidth = 4)
matplotlib.plot(meanOct2All, label = "octopod2", linewidth = 4)

matplotlib.xlabel("Generation")
matplotlib.ylabel("Average Fitness")
matplotlib.title("Average fitness over 10 runs")


handles, labels = matplotlib.gca().get_legend_handles_labels()
by_label = OrderedDict(zip(labels, handles))
matplotlib.legend(by_label.values(), by_label.keys())

#show plot
matplotlib.show()