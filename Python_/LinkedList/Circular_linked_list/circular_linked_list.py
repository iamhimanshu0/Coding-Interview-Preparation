
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head

        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return

        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next

        cur_node.next = new_node


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next

            cur.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        cur = self.head
        new_node.next = self.head

        if self.head == None:
            new_node.next = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node

    def remove(self, key):

        # if key == head node
        if self.head.data == key:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next

            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur_node = self.head
            prev_node = None
            # not equal to head node
            while cur_node.next != self.head:
                prev_node = cur_node
                cur_node = cur_node.next
                if cur_node.data == key:
                    prev_node.next = cur_node.next
                    cur_node = cur_node.next

    def find_length(self):
        cur_node = self.head
        count = 0

        while cur_node:
            count += 1
            cur_node = cur_node.next
            if cur_node == self.head:
                break

        # print(f"Length is {count}")
        return count

    def print_list(self):
        cur = self.head

        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    def find_middle(self):
        slow_pointer = self.head
        fast_pointer = self.head.next.next

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next

            if fast_pointer.next == self.head:
                break
        # print(f"Middle element is {slow_pointer.data}")
        return slow_pointer.data

    def split_list(self):
        middle = self.find_middle()
        cur_node = self.head
        prev_node = None

        split_start = None

        while cur_node.data != middle:
            prev_node = cur_node
            cur_node = cur_node.next

        #
        split_start = cur_node.next
        # point to itself
        cur_node.next = self.head

        # split cllist
        split_cllist = CircularLinkedList()
        while split_start.next != self.head:
            split_cllist.append(split_start.data)
            split_start = split_start.next

        split_cllist.append(split_start.data)

        self.print_list()

        print("")

        split_cllist.print_list()

    def remove_node(self, node):

        # if key == head node
        if self.head == node:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next

            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur_node = self.head
            prev_node = None
            # not equal to head node
            while cur_node.next != self.head:
                prev_node = cur_node
                cur_node = cur_node.next
                if cur_node == node:
                    prev_node.next = cur_node.next
                    cur_node = cur_node.next

    def josephus_circle(self, step):
        cur = self.head

        while self.find_length() > 1:
            count = 1
            while count != step:
                cur = cur.next
                count += 1
            print(f"Removed {cur.data}")
            self.remove_node(cur)
            cur = cur.next

    def is_circular_linked_list(self, input_list):
        cur = input_list.head
        while cur.next:
            cur = cur.next
            if cur.next == input_list.head:
                return True
        return False


c = CircularLinkedList()
c.append(1)
c.append(2)
c.append(3)
c.append(4)

s = LinkedList()
s.append(1)
s.append(2)
s.append(3)
s.append(4)

# s.print_list()
# c.append(5)
# c.append(6)
print(c.is_circular_linked_list(s))
print(c.is_circular_linked_list(c))
# c.josephus_circle(2)


# c.remove_node(c.head)
# c.print_list()
# c.remove(1)
# c.remove(3)
# c.remove(4)
# c.remove(8)

# c.remove(1)
# c.find_length()
# c.find_middle()
# c.split_list()
# c.print_list()
