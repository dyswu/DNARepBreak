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
#length of total, number of replisomes, min speed, max speed, % of the time in label 1, % of time in label 2, label 1 speed(%), label 2 speed(%)
sim = simulation(10000, 100, 5, 10, 100, 100, 1, 1)
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

for i in range(1000):
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