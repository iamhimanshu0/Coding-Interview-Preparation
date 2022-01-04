"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Input: head = [1], n = 1
Output: []

Input: head = [1,2], n = 1
Output: [1]
"""

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

    
    def removeNnode(self, value):
        length = 0
        count = 0 
        cur_node = self.head 

        while cur_node:
            length = length +1
            cur_node = cur_node.next 

        node = self.head
        prev = None


        while count < (length- value) and node.next:
            prev = node
            node = node.next 
            count = count +1


        print(prev.value,node.next.value)


        

    


llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.removeNnode(2)
# llist.printList()