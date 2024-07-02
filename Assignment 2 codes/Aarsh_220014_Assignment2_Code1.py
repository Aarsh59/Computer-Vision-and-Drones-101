import numpy as np 
import cv2
import math
def generate():
    reference = np.zeros((600,600,3) , dtype=np.uint8)
    for i in range(0,200):
        for j in range(0,600):
            reference[i][j][0]=31
            reference[i][j][1]=103
            reference[i][j][2]=255
            reference[200+i][j][0]=255
            reference[200+i][j][1]=255
            reference[200+i][j][2]=255
            reference[400+i][j][0]=56
            reference[400+i][j][1]=106
            reference[400+i][j][2]=4
    a = (300,300)
    cv2.circle(reference,a,100,(141,3,6),2)
    for i in range(0,24):
        b = i*math.pi/12
        c = (300+int(100*np.cos(b)),300+int(100*np.sin(b)))
        cv2.line(reference,a,c,(255,51,51),1)
    return reference
img = generate()
cv2.imshow('Flag',img)
cv2.waitKey(0)

    




