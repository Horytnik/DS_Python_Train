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

k=10
l=10
m_1=1
m_10=10
steps=500
startTime=0
endTime=10

localizationA = [0,0]
localizationB = [-l,0]

speedA=[0,0.5]
speedB=[-3,3]

gravity=9.81

x=np.linspace(startTime,endTime,steps+1)

dr=x[1]-x[0]

for ctr in range(0,len(x)):
    a1 = (dr * k * (1 - l/abs(dr))) /m_1
    a2 = (- dr * k * (1 - l/abs(dr)))/m_1

#accel=np.zeros((steps+1,2))