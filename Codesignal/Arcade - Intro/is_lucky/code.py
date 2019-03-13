'''
Questions
1. 

Observations
1. The length of the first half does not have to equal length of the second half, for the sums to be equal
2. All ticket numbers have even number of digits
3. Bit manipulation? 


Solution 1: turn number into list of digits. check if sum of 1st half = sum of 2nd half. Requires O(n) runtime and space

log(n) or constant time solution? 

Solution 2: 

'''

def get_digits(n):
    digits = []
    while n >= 10:
        digits.append(n % 10)
        n = n//10
    digits.append(n)
    return list(reversed(digits))

def isLucky(n):
    
    digits = [int(x) for x in list(str(n))]
    first_half_sum = sum(digits[i] for i in range(len(digits)//2))
    second_half_sum = sum(digits[i] for i in range(len(digits)//2, len(digits)))
    if first_half_sum == second_half_sum:
        return True
    return False
