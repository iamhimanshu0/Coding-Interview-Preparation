"""
https://leetcode.com/problems/middle-of-the-linked-list/

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

"""

class Node:
    def __init__(self, value):
        self.value =value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            return 
        
        cur_node = self.head 
        while cur_node.next:
            cur_node = cur_node.next 

        cur_node.next = new_node

    def printList(self):
        cur_node= self.head
        while cur_node:
            print(cur_node.value)
            cur_node = cur_node.next


    def middleNode(self):
        count = 0 
        cur_node = self.head

        while cur_node:
            count +=1
            cur_node = cur_node.next

        slow = self.head 
        fast = self.head.next
        

        while fast and fast.next:
            slow =  slow.next
            fast = fast.next.next
        
        
        if(count %2 == 0):
            self.head = slow.next
        else:
            self.head = slow
        
        # print(slow.value, fast.value)

llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
# llist.append(6)

llist.middleNode()
llist.printList()