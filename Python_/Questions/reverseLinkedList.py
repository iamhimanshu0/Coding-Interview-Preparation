"""
    Given the head of a singly linked list, reverse the list, and return the reversed list.
    
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

    https://leetcode.com/problems/reverse-linked-list/
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

    def reverseList(self):
        """
            / Before changing next of current, 
            // store next node 
            next = curr->next
            // Now change next of current 
            // This is where actual reversing happens 
            curr->next = prev 
            // Move prev and curr one step forward 
            prev = curr 
            curr = next
        """    
        prev = None 
        curr =self.head 
        nxt = None

        while curr:
            nxt = curr.next
            curr.next = prev

            prev = curr
            curr = nxt

        self.head = prev

   


llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(4)
llist.append(2)
llist.append(6)
llist.append(5)
# llist.reverseList()
llist.printList()