"""
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

def maxHeight(root):
    if not root: return 0

    stack = [root]
    m = 0
    while stack:
        currentMax = 0
        for _ in range(len(stack)):
            currentMax+=1
            node = stack.pop(0)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        m = max(m, currentMax)
    return m +1     

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(maxHeight(root))