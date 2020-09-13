import cv2
import numpy as np


def empty(a): # FUNCTION USED IN TRACK BAR
    pass


path = "Resources/pic2.png"

# CREATE NEW WINDOW FOR TRACK BAR
cv2.namedWindow("TrackBars")
# RESIZE WINDOW
cv2.resizeWindow("TrackBars",700,310)

# CREATE TRACKBAR FOR 6 DIFFERENT VALUES
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)  # max hue = 360 but for open cv it is 180
cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",153,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

# GET REAL TIME VALUES OF HSV BY TUNING THE TRACKBAR VALUES

while True:
    img = cv2.imread(path)

    # CONVERT RGB TO HSV
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min= cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)

    # GET MASK OF PERTICULAR OBJECT (BLACK = 0,WHITE = 1)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)

    # PERFORM AND OPERATION OF IMAGES WITH MASK
    imgResult = cv2.bitwise_and(img,img,mask=mask)

    # JOINED THE FINAL IMAGE WITH ACTUAL AND HSV IMAGE
    stackedImg = np.hstack((img,imgHSV,imgResult))

    # SHOW MASK AND IMAGES
    cv2.imshow("Mask",mask)
    cv2.imshow("StackedImage",stackedImg)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break

