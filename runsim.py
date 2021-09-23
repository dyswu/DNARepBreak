# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 17:46:21 2021

@author: derew
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from simulation import *
from parse import *

record = []
#length of total, number of replisomes, min speed, max speed, time in label 1, time in label 2, starting timeframe, label 1 speed(%), label 2 speed(%)

length = int(input("Enter total tract length: "))
n = int(input("Enter number of replisomes: "))
mins = int(input("Enter minimum replisome speed: "))
maxs = int(input("Enter maximum replisome speed: "))
tone = int(input("Enter time in label 1: "))
ttwo = int(input("Enter time in label 2: "))
tframe = int(input("Enter initialization time frame: "))
speed1 = int(input("Enter % speed modifier for label 1 (as a decimal): "))
speed2 = int(input("Enter % speed modifier for label 2 (as a decimal): "))
steps = int(input("Enter how long to run the simulation for (time): "))

#1000, 100, 3, 7, 100, 100, 1000, 1, 1, 1000
sim = simulation(length, n, mins, maxs, tone, ttwo, tframe, speed1, speed2)
print("time = ", sim.time, 
      "current time = ",
      sim.current, 
      "current type = ",
      sim.type,
      "time before = ",
      sim.before, 
      "time of switch = ",
      sim.switch, 
      "time of return = ",
      sim.after)

for i in range(steps):
    sim.step()
    record.append(sim.track.copy())
    #print(sim.track)

plt.imshow(np.array(record), interpolation='nearest', aspect='auto')
plt.colorbar()
plt.show()
#record.copy()

terminated, origin, ongoing, converged, diverged = parse(sim.track)

terminateddf = pd.DataFrame(terminated)
origindf = pd.DataFrame(origin)
ongoingdf = pd.DataFrame(ongoing)
convergeddf = pd.DataFrame(converged)
divergeddf = pd.DataFrame(diverged)