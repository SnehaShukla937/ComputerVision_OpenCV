# FACE DETECTION #

import cv2

# LOAD DEFAULT CASCADE
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
# LOAD INPUT IMAGE
img = cv2.imread("Resources/pic2.png")
cv2.imshow("Actual Image",img)
# CONVERT INTO GRAY IMAGE
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# FIND FACES IN THE IMAGE
faces = faceCascade.detectMultiScale(imgGray,1.1,1)
# DRAW RECTANGLE AROUND DETECTED FACES
for (x,y,w,h) in faces:
     img2 = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

# SHOW IMAGE
cv2.imshow("Face Detected Image",img2)
cv2.waitKey(0)