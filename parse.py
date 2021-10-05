# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 17:47:43 2021

@author: derew
"""
import numpy as np

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
            
        elif (current != [] and temp[i] == 0): #if current string ended
            one, two, three = count(current)
            total = len(current)
            #print(one, two, three, total)
            
            if (one == []): #if >3 segment
                doNothing = True
                #do nothing
            elif (one[0] == 1 and two == []): #if only 1st track segment (origin)
                origin.append(total)
            elif (one[0] == 2 and two == []): #if only 2nd track segment (terminated)
                terminated.append(total)
            elif (one[0] == 1 and two[0] == 2 and three == []): #if 1st and 2nd track segment (ongoing)
                ongoing.append([total, one[1], two[1]])
            elif (one[0]== 2 and two[0]== 1 and three == []): #if 1 and 2nd tracks in other order (ongoing)
                ongoing.append([total, two[1], one[1]])
            elif (one[0] == 1 and two[0] == 2 and three[0] == 1): #if 1 2 1 (converged)
                converged.append([total, one[1], two[1], three[1]])
            elif (one[0] == 2 and two[0] == 1 and three[0] == 2): #if 2 1 2 (diverged)
                diverged.append([total, one[1], two[1], three[1]])
                
            current = []
            
    return terminated, origin, ongoing, converged, diverged
    #return current
    
def count(array):
    first = []
    second = []
    third = []
    
    track = 1
    current = array[0]
    length = 0
    
    for i in range(len(array)):
        if (array[i] == current):
            length+=1
        elif (array[i] != current):
            if (track == 1): #End first tract
                first = [current, length]
            elif (track == 2): #End 2nd tract
                second = [current, length]
            elif (track == 3): #end third tract
                third = [current, length]
            else: 
                return [],[],[] #Discard >3 segment tracts
            
            current = array[i]
            length = 1
            track += 1
            
    #Check last tract
    if (track == 1): #End first tract
        first = [current, length]
    elif (track == 2): #End 2nd tract
        second = [current, length]
    elif (track == 3): #end third tract
        third = [current, length]
    else:  #end >3 tracts
        return [],[],[] #Discard >3 segment tracts
    
    return first, second, third