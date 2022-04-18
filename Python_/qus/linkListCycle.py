"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
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

    def detectCycle(self):
        slow = self.head
        fast = self.head 

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next 

            if slow == fast:
                return True
        return False


llist = LinkedList()
llist.append(3)
llist.append(2)
llist.append(0)
llist.append(-4)

llist.head.next.next.next.next = llist.head.next
print(llist.detectCycle())