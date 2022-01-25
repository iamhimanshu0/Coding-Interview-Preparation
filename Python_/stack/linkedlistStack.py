class Node:
    def __init__(self, value):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next


class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        value = [str(x.value) for x in self.LinkedList]
        return "\n".join(value)

    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
        if self.isEmpty:
            return "Nothing to remove"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.pop()
print(s)
# print(s.isEmpty())
