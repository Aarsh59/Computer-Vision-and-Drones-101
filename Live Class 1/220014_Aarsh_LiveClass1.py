import cv2
import numpy as np
img1 = r"C:\Users\HP\Downloads\download (3).jpeg"
img2 = r"C:\Users\HP\Downloads\download (2).jpeg"
# imread
img3 = cv2.imread(img1)
img4 = cv2.imread(img2)
#resizing to 256 by 256
img5 = cv2.resize(img3,(256,256),interpolation=cv2.INTER_LINEAR)
img6 = cv2.resize(img4,(256,256),interpolation=cv2.INTER_LINEAR)
# convert to gray scale
img7 = cv2.cvtColor(img5,cv2.COLOR_BGR2GRAY)
img8 = cv2.cvtColor(img6,cv2.COLOR_BGR2GRAY)
cv2.imshow('Dog',img7)
cv2.imshow('Cat',img8)
# finding fourier of two images
img9 =  cv2.dft(np.float32(img7),flags = cv2.DFT_COMPLEX_OUTPUT)
fourier1_shift = np.fft.fftshift(img9)
magnitude = 20*np.log(cv2.magnitude(fourier1_shift[:,:,0],fourier1_shift[:,:,1]))
magnitude = cv2.normalize(magnitude, None, 0, 1, cv2.NORM_MINMAX, cv2.CV_32F)
img10 =  cv2.dft(np.float32(img8),flags = cv2.DFT_COMPLEX_OUTPUT)
fourier2_shift = np.fft.fftshift(img10)
magnitude1 = 20*np.log(cv2.magnitude(fourier2_shift[:,:,0],fourier2_shift[:,:,1]))
magnitude1 = cv2.normalize(magnitude1, None, 0, 1, cv2.NORM_MINMAX, cv2.CV_32F)

cv2.imshow('Fourier 1',magnitude)
cv2.imshow('Fourier 2',magnitude1)
rows , col = img7.shape
crow,ccol = rows//2 , col//2
mask = np.zeros((rows,col,2),np.uint8)
mask1 = np.ones((rows,col,2),np.uint8)
mask[crow-15:crow+15 , ccol-15:ccol+15]=1
mask1=mask1-mask
a = np.ones((rows,col))
b = np.zeros((rows,col))
b[crow-20:crow+20 ,ccol-20:ccol+20]=1
a=a-b
cv2.imshow('Low pass',b)
cv2.imshow('High pass',a)
f1_after = np.multiply(mask[: , : , 0],magnitude)
f2_after = np.multiply(mask1[: , : , 0],magnitude1)
cv2.imshow('Fourier1 after filter',f1_after)
cv2.imshow('fourier2 after filter',f2_after)
f2shift = np.multiply(fourier2_shift,mask1)
f1shift = np.multiply(fourier1_shift,mask)
f_1shift = np.fft.ifftshift(f1shift)
f_2shift = np.fft.ifftshift(f2shift)
img1_back = cv2.idft(f_1shift)
img2_back = cv2.idft(f_2shift)
img1_back = cv2.magnitude(img1_back[:,:,0],img1_back[:,:,1])
img2_back = cv2.magnitude(img2_back[:,:,0],img2_back[:,:,1])
img1_back = cv2.normalize(img1_back, None, 0, 1, cv2.NORM_MINMAX, cv2.CV_32F)
img2_back = cv2.normalize(img2_back, None, 0, 1, cv2.NORM_MINMAX, cv2.CV_32F)
cv2.imshow('modified1',img1_back)
cv2.imshow('modified2',img2_back)
imgfinal = (img1_back+img2_back)/2
imgfinal = cv2.normalize(imgfinal, None, 0, 1, cv2.NORM_MINMAX, cv2.CV_32F)
cv2.imshow('Final',imgfinal)


cv2.waitKey(0)
    
    
    



    
    