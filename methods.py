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
    patterns = df[0].unique();
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

def compare(data1, data2):
    
    data1Origin
    data1Terminated
    data1Ongoing
    data1Diverged
    data1Converged
    
    data2Origin
    data2Terminated
    data2Ongoing
    data2Diverged
    data2Converged