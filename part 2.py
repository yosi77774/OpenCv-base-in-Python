import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)

path = "kitten.jpg"

img = cv2.imread(path,200)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(19,19),0)
imgkitten = cv2.Canny(imgBlur,50,50)
imgDilation = cv2.dilate(imgkitten,kernel,iterations=1)
imgErode = cv2.erode(imgDilation,kernel,iterations= 1)

cv2.imshow("kitten",img)
cv2.imshow("GrayScale",imgGray)
cv2.imshow("img Blur",imgBlur)
cv2.imshow("img kitten",imgkitten)
cv2.imshow("img Dilation",imgDilation)
cv2.imshow("img Erode",imgErode)

cv2.waitKey(0)
