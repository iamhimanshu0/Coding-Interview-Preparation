"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Node(-10)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)


def maxPathSum(root):
    max_path = float("-inf")

    def get_max_gain(node):
        nonlocal max_path
        if node is None:
            return 0

        gain_on_left = max(get_max_gain(node.left), 0)
        gain_on_right = max(get_max_gain(node.right), 0)

        current_max_path = node.val + gain_on_left + gain_on_right

        max_path = max(max_path, current_max_path)

        return node.val + max(gain_on_left, gain_on_right)

    get_max_gain(root)
    return max_path


print(
    maxPathSum(root),
    maxPathSum(root1)
)
