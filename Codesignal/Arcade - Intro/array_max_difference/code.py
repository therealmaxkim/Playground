'''
Questions


Observations
1. adjacent elements - meaning element to left or right. 

Solution 1: Have a counter that saves max. For each element, check if adjacent element difference is greater. 
'''


def arrayMaximalAdjacentDifference(inputArray):
    #Assuming at least 3 elements 
    max_difference = abs(inputArray[0] - inputArray[1])
    for i in range(len(inputArray)-1):
        max_difference = max(max_difference, abs(inputArray[i]-inputArray[i+1]))
    return max_difference