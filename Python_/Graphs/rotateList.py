"""
Given the head of a linked list, rotate the list to the right by k places.

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Input: head = [0,1,2], k = 4
Output: [2,0,1]
"""
from itertools import count


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, value):
        if self.head == None:
            self.head = ListNode(value)
            return
        
        curNode = self.head
        newNode = ListNode(value)

        while curNode.next:
            curNode = curNode.next

        curNode.next = newNode

    def printList(self):
        curNode = self.head
        while curNode:
            print(curNode.val)
            curNode = curNode.next

    def getLength(self):
        count = 1
        curNode = self.head
        while curNode.next:
            count +=1
            curNode = curNode.next
        return count

    def rotateList(self, k):
        head = self.head
        length = self.getLength()
        if not head:
            return None
        
        lastElemnt = head
        while lastElemnt.next:
            lastElemnt = lastElemnt.next
        
        k = k % length

        lastElemnt.next = head

        tempNode = head

        for _ in range(length-k-1):
            tempNode = tempNode.next

        answer = tempNode.next
        tempNode.next = None

        self.head = answer
        

llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)

# llist.printList()
llist.rotateList(2)
llist.printList()