class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)

    # isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    # push
    def push(self, value):
        self.list.append(value)
        return f"Element {value} has been inserted!"

    # pop
    def pop(self):
        if self.isEmpty():
            return "No element to remove"
        else:
            return self.list.pop()

    # peek
    def peek(self):
        if self.isEmpty():
            return "No top element"
        else:
            return self.list[len(self.list) - 1]

    # delete entire stack
    def delete(self):
        self.list = None


s = Stack()
s.push(1)
s.push(2)
s.push(3)
# print(s.peek())
# print(s)
