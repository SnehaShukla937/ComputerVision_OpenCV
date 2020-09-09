# Resizing and Cropping #
import cv2

# RESIZE IMAGE
img = cv2.imread("Resources/pic1.png") # load image
print(img.shape)  # get the actual shape of image (height,width,channel)

imgResize = cv2.resize(img,(1000,500)) # resize image
print(imgResize.shape) # get the shape of resized image

# CROP IMAGE
imgCropped = img[0:200,200:500] # get the image part of 0:200->height and 200:500-> width

# SHOW IMAGES
cv2.imshow("Actual Image",img)  # Actual Image
cv2.imshow("Resized Image",imgResize)  # Resized Image
cv2.imshow("Cropped image",imgCropped)  # Cropped Image
cv2.waitKey(0)

