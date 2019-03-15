'''
Guaranteed that head1 and head2 will not be none. Head nodes will be different. 
return the data value of the Node where the two lists merge.



1 ->    2 ->    7 ->    3 ->    4 ->    None
                ^
5 ->    6 ->    |

1 ->    2 ->    7 ->    3 ->    4 ->    None
        ^
9 ->    |

                1 ->    4 ->    None
                        ^
4 ->    5 ->    6 ->    |


returns 3. 

Problem: the index of step in which the lists merge are not the same
Don't know how long the two linked lists are

Questions
1. are all numbers unique? assumming not.


Observations
1. after the two lists merge, every node value afterwards will be shared
2. there is always a merge and the lists can never be empty
3. length before merge is not always same. but length after merge is always the same.
4.  1 -> 3 (lengths)
    3 -> 3

    4
    6

                    a ->    x ->    y ->    z ->    None
                            ^
    c ->    d ->    e ->    |

    while on list has longer length than the other, keep moving it forward. 

    move the longer one (6-4+1) and that pointer will contain the merge point


Solution 1: 
Use a set. Add each value as you move both pointers. If at any point, there exists already, 
that will be the start. Assuming unique numbers. Ignore the first head value. Doesn't work
if numbers are not unique.

Solution 2: If modification is allowed, reverse both lists and then double back until no longer
equal. the value before the point where no longer equal is the point.


Online solution O(N), constant space
Make an interating pointer like this: it goes forward every time till the end, and then jumps
to the beginning of the opposite list, and so on. Create two of these, pointing to two heads.
Advance each of the pointers by 1 every time, until they meet. This will happen after either
one or two passes.


'''

def findMergeNode(head1, head2):
    #Get the length of head1 and head2
    len_head1 = 0
    len_head2 = 0
    curr = head1
    while curr != None:
        len_head1 += 1
        curr = curr.next
    curr = head2
    while curr != None:
        len_head2 += 1
        curr = curr.next
    
    #Make the two pointers the same length or same distance from the merge point
    if len_head1 > len_head2:
        for _ in range(len_head1-len_head2):
            head1 = head1.next
    elif len_head2 > len_head1:
        for _ in range(len_head2-len_head1):
            head2 = head2.next

    #Kepe moving until you find the merge point
    while head1 != head2:
        head1 = head1.next
        head2 = head2.next
    return head1.data
    
    

    
