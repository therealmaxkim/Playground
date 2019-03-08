#Given an array of n integers and a number, d , perform d left rotations on the array.
#Then print the updated array as a single line of space-separated integers.

'''
[1, 2, 3, 4, 5] -> [2, 3, 4, 5, 1] -> [3, 4, 5, 1, 2]
 0, 1, 2, 3, 4      0, 1, 2, 3, 4      0, 1, 2, 3, 4
 d = 0              d = 1              d = 2
index
0 to 4
1 to 0
2 to 1
3 to 2
4 to 3

do in place by replacing one element to another position, saving the element at the position, and keep repeating.
moving from left to right.
formula to calculating new index for an element at this initial index

moving 1 index left is equal to moving len(a) + 1 digits to the right.
or ( len(a) - d + i ) % len(a)


'''


import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    new_array = [0] * n
    print(new_array)
    for i in range(0, len(a)):
        #1. calculate the new index from an old index
        new_i = (len(a)-d+i) % len(a)
        new_array[new_i] = a[i]

    for item in new_array:
        print(item, end=' ')
