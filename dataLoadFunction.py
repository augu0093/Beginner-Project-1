# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 13:49:13 2018

@author: Andreas Nilausen
"""
# This function loads a text file from your computer, and loads in into an array.
# Furthermore it uses a for-loop to discard lines of data which do not fit within
# the boundries stated in the projecet description. The function prints the lines
# in which the errors occur.
# It takes in a text file and outputs a set of data within the data limits. 

import numpy as np

# The function is defined. Input is the path to a file. 
def dataLoad(filename):
    # The file is loaded into an array.
    filein = open(filename, "r")
    lines = filein.readlines() 
    # An empty array to which the sorted data can be appended to. 
    data = np.array([])
    # A counter to state in which line the error occurs. 
    lineCount = 0
    
    # The data in lines is now one long string and is treated as text. It it
    # therefore hard to access each element individually.
    # Because of this, each column is seperated. The first to columns are converted
    # to floats and the third column as an integer. Further more, a counter is defined
    # which is later used to print error messages. 
    for line in lines:
        lineCount += 1
        line = line.split()
        line[0] = float(line[0])
        line[1] = float(line[1])
        line[2] = int(line[2])
      
        # Now invalid data is rejected. By using the continue-function we make sure to 
        # not compute unessecary data by continuing to the next row.      
        # The temperature is checked
        if (10 >= line[0]) or (line[0] >= 60):
            # The ".format(lineCount)" is used to print the line in which the error
            # occurs in the error messages.
            print("Error in row {}: Temperature is out of range.".format(lineCount))
            # Continues to the next row of data in case of an error. 
            continue
        
        # The growth rate is checked
        elif line[1] <= 0:
            print("Error in row {}: The growth rate is too low.".format(lineCount))
            continue
        
        # The bacteria type is checked
        elif line[2] != 1 and line[2] != 2 and line[2] != 3 and line[2] != 4:
            print("Error in row {}: The bacteria is not within the four specified types.".format(lineCount))
            continue
       
        # Lastly each line is appended to the empty array, data. 
        data = np.append(data, line)

    # Data now consists of one, long string. We know that the matrix is an "N x 3" matrix
    # and the array is therefore seperated between each third element.     
    data = np.reshape(data, (int(len(data) / 3), 3))
    
    return data
        
    