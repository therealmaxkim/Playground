'''
Questions
1. Can you get a string without parenthesis?
2. Are all the brackets guaranteed to have a closing bracket?
3. What types can be in the string?

Observations
1. Anything inside brackets will be guaranteed to reverse. It caneb recursive with nested parenthesis
2. The problem can be broken down into parts: simply reverse whatever is inside the bracket and attach it with the rest of the string. Reverse and attach.
3. When you come across a () and try to reverse the inside, you may come across another bracket. You can't just reverse whatever is inside because the double () will reverse the first reverse and make it the same order. 


Solution 1: Whenever you see (), call a function that will return the reverse. Within that function, you also check for more () so that the function is recursive.


When you know that you have to reverse, you have to find the ending ) of that ( in order to know where the characters go. If you come across a ( along the way, then you have to get the reversed version of that before you can continue to find the ending ). 


1. regular word
    add to list. Not reversing
2. (
    reverse everything after but stop when you reach )
3. ) 
    reversing stops here. 

Problem: You don't know when you stop reversing because the length of the reversed part is unknown. 

'''


# This function will handle reversing inside the (). Keep track of index and length. Length is needed
# in order to tell the outer function (that is not reversed) how far to jump ahead. Index is 
# needed because this function will need to jump ahead after recursively calling reverse. 
def reverse_string(inputString):
    words = []
    length = 0
    index = 0 
    
    while index < len(inputString):
        #Recursively call this function on the next part that needs to be reversed. 
        if inputString[index] == "(":
            recurse = reverse_string(inputString[index+1:])
            words.extend(recurse[0])
            #Add 1 because the '('
            index += recurse[1] + 1
            length += recurse[1] + 1
        elif inputString[index] == ")":
            length += 1
            break
        else:
            words.append(inputString[index])
            index += 1
            length += 1

    #Return the reversed list as well as the total length of this list. Can't just do len(list) because
    # you don't know how many times you recursed, so the number of () is unknown. 
    return (list(reversed(words)), length)


#Main function to handle non-reversing parts. Whenever you see a "(", call the helper function
# With the next part. 
def reverseInParentheses(inputString):
    words = []
    index = 0
    
    while index < len(inputString):
        #Call the function with the parts that need to be reversed. We don't know when the 
        #Reversing will stop. Index is needed so that we can jump ahead after the reversed
        # part. 
        if inputString[index] == '(':
            reversed_parts = reverse_string(inputString[index+1:])
            words.extend(reversed_parts[0])
            index += reversed_parts[1]
        elif inputString[index] == ')':
            index += 1
        else:
            words.append(inputString[index])
            index += 1
            
    return ''.join(words)



'''
Alternative solution
'''
def reverseInParentheses(inputString):
    stack = []
    for x in inputString:
        if x == ")": #if you reach a ')', you have to reverse everything before. 
            tmp = ""
            while stack[-1] != "(": #Handles nested () 
                tmp += stack.pop()
            stack.pop() # pop the (
            for item in tmp: #Put the reversed part back into the stack
                stack.append(item)
        else: #Add everything before ')' to the stack
            stack.append(x)
    
    return "".join(stack)