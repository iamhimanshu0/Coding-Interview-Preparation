class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
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

    # isFull
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    # push
    def push(self, value):
        if self.isFull():
            return "Can't add items it's full"
        else:
            self.list.append(value)
            return "Added Succssfully"

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


s = Stack(2)
print(s.isFull())
s.push(1)
s.push(2)
print(s.push(3))
print(s)
