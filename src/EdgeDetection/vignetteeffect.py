import cv2 as cv
import numpy as np

img = cv.imread("DataSets\IMG-3731.JPG")
print(img.shape)

rows,cols = img.shape[:2]

#generating vignette mask using gaussian kernals
kernal_x = cv.getGaussianKernel(cols,200)
kernal_y = cv.getGaussianKernel(rows,200)

kernel = kernal_x*kernal_y.T

#Normalizing the kernal
kernel = kernel/np.linalg.norm(kernel)

#Generating a mask to image
mask = 255 * kernel
output = np.copy(img)

#applying the mask to each channel in input image
for i in range(3):
    output[:,:,i]=output[:,:,i]*mask.reshape(1280,720)
cv.imshow('original',img)
cv.imshow('Vignette',output)
cv.waitKey()