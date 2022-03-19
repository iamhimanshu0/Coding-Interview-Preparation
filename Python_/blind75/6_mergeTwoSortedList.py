"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = [0]
Output: [0]
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

    def getList(self):
        return self.head

def mergeList(list1, list2):
    # print(list1.head, list2)
    p = list1.head
    q = list2
    dummy = curr = Node(0)

    if not p and q:
        return []

    while p or q:
        if p.val > q.val:
            curr.next = q
            q = q.next
        elif p.val < q.val:
            curr.next = p
            p = p.next
        else:
            curr.next = p
            p = p.next
        curr = curr.next
    if p:
        curr.next = p
    elif q:
        curr.next = q
    
    return dummy.next
    

list1 = LinkedList()
list1.append(1)
list1.append(2)
list1.append(3)

list2 = LinkedList()
list2.append(1)
list2.append(3)
list2.append(4)

print(mergeList(list1, list2))