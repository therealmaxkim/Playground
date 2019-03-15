'''
Given the head of a DLL and data, insert data and maintain sorted order
return the head

1. make new node with data
2. Find the place needed to insert
3. Do insertion

    None        x       y          z       None
                    ->       ->         ->
           <-       <-       <-         
    
    
    if at middle (between y and z)
        change z's previous
        change y's next
        make new node's next to be z
        make new node's previous to be y

    If at the beginning (between None and x)
        change x's previous to new node
        make new node's previous to None
        make new node's next to X

    If at the end (between z and None)
        change z's next to new node
        make new node's previous to z
        make new node's next to None

    check the previous and after if they are None.
'''

def sortedInsert(head, data):
    new_node = DoublyLinkedListNode(data)

    if head is None:
        return new_node
    
    curr = head

    while (curr.next != None) and (new_node.data <= curr.data):
        print("Curr is at", curr.data)
        curr = curr.next
    #need to insert before this curr pointer
    
    if curr.next == None:   #Inserting at the end of list
        curr.next = new_node
        new_node.prev = curr
        return head
    elif curr.prev == None: #Inserting at the front of list
        curr.prev = new_node
        new_node.next = curr
        return new_node
    else: #Inserting at other points in list
        before = curr.prev
        new_node.prev = before
        new_node.next = curr
        before.next = new_node
        curr.prev = new_node
        return head
    



    
    
