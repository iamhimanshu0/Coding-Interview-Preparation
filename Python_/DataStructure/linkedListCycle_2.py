"""
# https://leetcode.com/problems/linked-list-cycle-ii/

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
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

    def checkCycle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # print(slow.value, fast.value)
                break
        else:
            return None
        while self.head != slow:
            slow = slow.next
            self.head = self.head.next
        return self.head
        


llist = LinkedList()
llist.append(3)
llist.append(2)
llist.append(0)
llist.append(-4)

llist.head.next.next.next.next = llist.head.next
# llist.printList()  
print(llist.checkCycle())