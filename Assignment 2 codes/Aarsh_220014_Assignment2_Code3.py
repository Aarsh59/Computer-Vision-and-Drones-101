import cv2
import numpy as np
import math
from ordered_set import OrderedSet


def unskew(s):
    img = cv2.imread(s)
    vertical=OrderedSet()
    horizontal = OrderedSet()
    height , width = img.shape[:2]
    mid = int(width/2)
    mid1 = int(height/2)
    third = int(height/3)
    third1 = int(width/3)
    range1 = ((0,0,0),(32,32,32))
    range2 = ((224,224,224),(255,255,255))
    range3 = ((0,102,0),(102,255,102))
    range4 = ((0,76,153),(102,178,255))  
    for i in range(0,height):
        if img[i][mid][0]>=range1[0][0] and img[i][mid][0]<=range1[1][0] and  img[i][mid][1]>=range1[0][1] and img[i][mid][1]<=range1[1][1] and  img[i][mid][2]>=range1[0][2] and img[i][mid][2]<=range1[1][2] :
            continue
        elif img[i][mid][0]>=range2[0][0] and img[i][mid][0]<=range2[1][0] and  img[i][mid][1]>=range2[0][1] and img[i][mid][1]<=range2[1][1] and  img[i][mid][2]>=range2[0][2] and img[i][mid][2]<=range2[1][2]:
            vertical.add((255,255,255))
        elif img[i][mid][0]>=range3[0][0] and img[i][mid][0]<=range3[1][0] and  img[i][mid][1]>=range3[0][1] and img[i][mid][1]<=range3[1][1] and  img[i][mid][2]>=range3[0][2] and img[i][mid][2]<=range3[1][2]:
            vertical.add((0,153,0))
        elif  img[i][mid][0]>=range4[0][0] and img[i][mid][0]<=range4[1][0] and  img[i][mid][1]>=range4[0][1] and img[i][mid][1]<=range4[1][1] and  img[i][mid][2]>=range4[0][2] and img[i][mid][2]<=range4[1][2]:
            vertical.add((51,153,255))
        else:
            continue
    for i in range(0,width):
        if img[mid1][i][0]>=range1[0][0] and img[mid1][i][0]<=range1[1][0] and  img[mid1][i][1]>=range1[0][1] and img[mid1][i][1]<=range1[1][1] and  img[mid1][i][2]>=range1[0][2] and img[mid1][i][2]<=range1[1][2] :
            continue
        elif img[mid1][i][0]>=range2[0][0] and img[mid1][i][0]<=range2[1][0] and  img[mid1][i][1]>=range2[0][1] and img[mid1][i][1]<=range2[1][1] and  img[mid1][i][2]>=range2[0][2] and img[mid1][i][2]<=range2[1][2]:
            horizontal.add((255,255,255))
        elif img[mid1][i][0]>=range3[0][0] and img[mid1][i][0]<=range3[1][0] and  img[mid1][i][1]>=range3[0][1] and img[mid1][i][1]<=range3[1][1] and  img[mid1][i][2]>=range3[0][2] and img[mid1][i][2]<=range3[1][2]:
            horizontal.add((0,153,0))
        elif  img[mid1][i][0]>=range4[0][0] and img[mid1][i][0]<=range4[1][0] and  img[mid1][i][1]>=range4[0][1] and img[mid1][i][1]<=range4[1][1] and  img[mid1][i][2]>=range4[0][2] and img[mid1][i][2]<=range4[1][2]:
            horizontal.add((51,153,255))
        else:
            continue
    if len(vertical)==3:
        output = np.zeros((height,width,3), dtype=np.uint8)
        i = 0
        for color in vertical:
            for j in range(0,width):
                for k in range(i*third,(i+1)*third):
                    output[k][j][0]=color[0]
                    output[k][j][1]=color[1]
                    output[k][j][2]=color[2]
            i+=1
        cv2.circle(output,(mid,mid1),int(third/2),(255,51,51),2)
        radius = int(third/2)
        for i in range(0,24):
            b = i*math.pi/12
            c = (mid+int(radius*np.cos(b)),mid1+int(radius*np.sin(b)))
            cv2.line(output,(mid,mid1),c,(255,51,51),1)
        
        cv2.imshow('1',img)
        cv2.imshow('2',output)
        cv2.waitKey(0)                
    else:
        output = np.zeros((height,width,3), dtype=np.uint8)
        i = 0
        for color in horizontal:
            for j in range(0,height):
                for k in range(i*third1,(i+1)*third1):
                    output[j][k][0]=color[0]
                    output[j][k][1]=color[1]
                    output[j][k][2]=color[2]
            i+=1
        cv2.circle(output,(mid,mid1),int(third1/2),(255,51,51),2)
        radius = int(third1/2)
        for i in range(0,24):
            b = i*math.pi/12
            c = (mid+int(radius*np.cos(b)),mid1+int(radius*np.sin(b)))
            cv2.line(output,(mid,mid1),c,(255,51,51),1)
                
        cv2.imshow('1',img)
        cv2.imshow('2',output)
        cv2.waitKey(0)       
unskew(r"C:\Users\HP\Downloads\WhatsApp Image 2023-12-25 at 21.19.33 (3).jpeg") 
#r"C:\Users\HP\Downloads\WhatsApp Image 2023-12-25 at 21.19.32 (2).jpeg"
#r"C:\Users\HP\Downloads\WhatsApp Image 2023-12-25 at 21.19.32 (3).jpeg"
#r"C:\Users\HP\Downloads\WhatsApp Image 2023-12-25 at 21.19.33 (1).jpeg"
#r"C:\Users\HP\Downloads\WhatsApp Image 2023-12-25 at 21.19.33 (2).jpeg"
#r"C:\Users\HP\Downloads\WhatsApp Image 2023-12-25 at 21.19.33 (3).jpeg"
#r"C:\Users\HP\Downloads\WhatsApp Image 2023-12-25 at 21.19.33 (4).jpeg"   
            
            
        
        
              


    
            
        