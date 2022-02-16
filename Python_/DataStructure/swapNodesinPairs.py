"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Input: head = [1,2,3,4]
Output: [2,1,4,3]

Input: head = []
Output: []

Input: head = [1]
Output: [1]
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            return
        
        curNode = self.head 
        while curNode.next:
            curNode = curNode.next 

        curNode.next = new_node

    def printList(self):
        curNode = self.head
        while curNode:
            print(curNode.value)
            curNode = curNode.next

    def swapNode(self):
        currentNode = self.head
        curNode , nextNode = None, None
        
        while currentNode and currentNode.next:
            curNode = currentNode
            if curNode.next:
                nextNode = curNode.next 

                curNode.value , nextNode.value = nextNode.value, curNode.value

            currentNode = currentNode.next.next


llist = Linkedlist()
llist.append(1)
# llist.append(2)
# llist.append(3)
# llist.append(4)
        
llist.swapNode()
llist.printList()
