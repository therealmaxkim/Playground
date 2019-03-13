'''
Questions
1. can the list be empty?
2. can the length of the words change per row? No. 
3. can you have empty spaces between words (down the middle)
4. What types are the words


Observations
1. the border has to encompass the length of the words
2. the horizontal length of the border is the length of the word + 2
3. the vertical length of the border is the number of rows + 2

Solution 1: Find the horizontal length. At the beginning and end of the list, add the border of the same length. Then go through every row except the first and last row and add a * at the front and back. 

'''

def addBorder(picture):
    x_len = len(picture[0]) + 2
    
    for i in range(len(picture)):
        picture[i] = '*' + picture[i] + '*'
    
    picture.insert(0, '*' * x_len)
    picture.append('*' * x_len)
    
    return picture