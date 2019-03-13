'''
Questions
1. What types are in the strings?
2. Can a string be empty?

Observations
1. Order does not matter. Just the knowing how many of a character exists in entire string and comparing.
2. all lowercase letters - only 26 possible characters
3. Need a fast way to check how many characters are in string A in order to compare with B


Solution 1: Have a dictionary with keys being characters and the values being the frequency that appears in string A. This dictionary will be for string A. After creating that dict for string A, go through string B and for each character, check the frequency in dictionary. Then you have 2 options

    1. value is zero : skip 
    2. value is not zero : decrement and add 1 to common character count
    
takes O(n1+n2), where n1 is length of string A and n2 is length of string B. Lookup is constant. 


use defaultdict(int)

'''

from collections import defaultdict

def commonCharacterCount(s1, s2):
    characters = defaultdict(int)
    common_count = 0
    
    for char in s1:
        characters[char] += 1
    
    for char in s2:
        if characters[char] != 0:
            common_count += 1
            characters[char] -= 1
    
    return common_count