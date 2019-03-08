class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None
        
    #method for setting the head of the Linked List
    def setHead(self,head):
        self.head = head
                      
    #method for inserting a new node at the end of a Linked List   
    def insertAtEnd(self,data):
        #create a new node and set the data 
        newNode = Node()
        newNode.setData(data)
            
        #handle edge care where list is empty
        if (self.head == None):
            self.head = newNode
        else:
            #create a pointer which will point to the last node, defaults to head
            tailPointer = self.head
            #increment pointer until at the end
            while tailPointer.getNext() != None:
                tailPointer = tailPointer.getNext()
            #set the next node of the tail as the new node
            tailPointer.setNext(newNode)