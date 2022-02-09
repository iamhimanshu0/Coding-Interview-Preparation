"""
# https://leetcode.com/problems/binary-tree-level-order-traversal/

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Input: root = [1]
Output: [[1]]

Input: root = []
Output: []
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrderTraversal(root):
    if not root: return []
    stack = [root]
    res = []
    while stack:
        currentNode = []
        for _ in range(len(stack)):
            value = stack.pop(0)
            currentNode.append(value.val)
            if value.left:
                stack.append(value.left)

            if value.right:
                stack.append(value.right)

        res.append(currentNode)

    return res



root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left  = TreeNode(15)
root.right.right = TreeNode(7)

print(
    levelOrderTraversal(root)
)