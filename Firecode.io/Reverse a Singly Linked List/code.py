class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None
        
    #method for setting the head of the Linked List
    def setHead(self,head):
        self.head = head
    
    '''
    Questions
    1. Can the SLL be empty?
    2. double check meaning of "in place" -> do you mean O(1) constant space?
    
    Observations
    1. SLL means no pointer going backwards
    2. SLL has a head pointer that points to front
    3. We have to change the head pointer to point to new head after we reverse
    4. we can have multiple pointers to nodes
    5. the previous head will become the new end of the SLL
    
    Imagine a SLL with just one node. Imagine a SLL with just two nodes.  
    1 -> 2 turns into 2 -> 1
    
    1 -> 2 -> 3
    *    * 
    
    current = 1
    next = 2
    
    2 -> 1 , 3 
    *    *
    
    current = 2
    next = 3
    temp = None
    
    3 -> 2 -> 1
    
    Have two pointers that are adjacent to each other. Swap the next pointer of one node with the other. In order to not lose the 
    next node, save the next next node beforehand. Increment both pointers after swapping. The first next pointer must be set to None 
    
    '''
    def reverse(self):
        if self.head is None:
            return
        
        current_node = self.head
        next_node = current_node.getNext()
        current_node.setNext(None)
        #flip all nodes until the last node
        while next_node is not None:
            temp = next_node.getNext()
            next_node.setNext(current_node)
            current_node = next_node
            next_node = temp
        #set the last node as the head
        self.setHead(current_node)