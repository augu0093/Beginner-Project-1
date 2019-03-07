# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 10:00:34 2018

@author: Andreas Nilausen
"""

import numpy as np
import matplotlib.pyplot as plt

# PLOT 1 - BAR CHART
# This function computes the frequencies of each type of bacteria in the given data
# set. It also plots a bar chart of the bacteria types by frequency in different
# colors.
# It takes in a set of data and outputs a bar chart of the types of bacteria. 
def barChart(data):
    # The data has to be sorted by the frequencies of the given type of bacteria. For
    # this four variables with the value of zero is defined. 
    frequencyBacteriaType1 = 0
    frequencyBacteriaType2 = 0
    frequencyBacteriaType3 = 0
    frequencyBacteriaType4 = 0

    # Then a for-loop which runs over the data is used to compute the frequencies. It 
    # examines if elements of the third column is of type 1,2,3 or 4. 
    for line in data:
        if line[2] == int(1):
            frequencyBacteriaType1 += 1
            continue
        
        elif line[2] == int(2):
            frequencyBacteriaType2 += 1
            continue
        
        elif line[2] == int(3):
            frequencyBacteriaType3 += 1
            continue
        
        elif line[2] == int(4):
            frequencyBacteriaType4 += 1
            
    # Now the bar chart of the frequencies is defined and plotted. For this to happen
    # the frequencies are gathered in a list. 
    frequencies = [frequencyBacteriaType1, frequencyBacteriaType2, frequencyBacteriaType3, frequencyBacteriaType4]
    
    # The different bacteria types is defined to  be used as labels in the chart. 
    bacteriaTypes = ("Salmonella ent.", "Bacillus cer.", "Listeria", "Brocho. thermo.")
    
    # Positioning of the y-axis
    y_pos = np.arange(len(bacteriaTypes))

    # The features of the bar chart are defined.
    plt.bar(y_pos, frequencies, align="center", alpha=0.5, color =("r", "g", "b", "y"))
    plt.xticks(y_pos, bacteriaTypes)
    plt.ylabel("Frequency")
    plt.title("BACTERIA TYPES BY FREQUENCY")
    plt.show()
    
    # Lastly the function is returned. 
    return ""

# PLOT 2 - GROWTH RATE BY TEMPERATURE GRAPHS
# This function computes a plot with four graphs in the same window. It sorts the
# data into four different bacteria types and splits each type into temperature and 
# growth rate. Lastly it shows the graphs within the desired boundries.
# The function takes in a set of data and outputs a plot with the different 
# bacteria types. 

def gRateGraphs(data):
    # First the data is sorted by bacteria type so it is possible to plot each
    # type for itself. To do this four empty arrays are defined.
    bacteriaType1 = np.array([])
    bacteriaType2 = np.array([])
    bacteriaType3 = np.array([])
    bacteriaType4 = np.array([])
        
    # Then a for-loop which runs over the data is used to append the data into 
    # the different lists and hereby sorting the data bacteria type. 
    for line in data:
        # If the element in the third column is 1, the line is appened to bacteriaType1. 
        if line[2] == int(1):
            bacteriaType1 = np.append(bacteriaType1, line)
            continue
        # The same operations are used for the rest of the data.
        elif line[2] == int(2):
            bacteriaType2 = np.append(bacteriaType2, line)
            continue
        elif line[2] == int(3):
            bacteriaType3 = np.append(bacteriaType3, line)
            continue
        elif line[2] == int(4):
            bacteriaType4 = np.append(bacteriaType4, line)
        
    # Now the elements are sorted, though defined as a single one dimensional string. 
    # Therefore the data is reshaped into a "N x 3" matrix for further usage. 
    bacteriaType1 = np.reshape(bacteriaType1, (int(len(bacteriaType1) / 3), 3))
    bacteriaType2 = np.reshape(bacteriaType2, (int(len(bacteriaType2) / 3), 3))  
    bacteriaType3 = np.reshape(bacteriaType3, (int(len(bacteriaType3) / 3), 3))
    bacteriaType4 = np.reshape(bacteriaType4, (int(len(bacteriaType4) / 3), 3))

    # To make the correct plot, the data has to be sorted by temperature. That is 
    # the first column.
    bacteriaType1 = bacteriaType1[bacteriaType1[:, 0].argsort()]
    bacteriaType2 = bacteriaType2[bacteriaType2[:, 0].argsort()]
    bacteriaType3 = bacteriaType3[bacteriaType3[:, 0].argsort()]
    bacteriaType4 = bacteriaType4[bacteriaType4[:, 0].argsort()]

    # Then each bacteria type is split into temperature and growth rate. 

    # Bacteria type 1
    temperatureBacteriaType1 = bacteriaType1[:, 0]
    growthRateBacteriaType1 = bacteriaType1[:, 1]

    # Bacteria type 2
    temperatureBacteriaType2 = bacteriaType2[:, 0]
    growthRateBacteriaType2 = bacteriaType2[:, 1]

    # Bacteria type 3
    temperatureBacteriaType3 = bacteriaType3[:, 0]
    growthRateBacteriaType3 = bacteriaType3[:,1]

    # Bacteria type 4
    temperatureBacteriaType4 = bacteriaType4[:, 0]
    growthRateBacteriaType4 = bacteriaType4[:, 1]

    # The features of the bar chart are defined.
    plt.style.use("seaborn-darkgrid")
    plt.plot(temperatureBacteriaType1, growthRateBacteriaType1, "r")
    plt.plot(temperatureBacteriaType2, growthRateBacteriaType2, "g")
    plt.plot(temperatureBacteriaType3, growthRateBacteriaType3, "b")
    plt.plot(temperatureBacteriaType4, growthRateBacteriaType4, "y")

    # Limits and titles are defined.
    plt.title("GROWTH RATE BY TEMPERATURE")
    plt.xlabel("Temperature")
    plt.ylabel("Growth rate")
    plt.xlim([10, 60])
    plt.show()
    
    # The function is returned.
    return ""
