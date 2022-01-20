"""
Given the head of a sorted linked list,
delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list. 
Return the linked list sorted as well.

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
        new_node = Node(value)

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

    def deleteDuplicates(self):
        cur = self.head 

        while cur:
            while cur.next and cur.value == cur.next.value:
                cur.next = cur.next.next 

            cur = cur.next
        
        
    def removeAllOccurence(self):
        dummy = prev = Node(0)
        dummy.next = self.head 

        while self.head and self.head.next:
            if self.value == self.head.next.value:
                while self.head and self.head.next and self.head.value == self.head.next.value:
                    self.head = self.head.next
                
                self.head = self.head.next
                prev.next = self.head 
            else:
                prev = prev.next
                self.head = self.head.next
        return dummy.next


llist = LinkedList()
llist.append(1)
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(3)
llist.append(4)
llist.append(4)
llist.append(5)

llist.deleteDuplicates()
llist.printList()