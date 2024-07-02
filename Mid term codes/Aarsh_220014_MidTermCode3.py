import cv2
import numpy as np
def color(s):
    img  = cv2.imread(s)
    cv2.imshow('Orignal',img)
    img1 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    final = img.copy()
    lower1 = np.array([0,100,20])
    upper1 = np.array([10,255,255])
    lower2 = np.array([160,100,20])
    upper2 = np.array([179,255,255])
    mask1 = cv2.inRange(img1,lower1,upper1)
    mask2 = cv2.inRange(img1,lower2,upper2)
    mask = mask1+mask2
    final = cv2.bitwise_and(final,final,mask=mask)
    contours, hierarchy = cv2.findContours(mask, 
                                           cv2.RETR_TREE, 
                                           cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1 , (0, 255, 0), 2)
    cv2.imshow('RED Color',img)
    cv2.waitKey(0)
    
     