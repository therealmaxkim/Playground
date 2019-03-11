'''
Questions
1. Can the statue list be given sorted?

Observations
1. All sizes are non negative integers, unique. No repeats
2. kind of like sorting an array and seeing how many elements need to be in between
3. What is the minimum number of additional statues needed? 0. The maximum? The range of list, or largest-smallest
4. all statues are used. 
5. statue list can be sorted or unsorted. 

Solution 1: Sort array using counting sort. Doesn't have to be stable. O(n). Then go through list and count how many are "missing" by subtracting the current element and the previous element to see if it is 1, otherwise save to a counter variable. Additional O(n) space.

Solution 2: Similar to solution 1. Use a dictionary/map instead. The keys are the numbers, value is either 0 or 1. You go through list and find the largest element, and then iterate through map to check if that number exists. O(n) solution with O(n) time. 

Solution 3: Is there a way to do it with constant space? 
Yes you can. If you know the largest element in the list, and the smallest element in the list, you know the largest possible value of statues needed. So you can go through list again and subtract the size of the list. That will give you the missing elements. O(n) time but constant space. 


2, 3, 4, 5, 6, 7, 8
I  I        I     I

'''

def makeArrayConsecutive2(statues):
    #largest possible answer
    answer = max(statues) - min(statues) - 1 
    return answer - len(statues) + 2
