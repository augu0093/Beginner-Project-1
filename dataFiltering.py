# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 13:04:35 2018

@author: Andreas Nilausen
"""

# FILTERING BY BACTERIA TYPE
# This function filters the given data by type of bacteria. It uses a for-loop to
# go through the data and appends the filtered data to a new array. It takes 
# in a user input (code for the type of bacteria, 1-4) and a set of data as an array. 
# It outputs a new set of sorted data as an array which is used furter along in the
# program.

import numpy as np

def sortBacteriaType(choice, data):
    # To filter the bacteria an empty array to append to is defined.
    sortedBacteriaType = np.array([])
    # If the user chooses 1, it appends the elements of the third column with
    # the value 1 to the empty array. This is done by using a for loop which
    # runs through the data set. 
    if choice == 1:
        for line in data:
            if line[2] == int(1):
                sortedBacteriaType = np.append(sortedBacteriaType, line)
                # Lastly the data is reshaped into a "N x 3" matrix.  
                sortedBacteriaType = np.reshape(sortedBacteriaType, (int(len(sortedBacteriaType) / 3), 3))
       
    # If the user chooses 2, the same operations are applied.
    if choice == 2:
        for line in data:
            if line[2] == int(2):
                sortedBacteriaType = np.append(sortedBacteriaType, line)
                # # Lastly the data is reshaped into a "N x 3" matrix.
                sortedBacteriaType = np.reshape(sortedBacteriaType, (int(len(sortedBacteriaType) / 3), 3))

    # If the user chooses 3...
    if choice == 3:
        for line in data:
            if line[2] == int(3):
                sortedBacteriaType = np.append(sortedBacteriaType, line)
                sortedBacteriaType = np.reshape(sortedBacteriaType, (int(len(sortedBacteriaType) / 3), 3))

    # If the user chooses 4...
    if choice == 4:
        for line in data:           
            if line[2] == int(4):
                sortedBacteriaType = np.append(sortedBacteriaType, line)
                sortedBacteriaType = np.reshape(sortedBacteriaType, (int(len(sortedBacteriaType) / 3), 3))
        
        
    # Lastly the "sortedBacteriaType"-array is returned
    return sortedBacteriaType
    
  
# FILTERING BY GROWTH RATE
# This function filters the data by growth rate. It uses if-statements to print
# error messages. Furthermore it uses a for-loop to go through the data and append
# the filtered rows to a new array.
# It takes in a lower limit and an upper limit of growth rates and a set of data.
# The function outputs a new array with the filtered data. 

def sortGrowthRate(lowerLimit, upperLimit, data):
    # If the lower limit is below the minimum of the growth rate and the upper limit
    # is also below the minimum of the data, an error message is printed. 
    if lowerLimit < data[:,1].min() and upperLimit < data[:,1].min():
        print("There are no elements in the data set within the desired limits. Please try again with larger values.")
    
    # If the upper limit is above the maximum of the growth rate and the lower limit is
    # also above the maximum of the growth rate, an error message is printed.
    if upperLimit > data[:,1].max() and lowerLimit > data[:,1].max():
        print("There are no elements in the data set within the desired limits. Please try again with smaller values.")

    # If the lower limit and the upper limit are identical there is no interval.
    # Therefore an error message is also printed. 
    if lowerLimit == upperLimit:
        print("The boundries of the interval seem to be equal. Please try again.")

    # An empty array to append the valid data to is defined. 
    sortedGrowthRate = np.array([])

    # A for-loop which runs over the data is used to append the data to the empty array. 
    for line in data:
        if line[1] >= lowerLimit and line[1] <= upperLimit:
            sortedGrowthRate = np.append(sortedGrowthRate, line)
        
            # The new data is reshaped into a "N x 3" matrix.
            sortedGrowthRate = np.reshape(sortedGrowthRate, (int(len(sortedGrowthRate) / 3), 3))

    # Lastly the variable is returned
    return sortedGrowthRate












    
    
    
    
    
    
    
    
    
    
    
    
    
    