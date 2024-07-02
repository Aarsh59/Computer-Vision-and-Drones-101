import cv2
import numpy as np
def edge_detection(s):
    img2 = cv2.imread(s)
    img4 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    img3 = cv2.GaussianBlur(img4,(3,3),0)
    cv2.imshow('Input Image',img2)
    
    sobelx = cv2.Sobel(img3,cv2.CV_64F,1,0,ksize=5) 
    sobely = cv2.Sobel(img3,cv2.CV_64F,0,1,ksize=5)
    final_img = np.sqrt(np.square(sobelx)+np.square(sobely))
    final_img = cv2.normalize(final_img,None, 0, 1, cv2.NORM_MINMAX, cv2.CV_32F)
    cv2.imshow('Edge Detection',final_img)
    cv2.waitKey(0)

edge_detection(r"C:\Users\HP\Downloads\download.jpeg")    