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

    def mergeList(self, secondHead):
        dummy = Node(0)

        firstList = self.head 
        secondList = secondHead.head

        print(firstList.value, secondList.value)
        
        while firstList and secondList:
            if firstList.value > secondList.value:
                dummy.next = secondList
                secondList = secondList.next
            else:
                dummy.next = firstList
                firstList = firstList.next

            dummy = dummy.next

        if firstList:
            dummy.next = firstList
        elif secondList:
            dummy.next = secondList
        
        return dummy.next


llist1 = LinkedList()
llist1.append(2)
llist1.append(4)
llist1.append(6)
llist1.append(8)

llist2 = LinkedList()
llist2.append(1)
llist2.append(3)
llist2.append(5)
llist2.append(7)


llist1.mergeList(llist2)
llist1.printList()