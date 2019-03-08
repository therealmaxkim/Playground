'''
Questions
1. Can the string be empty?
2. What types are in the string? alphabets only? numbers?

Observations
1. the first and last letters are the same and continues to repeat as you move inwards
2.

compare the first and last letters. Move inwards on both sides and keep checking. If at any point they are not the same, return false. Else,
return true

'''

def checkPalindrome(inputString):

    for i in range(0, len(inputString) // 2):
        if inputString[i] != inputString[len(inputString)-1-i]:
            return False

    return True
