"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list. 

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
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

    def getList(self):
        return self.head

# def printAnotherList(l):
#     curNode = l.head()
#     while curNode:
#         print(curNode.val)
#         curNode = curNode.next
    

def merge(l1, l2):
    p1 = l1
    p2 = l2

    dummy = Node(0)
    m = dummy
    while p1 and p2:
        if p1.val <= p2.val:
            dummy.next = p1
            p1 = p1.next
        else:
            dummy.next = p2
            p2 = p2.next
        m = dummy.next
    
    if p1:
        m.next  = p1
    elif p2:
        m.next = p2
    
    return dummy.next
    

list1 = LinkedList()
list1.append(1)
list1.append(2)
list1.append(4)
# list1.printList()
# print("")
list2 = LinkedList()
list2.append(1)
list2.append(3)
list2.append(4)
# list2.printList()

print(merge(list1.getList(), list2.getList()))