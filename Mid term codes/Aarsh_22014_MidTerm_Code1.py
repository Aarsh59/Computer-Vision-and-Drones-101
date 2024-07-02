import cv2
import numpy as np
#imput is in raw string format
def hough_line(s):
    img = cv2.imread(s)
    cv2.imshow('orignal img',img)
    img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(img1,50,200,None,3)
    lines = cv2.HoughLines(edges,1,np.pi/180,150,None,0,0)
    for i in range (0,len(lines)):
        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
        pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
        cv2.line(img, pt1, pt2, (0,0,255), 3, cv2.LINE_AA)
    cv2.imshow('Line detection',img)
      
    cv2.waitKey(0)
hough_line(r"C:\Users\HP\Downloads\123.jpg")    