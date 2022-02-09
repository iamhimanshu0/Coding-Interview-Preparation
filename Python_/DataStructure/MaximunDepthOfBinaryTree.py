"""
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Input: root = [3,9,20,null,null,15,7]
Output: 3

Input: root = [1,null,2]
Output: 2
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def depthOfBinaryTree(root):
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

    return len(res)
        


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(depthOfBinaryTree(root))