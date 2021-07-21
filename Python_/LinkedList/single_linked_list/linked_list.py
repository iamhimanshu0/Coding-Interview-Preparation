import math
from typing import Dict


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

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def add_in_between(self, item, data):
        new_node = Node(data)

        cur_node = self.head
        prev_node = None
        while cur_node and cur_node.data != item:
            cur_node = cur_node.next
            prev_node = cur_node

        new_node.next = cur_node.next
        prev_node.next = new_node

    def length(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
            # print("Length of the LinkedList is:- ", count)

        return count

    # find_middle element of a LinkedList

    def find_middle(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next

        if count % 2 == 0:
            # two even node then /2 +1
            mid = math.ceil(count/2)
            print("Length is even ", mid)
            c = 0
            while self.head and c != mid:
                self.head = self.head.next
                c += 1

            print(self.head.data)
            print("even")
        else:
            # else celing
            mid = count//2
            print("Length is Odd ", mid)
            c = 0
            while self.head and c != mid:
                self.head = self.head.next
                c += 1

            print(self.head.data)

    # find_middle using 2 pointer method

    def find_middle_2_pointer(self):
        slow_pointer = self.head
        fast_pointer = self.head

        while fast_pointer and fast_pointer.next:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next

        print("middle element:- ", slow_pointer.data)

    # sum_of_data elements

    def sum_of_data(self):
        cur_node = self.head

        l_sum = 0

        while cur_node:
            l_sum += int(cur_node.data)
            cur_node = cur_node.next

        print("Sum of the LinkedList elements are :- ", l_sum)

    def reverse_list(self):
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

        prev_node = None
        cur_node = self.head
        next_node = None

        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev_node

            prev_node = cur_node
            cur_node = next_node

        self.head = prev_node

    def recursive_reverse(self, head):
        """
        1) Divide the list in two parts - first node and 
        rest of the linked list.
        2) Call reverse for the rest of the linked list.
        3) Link rest to first.
        4) Fix head pointer
        """

        if head is None or head.next is None:
            return head

        # reverse the rest link
        rest = self.recursive_reverse(head.next)

        # put first element at the end
        head.next.next = head
        head.next = None

        # fix the head pointer
        return rest

    def node_swap(self, key_1, key_2):

        if key_1 == key_2:
            return

        cur_1 = self.head
        prev_1 = None
        # check for key_1
        while cur_1 and cur_1.data != key_1:
            prev_1 = cur_1
            cur_1 = cur_1.next

        # print("key_1 is",key_1,"and Previous node is ", prev_1.data)

        cur_2 = self.head
        prev_2 = None
        # check for key_2
        while cur_2 and cur_2.data != key_2:
            prev_2 = cur_2
            cur_2 = cur_2.next

        # print("key_2 is",key_2, "and Previous node is ", prev_2.data)

        if not cur_1 or not cur_2:
            return

        # if prev_1:
        #     prev_1.next = cur_2
        # else:
        #     self.head = cur_2

        # if prev_2:
        #     prev_2.next = cur_1
        # else:
        #     self.head = cur_1

        # prev_1.next = cur_2
        # prev_2.next = cur_1

        cur_1.data, cur_2.data = cur_2.data, cur_1.data

    # remove duplicate
    def remove_duplicate(self):
        cur_node = self.head
        prev_node = None

        dup_values = dict()

        while cur_node:
            if cur_node.data in dup_values:
                # Remove node
                prev_node.next = cur_node.next
                cur_node = None
                pass
            else:
                # have not encounter element before
                dup_values[cur_node.data] = 1
                prev_node = cur_node

            cur_node = prev_node.next

    # N-th-to-last Node
    def nth_last_node_last(self, pos):
        cur_node = self.head

        l = self.length()
        while cur_node:
            if l == pos:
                print(cur_node.data)
                return
                # return cur_node.data
            l -= 1
            cur_node = cur_node.next

        # print(f"{pos} node for the last is {cur_node.data}")

    # nth node from last (new method)
    def nth_last_node_twoPointer(self, pos):
        p = self.head
        q = self.head

        count = 0
        while q and count < pos:
            q = q.next
            count += 1

        if not q:
            return "Sorry pos is greater then no of node in list"

        while p and q:
            p = p.next
            q = q.next

        print(p.data)
        return p.data

    # count the number of time the node appars
    def count_occurance(self, number):
        cur_node = self.head

        count = dict()
        while cur_node:
            if cur_node.data not in count:
                count[cur_node.data] = 1
            else:
                count[cur_node.data] += 1

            cur_node = cur_node.next

        print(count)


l = LinkedList()
l.append("A")
l.append("B")
l.append("C")
l.append("A")
l.append("D")
# l.append("E")
# l.append("F")
# l.append("5")
# l.append("6")
# l.append("7")
# l.add_in_between("2","3")
# print list

# l.nth_last_node_last(3)
# l.nth_last_node_twoPointer(3)
print(l.count_occurance("A"))

# l.print_list()

# print("Node Swap")
# l.node_swap("3","1")
# l.print_list()


# only works if data is int
# l.sum_of_data()

# print length of LinkedList
# l.length()
# find find_middle
# l.find_middle()
# l.find_middle_2_pointer()
# l.reverse_list()
# l.recursive_reverse(l.head)
# print("reverse_list")
# l.print_list()
# print("****")
# l.remove_duplicate()
# l.print_list()
