"""
# https://leetcode.com/problems/remove-linked-list-elements/

Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Input: head = [], val = 1
Output: []

Input: head = [7,7,7,7], val = 7
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


    # if linked list is sorted then use this
    def removeNode(self):
        cur_node = self.head 

        while cur_node:
            while cur_node.next and cur_node.value == cur_node.next.value:
                cur_node.next = cur_node.next.next
            
            cur_node = cur_node.next

    # if linked list in not sorted
    def removeGiveNode(self, value):
        dummy = Node(-1)

        prev, curr = dummy , self.head 

        while curr:
            nxt = curr.next 

            if curr.value == value:
                prev.next = nxt 
            else:
                prev = curr
            
            curr = nxt 
        return dummy.next
        


llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(2)
# llist.append(6)
llist.append(3)
llist.append(3)
llist.append(4)
llist.append(5)
llist.append(6)

# llist.removeNode()
llist.removeGiveNode(2)
llist.printList()