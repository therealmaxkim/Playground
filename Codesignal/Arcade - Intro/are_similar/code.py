'''
Questions
1. can the arrays be empty? 
2. What types are in the array? numbers?
3. are all the numbers unique?


Observations
1. Only 1 or 0 swaps are needed to make two arrays "similar"
2. The length of both arrays must be same for them to be similar
3. Swapping means swapping element with ANY other element in the array 
4. both arrays must be identical to each other when order is disregarded to have a chance to be similar. Does not guarantee similarity 
5. The order must be the same in all other places beside the swap.

Solution 1:
run through array and check that both are same. stop when you reach the "swap point"

Check in one of the arrays that the other element causing the violation exists. Can occur anywhere.

Check that if the swap does occur, then it will also match at that point

Continue going through until the end, making sure no more violations occur.

'''

def areSimilar(a, b):
    swapped = False
    #Assuming that a and b have the same length 
    for i in range(len(a)):
        if a[i] != b[i]:
            if swapped:
                return False
            
            for j in range(len(a)):
                if a[j] == b[i]:
#This is not always the right swap, but there may be more similar ones left. Can't return false here
                    if a[i] == b[j]:
                        a[i], a[j] = a[j], a[i]
                        swapped = True
                    
            if not swapped:
                return False
    
    return True
            
                
