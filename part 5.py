import cv2
import numpy as np

# width,height = 500,500
#
# path = "kitten.jpg"
# img = cv2.imread(path)
# print(img.shape)
# imgGray = cv2.imread("desert.jpg")
# print(img.shape)
#
# img = cv2.resize(img,(width,height))
# imgGray = cv2.resize(imgGray,(width,height))
#
#
# # img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
# # imgGray = cv2.cvtColor(imgGray,cv2.COLOR_GRAY2BGR)
#
# img = cv2.resize(img,(0,0),None,0.5,0.5)
# imgGray = cv2.resize(imgGray,(0,0),None,0.5,0.5)
#
# hor = np.hstack((img,imgGray))
# ver = np.vstack((img,imgGray))
#
# cv2.imshow("Vertical",ver)
# cv2.imshow("Horizontal",hor)
#
# cv2.waitKey(0)



kernel = np.ones((5,5),np.uint8)

path = "kitten.jpg"

img = cv2.imread(path,200)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(19,19),0)
imgkitten = cv2.Canny(imgBlur,50,50)
imgDilation = cv2.dilate(imgkitten,kernel,iterations=1)
imgErode = cv2.erode(imgDilation,kernel,iterations= 1)

scale = 1
img = cv2.resize(img,(0,0),None,scale,scale)
imgGray = cv2.resize(imgGray,(0,0),None,scale,scale)
imgBlur = cv2.resize(imgBlur,(0,0),None,scale,scale)
imgkitten = cv2.resize(imgkitten,(0,0),None,scale,scale)
imgDilation = cv2.resize(imgDilation,(0,0),None,scale,scale)
imgErode = cv2.resize(imgErode,(0,0),None,scale,scale)

# img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
imgGray = cv2.cvtColor(imgGray,cv2.COLOR_GRAY2BGR)
imgBlur = cv2.cvtColor(imgBlur,cv2.COLOR_GRAY2BGR)
imgkitten = cv2.cvtColor(imgkitten,cv2.COLOR_GRAY2BGR)
imgDilation = cv2.cvtColor(imgDilation,cv2.COLOR_GRAY2BGR)
imgErode = cv2.cvtColor(imgErode,cv2.COLOR_GRAY2BGR)

hor = np.hstack((img,imgGray,imgBlur))
hor2 = np.hstack((imgkitten,imgDilation,imgErode))
ver = np.vstack((hor,hor2))

cv2.imshow("vertical",ver)

cv2.waitKey(0)