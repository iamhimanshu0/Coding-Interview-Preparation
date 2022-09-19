"""
Given the root of a binary tree, invert the tree, and return its root.

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Input: root = [2,1,3]
Output: [2,3,1]

Input: root = []
Output: []
"""


from difflib import restore


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def invertTree(root):
    if not root:
        return

    left = root.left
    right = root.right

    root.left = invertTree(right)
    root.right = invertTree(left)

    return root


def usingStack(root):
    if not root:
        return

    stack = [root]

    while stack:
        node = stack.pop()
        left = node.left
        node.left = node.right
        node.right = left

        if node.left:
            stack.append(node.left)

        if node.right:
            stack.append(node.right)

    return root


def get_data(root):
    stack = [root]
    result = []
    while stack:
        node = stack.pop(0)
        result.append(node.val)

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return result


root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)

root.right = Node(7)
root.right.left = Node(6)
root.right.right = Node(9)


# root = Node(2)
# root.left = Node(1)
# root.right = Node(3)

print(invertTree(root))
print("")
print(get_data(usingStack(root)))
