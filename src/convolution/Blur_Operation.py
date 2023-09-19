import cv2 as cv
import numpy as np

img = cv.imread("DataSets\IMG-3731.JPG")

rows,cols = img.shape[:2]
#kernal blurring
kernal_blur = np.ones((25,25),np.float32)/625.0
Blur = cv.filter2D(img,-1,kernal_blur)

#BoxFilter and flur functi925,25on
output_blur = cv.blur(img,(25,25))
output_boxblur = cv.boxFilter(img,-1,(5,5),normalize=False)

#gaussian Blur
output_gaussian = cv.GaussianBlur(img,(5,5),0)

#Median Blur (noise reduction)
output_median = cv.medianBlur(img,5)

#bilateral filter (reducation of noise and preserve the edges)
output_bil = cv.bilateralFilter(img,5,6,0) 
cv.bilateralFilter()    
# high the sigmacolor then decrease the color propostionally
# high the sigmadistance then decrease the distance propostionally

cv.imshow("output",Blur)
cv.imshow("output_blur",output_blur)
cv.imshow("Blurbox",output_boxblur)
cv.imshow("Gaussian",output_gaussian)
cv.imshow("Median_Blur",output_median)
cv.imshow("Bilateral_Blur",output_bil)
cv.waitKey(0)
