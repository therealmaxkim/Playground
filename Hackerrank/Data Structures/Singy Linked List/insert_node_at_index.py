#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    #When head is empty
    if head is None:
        head = SinglyLinkedListNode(data)
        return head
    else:
        new_node = SinglyLinkedListNode(data)
        curr = head
        #When inserting a new head
        if position == 0:
            new_node.next = head
            return new_node
        #When inserting at other positions
        else:
            for _ in range(position-1):
                curr = curr.next
            #Make new node, make it the next and move over the next.next to be the new node's next
            save = curr.next
            curr.next = new_node
            new_node.next = save
            return head
        


if __name__ == '__main__':

