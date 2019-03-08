'''

SMPSEQ3 - Fun with Sequences
You are given a sorted sequence of n integers S = s1, s2, ..., sn and a sorted sequence of m integers Q = q1, q2, ..., qm. Please, print in the ascending order all such si that does not belong to Q.

Input data specification
In the first line you are given one integer 2<=n<=100, and in the following line n integers: 
-100 <= si <= 100, si <= si+1.

In the third line you are given one integer 2<=m<=100, and in the following line m integers: 
-100 <= qi <= 100, qi <= qi+1.

Output data specification
The sequence of requested integers separated by spaces.

Example
Input:
5
-2 -1 0 1 4
6
-3 -2 -1 1 2 3
Output:
0 4

Questions
1. Can you have repeats?

Observations
1. both lists of numbers are in sorted order.
2. if a number from S does not belong in Q, then the number in Q will be greater than S. Out of range
3. it is possible to go through the first list S and compare it with the elements in Q. As soon as you
are out of range, you know that number does not exist. For each element in S, see if the element in Q
is equal to, less than, or greater than. Three options. If less than, keep moving in Q. Equal to, print
and move to next element in S. Greater than, the number S does not exist so move on to next element in S

Post observations
the input sizes are very small. 1 to 100 length for both lists. THat means that long run time 
like n^2 or n^3 will run very fast. You can just do a quadratic time solve - check if number exists in 
second list for each number in first list. Or you can use a set. 

'''
#discard length
input()
A = [int(x) for x in input().split()]
#discard length
input()
B = [int(x) for x in input().split()]

a_i = 0
b_i = 0
while a_i < len(A) and b_i < len(B):
    #The B element is less than A element. Keep searching for A. 
    if B[b_i] < A[a_i]:
        b_i = b_i + 1
    #The B element == A element. Look at the next element of each list.
    elif B[b_i] == A[a_i]:
        a_i = a_i + 1
        b_i = b_i + 1
    #The B element is greater than A element. A element does not exist. Look at next A element but don't change B
    else:
        print(A[a_i], end = ' ')
        a_i = a_i + 1
#print remaining elements of A that are greater than end of B 
if a_i < len(A):
    for i in range(a_i, len(A)):
        print(A[a_i], end=' ')


 