"""
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Input: root = [1,2,3], targetSum = 5
Output: []

Input: root = [1,2], targetSum = 0
Output: []
"""

"""
DFS from the root down to it's descendants:
We need to keep current path (which stores elements in the path) so far.
We need to keep the remain targetSum so far (after minus value of elements in the path).
If we already reach into leaf node
Check if targetSum == 0 then we found a valid path from root to leaf node which sum equal to targetSum, so add current path to the answer.
Else dfs on left node and on the right node.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pathSum(root, target):
    
    def dfs(root, target, path):
        if not root: return None

        target -= root.val
        path.append(root.val)
        
        if not root.left and not root.right:
            if target == 0:
                ans.append(path.copy())
        else:
            dfs(root.left, target, path)
            dfs(root.right, target, path)
        
        path.pop()

    ans = []
    dfs(root, target, [])
    return ans

root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

print(
    pathSum(root,22)
)