# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 13:06:56 2018

@author: August
"""

# This function calculates different statistical values from the data set. It sorts 
# temperatures and growth rates for using in the calculation and prints error messages
# if the requirements of the desired output is not met. 
# It takes in a set of data and the desired statistical output and puts out the
# computed statistical figure. 

import numpy as np
import statistics as stat

def dataStatistics(data, statistics):        
    # Data lists for temperature and growth rate as well as growth rate lists for
    # temperatures under 20C and 50C are defined. 
    temp = []
    g_rate = []
    cold_temp = []
    hot_temp = []
    # The temperatures and growth rates are appended to the lists.
    for row in data:
        temp.append(row[0])
        g_rate.append(row[1])
        # The growth rates for temperatures under 20C and over 50C are appended.
        if row[0]<20:
            cold_temp.append(row[1])
        elif row[0]>50:
            hot_temp.append(row[1])

    # It is checked if the size og the data set is big enough for calculating the standard deviation.  
    # If it is not, an error message is printed. 
    if len(temp) < 2 and statistics == "Standard Deviation of Temperature" or len(temp) < 2 and statistics == "Standard Deviation of Growth Rate":
        result = "Error: Size of current dataset must be bigger than 1 to calculate standard deviation." 
    
    # Errormessage for mean-calculations in case dataset has no values
    elif len(temp) == 0 and statistics == "Mean Temperature" or len(temp) == 0 and statistics == "Mean Growth Rate":
        result = "Error: Size of current dataset is 0, therefor no mean can be calculated."
    
    # Calculating mean temperature.
    elif statistics == "Mean Temperature":
        result = np.mean(temp)
    
    # Calculating mean growth rate.
    elif statistics == "Mean Growth Rate":
        result = np.mean(g_rate)
    
    # Calculating standard deviation (std) of temperature.
    elif statistics == "Standard Deviation of Temperature":
        result = stat.stdev(temp)
    
    # Calculating std of growth rate.
    elif statistics == "Standard Deviation of Growth Rate":
        result = stat.stdev(g_rate)
    
    # Returning number of rows.
    elif statistics == "Number of Rows":
        if len(temp) == 0:
            result = "There are no rows in current dataset."
        else:
            result = len(temp)
    
    # Calculating the growth rate for temperatures less than 20C
    elif statistics == "Mean Cold Growth Rate":
        if len(cold_temp) == 0:
            result = "No growth rates recorded at temperature under 20 degrees."
        else:
            result = np.mean(cold_temp)
    
    # Calculating growth rates for temperatures higher than 50C
    elif statistics == "Mean Hot Growth Rate":
        if len(hot_temp) == 0:
            result = "No growth rates recorded at temperature over 50 degrees."
        else:
            result = np.mean(hot_temp)
    
    # Returning the calculated statistical value.              
    return result

