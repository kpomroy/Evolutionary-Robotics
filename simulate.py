import pybullet as p
import time

physicsClient = p.connect(p.GUI)

#read in the world described in box.sdf
p.loadSDF("box.sdf")

#loop to keep simulated environment open
for i in range(1000):
    p.stepSimulation()
    time.sleep(1/60)
    print(i)

p.disconnect()