import random
from replisome import *

random.seed()

class simulation:  
    #length of track, number of replisomes, min speed, max speed, percentage time 1, percentage time 2, 
    #speed modifier for 1st label, speed modified for 2nd label
    
    def __init__(self, length, n, mins, maxs, tone, ttwo, speed1, speed2):
        self.time = 1000
        self.current = 0
        self.type = 0

        combinet = tone + ttwo
        self.before = random.randint(0, self.time-combinet)
        self.switch = self.before+tone
        self.after = self.switch+ttwo
        
        self.length = length
        self.track = [-1] * length
        self.replisomes = []
        self.stopped = []
        #Create positive and negative direction for each origin event
        for i in range(n):
            startloc = random.randint(1, length-1)
            starttime = random.randint(0, self.time)
            
            self.replisomes.append(replisome(startloc, 
                                             starttime, 
                                             round(random.randint(mins, maxs)*speed1)))
            self.replisomes.append(replisome(startloc-1, 
                                             starttime, 
                                             -round(random.randint(mins, maxs)*speed2)))
        #for i in range(len(self.replisomes)):
            #print(self.replisomes[i].loc, self.replisomes[i].time, self.replisomes[i].speed)
    def step(self):
        #set up current label
        if (self.current == self.before):
            self.type = 1
        if (self.current == self.switch):
            self.type = 2
        if (self.current == self.after):
            self.type = 0
        
        #Run through all replisomes in the set
        for replisome in self.replisomes:
            location = replisome.loc
            speed = replisome.speed
            age = self.current - replisome.time
            
            #Check if current replisome stops at current time
            if (age*random.random() > self.time/len(self.replisomes)):
                #print("stop old age", replisome.speed)
                replisome.update(location, False)
                self.stopped.append(replisome)
                self.replisomes.remove(replisome)
                break
            if (replisome.check(self.current)):
                if (location >= self.length-1 or location <= 0):
                    replisome.update(location, False)
                    self.stopped.append(replisome)
                    self.replisomes.remove(replisome)
                    break
                if (speed > 0):
                    for i in range(speed):
                        if (location >= self.length-1):
                            #print("reach end")
                            self.stopped.append(replisome)
                            self.replisomes.remove(replisome)
                            break
                        if (self.track[location] == -1):
                            self.track[location] = self.type
                            location += 1
                            replisome.update(location, True)
                        else:
                            replisome.update(location, False)
                            self.stopped.append(replisome)
                            self.replisomes.remove(replisome)
                            break
                else:
                    for i in range(abs(speed)):
                        if (location <= 0):
                            #print("reach begining")
                            replisome.update(location, False)
                            self.stopped.append(replisome)
                            self.replisomes.remove(replisome)
                            break
                        if (self.track[location] == -1):
                            self.track[location] = self.type
                            location -= 1
                            replisome.update(location, True)
                        else:
                            replisome.update(location, False)
                            self.stopped.append(replisome)
                            self.replisomes.remove(replisome)
                            break
        self.current += 1
        
    def gettrack(self):
        return self.track
        
                