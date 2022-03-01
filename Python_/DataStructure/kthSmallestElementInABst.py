"""
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

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
    if not root: return None

    # first travesal through the tree
    def dfs(root):
        result = []
        stack = [root]

        while stack:
            node = stack.pop()

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

            result.append(node.val)
        return result
    
    value = dfs(root)
    # dfs(root).sort()
    value.sort()
    return value[k-1]

def inOrderTraversal(root, k):

    def travel(root):
        if not root: return []
        return travel(root.left) + [root.val] + travel(root.right)

    return travel(root)[k-1]

def inOrderTraversalOnlyKTimes(root, k):
    stack = []

    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k-=1

        if not k:
            return root.val
        root = root.right


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)

print(
    #inOrderTraversal(root,3)
    inOrderTraversalOnlyKTimes(root,3)
    # kthSmallest(root,3)
)