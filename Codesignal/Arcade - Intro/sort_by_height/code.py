'''
Questions
1. Are all heights unique? 
2. Is there a minimum or maximum number of trees?


Observations
1. trees are represented by -1
2. all heights are positive or greater than -1
3. 

Solution 1: Make a new list without the trees. Sort that list using non stable counting sort
. Go through original list and replace the heights in the same order as the new list, but do not touch the trees. 
O(n) counting sort since there is the constraint on height sizes. O(n) extra space. 
COunting sort does not have to be stable because they're just numbers

Is there a way to sort in place without extra space? 

all other sorting algorithms would take O(nlogn) time. 



'''

from collections import defaultdict

def counting_sort(numbers):
    #maximum number is 1000 which is the range. Use a dictionary instead of a list and run from o to 1000
    dict = defaultdict(int)
    for number in numbers:
        dict[number] += 1
    
    sorted = []
    for i in range(1001):
        while dict[i] != 0:
            sorted.append(i)
            dict[i] -= 1
    
    return sorted
            
def remove_trees(numbers):
    removed = []
    for number in numbers:
        if number != -1:
            removed.append(number)
    
    return removed

def sortByHeight(a):
    removed = remove_trees(a)
    sorted = counting_sort(removed)
    
    index = 0
    for i in range(len(a)):
        if a[i] != -1:
            a[i] = sorted[index]
            index += 1
    
    return a

