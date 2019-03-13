'''
Questions
1. string always in correct format? No. 


Observations
1. IPv4 rules - 4 numbers separated by dot, all within range inclusive 0 to 255.
2. There are four parts that we need to verify - checking if numbers are in range, and checking if only 4 numbers exist. 



Solution 1: split string by dot. Check if 4 elements exist. For each part, convert to number and check if within range. If there is an error at any point, return false. 
'''



def isIPv4Address(inputString):
    numbers = inputString.split('.')
    if len(numbers) != 4:
        return False
    for number in numbers:
        try:
            if not (int(number) >= 0 and int(number) <= 255):
                return False
        except:
            return False
    return True
