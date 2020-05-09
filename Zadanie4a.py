import matplotlib.image as im
import matplotlib.pyplot as plt
from zadanie3 import matrixReduce
import numpy as np


readImg = im.imread('meil.png')

reduImage1 = np.array(matrixReduce(readImg[:,:,0],[20,20]))
reduImage2 = np.array(matrixReduce(readImg[:,:,1],[20,20]))
reduImage3 = np.array(matrixReduce(readImg[:,:,2],[20,20]))

reshapImg = np.dstack([reduImage1, reduImage2, reduImage3])


ax1=plt.subplot(1, 2, 1)
plt.title('Original size')
ax1.imshow(readImg)

ax2=plt.subplot(1, 2, 2)
plt.title('Resized')
ax2.imshow(reshapImg)
plt.show()

