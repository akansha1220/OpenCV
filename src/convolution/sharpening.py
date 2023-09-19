import cv2 as cv
import numpy as np

img = cv.imread("DataSets\IMG-3731.JPG")

#reading image
gaussian = cv.GaussianBlur(img,(7,7),2)
sharp1 = cv.addWeighted(img,1.5,gaussian,-0.5,0)    #alpha - beta = 1 (source1*alpha+source2*beta+gaama),adding and blending 2 images
'''alpha – weight of the first array elements.
 src2 – second input array of the same size and channel number as src1. 
beta – weight of the second array elements. 
dst – output array that has the same size and number of channels as the input arrays. 
gamma – scalar added to each sum'''

sharp2 = cv.addWeighted(img,3.5,gaussian,-2.5,0)

sharp3 = cv.addWeighted(img,7.5,gaussian,-0.5,0)

cv.imshow("sharp1",sharp1)
cv.imshow("sharp2",sharp2)
cv.imshow("sharp3",sharp3)
cv.waitKey()