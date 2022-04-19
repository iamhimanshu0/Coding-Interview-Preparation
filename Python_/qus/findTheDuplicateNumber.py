"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Input: nums = [1,3,4,2,2]
Output: 2

Input: nums = [3,1,3,4,2]
Output: 3
"""

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
    
    def findDuplicate(self):
        check = {}

        curNode = self.head
        while curNode:
            if curNode.val not in check:
                check[curNode.val] = 1
            else:
                return curNode.val

            curNode = curNode.next

        

llist = LinkedList()
llist.append(3)
llist.append(1)
llist.append(3)
llist.append(4)
llist.append(2)

print(llist.findDuplicate())