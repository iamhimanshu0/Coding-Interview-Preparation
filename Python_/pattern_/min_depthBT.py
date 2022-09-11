"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Input: root = [3,9,20,null,null,15,7]
Output: 2

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def minDepth(root):
    if not root:
        return 0

    stack = [(root, 1)]

    while stack:
        node, level = stack.pop(0)
        if not node.left and not node.right:
            return level

        if node.left:
            stack.append([node.left, level+1])
        if node.right:
            stack.append([node.right, level+1])


root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)


# root = Node(2)
# root.right = Node(3)
# root.right.right = Node(4)
# root.right.right.right = Node(5)
# root.right.right.right.right = Node(6)

print(
    minDepth(root)
)
