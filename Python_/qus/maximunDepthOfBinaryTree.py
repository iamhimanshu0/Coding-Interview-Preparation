"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Input: root = [3,9,20,null,null,15,7]
Output: 3

Input: root = [1,null,2]
Output: 2
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepthBFS(node):
    if node == None:
        return 0
    
    stack = [node]
    result = []

    while stack:
        res = []
        for i in range(len(stack)):
            curNode = stack.pop(0)
            
            if curNode.left:
                stack.append(curNode.left)
            if curNode.right:
                stack.append(curNode.right)
        result.append(res)

    return len(result)

def maxDepthDFS(root):
    if not root: return 0

    depth = 0
    stack = [root]

    while stack:
        
        currentDepth = 1
        for _ in range(len(stack)):
            currentDepth +=1
            curNode = stack.pop()
            if curNode.left:
                stack.append(curNode.left)
            if curNode.right:
                stack.append(curNode.right)
        depth = max(currentDepth, depth)

    return depth

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(
    maxDepthDFS(root)
)