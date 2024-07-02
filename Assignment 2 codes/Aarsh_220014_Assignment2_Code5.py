import numpy as np
import cv2
def aruco_display(corners,ids,rejected,image):
    if(len(corners)>0):
     
        ids=ids.flatten()
        for(markerCorner,markerID) in zip(corners,ids):
            corners=markerCorner.reshape((4,2))
            (topLeft,topRight,bottomRight,bottomLeft)=corners
            topRight=(int(topRight[0]),int(topRight[1]))
            topLeft=(int(topLeft[0]),int(topLeft[1]))
            bottomRight=(int(bottomRight[0]),int(bottomRight[1]))
            bottomLeft=(int(bottomLeft[0]),int(bottomLeft[1]))
            cv2.line(image,topLeft,topRight,(0,255,0),2)
            cv2.line(image,topRight,bottomRight,(0,255,0),2)
            cv2.line(image,bottomRight,bottomLeft,(0,255,0),2)
            cv2.line(image,bottomLeft,topLeft,(0,255,0),2)
            cX=int((topLeft[0]+bottomRight[0]+topRight[0]+bottomLeft[0])/4)
            cY=int((topLeft[1]+bottomLeft[1]+bottomRight[1]+topRight[1])/4)
            cv2.circle(image,(cX,cY),4,(0,0,255),-1)
            
            height,width,_ = image.shape
            print((height/2-cX,width/2-cY))
            
            
   
    return image
def pose_estimation(frame, aruco_dict_type, matrix_coefficients, distortion_coefficients):

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    arucoDict=cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)
    arucoParams=cv2.aruco.DetectorParameters_create()
    corners, ids, rejected_img_points=cv2.aruco.detectMarkers(gray,arucoDict,parameters=arucoParams)
    
   	 
    if len(corners) > 0:
        for i in range(0, len(ids)):
            rvec, tvec, markerPoints = cv2.aruco.estimatePoseSingleMarkers(corners[i], 0.02, matrix_coefficients,distortion_coefficients)
            print(tvec)
            cv2.aruco.drawDetectedMarkers(frame, corners)
            cv2.drawFrameAxes(frame, matrix_coefficients, distortion_coefficients, rvec, tvec, 0.01)
           
			
    return frame
arucoDict=cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)
arucoParams=cv2.aruco.DetectorParameters_create()
def marker(s):
    img=cv2.imread(s)
    h,w,_=img.shape
    width=1000
    height=int(width*(h/w))
    img=cv2.resize(img,(width,height),interpolation=cv2.INTER_CUBIC)
    corners,ids,rejected=cv2.aruco.detectMarkers(img,arucoDict,parameters=arucoParams)
   
    
    
    
    
    detected_markers=aruco_display(corners,ids,rejected,img)
    intrinsic_camera = np.array(((3442.97818, 0, 297.763102),(0 ,3427.93522, 292.958279),(0 ,0 ,1)))

    distortion = np.array((31.7980238 ,-2010.71594 , 0.696080651 ,-0.515058808,
    75545.7900))

    detected_markers1=pose_estimation(img,cv2.aruco.DICT_4X4_50,intrinsic_camera,distortion)
    cv2.imshow("Image",detected_markers1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
marker(r"C:\Users\HP\Pictures\Camera Roll\WIN_20231226_14_54_51_Pro.jpg")
