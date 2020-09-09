# BASIC FUNCTIONS #
import cv2
import numpy as np

img = cv2.imread("Resources/pic1.png")  # import coloured image

# 1. CONVERT RGB IMAGE TO GRAY IMAGE
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 2. GETTING THE BLURRED IMAGE
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)

# 3. CANNY EDGE DETECTOR : FIND EDGES IN IMAGE
imgCanny = cv2.Canny(img,100,100)

# 4. IMAGE DILATION
imgDilation = cv2.dilate(imgCanny,np.ones((5,5),np.uint8),iterations=1)

# 5. IMAGE EROSION
imgEroded = cv2.erode(imgDilation,np.ones((5,5),np.uint8),iterations=1)


# SHOW IMAGES
cv2.imshow("RGB Image",img) # RGB
cv2.imshow("Gray Image",imgGray) # Gray
cv2.imshow("Blur Image", imgBlur) # Blurred image
cv2.imshow("Edge Detector",imgCanny)  # edge detector
cv2.imshow("Image Dilation",imgDilation) # Image Dilation
cv2.imshow("Image Erosion",imgEroded) # Image Erosion
cv2.waitKey(0)