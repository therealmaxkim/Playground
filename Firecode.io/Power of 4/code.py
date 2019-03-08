'''
Questions
1. is modulus, add, subtract, square root allowed?


Observations
1. define what it means to be a power of 4 - any number of 4s must be multiplied to get that number
2. We do not need to know how many times we need to multiple 4 to get number. Only need to return true or False
3. Multiplying by 4 is the same as adding that number 4 times
4. there are no number tricks - can't add up digits and see if it is divisible by 4
5. all powers of 4 are even numbers

4 = 4
4 * 4 = 16
4 * 4 * 4 = 64
4 * 4 * 4 * 4 = 256

bit manipulation
decimal     binary
4           100 
16          10000
64          1000000

notice that there is only 1 bit on the very left for all powers of 4. How can we use bit manipulation to check this?
decimal     binary
3 (4-1)     011
15 (16-1)   01111
63 (64-1)   0111111

try x & (x-1) will tell us if x is a power of 4. If result is equal to zero, then return true. 
Exception: zero. zero should be checked separately since (0-1) would be a negative number.
'''

def is_power_of_four(number):
    not_zero = number != 0
    power_two = not bool((number & (number - 1)))
    only_four = bool((number & (0x55555555)))
    return not_zero and power_two and only_four