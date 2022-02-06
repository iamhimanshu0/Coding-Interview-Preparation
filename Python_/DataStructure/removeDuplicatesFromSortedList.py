"""
# https://leetcode.com/problems/remove-duplicates-from-sorted-list

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Input: head = [1,1,2]
Output: [1,2]

Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""

class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 

    def append(self, value):
        new_node =  Node(value)

        if self.head == None:
            self.head = new_node
            return 

        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next 

        cur_node.next = new_node

    def printList(self):
        cur_node = self.head 
        while cur_node:
            print(cur_node.value)
            cur_node = cur_node.next 

    def removeOccurance(self):
        
        curr = self.head 

        while curr:
            while curr.next and curr.value == curr.next.value:
                curr.next = curr.next.next

            curr = curr.next

        # self.head =curr
        return self.head
                



llink = LinkedList()
llink.append(1)
llink.append(1)
llink.append(2)
llink.append(3)
llink.append(3)

llink.removeOccurance()
llink.printList()
