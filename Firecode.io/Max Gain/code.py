'''
Questions
1. is the list sorted?
2. can negative integers be in list
3. Can i modify the original list
4. can you have repeated numbers

observations
1. larger element appearing after the smaller one means that you only need to compare with elements that are behind for each element
2. if a number before an index is larger, then you can just move past iter
3. you can save the smallest number and the largest number by moving through the list. 
4. What if you only save the smallest number? that way you can just compare with each element as you move down and only
update the smallest number. 

'''

def max_gain(input_list):
    if len(input_list) == 0:
        return 0
    smallest_number = input_list[0]
    difference = 0
    for number in input_list:
        if number < smallest_number:
            smallest_number = number
        if number - smallest_number > difference:
            difference = number - smallest_number
    return difference