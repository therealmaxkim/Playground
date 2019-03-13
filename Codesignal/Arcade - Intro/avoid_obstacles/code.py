'''
Questions
1. Can there be no obstacles?
2. is the list of obstacle coordinates sorted? No

Observations
1. Only given coordinates of obstacles. All other points are open
2. You are only allowed to make jumps of the same length
3. We want to minimize the length of the jump
4. The destination that we want to go to is the last obstacle's coordinate plus 1 all the way to infinity. 
5. Starting position is at coordinate 0
6. The minimum jump distance is just the least non common factor of the whole list???

Non factor - Makes sense, but for 5, it will try to avoid 10, 5, etc which might not be an obstacle. 



Solution 1: Start the minimum jump at 1. Look at each number in the obstacles. If the obstacle number is divisible by that number, that means that the min jump will collide. Increase min jump by 1 reset from beginning of list. Brute force. Bad runtime. Could take O(n^2) runtime [correct "working" answer]

How can we drop runtime to O(n)? Can drop it to nlogn by sorting the list beforehand. Would not have to go back and check min_jump against other elements [Wrong answer]

What if you find the minimum element O(n), and then do it from there? It would guarantee that the smallest possible length would be tested first and gradually increased. [Wrong answer. ]

Solution 2: start with min_jump = 1. Test that it does not evenly divide with obstacle. If it does, keep incrementing it until it is no evenly divisible. Then multiply the next obstacle and keep repeating test.  

Solution 2 is incorrect.

Problem: you need to able to check that the min_jump is not an obstacle or that the min_jump is not a factor of the obstacle coord. 


'''

def avoidObstacles(inputArray):
    min_jump = 1
    index = 0
    while index < len(inputArray):
        if inputArray[index] % min_jump == 0:
            min_jump += 1
            index = 0
        else:
            index += 1
        
    return min_jump

#Is O(n^2) really the best solution?
    

