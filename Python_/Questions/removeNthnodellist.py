"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Input: head = [1], n = 1
Output: []

Input: head = [1,2], n = 1
Output: [1]

https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""

from typing import Counter, Deque


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            return
        
        cur_node = self.head 
        while cur_node.next:
            cur_node = cur_node.next 

        cur_node.next = new_node

    
    def printList(self):
        cur_node = self.head 
        while cur_node.next:
            print(cur_node.value)
            cur_node = cur_node.next 

    
    def removeNnode(self, n):
        fast = slow = self.head
        for _ in range(n):
            fast = fast.next 
            
        if not fast:
            return self.head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return self.head


llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.removeNnode(1)

llist.printList()

