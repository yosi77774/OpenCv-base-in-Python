import cv2

path = "kitten.jpg"

img = cv2.imread(path)

width,height = 1000,1000
imgResize = cv2.resize(img,(width,height))

imgCropped = img[300:600,0:2000]#--חיתוך תמונה--
imgCroppedResize = cv2.resize(imgCropped,(img.shape[1],img.shape[0]))#--החזרה לגודל הרגיל של התמונה רק עם תצוגת התמונה החדשה לאחר החיתוך

cv2.imshow("imgResize",imgResize)
# cv2.imshow("kitten",img)
cv2.imshow("imgCropped",imgCropped)
cv2.imshow("imgCroppedResize",imgCroppedResize)

cv2.waitKey(0)