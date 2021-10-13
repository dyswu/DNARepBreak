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
from methods import *

def visualizesim():
    record = []
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
    
    #Run first time and show results 
    
    #Sample parameters:
    #1, 1000, 100, 1, 5, 100, 100, 1000, 1, 1, 1000
    sim = simulation(length, n, mins, maxs, tone, ttwo, tframe, speed1, speed2)
    
    for i in range(steps):
        sim.step()
        record.append(sim.track.copy())
    
    plt.imshow(np.array(record), interpolation='nearest', aspect='auto')
    plt.colorbar()
    plt.xlabel("Position")
    plt.ylabel("Time")
    plt.show()
    
def generatesim():
    runs = int(input("Enter number of iterations: "))-1
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
    
    #Run first time and show results 
    
    #Sample parameters:
    #1, 1000, 100, 1, 5, 100, 100, 1000, 1, 1, 1000
    sim = simulation(length, n, mins, maxs, tone, ttwo, tframe, speed1, speed2)
    
    for i in range(steps):
        sim.step()
        #print(sim.track)
    
    terminated, origin, ongoing, converged, diverged = parse(sim.track)
    
    #Build first dataset
    terminateddf = pd.DataFrame(terminated)
    origindf = pd.DataFrame(origin)
    ongoingdf = pd.DataFrame(ongoing)
    convergeddf = pd.DataFrame(converged)
    divergeddf = pd.DataFrame(diverged)
    
    #repeat runs
    for i in range(runs):
        sim = simulation(length, n, mins, maxs, tone, ttwo, tframe, speed1, speed2)
    
        for i in range(steps):
            sim.step()
            
        terminated, origin, ongoing, converged, diverged = parse(sim.track)
    
        #Add new datasets
        terminatedtemp = pd.DataFrame(terminated)
        origintemp = pd.DataFrame(origin)
        ongoingtemp = pd.DataFrame(ongoing)
        convergedtemp = pd.DataFrame(converged)
        divergedtemp = pd.DataFrame(diverged)
        
        terminateddf = pd.concat([terminateddf, terminatedtemp], ignore_index=True)
        origindf = pd.concat([origindf, origintemp], ignore_index=True)
        ongoingdf = pd.concat([ongoingdf, ongoingtemp], ignore_index=True)
        convergeddf = pd.concat([convergeddf, convergedtemp], ignore_index=True)
        divergeddf = pd.concat([divergeddf, divergedtemp], ignore_index=True)
        
    #plot sim data
    segmentdist(terminateddf, origindf, ongoingdf, convergeddf, divergeddf)
    
    segmentlen(terminateddf, origindf, ongoingdf, convergeddf, divergeddf)
    
    segmentlen2(terminateddf, origindf, ongoingdf, convergeddf, divergeddf)
    
    firstlen(terminateddf, origindf, ongoingdf, convergeddf, divergeddf)
    
    secondlen(terminateddf, origindf, ongoingdf, convergeddf, divergeddf)
    
    #Format dataframe and save to csv
    terminateddf.insert(0, "Type", ["terminated"]*len(terminateddf))
    origindf.insert(0, "Type", ["origin"]*len(origindf))
    ongoingdf.insert(0, "Type", ["ongoing"]*len(ongoingdf))
    convergeddf.insert(0, "Type", ["converged"]*len(convergeddf))
    divergeddf.insert(0, "Type", ["diverged"]*len(divergeddf))
    
    total = pd.concat([terminateddf, origindf, ongoingdf, convergeddf, divergeddf], ignore_index=True)
    
    total.to_csv('simmaRTA.csv', index=False)
    
visualizesim()
generatesim()
