"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Input: root = [3,9,20,null,null,15,7]
Output: 3

Input: root = [1,null,2]
Output: 2
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def maxDepth(root):
    if not root:
        return 0

    result = 0

    stack = [root]

    while stack:
        result += 1
        for _ in range(len(stack)):
            node = stack.pop(0)

            if node:
                if node.left:
                    stack.append(node.left)

                if node.right:
                    stack.append(node.right)

    return result


root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

print(maxDepth(root))
