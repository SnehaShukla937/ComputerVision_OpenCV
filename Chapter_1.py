import cv2
print("package imported")

# UPLOAD IMAGES
img = cv2.imread("Resources/pic1.png")    # import image from resources
cv2.imshow("Output",img)   # show image
cv2.waitKey(0)   # assign waitkey

# UPLOAD VIDEOS
cap = cv2.VideoCapture("Resources/video1.mp4")    # import video from resources

while True:
    success, imgCap = cap.read()   # get images from video
    cv2.imshow("Output",imgCap)     # show images in loop
    if cv2.waitKey(1) & 0xFF == ord('q'):   # break the loop when pressing 'q'
        break

# Using Webcam
cap = cv2.VideoCapture(0)    # import video from webcam;0 is id for our cam ( if one cam )
cap.set(3,640)  # set width
cap.set(4,480)  # set height
cap.set(10,100) # set brightness

while True:
    success, imgCap = cap.read()   # get images from video
    cv2.imshow("Output",imgCap)     # show images in loop
    if cv2.waitKey(1) & 0xFF == ord('q'):   # break the loop when pressing 'q'
        break