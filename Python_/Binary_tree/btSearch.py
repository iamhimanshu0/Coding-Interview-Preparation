class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:

    def depthFirstSearch(self, root):
        result = []
        stack = [root]
        while len(stack) > 0:
            current = stack.pop()
            result.append(current.value)

            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

        return result

    def treeNodeAddition(self, root):
        return sum(self.depthFirstSearch(root))

    def treeSearchNode(self, root, node):
        isFind = 0
        stack = [root]
        while len(stack) > 0:
            current = stack.pop()
            if current.value == node:
                isFind = 1
            else:
                if current.left:
                    stack.append(current.left)
                if current.right:
                    stack.append(current.right)

        if isFind == 0:
            return False
        else:
            return True


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#     1
#    /  \
#    2  5
#  /  \  \
#  3  4   6

# print(BinaryTree().depthFirstSearch(a))
# print(BinaryTree().treeNodeAddition(a))
# print(BinaryTree().treeSearchNode(a, 2))
# print(BinaryTree().treeSearchNode(a, 5))
# print(BinaryTree().treeSearchNode(a, 6))
# print(BinaryTree().treeSearchNode(a, 1))
# print(BinaryTree().treeSearchNode(a, 10))
