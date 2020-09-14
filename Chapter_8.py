# Shape and Contour detection from image

import  cv2
import numpy as np


# FUNCTION TO GET CONTOUR AND FINAL SHAPE DETECTION
def getContours(imgCanny):
    # FIND CONTOUR OF EACH DETECTED SHAPE
    contours,hierarchy = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    # LOOP TO ACCESS EACH CONTOUR
    for c in contours:
        # GET AREA
        area = cv2.contourArea(c)
        print(area)
        # DRAW CONTOUR ON THE DETECTED SHAPE (blue outline)
        cv2.drawContours(imgC, c, -1, (255, 0, 0), 3)
        # GET ARC LENGTH
        arc = cv2.arcLength(c,True)
        # GET APPROX CONTOUR
        approx = cv2.approxPolyDP(c,0.02*arc,True)
        print("NO. OF CORNERS:",len(approx))
        # GET NO.OF CORNERS
        objCorner = len(approx)
        # DRAW BOUNDING RECTANGLE ON THE APPROX CONTOUR
        x, y, w, h = cv2.boundingRect(approx)
        if objCorner == 3:  # IF NO. OF CORNERS IS 3
            objText = "T"   # IT IS TRIANGLE
        elif objCorner == 4:  # IF NO. OF CORNERS IS 4
            aspRatio = w/h
            if aspRatio > 0.8 and aspRatio < 1.05 :
                objText = "S"   # SQUARE
            else:objText = "R"  # RECTANGLE
        elif objCorner > 5:  # IF NO. OF CORNERS IS 5
            objText = "C"  # CIRCLE
        else: objText = "None"
        cv2.rectangle(imgC,(x,y),(x+w,y+h),(0,250,0),2)
        # PUT THE SHAPE NAME ON THE DETECTED CONTOUR
        cv2.putText(imgC,objText,(x+(w//2)-5,y+(h//2)-5),
                    cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)

# GET INPUT IMAGE
path = "Resources/imgShape.jpg"
img = cv2.imread(path)
img = cv2.resize(img,(250,250))
imgC = img.copy() # GET A COPY OF IMAGE
# CONVERT IMAGE TO GRAYSCALE
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# GET BLURRED IMAGE
imgBlur = cv2.GaussianBlur(imgGray,(7,7),2)
# EDGE DETECTED IMAGE
imgCanny = cv2.Canny(imgBlur,50,50)

# CALL FUNCTION TO DETECT SHAPE
getContours(imgCanny)

# JOIN IMAGES
stack1 = np.hstack((imgGray,imgBlur,imgCanny))
stack2 = np.hstack((img,imgC))

# SHOW IMAGES
cv2.imshow("Gray, Blurred, Edge Detected Image",stack1)
cv2.imshow("Input & Output Image",stack2)
cv2.waitKey(0)