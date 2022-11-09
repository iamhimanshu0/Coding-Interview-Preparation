"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Input: root = [1,2]
Output: 1
 
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def diameter(root):

    max_val = 0

    def get_len(root):
        nonlocal max_val
        if not root:
            return 0

        left_len = get_len(root.left)
        right_len = get_len(root.right)

        max_val = max(max_val, left_len + right_len)
        return 1 + max(left_len, right_len)

    get_len(root)
    return max_val


root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)

print(
    diameter(root)
)
