'''
Questions


Observations
1. For the matrix, the rows are independent of each other. Each column determines whether or not is it a valid room. 
2. You can add up the each column by column starting top down and stop if you reach a zero. 
3. the column and row size are different. rectangular matrix


Solution 1: Go column by column. Move from top the bottom of each column, and add to sum until you reach zero. When you reach zero or the end, move to the next column. 

'''


def matrixElementsSum(matrix):
    total = 0
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            if matrix[row][col] == 0:
                break
            total += matrix[row][col]
            
    return total