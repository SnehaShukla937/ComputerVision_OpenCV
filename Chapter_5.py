# WARP PERSPECTIVE ON IMAGE #
import cv2
import numpy as np

width,height = 280,380
img = cv2.imread("Resources/cardPic.png") # get input image
#STEP:1
# coordinates of 4 different pts of a card in image
pts1 = np.float32([[208,141],[538,121],[244,500],[577,484]])
# get new points for warpPerspective based on input points
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
# STEP:2
# get matrix of new points (PerspectiveTransform from pts1 to pts2)
matrix = cv2.getPerspectiveTransform(pts1,pts2)
# STEP:3
# get warp perspective of an image based on points
imgWarp = cv2.warpPerspective(img,matrix,(width,height))

# SHOW IMAGES
cv2.imshow("Actual Image",img) # Actual Image
cv2.imshow("Warp Image",imgWarp) # transformed image
cv2.waitKey(0)