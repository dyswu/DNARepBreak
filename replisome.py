# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 02:14:27 2021

@author: derew
"""

class replisome:
    #Starting location, starting time, forward speed, backwards speed
    def __init__(self, start, time, speed):
        self.active = False
        self.loc = start
        self.time = time
        self.speed = speed
    
    def check(self, current):
        if(self.active):
            return True
        if(self.time == current):
            self.active = True
            return True
        return False
        
    def update(self, newloc, status):
        self.loc = newloc
        self.active = status          
            