"""
# https://leetcode.com/problems/search-in-a-binary-search-tree/

You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Input: root = [4,2,7,1,3], val = 5
Output: []
"""

from pickletools import stackslice


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def searchBST(root, val):
    
    stack = [root]
    res = None

    while stack:
        node = stack.pop(0)

        if node.val == val:
            # return bfs(node)
            return node
        else:
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

    return res
            
        
    # return res

# if we need to return all the subtree nodes then use this 
def bfs(root):
    res = []
    stack = [root]

    while stack:
        node = stack.pop(0)
        res.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return res

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)

root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

print(
    searchBST(root, 3)
)