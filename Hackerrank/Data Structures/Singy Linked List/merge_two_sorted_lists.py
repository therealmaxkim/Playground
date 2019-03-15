'''
1 ->    2 ->    3 ->    None
4 ->    6 ->    None

Have two pointers. Compare the value in the two pointers. Have a new linked list. Add the value 
depending on which is greater. Increment the pointer that its value is added.
At the end, if one of the pointers is not None, then the lists are not the same length. 
Simply just add everything from longer list to the new list until None.

'''
def mergeLists(head1, head2):
    new_list = SinglyLinkedList()

    while head1 != None and head2 != None:
        if head1.data < head2.data:
            new_list.insert_node(head1.data)
            head1 = head1.next
        elif head1.data == head2.data:
            new_list.insert_node(head1.data)
            new_list.insert_node(head2.data)
            head1 = head1.next
            head2 = head2.next
        else:
            new_list.insert_node(head2.data)
            head2 = head2.next
    
    while head1 != None:
        new_list.insert_node(head1.data)
        head1 = head1.next
    while head2 != None:
        new_list.insert_node(head2.data)
        head2 = head2.next
    
    return new_list.head