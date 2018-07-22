# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 06:53:16 2017

@author: JUNAID
"""
import cv2 
import numpy as np

xPoints=[(1195.2381591796875,17.539106369018555)
,(937.64990234375, 64.34162902832031) 
,(940.8167114257812, 55.39308547973633) 
,(1225.3709716796875, 49.2425651550293) 
,(982.4801025390625, 48.333927154541016) 
,(939.9161987304688, 53.08941650390625) 
,(981.7363891601562, 53.277523040771484) 
,(1040.7928466796875, 97.88645935058594) ]

xPrimePoints=[(1151.4892578125, 75.1097412109375)
,(973.6874389648438, 58.0516471862793)
,(975.284912109375, 52.61429214477539)
,(886.1126708984375, 178.70864868164062)
,(1018.3585815429688, 44.8651123046875)
,(974.3494873046875, 50.034427642822266)
,(1017.7317504882812, 50.03559875488281)
,(1048.7313232421875, 82.11563873291016)]


A_Matrix=np.zeros((8, 9))
#b=np.zeros((1,9),dtype=float)
for i in range(len(A_Matrix)):
    A_Matrix[i][0]= (xPrimePoints[i][0])*(xPoints[i][0])
    A_Matrix[i][1]= xPrimePoints[i][0]*xPoints[i][1]
    A_Matrix[i][2]= xPrimePoints[i][0]
    A_Matrix[i][3]= xPrimePoints[i][1]*xPoints[i][0]
    A_Matrix[i][4]= xPrimePoints[i][1]*xPoints[i][1]
    A_Matrix[i][5]= xPrimePoints[i][1]
    A_Matrix[i][6]= xPoints[i][0]
    A_Matrix[i][7]= xPoints[i][1]
    A_Matrix[i][8]= 1
    


#computing fundamental matrix by svd of matrix A
U, S, V = np.linalg.svd(A_Matrix)
fundamental_mat = V[-1].reshape(3, 3)
print(fundamental_mat)
print("determinant of matrix is :")
print(np.linalg.det(fundamental_mat))

#

img_points1 = np.array(xPoints, dtype=float)
img_points2 = np.array(xPrimePoints, dtype=float)
# Psamos a obtener la matriz fundamental con el 
# algoritmo de los 8 puntos usando RANSAC
fundamental_mat, mask = cv2.findFundamentalMat(points1 = img_points1, 
                                         points2 = img_points2,
                                         method = cv2.FM_8POINT, 
                                         param1 = 10**-2,
                                         param2 = 10**-5)

print(fundamental_mat)
print("determinant of matrix is :")
print(np.linalg.det(fundamental_mat))
