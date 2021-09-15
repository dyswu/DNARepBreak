# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 17:47:43 2021

@author: derew
"""

#parse
def parse(set):
    temp = np.array(set)
    temp[temp == -1] = 0
    
    current = []

    terminated = [] #1
    origin = [] #2
    
    ongoing = [] #1, 2 

    converged = [] #1,2,1
    diverged = [] #2,1,2
    extra = [] #etc
    
    for i in range(len(temp)):
        if (temp[i] != 0):
            current.append(temp[i])
        if (current != [] and temp[i] == 0): #if current string ended
            count(current)
            total = len(current)
            one = len(first)
            two = len(second)
            three = len(third)
            
    #return terminated, origin, ongoing, converged, diverged
    return current
    
def count(array):
    return array