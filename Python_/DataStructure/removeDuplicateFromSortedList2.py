"""
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Input: head = [1,1,1,2,3]
Output: [2,3]
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

    def removeFromSorted(self):
        dummy  =  Node(0)
        dummy.next = self.head 

        pre = dummy
        curr= self.head

        while curr:
            if curr.next and curr.value == curr.next.value :
                while curr and curr.next and curr.value == curr.next.value:
                    curr = curr.next
                pre.next = curr.next
            else:
                pre = pre.next
            curr =curr.next
        return dummy.next


    def removeOccurence(self):
        pass


llink = LinkedList()
llink.append(1)
llink.append(2)
llink.append(3)
llink.append(3)
llink.append(4)
llink.append(4)
llink.append(5)
llink.removeFromSorted()
llink.printList()