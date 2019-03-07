# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 21:01:17 2018

@author: August
"""


# Numpy is used for various statistical calculations and analysis and Time is added
# as a for a tactile feeling of our program. 
import numpy as np
import time

# Descriptions of the different functions can be found in the individual function
# files. 
from menuFunction import displayMenu
from dataLoadFunction import dataLoad
from dataFiltering import sortBacteriaType
from dataFiltering import sortGrowthRate
from dataStatistics import dataStatistics
from dataPlotFunction import barChart
from dataPlotFunction import gRateGraphs

# Defining menu items
menuItems = np.array(["Load data", "Filter data", "Display statistics", "Generate plots", "Quit"])

# Defining available data filtration menu items.
filterItems = np.array(["Filter Data for Type of Bacteria", "Filter Data for Chosen Interval in Growth Rate", "Remove Filters", "Go back"])

# Defining available bacteria to filter for as menu items.
bacteriaItems = np.array(["Salmonella Enterica", "Bacillus Cereus", "Listeria", "Brochothrix Thermosphacta", "Go back"])

# Defining available statistical calculations as menu items.
statCalcItems = np.array(["Mean Temperature", "Mean Growth Rate", "Standard Deviation of Temperature", "Standard Deviation of Growth Rate", "Number of Rows", "Mean Cold Growth Rate", "Mean Hot Growth Rate", "Go back"])

# Defining available plots as menu items.
plotFunctionItems = np.array(["Bar Chart for Number of Bacteria", "Plot with Growth Rate by Temperature", "Both of The Above", "Go back"])

# Messages to be printed if the data is filtered are made
filterMessages = np.array(["Salmonella Enterica", "Bacillus Cereus", "Listeria", "Brochothrix Thermosphacta"])

# Defining an empty dataFile variable as a string
dataFile = ""

# Number that defines whether or not a dataload has been succesfully completed.
dataLoadTick = 0

# Number that defines whether or not a data filtration has taken place are defined.
bacteriaFilterTick = 0
limitFilterTick = 0
# The limits are defined as empty float variables
lowerLimit = float()
upperLimit = float()

# The beginning of the user input menu
while True:
    # In case of filtering, the program prints
    print("\nMain Menu:")
    if bacteriaFilterTick > 0:
        print("Note: Data is filtered for {0}.".format(filterMessages[int(bacteriaFilterTick)-1]))
    if limitFilterTick > 0:
        print("Note: Data is filtered for growth rate limits {0} to {1}.".format(lowerLimit, upperLimit))
        
    # Displaying menu options and asks the user to choose a menu item
    choice = displayMenu(menuItems)
    
    # 1. Load data
    if choice == 1:
        while True:
            try:
                # Asking the user to input name and save it in variable
                dataFile = input("Please input the name of your datafile or enter 'B' to go back: ")
                
                # If the user types in "B" the program breaks and returns to the
                # previous option menu.
                if dataFile == "B":
                    print("")
                    break
                
                    
                else:
                    print("\nData is being loaded...\n")
                    # The dataLoad function is called. 
                    data = dataLoad(dataFile)
                    
                    # dataLoadTick is set to one and the other functions are now
                    # accessible.
                    dataLoadTick = 1 
                    time.sleep(0.5)
                    print("\nData has been loaded succesfully\n")
                    break
            # If no file is found an error message is printed.
            except:
                print("Given filename couldn't be matched with excisting file. Please try again.")
    
    # 2. Filter data
    elif choice == 2:
        # If the dataLoadTick is zero it means that no data has been loaded. 
        while True:
            if dataLoadTick == 0:
                print("\nNo data filtering can be made without data, please load data first.\n")
                break
            
        # The program will now filter the data
            else:
                print("\nData Filtering:")
                if bacteriaFilterTick > 0:
                    print("Note: Data is filtered for {0}.".format(filterMessages[int(bacteriaFilterTick)-1]))
                if limitFilterTick > 0:
                    print("Note: Data is filtered for growth rate limits {0} to {1}.".format(lowerLimit, upperLimit))
                
                # Filtering options are shown
                filterChoice = displayMenu(filterItems)
                
                # The user input decides how the data is filtered. 
                if filterChoice == 1:
                    print("Filter Data for Type of Bacteria:")
                    bacteriaChoice = displayMenu(bacteriaItems)
                    
                    # If the user input in between 1 and 4 the desired type of bacteria 
                    # i chosen. 
                    if 1 <= bacteriaChoice <= 4:
                        
                        data = sortBacteriaType(bacteriaChoice, data)
                        print("\nThe loaded data now only contains data related to the bacteria {0}".format(bacteriaItems[int(bacteriaChoice-1)]))
                        bacteriaFilterTick = bacteriaChoice
                
                elif filterChoice == 2:
                    while True:
                        try:
                            
                            while True:
                                # Getting the input for the lower limit
                                lowerLimit = float(input("Please input the lowest growth rate in the desired filtered dataset: "))
                                
                                # If the growth rate not within the desired boundries
                                # an error message is printed. 
                                if lowerLimit < 0:
                                    lowerLimit = 0
                                    print("A negative growth rate cannot be used. Please input a positive growth rate as lower limit.")
                                    break
                                
                                #Getting the input for the upper limit
                                upperLimit = float(input("Please input the highest growth rate in the desired filtered dataset: "))
        
                                if float(upperLimit) <= float(lowerLimit):
                                    print("\nYou have set the upper limit to be lower or equal to the lower limit, which is not valid")
                                    break
                                
                                data = sortGrowthRate(lowerLimit, upperLimit, data)
                                print("\nThe loaded data has now been filterede according to your specified growth rate limits.")
                                limitFilterTick = 5
                                break
                        
                        # If the input is of wrong type.
                        except:
                            print("Limits have to be defined as numbers:")
                        
                        if limitFilterTick > 0:
                            break
                            
                elif filterChoice == 3:
                    data = dataLoad(dataFile)
                    print("\nDatafilter has been removed")
                    bacteriaFilterTick = 0
                    limitFilterTick = 0
                    
                
                elif filterChoice == 4:
                    break


    # 3. Displaying statistics.
    elif choice == 3:
        while True:
            # If no data is loaded
            if dataLoadTick == 0:
                print("\nNo statistical calculations can be made without data, please load data first.\n")
                break
            
            # Running the statistics in the program
            else:
                print("\nStatistical Calculations:")
                # Message in interface if data has been filtered.
                if bacteriaFilterTick > 0:
                    print("Note: Data is filtered for {0}.".format(filterMessages[int(bacteriaFilterTick)-1]))
                if limitFilterTick > 0:
                    print("Note: Data is filtered for growth rate limits {0} to {1}.".format(lowerLimit, upperLimit))
                # Menu options for calculating different statistical figures.
                statChoice = displayMenu(statCalcItems)
                
                if 7 >= statChoice >=1:
                    print("Calculating...")
                    time.sleep(0.5)
                    print("{0} is: {1}".format(statCalcItems[int(statChoice)-1], dataStatistics(data, statCalcItems[int(statChoice)-1])))
                    print("")
                    print("Feel free to choose another statistical value")
                elif statChoice == 8:
                    break


    # 4. Generating plots
    elif choice == 4:
        while True:
            if dataLoadTick == 0:
                print("\nNo graphs can be made without data, please load data first.\n")
                break
            
            else:
                print("\nData Plotting:")
                if bacteriaFilterTick > 0:
                    print("Note: Data is filtered for {0}.".format(filterMessages[int(bacteriaFilterTick)-1]))
                if limitFilterTick > 0:
                    print("Note: Data is filtered for growth rate limits {0} to {1}.".format(lowerLimit, upperLimit))
                plotChoice = displayMenu(plotFunctionItems)
                
                if plotChoice == 1:
                    
                    print(barChart(data))
                elif plotChoice == 2:
                    print(gRateGraphs(data))
                elif plotChoice == 3:
                    print(barChart(data))
                    print(gRateGraphs(data))
                elif plotChoice == 4:
                    break

    # 5. Quit
    elif choice == 5:
        # End
        break