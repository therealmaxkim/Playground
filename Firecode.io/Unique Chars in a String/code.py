def unique_chars_in_string(input_string):
    '''
    Questions
    1. Is there a min/max length of string?
    2. Can there be a empty string?
    3. Is the string alphanumeric?
    
    Observations
    1. we need to simply determine if a character is repeated. Not returning what character is repeated but saying true/false
    2. we need a way to "remember" each individual character in order to determine if it was repeated
    3. need a fast way to check if a character was already used
    
    
    brute force solution: For each character, check that character against the rest of characters that come after it. 
    would require O(n^2) runtime, but O(1) space complexity. 
    
    Need a fast way to remember and to check if a character was repeated for single characters. A data structure that supports
    fast input and lookup is a map or set. 
    
    We keep a set that will contain single characters. For each character in the string, we check if that character exists. If 
    it does, we found the repeated letter. If not, we add it to the set. If we manage to go through each character without 
    repeats, then we can return true since there are no repeats. O(n) worst case space complexity for set but O(n) runtime. 
    '''
    
    letters = set()
    for char in input_string:
        if char in letters:
            return False
        else:
            letters.add(char)
    return True