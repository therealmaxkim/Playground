'''
split up the problem into 4 parts. Each top/bottom, left/right are simply just reversed repeats of each other. Start by printing the 
top lines, then the middle line, and finally the bottom lines. Each line will print the left parts, middle part, then the right parts. 
The trick is to save the top lines as a list of strings in order to reverse and print them as bottom lines. Same thing with the left 
side of a line, save into a list and then print the reversed version as the right side of a line. 
'''

'''
This function handles the printing of individual rows. It will call the function "print_horizontal" with the size and a variable that 
represents how many alphabet letters are on each side. A list of all the horizontal lines will be returned. 
'''
def print_vertical(size):
    lines = []
    for i in range(1, size):
        lines.append(print_horizontal(size, i-1))
    return lines

'''
This function handles the printing of each individual line. Given the size and length (which is how many letters are on the side. 
For example, for size 3, there are 1 or 0 alphabet letters on each side). Returns a string that is the individual line. 
'''
def print_horizontal(size, length):
    line = []
    left = []

    #add the left side 
    #add the left '-' lines
    for i in range(1, size-length):
        left.append('--')

    #account for 'a' being 1. Subtract 1. But not before the lines above
    size = size - 1

    #add the left letters
    for i in range(0, length):
        left.append(chr(ord('a')+size))
        left.append('-')
        size = size-1
    line.extend(left)

    #add the middle letter
    line.append(chr(ord('a')+size))

    #add the right side (just reversed of left side)
    line.extend(list(reversed(left)))

    return ''.join(line)

'''
This function is the overall function that handles the overall progress. The trick is to grab a list of all of the lines that are the 
"top part", or all lines above the middle line. Save that list in order to print it as the "bottom part", which is simply just the 
reverse of that line. 
'''
def print_rangoli(size):
    #print the top part
    top = print_vertical(size)
    for line in top:
        print(line)

    #print the middle part
    print(print_horizontal(size, size-1))

    #print the bottom part (just reversed order of top part)
    for line in list(reversed(top)):
        print(line)

if __name__ == '__main__':
  n = int(input())
  print_rangoli(n)
