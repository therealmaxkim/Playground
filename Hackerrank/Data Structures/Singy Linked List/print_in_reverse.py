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

def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end='')

        node = node.next

        if node:
            print(sep, end='')

# Complete the reversePrint function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
# Solution 1: Reverse the SLL, print, Reverse SLL again back into original form
# Solution 2: Add elements to stack
# Solution 3: recursively call function on next node, then print


def reversePrint(head):
    stack = []
    curr = head
    while curr != None:
        stack.append(curr.data)
        curr = curr.next
    while len(stack) > 0:
        print(stack.pop())


if __name__ == '__main__':

