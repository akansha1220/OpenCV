import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('DataSets\images.jpg')
img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)


hist = cv.calcHist([img],[0],None,[256],[0,256])

cv.imshow('normal hist',img)
plt.plot(hist)
plt.show()
cv.waitKey()

#histogram equalization
img_hist = cv.equalizeHist(img)
hist = cv.calcHist([img_hist],[0],None,[256],[0,256])

cv.imshow('normal hist',img_hist)
plt.plot(hist)
plt.show()
cv.waitKey()