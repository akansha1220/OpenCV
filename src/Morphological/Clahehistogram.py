import cv2 as cv
import numpy as np


img = cv.imread('DataSets\images.jpg')
img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#the declartion of CLAHE
#cliplimit->threshold for contrast limiting

clahe = cv.createCLAHE(clipLimit=5)
final_img = clahe.apply(img)

#histogram equalization
img_hist = cv.equalizeHist(final_img)
hist = cv.calcHist([img_hist],[0],None,[256],[0,256])

cv.imshow('normal image',img)
cv.imshow('Clahe',final_img)
cv.imshow('Equalize image',img_hist)
cv.waitKey()