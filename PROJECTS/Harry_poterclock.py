import cv2 as cv
import numpy as np

def setValues(x):
    print("")
    
cap = cv.VideoCapture(0)    
cv.namedWindow("Color detectors")

cv.createTrackbar("Upper Hue","Color detectors",110,180,setValues)
cv.createTrackbar("Upper Saturation","Color detectors",255,255,setValues)
cv.createTrackbar("Upper Value","Color detectors",255,255,setValues)
cv.createTrackbar("Lower Hue","Color detectors",68,180,setValues)
cv.createTrackbar("Lower Saturation","Color detectors",55,255,setValues)
cv.createTrackbar("Lower Value","Color detectors",54,255,setValues)


while(True):
    cv.waitKey(1000)
    Ret,init = cap.read()

    if Ret:
        break

while(True):
    ret,frame = cap.read()

    inspect = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    u_hue = cv.getTrackbarPos("Upper Hue","Color detectors")
    u_saturation = cv.getTrackbarPos("Upper Saturation","Color detectors")
    u_value = cv.getTrackbarPos("Upper Value","Color detectors")
    l_hue = cv.getTrackbarPos("Lower Hue","Color detectors")
    l_saturation = cv.getTrackbarPos("Lower Saturation","Color detectors")
    l_value = cv.getTrackbarPos("Lower Value","Color detectors")

    #kernal to be used dilation
    kernal = np.ones((3,3),np.uint8)

    Upper_hsv = np.array([u_hue,u_saturation,u_value])
    Lower_hsv = np.array([l_hue,l_saturation,l_value])

    mask = cv.inRange(inspect,Lower_hsv,Upper_hsv)
    mask = cv.medianBlur(mask,3)
    mask_inv = 255-mask

    mask = cv.dilate(mask,kernal,5)


    #the mixing of frames in a combination to achieve the required frame

    b = frame[:,:,0]
    g = frame[:,:,1]
    r = frame[:,:,2]
    b = cv.bitwise_and(mask_inv,b)
    g = cv.bitwise_and(mask_inv,g)
    r = cv.bitwise_and(mask_inv,r)

    frame_inv = cv.merge((b,g,r))

    b = frame[:,:,0]
    g = frame[:,:,1]
    r = frame[:,:,2]
    b = cv.bitwise_and(b,mask_inv)
    g = cv.bitwise_and(g,mask_inv)
    r = cv.bitwise_and(r,mask_inv)

    blanket_area = cv.merge((b,g,r))

    final = cv.bitwise_or(frame_inv,blanket_area)

    cv.imshow("Harry clock",final)
    cv.imshow("Original",frame)

    if(cv.waitKey(3)==ord("q")):
        break

cv.destroyAllWindows()
cv.release()