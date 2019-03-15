'''
linked list is in sorted ascending order. remove all duplicates


1 ->    1 ->    2 ->    2 ->    3 ->    None

1 ->    2 ->    3 ->

save the current value that you are looking at. Go to next. If the same value exists, delete 
that pointer. Won't work because you can't go back and set the previous node's next to a different
node. 

save the current value that you are looking at. Have two pointers, initialize both to same node.
Increment one pointer and check. Either the value in the next pointer will be equal to or not
equal. While it is equal, keep moving. As soon as you reach a node that is not the same, set 
the other pointer's next to this node. Repeat steps 1 and 2. Check if none before moving
next pointer.

1. set both pointers to head
2. increment next pointer until value is no longer equal
3. set curr pointer's next to be the next pointer
4. assign current and next to be the curr's next
5. repeat until curr is None
'''

def removeDuplicates(head):
    if head is None:
        return head
    
    curr = head
    next = head
    while curr is not None:
        while next is not None and curr.data == next.data:
            next = next.next
        curr.next = next
        curr = curr.next

    return head

    
