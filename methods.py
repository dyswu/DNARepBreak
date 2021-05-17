# -*- coding: utf-8 -*-
"""
Methods for DigestionGUI modeling

Created on Sun Apr 18 16:30:12 2021

@author: derew
"""

# import for digestions
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

def loaddata(originalpath, treatmentpath):
    original = pd.read_csv(originalpath, header=None)
    treatment = pd.read_csv(treatmentpath, header=None)
    
    dfOrig = pd.DataFrame(original);
    dfOrig = dfOrig.dropna(how = "all");
    
    dfTreat = pd.DataFrame(treatment);
    dfTreat = dfTreat.dropna(how = "all");
    
    return dfOrig, dfTreat

def simplify(df):
    patterns = df[0].unique;
    # if in segment1/segment2 pattern, if patterns are named no need
    #patternsSorted = patterns.sort(key = lambda e: (len(e), e[0]))
    eachpattern = [];
    
    for pattern in patterns: #Sorted:
        eachpattern.append(df[df[0] == pattern])
    
    return patterns, eachpattern

#Empirical cumulative distribution function
def ecdf(data):
    x = np.sort(data)
    n = x.size
    y = np.arange(1, n+1) / n
    return(x,y)

#Generate Table function uniform
def lindigestGandR(data):
    values = data#[1]
    random.seed()
    maxLength = 200#max(values)
    newValues = []
    for i in values:
        breakage = (random.random()*maxLength)
        if breakage < i:
            newValues.append(i-breakage)
            newValues.append(breakage)
        else:
            newValues.append(i)
    return newValues

#Generate Table function normal
def normdigestGandR(data, mu, sigma):
    values = data
    random.seed()
    maxLength = max(values)
    newValues = []
    for i in values:
        breakage = (abs(random.normalvariate(mu, sigma)*maxLength))
        if breakage < i:
            newValues.append(i-breakage)
            newValues.append(breakage)
        else:
            newValues.append(i)
    return newValues

#Generate Table function triangular
def tridigestGandR(data, low, high):
    values = data[1]
    random.seed()
    maxLength = values.max()
    newValues = []
    for i in values:
        breakage = (random.triangular(low, high, mode)*maxLength)
        if breakage < i:
            newValues.append(i-breakage)
            newValues.append(breakage)
        else:
            newValues.append(i)
    return newValues

#Generate Table function, gauss
def guassdigestGandR(data, mu, sigma):
    values = data[1]
    random.seed()
    maxLength = values.max()
    newValues = []
    for i in values:
        breakage = (random.gauss(mu, sigma)*maxLength)
        if breakage < i:
            newValues.append(i-breakage)
            newValues.append(breakage)
        else:
            newValues.append(i)
    return newValues

#Generate Table function, beta distribution
def betadigestGandR(data, alpha, beta):
    values = data[1]
    random.seed()
    maxLength = values.max()
    newValues = []
    for i in values:
        breakage = (random.betavariate(alpha, beta)*maxLength)
        if breakage < i:
            newValues.append(i-breakage)
            newValues.append(breakage)
        else:
            newValues.append(i)
    return newValues

#Generate Table function, exponential distribution
def expdigestGandR(data, lambd):
    values = data#[1]
    random.seed()
    maxLength = max(values)
    newValues = []
    for i in values:
        breakage = (random.expovariate(1)*maxLength)
        if breakage < i:
            newValues.append(i-breakage)
            newValues.append(breakage)
        else:
            newValues.append(i)
    return newValues

#Generate Table function, uniform
#uniform digestion method (2 sections combined as 1)
def lindigestGRT(data):
    df = data.reset_index(drop=True)
    random.seed()
    maxLength = df[3].max()
    newTotal = []
    newGreen = []
    newRed = []
    newSingRed = []
    newSingGreen = []
    for i in range(len(data)):
        breakage = (random.random()*maxLength)
        if breakage < df[3][i]:
            newTotal.append(df[3][i]-breakage)

            if df[1][i] > breakage:
                newSingGreen.append(breakage)
                newGreen.append(df[1][i] - breakage)
                newRed.append(df[2][i])
                
            else:
                newRed.append(breakage - df[1][i])
                newSingRed.append(df[3][i]-breakage)
                newGreen.append(df[1][i])
                
        else:
            newGreen.append(df[1][i])
            newRed.append(df[2][i])
            newTotal.append(df[3][i])
    
    newValues = pd.DataFrame({1:pd.Series(newGreen), 2:pd.Series(newRed), 3:pd.Series(newTotal), 
                              4:pd.Series(newSingGreen), 5:pd.Series(newSingRed)})
    return newValues

#Generate Table function each side independant, uniform
#uniform digestion method (2 sections independant)
def lindigestGRT2(data):
    df = data.reset_index(drop=True)
    random.seed()
    maxLengthG = df[1].max()
    maxLengthR = df[2].max()
    newTotal = []
    newGreen = []
    newRed = []
    newSingRed = []
    newSingGreen = []
    for i in range(len(data)):
        breakageG = (random.random()*maxLengthG)
        breakageR = (random.random()*maxLengthR)
        
        if breakageG < df[1][i]:
            newSingGreen.append(breakageG)
            newGreen.append(df[1][i]-breakageG)
        else:
            newGreen.append(df[1][i])

        if breakageR < df[2][i]:
            newSingRed.append(df[2][i] - breakageR)
            newRed.append(breakageR)
        else:
            newRed.append(df[2][i])
            
        newTotal.append(newGreen[-1] + newRed[-1])
    
    newValues = pd.DataFrame({1:pd.Series(newGreen), 2:pd.Series(newRed), 3:pd.Series(newTotal), 
                              4:pd.Series(newSingGreen), 5:pd.Series(newSingRed)})
    return newValues

#Generate Table function each side independant, uniform
#normal digestion method (2 sections independant)
def normdigestGRT(data, mu, sigma):
    df = data.reset_index(drop=True)
    random.seed()
    maxLengthG = df[1].max()
    maxLengthR = df[2].max()
    newTotal = []
    newGreen = []
    newRed = []
    newSingRed = []
    newSingGreen = []
    for i in range(len(data)):
        breakageG = abs((random.normalvariate(mu, sigma)*maxLengthG))
        breakageR = abs((random.normalvariate(mu, sigma)*maxLengthR))
        
        if breakageG < df[1][i]:
            newSingGreen.append(breakageG)
            newGreen.append(df[1][i]-breakageG)
        else:
            newGreen.append(df[1][i])

        if breakageR < df[2][i]:
            newSingRed.append(df[2][i] - breakageR)
            newRed.append(breakageR)
        else:
            newRed.append(df[2][i])
            
        newTotal.append(newGreen[-1] + newRed[-1])
    
    newValues = pd.DataFrame({1:pd.Series(newGreen), 2:pd.Series(newRed), 3:pd.Series(newTotal), 
                              4:pd.Series(newSingGreen), 5:pd.Series(newSingRed)})
    return newValues

