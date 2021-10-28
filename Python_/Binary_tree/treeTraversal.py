
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:

    def PreOrder(self, root):
        """root -> left -> right"""

        if root:
            print(root.value, end="->")
            self.inOrder(root.left)
            self.inOrder(root.right)

    def PostOrder(self, root):
        """left -> right -> root"""

        if root:
            self.PostOrder(root.left)
            self.PostOrder(root.right)
            print(root.value, end="->")

    def InOrder(self, root):
        """left -> root -> right"""
        if root:
            self.InOrder(root.left)
            print(root.value, end="->")
            self.InOrder(root.right)

    def DepthFirstSearch(self, root):
        if not root:
            return []

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


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)


#     1
#    / \
#   2   3
#  / \ / \
# 4  5 6  7

# print(BinaryTree().PreOrder(root))
# print(BinaryTree().PostOrder(root))
# print(BinaryTree().InOrder(root))
print(BinaryTree().DepthFirstSearch(root))
