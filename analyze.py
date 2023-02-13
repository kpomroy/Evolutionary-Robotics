import numpy as np
import matplotlib.pyplot as matplotlib

""" backLegSensorValues = np.load("data/backLegSensorValues.npy")

frontLegSensorValues = np.load("data/frontLegSensorValues.npy")

print(backLegSensorValues)
print(frontLegSensorValues)

matplotlib.plot(backLegSensorValues, label = "Back Leg", linewidth = 3)
matplotlib.plot(frontLegSensorValues, label = "Front Leg")

#add legend to plot
matplotlib.legend()

#show plot
matplotlib.show() """

targetAngleValues = np.load("data/targetAngleValues.npy")
frontLegTargetAngleValues = np.load("data/frontLegTargetAngleValues.npy")

matplotlib.plot(targetAngleValues, label = "Back Leg")
matplotlib.plot(frontLegTargetAngleValues, label = "Front Leg")

matplotlib.legend()

matplotlib.show()
