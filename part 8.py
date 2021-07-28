import cv2
import numpy as np
import StackImages_function as St_F


frmaeWidth = 300
frmaeHeight = 300

cap = cv2.VideoCapture(0)
cap.set(3,frmaeWidth)
cap.set(4,frmaeHeight)

def empty(a):
    pass

cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters",640,240)
cv2.createTrackbar("Threshold1","Parameters",23,255,empty)
cv2.createTrackbar("Threshold2","Parameters",20,255,empty)
cv2.createTrackbar("Area","Parameters",5000,30000,empty)

def getContours(img,imgContour):

    Contour , hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    areaMin =cv2.getTrackbarPos("Area","Parameters")
    for cnt in Contour:
        area = cv2.contourArea(cnt)
        if area > areaMin:
         cv2.drawContours(imgContour, Contour, -1, (255, 0, 0), 3)
         peri = cv2.arcLength(cnt,True)
         approx = cv2.approxPolyDP(cnt,0.02 * peri,True)
         print(len(approx))
         x,y,w,h = cv2.boundingRect(approx)
         cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),5)

         cv2.putText(imgContour,"Points: " + str(len(approx)),(x+w+20,y+20),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),2)
         cv2.putText(imgContour,"Area: " + str(len(approx)),(x+w+20,y+45),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),2)

while True:
    success, img = cap.read()
    imgContour = img.copy()

    imgBlur = cv2.GaussianBlur(img,(7,7),1)
    imgGray = cv2.cvtColor(imgBlur,cv2.COLOR_BGR2GRAY)

    threshold1 = cv2.getTrackbarPos("Threshold1","Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2","Parameters")
    imgCanny = cv2.Canny(imgGray, threshold1, threshold2)
    Kernel = np.ones((5,5))
    imgDil = cv2.dilate(imgCanny, Kernel, iterations=1)

    getContours(imgDil,imgContour)
    imgStack = St_F.stackImages(0.8, ([img, imgGray, imgCanny],[imgDil,imgContour,imgContour]))
    cv2.imshow("Result",imgStack)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break