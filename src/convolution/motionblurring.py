import cv2 as cv
import numpy as np

img =cv.imread('F:\Project\FaceRecognisation\DataSets\download (2).jpg')

kernal_size = 15

kernal = np.zeros((kernal_size,kernal_size))

# changing the middle row of kernal to all zeros in it
kernal[int((kernal_size-1)/2),:] = np.ones(kernal_size)

#Normalizing the kernal
kernal = kernal/kernal_size

output = cv.filter2D(img,-1,kernal)

cv.imshow("motion blurr",output)
cv.imshow("normal",img)
cv.waitKey()
