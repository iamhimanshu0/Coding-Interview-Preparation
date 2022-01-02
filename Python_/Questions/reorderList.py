"""
    You are given the head of a singly linked-list. The list can be represented as:
        L0 → L1 → … → Ln - 1 → Ln
    Reorder the list to be on the following form:
        L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

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



    def reorderList(self):
        slow, fast = self.head, self.head.next 
        # find middle of the list

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # second half of the list
        second = slow.next 
        slow.next = None 

        # reversing
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merger and reorder
        first , second = self.head, prev
        while second:
            tmp1 , tmp2 = first.next, second.next
            first.next = second
            second.next  = tmp1

            first, second = tmp1, tmp2



    

        


llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)

llist.reorderList()
llist.print_list()