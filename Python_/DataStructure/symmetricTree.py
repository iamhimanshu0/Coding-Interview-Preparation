"""
# https://leetcode.com/problems/symmetric-tree/

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Input: root = [1,2,2,3,4,4,3]
Output: true

Input: root = [1,2,2,null,3,null,3]
Output: false
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root):

    def isMirror(left, right):
        if left in None and right is None:
            return True
        if left in None or right is None:
            return False
        
        if left.val == right.val:
            outPair = isMirror(left.left, right.right)
            inPair = isMirror(left.right, right.left)
            return outPair and inPair
        else:
            return False

    if root is None:
        return True
    else:
        return isMirror(root.left, root.right)
