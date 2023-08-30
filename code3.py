import cv2
import numpy as np
img=cv2.imread(r"C:\Users\vssin\Downloads\TIGER.jpg")
kernal =np.ones((10,5),np.uint8)
imgGray= cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny =cv2.Canny(img,100,100)
imgDialation=cv2.dilate(imgCanny,kernal,iterations=1)
cv2.imshow("gray image", imgGray)
cv2.imshow("blur image", imgBlur)
cv2.imshow("canny image", imgCanny)
cv2.imshow("cdialation image", imgDialation)

cv2.waitKey(0)