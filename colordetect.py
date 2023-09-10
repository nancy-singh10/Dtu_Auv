import cv2
image=cv2.imread(r"C:\Users\vssin\Downloads\Awesome-Shapes-Image.jpg")
gray_image=cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
_,thresh_image=cv2.threshold(gray_image,220,255,cv2.THRESH_BINARY)
contours ,hierarchy=cv2.findContours(thresh_image,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for i,contours in  enumerate(contours):
    if i==0:
        continue

    epsilon=0.01*cv2.arcLength(contours,True)
    approx=cv2.approxPolyDP(contours,epsilon,True)
    cv2.drawContours(image,contours,0,(0,0,0),4)
    x,y,w,h=cv2.boundingRect(approx)
    x_mid=int(x+w/3)
    y_mid=int(y+h/1.5)

    coords=(x_mid ,y_mid)
    colour=(0,0,0)
    font=cv2.FONT_HERSHEY_DUPLEX
    if len(approx)==3:
         cv2.putText(image,"Triangle",coords,font,0.5,colour,1)
    elif len(approx) == 4 and len(approx)<5:
        cv2.putText(image, "quadrilateral", coords, font, 0.5, colour, 1)
    elif len(approx) == 5:
        cv2.putText(image, "pentgon", coords, font, 0.5, colour, 1)
    elif len(approx) == 6:
         cv2.putText(image, "hexagon", coords, font, 0.5, colour, 1)
    else:
        cv2.putText(image, "circle", coords, font, 0.5, colour, 1)

cv2.imshow("window",image)
cv2.waitKey(0)




