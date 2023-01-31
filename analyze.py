import numpy as np
import matplotlib.pyplot as matplotlib

backLegSensorValues = np.load("data/backLegSensorValues.npy")

print(backLegSensorValues)

matplotlib.plot(backLegSensorValues)

matplotlib.show()