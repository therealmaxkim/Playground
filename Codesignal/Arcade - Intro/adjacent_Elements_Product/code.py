'''
Questions
1. can the array be empty?

Observations
1. The elements must be next to each other. That means that for each element, there are two possible products -> multiply with left or multiply
with right element.
2. Because the elements must be adjacent, we can use the "window sliding technique".
3. Running from left to right with window sliding technique gives you all possible products of adjacent elements.
4. Keep a separate variable to remember the largest and compare with sum from window sliding technique.


'''

def adjacentElementsProduct(inputArray):
    #The smallest size is two elements, default this as the largest product
    largestProduct = inputArray[0]*inputArray[1]

    #Calculate all other adjacent products and update the variable if it is bigger.
    for i in range(0, len(inputArray)-1):
        largestProduct = max(inputArray[i] * inputArray[i+1], largestProduct)

    return largestProduct
