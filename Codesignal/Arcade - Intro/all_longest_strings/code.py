'''
Questions
1. What types can the string have?
2. Can list be empty?


Observations
1. In order to find the longest string you need to look at the whole array. No way around it
2. 

Solution 1: Run through list and find the longest length. Rerun through array and add the words that have the same length as the longest string to a new array. Takes O(n) and O(n) run/space time.

Solution 2: Insert the first word into new array. This word length is the "max" length. Then there are 3 options as you run through original list
1. word length > "max" : in this case you delete the whole array and add in new word
2. word length = "max" : add in the word to array
3. word length < "max" : skip to next word
worst case you have to keep adding word and then removing it. That takes constant time. So O(n) solution. Only have to loop through array once. instead of twice.

Can we get faster runtime? constant time or logn? Sorting the list would take nlogn. Worse than previous solutions. Maybe there is a way to save space - constant space or do it in place? 

'''


def allLongestStrings(inputArray):
    new_array = []
    longest_length = len(max(inputArray, key=len))
    for word in inputArray:
        if len(word) == longest_length:
            new_array.append(word)
    
    return new_array
        
