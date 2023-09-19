import cv2 as cv
import numpy as np


#default tracbar function
def setValues(x):
    print("")

#Creating the tracbars needed for adjusting the marker color

cv.namedWindow("Color detectors")
cv.createTrackbar("Upper Hue","Color detectors",153,180,setValues)
cv.createTrackbar("Upper Saturation","Color detectors",255,255,setValues)
cv.createTrackbar("Upper Value","Color detectors",255,255,setValues)
cv.createTrackbar("Lower Hue","Color detectors",64,180,setValues)
cv.createTrackbar("Lower Saturation","Color detectors",72,255,setValues)
cv.createTrackbar("Lower Value","Color detectors",49,255,setValues)

#capture the input from the webcam

def get_frame(cap,scaling_factor):
    ret,frame= cap.read()
    # Iterate until the user press ESC key
    frame = cv.resize(frame,None,fx = scaling_factor,fy=scaling_factor,interpolation=cv.INTER_AREA)

    return frame

if __name__=='__main__':
    cap = cv.VideoCapture(0)
    scaling_factor = 0.9
    #Iterate until the user press ESC key

    while True:
        frame = get_frame(cap,scaling_factor)

        #convert the HSV COLOR

        hsv = cv.cvtColor(frame,cv.COLOR_RGB2HSV)
        u_hue = cv.getTrackbarPos("Upper Hue","Color detectors")
        u_saturation = cv.getTrackbarPos("Upper Saturation","Color detectors")
        u_value = cv.getTrackbarPos("Upper Value","Color detectors")
        l_hue = cv.getTrackbarPos("Lower Hue","Color detectors")
        l_saturation = cv.getTrackbarPos("Lower Saturation","Color detectors")
        l_value = cv.getTrackbarPos("Lower Value","Color detectors")


        #define 'color range' in HSV colorspace
        Upper_hsv = np.array([u_hue,u_saturation,u_value])
        Lower_hsv = np.array([l_hue,l_saturation,l_value])

        #thresholde the HSV image to get only selected color
        mask = cv.inRange(hsv,Lower_hsv,Upper_hsv)

        #bitwise AND mask and original image
        res = cv.bitwise_and(frame,frame,mask=mask)
        res = cv.medianBlur(res,5)
        cv.imshow('original image',frame)
        cv.imshow("color detector", res)

        #check for key press
        c = cv.waitKey(5)
        if c == 27:
            break

    cv.destroyAllWindows()
        