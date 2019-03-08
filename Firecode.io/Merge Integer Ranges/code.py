'''
#1st attempt 
def merge_ranges(input_range_list):
    new_range = []
    
    for item in input_range_list:
        #Boolean value used to remember if this current range is outside of all other ranges
        modified = False
        #Looping through the new range list
        for new_item in new_range:
            #Check if range is within an existing range in new range list
            if item.lower_bound <= new_item.upper_bound:
                #Update the lower_bound and upper_bound of range in new range list
                new_item.lower_bound = (new_item.lower_bound, item.lower_bound)[item.lower_bound < new_item.lower_bound]
                new_item.upper_bound = (new_item.upper_bound, item.upper_bound)[item.upper_bound > new_item.upper_bound]
                #Indicate that a change was made to the new range list and break
                modified = True
                break
        if not modified:
            #this current range is a new range that is outside of all existing ranges
            new_range.append(item)
    
    return new_range
'''

'''
    Observations
    1. list is sorted, meaning that the lower_bound is given in increasing order
    2. however, the upper_bound is not in increasing order
    3. The list only contains a range object, which contains a two numbers. a low and a max.
    3. you only need to check if the lower_bound of next is bigger than max of last range in new range list. If it is, change the the upper_bound to be the max(old_upper_bound, new_upper_bound). 
    4. If the lower bound of next is bigger than max of old, then simply append. This will be a new range. Now compare every next with this one. 
    
    Questions
    1. Can a range have two same numbers? Such as [8, 8]?
    2. Can negative numbers be included in range?
    3. Is there a minimum/maximum number of ranges given in input?
'''
    
#2nd attempt
def merge_ranges(input_range_list):
    new_range = []
    new_range.append(input_range_list[0])
    
    for item in input_range_list:
        #For each item in input_range_list, check if its lower_bound is less than or equal to the upper_bound of the last element in the new list. 
        if item.lower_bound <= new_range[-1].upper_bound:
            #Update the upper_bound of the last element in the new list to be the max of two comparing ranges
            new_range[-1].upper_bound = max(item.upper_bound, new_range[-1].upper_bound)
        #Since the item's lower_bound is bigger than the upper_bound of the last element in then new list, that means that it is a new range. 
        else:
            new_range.append(item)
    
    return new_range