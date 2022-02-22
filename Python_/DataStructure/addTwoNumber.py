"""
# https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Input: l1 = [0], l2 = [0]
Output: [0]

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self) -> None:
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

    def getHead(self):
        return self.head

    def printList(self):
        curNode = self.head
        while curNode:
            print(curNode.val)
            curNode = curNode.next

    
def addTwoNumbers(l1, l2):
    dummy = cur = Node(0)
    carry = 0
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        cur.next = Node(carry%10)
        cur = cur.next
        carry //= 10
    return dummy.next




l1 = LinkedList()
l1.append(2)
l1.append(4)
l1.append(3)

l2 = LinkedList()
l2.append(5)
l2.append(6)
l2.append(4)

print(
    addTwoNumbers(l1.getHead(), l2.getHead())
)