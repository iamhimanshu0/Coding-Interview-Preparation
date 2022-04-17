"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

Input: head = []
Output: []
"""

from httpx import head


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

    def reverse(self):
        """
         1 -> 2 -> 3 -> 4 -> 5

         5 -> 4 -> 3 -> 2 -> 1
        """

        prev , curr , nxt = None, self.head, None

        while curr:
            nxt = curr.next 
            curr.next = prev
            
            prev = curr 
            curr  = nxt
        self.head = prev
        
        return head




llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.reverse()
llist.printList()