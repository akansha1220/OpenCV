import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('DataSets\images.jpg')
b,g,r = cv.split(img)

cv.imshow('normal hist',img)
hist_b = cv.calcHist([b],[0],None,[256],[0,256])
plt.plot(hist_b)
hist_g= cv.calcHist([g],[0],None,[256],[0,256])
plt.plot(hist_g)
hist_r = cv.calcHist([r],[0],None,[256],[0,256])
plt.plot(hist_r)

plt.show()
cv.waitKey()
#-----------------------------------equalize

img_hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
H,S,V = cv.split(img_hsv)

equalise = cv.equalizeHist(V)             #valueize channel pr hi histogram lgana h

merge_V = cv.merge((H,S,V))
img_hsv = cv.cvtColor(merge_V,cv.COLOR_HSV2BGR)

cv.imshow("normal",img)
cv.imshow("inhance",img_hsv)
cv.waitKey()

hist_b = cv.calcHist([H],[0],None,[256],[0,256])
plt.plot(hist_b)
hist_g= cv.calcHist([S],[0],None,[256],[0,256])
plt.plot(hist_g)
hist_r = cv.calcHist([V],[0],None,[256],[0,256])
plt.plot(hist_r)

plt.show()