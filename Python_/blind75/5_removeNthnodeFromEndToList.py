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
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, value):
        newNode = Node(value)

        if self.head == None:
            self.head = newNode
            return
        
        curNode = self.head
        while curNode.next:
            curNode = curNode.next
        
        curNode.next = newNode
    
    def printList(self):
        curNode = self.head
        while curNode:
            print(curNode.val)
            curNode = curNode.next

    def removeNthFromEnd(self, n):
        fast = slow = self.head
        for _ in range(n):
            fast = fast.next
        
        if not fast:
            return self.head.next

        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        

llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)

llist.removeNthFromEnd(2)
llist.printList()