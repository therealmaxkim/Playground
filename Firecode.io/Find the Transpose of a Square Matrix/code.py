'''
Questions
1. Can the matrix be empty?
2. By "square matrix", does that mean that the length of x and y length of matrix is the same?
3. 

Observations
1. x and y length of matrix are the same
2. transposing is just rotating the matrix 90 degrees clockwise. 
3. must be done in place - which means we will have to swap somewhere
4. if we have to swap, what and where would we swap? we would swap the lower element with the element on the right. Think of
moving in two directions - south and east at the same time and swapping. 
5. how many times would we have to do this swap? after doing this on the first vertical column, what about the second column?


123
123
123

after swapping the first column 

111
223
323

then you would move down (south) 1 and then right (east) 1. repeat same process

111
222
333

steps
1. determine the initial starting place to swapping
2. swap 
keep repeating these two steps. 

'''
def transpose_matrix(matrix):
    
    def swap(matrix, starting_index):
        for i in range(starting_index, len(matrix)-1):
            matrix[starting_index][i+1], matrix[i+1][starting_index] = matrix[i+1][starting_index], matrix[starting_index][i+1]
            
    for i in range(len(matrix)):
        swap(matrix, i)
        
    
