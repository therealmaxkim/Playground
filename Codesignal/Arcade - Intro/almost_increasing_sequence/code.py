'''
Questions
1.


Observations
1. You can only remove 1 element from the array from any position
2. list must be strictly increasing - the next element is bigger than previous. Doesn't matter by how much
3. The list can be either sorted or unsorted

Solution 1: Go through list and check that it is increasing. You can only have 1 place in the list where the violation occurs. If you get more than 1 violation, then list can't get become increasing sequence.
The problem is, if there is a violation, which element do you remove? Does not matter. List must be increasing, no equal to the element before. O(n) solution with constant time. 

Can you do this faster? The only faster runtime is O(logn) or O(1) runtime. List is unsorted so there is nothing O(logn) that you can do. 

SOlution1 does not work.

The problem is, what do you do when you run into a violation? You can remove 2 elements - either the one that causes the violation or the element before it. 


1. Remove the element causing the violation

2. Remove the element before the violation



CORRECT SOLUTION
There are two options when you come across a violation. Let's call the rest of the array where the violation happens as the "2nd array". Tested that this is in sorted order. 

1. replace end of 1st array with start of 2nd array
2. replace start of 2nd array with end of 1st array

These are the only options that must happen for it to be sorted. Of course, the 2nd array must be sorted or else it will not work because more than 1 violation.

Check that one of these happens. If so, then True. If not, then False


'''


    

def almostIncreasingSequence(sequence):
    for i in range(0, len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            #Check second half of array is sorted
            for j in range(i+1, len(sequence)-1):
                if sequence[j] >= sequence[j+1]:
                    return False
            
    #Option 1. Beginning of 2nd array becomes end of 1st array
            if i-1 >= 0:    
                if sequence[i-1] < sequence[i+1]:
                    return True
    #Edge cases at beginning/end of array. Always true. 
            else:
                return True
            
    #Option 2. End of 1st array becomes beginning of 2nd array
            if i+2 < len(sequence):
                if sequence[i] < sequence[i+2]:
                    return True
    #Edge cases at beginning/end of array. Always true.
            else: 
                return True
            
    #Option 3. Option 1 and 2 did not work, therefore will not work.
            return False
            
    #Already in sorted order         
    return True
