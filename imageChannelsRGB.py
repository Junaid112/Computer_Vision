# -*- coding: utf-8 -*-
"""
Created on Mon May  8 11:22:23 2017

@author: ""
"""



import numpy as np
import cv2


colorImage=cv2.imread("0000000002_color.png")
cv2.imshow("ColorImage",colorImage)
cv2.waitKey(2000)
RedChannel=colorImage[:,:,2]
BlueChannel=colorImage[:,:,1]
GreenChannel=colorImage[:,:,0]

cv2.imshow("Red_Channel",RedChannel)
cv2.imshow("Green_Channel",GreenChannel)
cv2.imshow("Blue_Channel",BlueChannel)
cv2.waitKey(2000)
cv2.destroyAllWindows() 

#################################to see different color channel explicitly uncomment below code for each portion separately
RedChannelFull=colorImage
RedChannelFull[:,:,0]=0
RedChannelFull[:,:,1]=0
cv2.imshow("Red_Channel_asRed",RedChannelFull)
cv2.waitKey(4000)
cv2.destroyAllWindows() 
