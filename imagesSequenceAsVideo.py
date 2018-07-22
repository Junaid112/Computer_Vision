# -*- coding: utf-8 -*-
"""
Created on Mon May  8 11:22:23 2017

@author: JUNAID AHMED GHAURI
"""



import numpy as np
import cv2


#############assume that images are in same folder and name as 0000000000, 0000000001----so on
n=22 #because we have 22 images in folder.. if your have different number of images change n to that much number
images=[] #I'll store all images in to this matrix
for i in range(n):
    cv2.waitKey(200) # you can vary speed 1000 means interval of one second
    images.append(cv2.imread(str(i).zfill(10)+'.png',cv2.IMREAD_GRAYSCALE))
    cv2.imshow('oneScene',images[i])
cv2.destroyAllWindows()     
    

########for example read image file
greyImage=cv2.imread("picgrey.jpg",cv2.IMREAD_GRAYSCALE)
# each cell will be a pixel value
print("A pixel value is: "+str(greyImage[5][5]))# any pixel # this is greyScale so value will be in 0-255
# we can cahnge pixel value by assignig, adding or subtract integer from it like:

greyImage[5][5]=195 # I just change value of pixel
print("A pixel value is: "+str(greyImage[5][5]))    
#or
greyImage[5][5]+=1 # I just ass one value can be any value
print("A pixel value is: "+str(greyImage[5][5]))    
#or
greyImage[5][5]-=1 # I just subtract 1 value
print("A pixel value is: "+str(greyImage[5][5]))    

