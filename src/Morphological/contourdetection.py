import cv2 as cv
import numpy as np

#read image and convert it into gray scale

img =  cv.imread('DataSets\IMG-3731.JPG')
#img = cv.resize('img',None,fx=0.9,fy=0.9)

Gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#Now convert gray scale to the binary image
ret,binary = cv.threshold(Gray,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

#Now detect the contour
contours,hierarchy = cv.findContours(binary,mode=cv.RETR_TREE,method=cv.CHAIN_APPROX_NONE)

#visualise the data Structure
print("Lenght of the contour{}".format(len(contours)))
#print(contours)

#draw contours on the original image
image_copy = img.copy()
img_contours= cv.drawContours(image_copy,contours,-1,(0,255,0),thickness=2,lineType=cv.LINE_AA)

#visualize the result
cv.imshow('Grayscale Image',Gray)
cv.imshow('Draw Contours',img_contours)
cv.imshow("Binary",binary)

cv.waitKey()
cv.destroyAllWindows()
