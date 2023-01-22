import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

length = 1
width = 1
height = 1

x = -2
y = -2
z = 0.5

for i in range(5):
    for i in range(5):
        length = 1
        width = 1
        height = 1
        if y>=3:
            y = -2
            x = x+1
        z = 0.5
        for i in range(10):
            pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
            length = length*0.9
            width = width*0.9
            height = height*0.9
            z = z+1
        y = y+1

pyrosim.End()