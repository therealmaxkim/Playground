'''
Questions
1. can n be zero?

Observations
1. 
n=0, area=0,
                jump=0
n=1, area=1, 
                jump=4
n=2, area=5, 
                jump=8
n=3, area=13, 
                jump=12
n=4, area=25, 
                jump=16
n=5, area=41, 

2. is there a formula to getting the area based on n?
3. the way that the polygon builds up is adding 1 extra layer on top of all of its sides. That means that are the (n-1) polygon grows, the next
one will increase in size more than the previous (n-1) did from (n-2). 
4. Could this be similar to fibonacci sequence? Since each n polygon depends on the size of the polygon before it. 

5. The difference between each n polygon is called "jump". We can see that there is a clear pattern in "jump" - the difference between each 
successive n polygon increases by 4 each time. This makes sense - if you look at n=1 and n=2, the difference is 4. This pattern will keep repeating.

6. Now we can make up a mathematical formula. 
n = arithmetic/geometric sum + previous

1 + 4 + 8 + 12 + 16


base case: n=1 
nth polygon = function(n-1) + (n-1)+4

'''


def shapeArea(n):
    current = 1
    jump = 0
    for i in range(1, n):
        current = current + jump+4
        jump = jump+4
    return current
