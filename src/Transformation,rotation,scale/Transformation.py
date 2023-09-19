import cv2 as cv
import numpy as np

img = cv.imread("F:\Project\FaceRecognisation\DataSets\download (2).jpg")

#Resize of image(zoom)

Linear_img = cv.resize(img,None,fx=1.5,fy=1.5, interpolation=cv.INTER_LINEAR)

Cubic_img = cv.resize(img, None ,fx=2.5, fy=1.5,interpolation = cv.INTER_CUBIC)

Area_img = cv.resize(img, None ,fx=1.5, fy=1.5,interpolation = cv.INTER_AREA)

cv.imshow("Linear",Linear_img)
cv.imshow("Cubic",Cubic_img)
cv.imshow("Area",Area_img)

cv.waitKey()
