import cv2 as cv
import numpy as np

img = cv.imread("F:\Project\FaceRecognisation\DataSets\download (2).jpg")

#Resize of image(zoom)

matrix=np.float32([[1,0,100],[0,1,100]])

#matrix transformation
width,hight = img.shape[:2]
Rotation_matix = cv.getRotationMatrix2D((hight,width),10,1)
translation_img = cv.warpAffine(img,Rotation_matix,(img.shape[1]+100,img.shape[0]+100))

cv.imshow("translation",translation_img)


cv.waitKey()
