'''
Questions
1. What types are in string? Min/Max length?


Observations
1. In order for a word to be a palindrome, it must contain an even number of frequency for each character, except for 1 and 0 characters. 
2. We can use a dictionary to keep track of frequency of each word. As long as each frequency is even number, except for 1 or 0 character, it can be rearranged into a palindrome

Solution 1: Get frequency of each letter into a dictionary. 

From a to z, check that the value is an even number. 1 or 0 characters will be allowed to be non even. 

'''

from collections import defaultdict

def palindromeRearranging(inputString):
    frequency = defaultdict(int)
    one_odd = False
    for char in inputString:
        frequency[char] += 1
    
    for number in frequency.values():
        if number % 2 != 0:
            if one_odd:
                return False
            one_odd = True
    
    return True
