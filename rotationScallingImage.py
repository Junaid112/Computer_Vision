# -*- coding: utf-8 -*-
"""
Created on Mon May  8 11:22:23 2017

@author:  JUNAID AHMED GHAURI
"""



import numpy as np
import cv2


image = cv2.imread('image_02//data/0000000002.png')
rows,cols = image[:,:,0].shape

                 
########## orignal image #############
cv2.imshow('Orignal Image',image)
cv2.waitKey(2000)
cv2.destroyAllWindows()  

########## Translation transformation shift in x=5- and y=50 ############
TransformationMatrix = np.float32([[1,0,50],[0,1,50]])
resultantImage = cv2.warpAffine(image,TransformationMatrix,(cols,rows))
cv2.imshow('Translated Image',resultantImage)
cv2.waitKey(2000)
cv2.destroyAllWindows()  

######## Rotation transformation 180 degree anti-clockwise######

TransformationMatrix = cv2.getRotationMatrix2D((cols/2,rows/2),180,1)
resultantImage = cv2.warpAffine(image,TransformationMatrix,(cols,rows))
cv2.imshow('Image After Rotation',resultantImage)
cv2.waitKey(2000)
cv2.destroyAllWindows() 


######## Scale to half then 90 degree clockwise######
scaleImage =  cv2.resize(image, (0,0), fx=0.5, fy=0.5) 
scaleRows,scaleCols=scaleImage[:,:,0].shape
cv2.imshow('Scaled_Image',scaleImage)
cv2.waitKey(2000)
cv2.destroyAllWindows() 

RotationMatrix= cv2.getRotationMatrix2D((scaleCols/2,scaleRows/2),-90,1)

resultantImage = cv2.warpAffine(scaleImage,RotationMatrix,(scaleCols,scaleRows))
cv2.imshow('Scaled and Rotated Image ',resultantImage)
cv2.waitKey(2000)
cv2.destroyAllWindows() 
