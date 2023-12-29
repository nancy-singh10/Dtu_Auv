import cv2
import numpy as np
import math

img = cv2.imread("E:\path.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 50, 150)

lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=50, minLineLength=50, maxLineGap=10)


if lines is not None:
    for line in lines:
        # print (line)
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)


    intersection_points = []
    for i in range(len(lines) - 1):
        for j in range(i + 1, len(lines)):
            x1, y1, x2, y2 = lines[i][0]
            x3, y3, x4, y4 = lines[j][0]


            det = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
            if det != 0:
                px = ((x1*y2 - y1*x2) * (x3 - x4) - (x1 - x2) * (x3*y4 - y3*x4)) / det
                py = ((x1*y2 - y1*x2) * (y3 - y4) - (y1 - y2) * (x3*y4 - y3*x4)) / det

                intersection_point = (int(px), int(py))
                intersection_points.append(intersection_point)
                cv2.circle(img, intersection_point, 1, (255, 0, 0), 1)
    points=(intersection_points)
    pt1=points[0]
    pt2=points[5]

    grad=(pt2[1]-pt1[1])/(pt2[0]-pt1[0])


    m2=grad
    m1=0
    angR= math.atan((m2-m1)/(1+(m2*m1)))
    angleD=abs(math.degrees((angR)))
    print("angle with horizontal :)",angleD)

cv2.imshow("Edges and Lines", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Intersection Points:", intersection_points)
