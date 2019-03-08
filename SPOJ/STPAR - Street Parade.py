'''
For sure, the love mobiles will roll again on this summer's street parade. Each year, the organisers decide on a fixed order for the decorated trucks. Experience taught them to keep free a side street to be able to bring the trucks into order. 

The side street is so narrow that no two cars can pass each other. Thus, the love mobile that enters the side street last must necessarily leave the side street first. Because the trucks and the ravers move up closely, a truck cannot drive back and re-enter the side street or the approach street. 

You are given the order in which the love mobiles arrive. Write a program that decides if the love mobiles can be brought into the order that the organisers want them to be.

Input
There are several test cases. The first line of each test case contains a single number n, the number of love mobiles. The second line contains the numbers 1 to n in an arbitrary order. All the numbers are separated by single spaces. These numbers indicate the order in which the trucks arrive in the approach street. No more than 1000 love mobiles participate in the street parade. Input ends with number 0.

Output
For each test case your program has to output a line containing a single word "yes" if the love mobiles can be re-ordered with the help of the side street, and a single word "no" in the opposite case.

Example
Sample input:
5
5 1 2 4 3 
0

Sample output:
yes



Questions
1. 

Observations
1. trucks cannot back up or move anywhere
2. THe only way that you can "change" the order is by using a stack like side input. 
3. Your "moves" for this problem are limited.
    If you have an empty stack (side entrance)
        1. you move the truck forwards
        2. you move the truck into the side
    If you have atleast 1 truck in stack
        1. you can move the truck forwards
        2. you can move the truck into the side
        3. you can bring out the truck from the side
4. Now the question is, when do you do which action? 
5. The goal is to order the numbers in ascending order. 
6. basically sorting a list of numbers using a stack
7. The list is always 1 to n, inclusive 

If the truck you are looking at is in right order, you move it to the right
    If not, you move truck to the stack
If the truck is not in right order,
    1. check if the stack has a truck. Check if that truck is the right one. Move it 
    2. Otherwise, add that truck to the stack.

How do you know if reordering can work? How to know when it fails?

Example of when it DOES NOT work
3 5 4 2 1

3 5     2 1
    4

3       2 1 
    5
    4

    3 2 1
5
4

Post observation
1. you want the end result to be in sorted order
2. That means that number 1 will be the first on line.
3. when the truck that we are looknig for is not the one, and the truck at the top of the list
is greater than the truck already in a stack, then will the list ever be in sorted order?

4       1
    3

truck number 3 will be stuck because it will turn out to be behind truck 4, which is supposed to go after.
Not just adding the truck into the side stack regardless. The stack must be in decreasing order. 
        
        1
    4
    3


4. Another edge case - if you have something like this

8 7       looking for truck #5 
    5
    6

you cannot pass in 5 from the stack and then move on to next truck in left list. you have to stick to truck 7 and not move 
forward in the loop. 

5. try to clean up the lane first before looking at the truck - solves above edge condition
'''

def check_if_sortable():

    stack = []

    #discard input 
    input()
    trucks = [int(x) for x in input().split()]
    #discard input
    input()
    sorted_order = []

    counter = 1
    for truck in trucks:
        if truck == counter:
            sorted_order.append(truck)
            counter = counter + 1
        else:
            if len(stack) != 0 and stack[len(stack)-1] == counter:
                sorted_order.append(stack.pop())
                counter = counter + 1
            else:
                if len(stack) !=0 and truck > stack[len(stack)-1]:
                    return False
                stack.append(truck)

    #If at this point, everything worked
    return True

print(check_if_sortable())