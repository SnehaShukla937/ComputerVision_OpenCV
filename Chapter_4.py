# SHAPES AND TEXTS #
import cv2
import numpy as np

# Get a simple black 2-d image (all elements 0)
image = np.zeros((512,512)) # get a black image (0->image)
print(image.shape)  # a 2-d shape as we have not mentioned the channel

# Get a simple black 3-d image (all elements 0)
def get_img():
    img = np.zeros((512,512,3),np.uint8) # get a black image (0->image)
    print(img.shape)  # a 3-d shape
    return img

img = get_img()

# COLOUR THE IMAGE
img1 = get_img() # get image
img1[:] = 255,0,0   # get a complete blue image
img1[100:400,100:400] = 0,255,0   # coloured specific part with green
img1[200:300,200:300] = 0,0,255   # coloured specific part with red


# CREATE SHAPES IN AN IMAGE

# get a black diagonal line in the shape of image
img2 = get_img()
cv2.line(img2,(0,0),(img2.shape[1],img2.shape[0]),(0,255,0),3)

# get a red line in the specified position of image
img3 = get_img()
cv2.line(img3,(0,0),(200,200),(0,0,255),3)

# draw rectangle  and circle in the image
cv2.rectangle(img2,(0,0),(200,200),(0,0,255),2)
cv2.circle(img2,(400,50),30,(255,255,0),4)

cv2.rectangle(img2,(100,400),(200,250),(0,0,255),cv2.FILLED) # filled
cv2.circle(img2,(400,150),30,(255,255,0),cv2.FILLED) # filled

# PUT TEXT ON THE IMAGE
cv2.putText(img2,"OPEN_CV",(300,290),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),2)

# SHOW IMAGES
cv2.imshow("blackImage",img)
cv2.imshow("ColouredImage",img1)
cv2.imshow("ImageShapes",img2)
cv2.waitKey(0)