import cv2
cap=cv2.VideoCapture(r"C:\Users\vssin\Downloads\heey.mp4.mkv")
while True:
    success,img =cap.read()
    cv2.imshow("video",img)
    if