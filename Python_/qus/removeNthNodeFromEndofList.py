"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Input: head = [1], n = 1
Output: []

Input: head = [1,2], n = 1
Output: [1]
"""

head = [1,2,3,4,5]
n = 2

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, val):
        newNode = Node(val)
        
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
        slow = self.head
        fast = self.head
        for _ in range(n):
            fast = fast.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return self.head


list1 = LinkedList()
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)
list1.append(5)

list1.removeNthFromEnd(1)

list1.printList()