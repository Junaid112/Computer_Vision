# -*- coding: utf-8 -*-
"""
Created on Mon May  8 11:22:23 2017

@author: 
"""



import cv2
import numpy as np
from matplotlib import pyplot as plt

# loading image

greyImage = cv2.imread('0000000002_grey.png')[:,:,0]# jsut took 1 matrix because this is alerady grey


# remove noise
img = cv2.GaussianBlur(greyImage,(3,3),0)

# convolute with proper kernels
cannyEdges = cv2.Canny(img,100,200) # canny edge detection
laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,2,0,ksize=5)  # x
sobely = cv2.Sobel(img,cv2.CV_64F,0,2,ksize=5)  # y

cv2.imshow('orignalImage',greyImage)
cv2.waitKey(3000)
cv2.destroyAllWindows() 

cv2.imshow('cannyEdges',cannyEdges)
cv2.imshow('laplacian',laplacian)
cv2.imshow('sobelx',sobelx)
cv2.imshow('sobely',sobely)
cv2.waitKey(45000)
cv2.destroyAllWindows()

######################################### to show as plot

#plt.subplot(2,2,1),plt.imshow(cannyEdges,cmap = 'gray')
#plt.title('cannyEdges'), plt.xticks([]), plt.yticks([])
#plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
#plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
#plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
#plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
#plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
#plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
#plt.show()