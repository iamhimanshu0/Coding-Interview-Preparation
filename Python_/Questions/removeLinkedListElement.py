"""
    Remove Linked List Elements

    Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
    
    Input: head = [1,2,6,3,4,5,6], val = 6
    Output: [1,2,3,4,5]

    Input: head = [], val = 1
    Output: []

    Input: head = [7,7,7,7], val = 7
    Output: []

    https://leetcode.com/problems/remove-linked-list-elements/

"""

class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

class LinkedList:
    def __init__(self):
        self.head = None 

    def append(self,value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            return

        cur_node = self.head 
        while cur_node.next:
            cur_node = cur_node.next 

        cur_node.next = new_node

    
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.value)
            cur_node = cur_node.next


    def removeElements(self, value):
        dummy = Node(self.head)
        prev, curr = dummy, self.head 

        while curr:
            nxt = curr.next 
            if curr.value == value:
                prev.next = nxt 
            else:
                prev = curr

            curr  = nxt

        return dummy.next


llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(6)
llist.append(3)
llist.append(4)
llist.append(5)
llist.append(6)

llist.removeElements(6)
llist.print_list()