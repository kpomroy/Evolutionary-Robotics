import pybullet as p
import pybullet_data

class WORLD:
    def __init__(self):
        #create floor
        self.planeId = p.loadURDF("plane.urdf")

        #read in the world described in box.sdf
        p.loadSDF("world.sdf")