'''
Input
The input consists of N cases (equal to about 10000). The first line of the input contains only positive integer N. Then follow the cases. Each case consists of exactly one line with two positive integers separated by space. These are the reversed numbers you are to add.

Output
For each case, print exactly one line containing only one integer - the reversed sum of two reversed numbers. Omit any leading zeros in the output.

Example
Sample input: 

3
24 1
4358 754
305 794

Sample output:

34
1998
1
'''


num_of_cases = int(input())
for _ in range(num_of_cases):
    numbers = input().split()
    
    a = int(numbers[0])
    b = int(numbers[1])

    #convert each number to a list of digits in reverse by dividing by 10.
    #convert each list of digits to a number and add.
    #convert the answer to a list of digits in reverse by dividing by 10.
    #convert back to number and return. 

    a_digits_reversed = []
    b_digits_reversed = []

    def reverse_number(arr, number):
        while number >= 10:
            arr.append(number % 10)
            number = number//10
        if number != 0:
            arr.append(number)
    
    reverse_number(a_digits_reversed, a)
    reverse_number(b_digits_reversed, b)

    a_reversed = int(''.join(map(str, a_digits_reversed)))
    b_reversed = int(''.join(map(str, b_digits_reversed)))

    sum_of_a_b = a_reversed + b_reversed

    sum_digits_reversed = []

    reverse_number(sum_digits_reversed, sum_of_a_b)

    sum_reversed = int(''.join(map(str, sum_digits_reversed)))

    print(sum_reversed)
    