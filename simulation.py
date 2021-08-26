# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 02:14:10 2021

@author: derew
"""

class simulation:  
    #length of track, number of replisomes, min speed, max speed, percentage time 1, percentage time 2
    def __init__(self, length, n, mins, maxs, tone, ttwo):
        self.time = 100
        self.current = 0
        self.type = 0

        combinet = tone + ttwo
        self.before = random.randint(0, self.time-combinet)
        self.switch = self.before+tone
        self.after = self.switch+ttwo
        
        self.length = length
        self.track = [-1] * length
        self.replisomes = []
        #Create positive and negative direction for each origin event
        for i in range(n):
            startloc = random.randint(1, length-1)
            starttime = random.randint(0, self.time)
            
            self.replisomes.append(replisome(startloc, 
                                             starttime, 
                                             random.randint(mins, maxs)))
            self.replisomes.append(replisome(startloc-1, 
                                             starttime, 
                                             -random.randint(mins, maxs)))
        #for i in range(len(self.replisomes)):
            #print(self.replisomes[i].loc, self.replisomes[i].time, self.replisomes[i].speed)
    def step(self):
        if (self.current == self.before):
            self.type = 1
        if (self.current == self.switch):
            self.type = 2
        if (self.current == self.after):
            self.type = 0
            
        for replisome in self.replisomes:
            location = replisome.loc
            speed = replisome.speed
            if (replisome.check(self.current)):
                if (location >= self.length-1 or location <= 0):
                    replisome.update(location, False)
                    self.replisomes.remove(replisome)
                if (speed > 0):
                    for i in range(speed):
                        if (self.track[location] == -1):
                            self.track[location] = self.type
                            location += 1
                            replisome.update(location, True)
                        else:
                            replisome.update(location, False)
                            #self.replisomes.remove(replisome)
                            break
                else:
                    for i in range(abs(speed)):
                        if (self.track[location] == -1):
                            self.track[location] = self.type
                            location -= 1
                            replisome.update(location, True)
                        else:
                            replisome.update(location, False)
                            #self.replisomes.remove(replisome)
                            break
        self.current += 1
        
                