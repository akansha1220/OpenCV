import cv2 as cv
import numpy as np

img = cv.imread("DataSets\IMG-3731.JPG")

img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#performing the edge detection

gradients_sobelx = cv.Sobel(img,-1,1,0)
gradients_sobely = cv.Sobel(img,-1,0,1)
gradients_sobelxy = cv.addWeighted(gradients_sobelx,0.5,gradients_sobely,0.5,0)

gradients_laplacian = cv.Laplacian(img,-1)

canny = cv.Canny(img,80,150)         #(img,threshold1,threshorld2)


cv.imshow('Solo X',gradients_sobelx)
cv.imshow('Solo y',gradients_sobely)
cv.imshow('Solo XY',gradients_sobelxy)
cv.imshow('laplacian',gradients_laplacian)
cv.imshow('canny',canny)
cv.waitKey()