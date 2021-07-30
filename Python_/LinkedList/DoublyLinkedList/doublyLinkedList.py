class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):

        if not self.head:
            new_node = Node(data)
            self.head = new_node
            new_node.next = None
            new_node.prev = self.head
        else:
            cur_node = self.head
            new_node = Node(data)

            while cur_node.next:
                cur_node = cur_node.next

            cur_node.next = new_node
            new_node.prev = cur_node
            new_node.next = None

    def prepend(self, data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
            new_node.next = None
            new_node.prev = self.head
        else:
            new_node = Node(data)

            new_node.next = self.head
            new_node.pre = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_at_given_node(self, node, data):
        cur_node = self.head
        new_node = Node(data)
        while cur_node.data != node:
            cur_node = cur_node.next

        # ask as to add the data in last position (but there is no next)
        if not cur_node.next:
            cur_node.next = new_node
            new_node.prev = cur_node
            new_node.next = None
        else:
            # cur_node.next = new_node
            # new_node.prev = cur_node
            new_node.next = cur_node.next
            cur_node.next.prev = new_node
            new_node.prev = cur_node
            cur_node.next = new_node

    def remove(self, data):
        # if want to remove head node
        if not self.head.data:
            cur_node = self.head
            self.head = cur_node.next
            cur_node.next.prev = self.head
            cur_node = None
        else:
            cur_node = self.head
            prev_node = None
            while cur_node.data != data:
                prev_node = cur_node
                cur_node = cur_node.next

            # if last node is empty
            if not cur_node.next:
                prev_node.next = None
                cur_node = None
            else:
                prev_node.next = cur_node.next
                cur_node.next.prev = prev_node

                cur_node = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next


d = DoublyLinkedList()
d.append(1)
d.append(2)
d.append(3)
d.append(4)
d.prepend(0)
# d.add_at_given_node(4,20)
d.remove(0)
d.remove(4)
d.print_list()
