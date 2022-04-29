"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.


Input: root = [3,1,4,null,2], k = 1
Output: 1

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root, k):
    if not root: return 0

    result = []
    stack = [root]
    
    while stack:
        curNode = stack.pop()
        result.append(curNode.val)

        if curNode.left:
            stack.append(curNode.left)
        if curNode.right:
            stack.append(curNode.right)
    
    result.sort()
    return result[k-1]

def inOrderKthSmallest(root,k):

    def inOrder(root):
        if not root: return []

        return inOrder(root.left) + [root.val] + inOrder(root.right)

    return inOrder(root)[k-1]

# root = TreeNode(3)
# root.left = TreeNode(1)
# root.right = TreeNode(4)
# root.left.right = TreeNode(2)

root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.left.left = TreeNode(1)
root.right = TreeNode(6)

print(inOrderKthSmallest(root,3))