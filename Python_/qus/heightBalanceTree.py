"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Input: root = [3,9,20,null,null,15,7]
Output: true

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O(n^2)
def isBalanced(root):
    
    def height(root):
        if not root:
            return 0 
        return max(height(root.left), height(root.right)) + 1

    if not root:
        return True
    
    leftHeight = height(root.left)
    rightHeight = height(root.right)

    if abs(leftHeight - rightHeight) <=1 and isBalanced(root.left) is True and isBalanced(root.right) is True:
        return True
    
    return False


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(isBalanced(root))