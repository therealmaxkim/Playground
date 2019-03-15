'''
x ->    x ->    x ->    x ->    None
4       3       2       1       0

0       1       2       3       
The problem is that you don't know how long the linked list is. You have to start from the
beginning - try counting from 0. 

x ->    x ->    None
2       1       0

0       1       

Solution 1: create a hashmap corresponding to index from beginning and the value in the ith
position in linked list. When you reach the end of list, you know that the ith element is 
the length of the element - ith from tail. O(n) run time and space

Solution 2: use a stack. add values from start to end. At the end, you know how many times
you have to pop. O(n) runtime and space

Is there a way to reduce the space needed?

Solution 3: Assuming that we can modify the original list, we can reverse the list as we go. THen at the
end, just travel ith times. This requires O(n) time and constant space. 
'''

from collections import defaultdict

def getNode(head, positionFromTail):
    dict =defaultdict(int)
    index = 0
    while head != None:
        dict[index] = head.data
        index += 1 
        head = head.next
    
    #None is not counted, so subtract 1. 
    return dict[index-positionFromTail-1]