"""
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].

Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def averageOfLevels(root):
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        s = 0
        size = len(stack)
        for i in range(size):
            node = stack.pop(0)
            s += node.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        result.append(s/size)

    return result


root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

print(
    averageOfLevels(root)
)
