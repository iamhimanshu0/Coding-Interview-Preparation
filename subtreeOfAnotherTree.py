"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def isSubtree(root, subRoot):
    if not subRoot:
        return True
    
    def checkTree(root1, root2):
        if not root1 and not root2:
            return True

        elif root1 and not root2 or root2 and not root1:
            return False
        
        if root1.val != root2.val:
            return False

        return checkTree(root1.left, root2.left) and checkTree(root1.right, root2.right)

    
    def dfs(s,t):
        if not s:
            return False
        
        if s.val == t.val and checkTree(s,t):
            return True
        
        return dfs(s.left, t) or dfs(s.right,t)

    return dfs(root, subRoot)
   

root = Node(3)
root.left = Node(4)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(2)


subRoot = Node(4)
subRoot.left = Node(1)
subRoot.right = Node(2)


print(
    isSubtree(root, subRoot)
)
