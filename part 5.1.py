import cv2
import numpy as np
import StackImages_function as st_f


frmaeWidth = 300
frmaeHeight = 300

cap = cv2.VideoCapture(0)

while True:
 sucess,img = cap.read()
 cv2.imshow("Video",img)

 kernel = np.ones((5,5),np.uint8)

 imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 imgBlur = cv2.GaussianBlur(imgGray,(19,19),0)
 imgkitten = cv2.Canny(imgBlur,50,50)
 imgDilation = cv2.dilate(imgkitten,kernel,iterations=1)
 imgErode = cv2.erode(imgDilation,kernel,iterations= 1)

 scale = 1

 imgBlank = np.zeros((200,200),np.uint8)

 StackdImages = st_f.stackImages(0.8,([img,imgGray,imgBlur],[imgkitten,imgDilation,imgErode]))
 cv2.imshow("Stackd Images",StackdImages)

 if cv2.waitKey(1) & 0xFF == ord("q"):
  break

