import cv2
import numpy as np


# frmaeWidth = 640
# frmaeHeight = 480
#
# cap = cv2.VideoCapture(0)
# cap.set(3,frmaeWidth)
# cap.set(4,frmaeHeight)
#
# def empty(a):
#     pass
#
# # cv2.namedWindow("HSV")
# # cv2.resizeWindow("HSV",640,240)
# # cv2.createTrackbar("HUE Min","HSV",0,179,empty)
# # cv2.createTrackbar("HUE Max","HSV",179,179,empty)
# # cv2.createTrackbar("HUE Min","HSV",0,255,empty)
# # cv2.createTrackbar("HUE Max","HSV",255,255,empty)
# # cv2.createTrackbar("HUE Min","HSV",0,255,empty)
# # cv2.createTrackbar("HUE Max","HSV",255,255,empty)
#
# while True:
#     img = cap.read()
#     imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#
#     # h_min=cv2.getTrackbarPos("HUE Min", "HSV", 0, 179, empty)
#     # h_max=cv2.getTrackbarPos("HUE Max", "HSV", 179, 179, empty)
#     # s_min=cv2.getTrackbarPos("SAT Min", "HSV", 0, 255, empty)
#     # s_max=cv2.getTrackbarPos("SAT Max", "HSV", 255, 255, empty)
#     # v_min=cv2.getTrackbarPos("VALUE Min", "HSV", 0, 255, empty)
#     # v_max=cv2.getTrackbarPos("VALUE Max", "HSV", 255, 255, empty)
#     # # print(h_min)
#     cv2.imshow("Video",img)
#     cv2.imshow("imgHsv",imgHsv)
#
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break
#
# cap.release()
# cv2.destroyAllWindows()

frmaeWidth = 300
frmaeHeight = 300

cap = cv2.VideoCapture(0)
cap.set(3,frmaeWidth)
cap.set(4,frmaeHeight)

def empty(a):
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",640,240)
cv2.createTrackbar("HUE Min","HSV",0,179,empty)
cv2.createTrackbar("HUE Max","HSV",179,179,empty)
cv2.createTrackbar("SAT Min","HSV",0,255,empty)
cv2.createTrackbar("SAT Max","HSV",255,255,empty)
cv2.createTrackbar("VALUE Min","HSV",0,255,empty)
cv2.createTrackbar("VALUE Max","HSV",255,255,empty)


while True:
    sucess,img = cap.read()
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


    h_min = cv2.getTrackbarPos("HUE Min", "HSV")
    h_max = cv2.getTrackbarPos("HUE Max", "HSV")
    s_min = cv2.getTrackbarPos("SAT Min", "HSV")
    s_max = cv2.getTrackbarPos("SAT Max", "HSV")
    v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
    v_max = cv2.getTrackbarPos("VALUE Max", "HSV")
    print(h_min)

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHsv,lower,upper)
    result = cv2.bitwise_and(img,img,mask=mask)

    mask = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
    hStack = np.hstack([img,mask,result])
    # cv2.imshow("Video",img)
    # # cv2.imshow("imgHsv", imgHsv)
    # cv2.imshow("Mask",mask)
    # cv2.imshow("Result",result)
    cv2.imshow("stack",hStack)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
