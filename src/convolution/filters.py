import cv2 as cv
import numpy as np

img = cv.imread("F:\Project\FaceRecognisation\DataSets\download (2).jpg")

#kernal
Kernal_identity = np.array([[0,0,0],[0,1,0],[0,0,0]])
kernal_3 = np.ones((3,3),dtype=np.float32)
kernal_11 = np.ones((11,11),dtype=np.float32)

#Normalize:

kernal_3 = np.ones((3,3),dtype=np.float32)/9.0
kernal_11 = np.ones((11,11),dtype=np.float32)/121.0

#Apply the filter
output1 = cv.filter2D(img,-1,Kernal_identity)
output2 = cv.filter2D(img,-1,kernal_3)
output3 = cv.filter2D(img,-1,kernal_11)

cv.imshow("Output1",output1)
cv.imshow("Output2",output2)
cv.imshow("Output3",output3)
cv.waitKey()