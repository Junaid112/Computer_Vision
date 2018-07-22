# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 15:45:16 2017

@author: JUNAID
"""

import random
import numpy as np
import matplotlib.pyplot as plt

def augment(xys):
	axy = np.ones((len(xys), 3))
	axy[:, :2] = xys
	return axy

def estimate(xys):
    axy = augment(xys[:2])
    return np.linalg.svd(axy)[-1][-1, :]
def is_inlier(coeffs, xy, threshold):
    return np.abs(coeffs.dot(augment([xy]).T)) < threshold

def run_ransac(data, estimate, is_inlier, sample_size, goal_inliers, max_iterations, stop_at_goal=True, random_seed=None):
    best_ic = 0 # count best inlier contain
    best_model = None  # object for best modal
    random.seed(random_seed)
    for i in range(max_iterations):
        s = random.sample(data, int(sample_size)) # get random sample from data
        m = estimate(s) # estimate modal for this new sample
        ic = 0
        for j in range(len(data)):
            if is_inlier(m, data[j]):    # here cout inliers for new model
                ic += 1
        print(s)
        print('estimate:', m)
        print('# inliers:', ic)

        if ic > best_ic: # if num of inliers are greater that last best inliers contain count then update
            best_ic = ic  # update new count for inliers
            best_model = m   # update new best moda fit for this sampel data 
            if ic > goal_inliers and stop_at_goal:    # max inliers doals or till threshold acheive then we stop
                break
    print('took iterations:', i+1, 'best model:', best_model, 'explains:', best_ic)
    return best_model, best_ic

Data=[(1,1.01),(2,-4.22),(1,8.97),(1,0.97), (8,64.006), (-7, 48.978)]


n = 100
max_iterations = 100
goal_inliers = n * 0.3

	# RANSAC
m, b = run_ransac(Data, estimate, lambda x, y: is_inlier(x, y, 0.01),3, goal_inliers, max_iterations,True, 20)
a, b, c = m
plt.plot([0, 10], [-c/b, -(c+10*a)/b], color=(0, 1, 0))
