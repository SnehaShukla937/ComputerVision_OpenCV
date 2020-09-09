# JOINING IMAGE #

import cv2
import numpy as np

img = cv2.imread("Resources/pic1.png")
img1 = cv2.imread("Resources/cardPic.png")

imgHor = np.hstack((img,img))  # horizontal stacking
imgVer = np.vstack((img1,img1)) # vertical stacking

cv2.imshow("Horizontal",imgHor)
cv2.imshow("Vertical",imgVer)
cv2.waitKey(0)