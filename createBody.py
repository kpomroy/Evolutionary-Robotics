import pyrosim.pyrosim as pyrosim


pyrosim.Start_URDF("body.urdf")

#torso
pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[3,1,1])


#left middle leg
pyrosim.Send_Joint(name = "Torso_LeftMidLeg" , parent= "Torso" , child = "LeftMidLeg" , type = "revolute", position = [0,-0.5,1], jointAxis = "1 0 0")

pyrosim.Send_Cube(name="LeftMidLeg", pos=[0,-0.5,0] , size=[0.2,1,0.2])


#left middle lower leg
pyrosim.Send_Joint(name = "LeftMidLeg_LeftMidLowerLeg" , parent= "LeftMidLeg" , child = "LeftMidLowerLeg" , type = "revolute", position = [0,-1,0], jointAxis = "0 1 0")

pyrosim.Send_Cube(name="LeftMidLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])


#left front leg
pyrosim.Send_Joint(name = "Torso_LeftFrontLeg" , parent= "Torso" , child = "LeftFrontLeg" , type = "revolute", position = [-1,-0.5,1], jointAxis = "1 0 0")

pyrosim.Send_Cube(name="LeftFrontLeg", pos=[0,-0.5,0] , size=[0.2,1,0.2])

#left front lower leg
pyrosim.Send_Joint(name = "LeftFrontLeg_LeftFrontLowerLeg" , parent= "LeftFrontLeg" , child = "LeftFrontLowerLeg" , type = "revolute", position = [0,-1,0], jointAxis = "0 1 0")

pyrosim.Send_Cube(name="LeftFrontLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])

#left back leg
pyrosim.Send_Joint(name = "Torso_LeftBackLeg" , parent= "Torso" , child = "LeftBackLeg" , type = "revolute", position = [1,-0.5,1], jointAxis = "1 0 0")

pyrosim.Send_Cube(name="LeftBackLeg", pos=[0,-0.5,0] , size=[0.2,1,0.2])

#left back lower leg
pyrosim.Send_Joint(name = "LeftBackLeg_LeftBackLowerLeg" , parent= "LeftBackLeg" , child = "LeftBackLowerLeg" , type = "revolute", position = [0,-1,0], jointAxis = "0 1 0")

pyrosim.Send_Cube(name="LeftBackLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])

#right middle leg
pyrosim.Send_Joint(name = "Torso_RightMidLeg" , parent= "Torso" , child = "RightMidLeg" , type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0")

pyrosim.Send_Cube(name="RightMidLeg", pos=[0,0.5,0] , size=[0.2,1,0.2])

#right middle lower leg
pyrosim.Send_Joint(name = "RightMidLeg_RightMidLowerLeg" , parent= "RightMidLeg" , child = "RightMidLowerLeg" , type = "revolute", position = [0,1,0], jointAxis = "0 1 0")

pyrosim.Send_Cube(name="RightMidLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])


#right front leg
pyrosim.Send_Joint(name = "Torso_RightFrontLeg" , parent= "Torso" , child = "RightFrontLeg" , type = "revolute", position = [-1,0.5,1], jointAxis = "1 0 0")

pyrosim.Send_Cube(name="RightFrontLeg", pos=[0,0.5,0] , size=[0.2,1,0.2])


#right front lower leg
pyrosim.Send_Joint(name = "RightFrontLeg_RightFrontLowerLeg" , parent= "RightFrontLeg" , child = "RightFrontLowerLeg" , type = "revolute", position = [0,1,0], jointAxis = "0 1 0")

pyrosim.Send_Cube(name="RightFrontLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])

#right back leg
pyrosim.Send_Joint(name = "Torso_RightBackLeg" , parent= "Torso" , child = "RightBackLeg" , type = "revolute", position = [1,0.5,1], jointAxis = "1 0 0")

pyrosim.Send_Cube(name="RightBackLeg", pos=[0,0.5,0] , size=[0.2,1,0.2])

#right back lower leg
pyrosim.Send_Joint(name = "RightBackLeg_RightBackLowerLeg" , parent= "RightBackLeg" , child = "RightBackLowerLeg" , type = "revolute", position = [0,1,0], jointAxis = "0 1 0")

pyrosim.Send_Cube(name="RightBackLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])

pyrosim.End()