import numpy as np

def matrixReduce(inpTab, finalSize):
    try:
        if len(finalSize) == 2:
            finalSizeX = finalSize[0]
            finalSizeY = finalSize[1]
    except:
        finalSizeX = finalSize
        finalSizeY = finalSize

    inpArray = np.array(inpTab)
    zeroTab = np.zeros((finalSizeX,finalSizeY),dtype='float')
    inpSize = np.shape(inpArray)
    sizeDiffX = round(inpSize[0] / finalSizeX)
    sizeDiffY = round(inpSize[1] / finalSizeY)
    closElem = []

    if sizeDiffX !=0 or sizeDiffY !=0:
        for x in range(0, finalSizeX):
            for y in range (0, finalSizeY):
                closElem.append(inpArray[x*sizeDiffX][y*sizeDiffY])

                try:
                    closElem.append(inpArray[x*sizeDiffX + 1][y*sizeDiffY])
                except:
                    pass

                if (x*sizeDiffX - 1) >= 0:
                    closElem.append( inpArray[x*sizeDiffX - 1][y*sizeDiffY])
                else:
                    pass

                try:
                    closElem.append(inpArray[x*sizeDiffX][y*sizeDiffY + 1])
                except:
                    pass

                if (y*sizeDiffY - 1) >= 0:
                    closElem.append(inpArray[x*sizeDiffX][y*sizeDiffY - 1])
                else:
                    pass
                zeroTab[x][y] = sum(closElem)/len(closElem)
                closElem = []

        return zeroTab
    else:
        return inpTab




if __name__ == "__main__":
    list = [[1,2,3,4,5],[6,7,8,9,10,],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25],[26,28,29,30,31],[32,33,34,35,36]]

    print(list)
    print(matrixReduce(list, [5,4]))