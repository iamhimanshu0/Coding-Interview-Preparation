"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Input: root = [1]
Output: [[1]]

Input: root = []
Output: []
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrdertraversal(root):
    if not root: return []

    stack = [root]
    result = []

    while stack:
        current = []
        for _ in range(len(stack)):
            curNode = stack.pop(0)
            current.append(curNode.val)
            if curNode.left:
                stack.append(curNode.left)
            if curNode.right:
                stack.append(curNode.right)
        result.append(current)
    return result

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(
    levelOrdertraversal(root)
)