"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.


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

    def getList(self):
        return self.head

def getIntersectionNode(l1, l2):
    if not l1 or not l2: return None

    l1Head = l1
    l2Head = l2
    check = {}
    if l1Head.value == l2Head.value:
        return None
    
    while l1Head and l2Head:
        if l1Head.value not in check:
            check[l1Head.value] =1
        else:
            return l1Head.next.value

        if l2Head.value not in check:
            check[l2Head.value]=1
        else:
            # check[l2Head.value]+=1
            return l2Head.next.value

        l1Head = l1Head.next
        l2Head = l2Head.next
    print(check)
              
def getIntersectionNode2(headA, headB):
    l1, l2 = headA, headB 

    while l1 != l2:
        l1 = l1.next if l1 else headB
        l2 = l2.next if l2 else headA

    return l1


l1 = LinkedList()
l1.append(1)
l1.append(9)
l1.append(1)
l1.append(2)
l1.append(4)

l2 = LinkedList()
l2.append(3)
l2.append(2)
l2.append(4)
# l2.append(8)
# l2.append(4)
# l2.append(5)

print(
    getIntersectionNode(l1.getList(), l2.getList())
)