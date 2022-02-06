"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

Input: head = []
Output: []
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

    def reverse(self):
        prev, curr, nxt= None, self.head, None

        while curr:
            nxt = curr.next 
            curr.next = prev

            prev = curr
            curr = nxt 

        self.head = prev   


llink = LinkedList()
llink.append(1)
llink.append(2)
llink.append(3)
llink.append(4)
llink.append(5)

# llink.printList()
llink.reverse()
llink.printList()




    