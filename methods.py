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
        eachpattern.append(df[df[0] == pattern].dropna(how='all'))
    
    return patterns, eachpattern

#Empirical cumulative distribution function
def ecdf(data):
    x = np.sort(data)
    n = x.size
    y = np.arange(1, n+1) / n
    return(x,y)

def segmentdist(terminateddf, origindf, ongoingdf, convergeddf, divergeddf):
    labels = []
    sizes = []
    
    if not (terminateddf.empty):
        labels.append("Terminated")
        sizes.append(len(terminateddf))
    
    if not (origindf.empty):
        labels.append("Origin")
        sizes.append(len(origindf))
    
    if not (ongoingdf.empty):
        labels.append("Ongoing")
        sizes.append(len(ongoingdf))
    
    if not (convergeddf.empty):           
        labels.append("Converged")
        sizes.append(len(convergeddf))
    
    if not (divergeddf.empty):
        labels.append("Diverged")
        sizes.append(len(divergeddf))
    
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Percentage of each segment type')
    plt.show()
    
def segmentlen(terminateddf, origindf, ongoingdf, convergeddf, divergeddf):

    fig1, ax1 = plt.subplots(figsize=(10,10))
    
    if not (terminateddf.empty):
        x,y = ecdf(terminateddf[0])
        plt.scatter(x=x, y=y, label = "Terminated")
    
    if not (origindf.empty):
        x,y = ecdf(origindf[0])
        plt.scatter(x=x, y=y, label = "Origin")
    
    if not (ongoingdf.empty):
        x,y = ecdf(ongoingdf[0])
        plt.scatter(x=x, y=y, label = "Ongoing")
    
    if not (convergeddf.empty):           
        x,y = ecdf(convergeddf[0])
        plt.scatter(x=x, y=y, label = "Converged")
    
    if not (divergeddf.empty):
        x,y = ecdf(divergeddf[0])
        plt.scatter(x=x, y=y, label = "Diverged")
    
    ax1.legend()
    plt.xlabel('Length', fontsize=16)
    plt.ylabel('Cumulative probability', fontsize=16)
    plt.title('Length distributions for each segment type')
    
def segmentlen2(terminateddf, origindf, ongoingdf, convergeddf, divergeddf):
    data = [terminateddf[0], origindf[0], ongoingdf[0], convergeddf[0], divergeddf[0]]
    fig1, ax1 = plt.subplots()
    ax1.set_title("Length of each segment type")
    ax1.boxplot(data)
    
    plt.show()

def firstlen(terminateddf, origindf, ongoingdf, convergeddf, divergeddf):

    fig1, ax1 = plt.subplots(figsize=(10,10))
    
    if not (origindf.empty):
        x,y = ecdf(origindf[0])
        plt.scatter(x=x, y=y, label = "Origin")
    if not (ongoingdf.empty):
        x,y = ecdf(ongoingdf[1])
        plt.scatter(x=x, y=y, label = "Ongoing")
    if not (convergeddf.empty):            
        x,y = ecdf(convergeddf[1])
        plt.scatter(x=x, y=y, label = "Converged")
        
        x,y = ecdf(convergeddf[3])
        plt.scatter(x=x, y=y, label = "Converged2")
    if not (divergeddf.empty):
        x,y = ecdf(divergeddf[2])
        plt.scatter(x=x, y=y, label = "Diverged")
    
    ax1.legend()
    plt.xlabel('Length', fontsize=16)
    plt.ylabel('Cumulative probability', fontsize=16)
    plt.title('Length distributions for each segment type')
    
def secondlen(terminateddf, origindf, ongoingdf, convergeddf, divergeddf):

    fig1, ax1 = plt.subplots(figsize=(10,10))
    
    if not (terminateddf.empty):
        x,y = ecdf(terminateddf[0])
        plt.scatter(x=x, y=y, label = "Terminated")
    if not (ongoingdf.empty):
        x,y = ecdf(ongoingdf[2])
        plt.scatter(x=x, y=y, label = "Ongoing")
    if not (convergeddf.empty):            
        x,y = ecdf(convergeddf[2])
        plt.scatter(x=x, y=y, label = "Converged")
    if not (divergeddf.empty):
        x,y = ecdf(convergeddf[1])
        plt.scatter(x=x, y=y, label = "Diverged")
        
        x,y = ecdf(divergeddf[3])
        plt.scatter(x=x, y=y, label = "Diverged2")
    
    ax1.legend()
    plt.xlabel('Length', fontsize=16)
    plt.ylabel('Cumulative probability', fontsize=16)
    plt.title('Length distributions for each segment type')
    
def rename(data, patterns):
    order = ["origin", "terminated", "ongoing", "diverged", "converged"]
    for patternIndex in len(patterns):    
        data[data[1]==patterns[patternIndex]] = patternIndex[order]
    data[data[1].isin(order)]
    
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