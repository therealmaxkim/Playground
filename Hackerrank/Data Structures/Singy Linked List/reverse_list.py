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

# Complete the reverse function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
'''
    prev    curr
    None    1 ->    2  ->   None
            next

    prev=None, curr=head, next=head

    prev    curr
    None    1 ->    2  ->   3  -> None
                    next

    next = curr.next

            temp
    prev    curr
    None    1 ->    2  ->   3  -> None
                    next
    
    temp = curr

            temp
    prev    curr
    None <- 1       2  ->   3  -> None
                    next

    curr.next = prev

            temp
    prev            curr
    None <- 1       2  ->   3  -> None
                    next

    curr = next

            temp
            prev    curr
    None <- 1       2  ->   3  -> None
                    next

    prev = temp
              
    At the very end, curr and next are None. Return prev, which is the very last element
'''
def reverse(head):
    if head is None:
        return head

    prev = None
    next = head
    curr = head

    while curr is not None:
        next = curr.next
        temp = curr
        curr.next = prev
        curr = next
        prev = temp
    
    return prev

if __name__ == '__main__':

