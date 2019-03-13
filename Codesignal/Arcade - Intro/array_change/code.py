'''
Questions
1. Can numbers be negative?


Observations
1. a3 > a2 > a1 . In order to maintain strictly increasing property, we need to increase the element by the smallest amount possible just so that it is bigger than the element before it. 

Solution 1: Keep a counter of # of moves. Run through list with two pointers. If the element in front is smaller or equal to to the element before it, find the smallest amount possible needed so that the front element is bigger than the element before it by 1. Formula is absolute value (front-back)+1. Update the front element to be bigger and continue. Increment counters.

-2, -7, -1, 0

'''

def arrayChange(inputArray):
    moves = 0
    before = 0
    for after in range(1, len(inputArray)):
        if inputArray[after] <= inputArray[before]:
            add = abs(inputArray[after]-inputArray[before])+1
            moves += add
            inputArray[after] += add 
        before += 1
            
    return moves
