import os
import shutil


# Zadanie 1

fileList = os.listdir("./files") #returns files and directories but we have only files in our directory
resultDirList = os.listdir("./resultFolders")

for file in fileList:
    openedFile = open("./files/{}".format(file), "r")
    text = openedFile.read()
    dirBegin = text.find("dir")
    dirName = text[dirBegin : dirBegin + 4] #  4 because dir + number
    openedFile.close()

    if dirName in resultDirList:
        shutil.copy("./files/{}".format(file),"./resultFolders/{}".format(dirName))
    else:
        os.mkdir("./resultFolders/{}".format(dirName))
        resultDirList = os.listdir("./resultFolders")
        shutil.copy("./files/{}".format(file), "./resultFolders/{}".format(dirName))



# Zadanie 2



'''
    Equations of motion
    dr = x2 - x1
    m a1 = dr k (1 - l/|dr|)
    m a2 = - dr k (1 - l/|dr|)
    '''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation
from scipy.integrate import odeint
from numpy.linalg import norm
from matplotlib import animation

k=10
l=10
m=10
steps=500
frames = 100
startTime=0
endTime=10

locA = [0,0]
locB = [-l,0]
speedA = [0, 50]
speedB = [-30, 30]

gravity=9.81

x=np.linspace(startTime,endTime,steps+1)

#accel=np.zeros((steps+1,2))

startCond = np.array([locA,speedA,locB,speedB]).reshape(8)


 # copy from https://4programmers.net/Forum/Python/320835-wykres_ruchu_dwoch_cial
def equation(Y, t):
    '''
    Equations of motion
    dr = x2 - x1
    m a1 = dr k (1 - l/|dr|)
    m a2 = - dr k (1 - l/|dr|)
    '''
    x1 = Y[:2]
    u1 = Y[2:4]
    x2 = Y[4:6]
    u2 = Y[6:]

    dr = x2-x1

    dY = np.zeros(8)

    if x1[1] < 0 or x2[1] <0:
        return dY

    dY[2:4] = dr*k/m*(1-l/norm(dr))
    dY[3] -= 9.81
    dY[6:] = -dr*k/m*(1-l/norm(dr))
    dY[7] -= 9.81
    dY[:2] = u1
    dY[4:6] = u2

    return dY

result = odeint(equation,startCond, x)

fig = plt.figure()

plt.plot(result[:,0], result[:,1])
plt.plot(result[:,4], result[:,5])

p1, = plt.plot(startCond[0],startCond[1], '*', markersize=10, color="blue")
p2, = plt.plot(startCond[4],startCond[5], '*', markersize=10, color="green")
spring, = plt.plot(startCond[0],startCond[0], '-', markersize=10, color="red")

def anim(frame):
    t = int(len(result)*float(frame)/frames)
    x1 = result[t,:2]
    x2 = result[t,4:6]

    p1.set_data(x1)
    p2.set_data(x2)
    spring.set_data([x1[0],x2[0]], [x1[1], x2[1]])

a = animation.FuncAnimation(fig, anim, frames=frames, interval=10, repeat=False)

plt.show()



