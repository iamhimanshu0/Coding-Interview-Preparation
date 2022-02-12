"""
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findTarget(root, k):
    if not root: return False

    stack = [root]
    res =  []
    
    while stack:
        node = stack.pop(0)
        res.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    d = {}
    for i, n in enumerate(res):        
        value = k - n
        if value in d:
            return True
        else:
            d[n] = i

    return False        

def findTarget2(root,k):
    if not root: return False
    bfs, s = [root] , set()
    for i in bfs:
        if k - i.val in s: return True
        s.add(i.val)

        if i.left: bfs.append(i.left)
        if i.right: bfs.append(i.right)
    return False

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)

root.left.left = TreeNode(2)
root.left.right = TreeNode(4)

root.right.right = TreeNode(7)

k = 9 

print(
    findTarget(root,k)
)
