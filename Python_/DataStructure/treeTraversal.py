"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.

Tree traversal
- Binary Tree Preorder Traversal
# https://leetcode.com/problems/binary-tree-preorder-traversal/


"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

def preorderTraversal(node):
    if not node:
        return []
    
    s = [root.value]
    s += preorderTraversal(root.left)
    s += preorderTraversal(root.right)

    return s

    
def inorderTraversal(node):
    if not node:
        return []
    s = []

    s += preorderTraversal(root.left)
    s = [root.value]    
    s += preorderTraversal(root.right)

    return s


def postorderTraversal(node):
    if not node:
        return []
    s = []


    s += preorderTraversal(root.left)
    s += preorderTraversal(root.right)
    s += [root.value]    
    

    return s


root = Node(1)
root.right = Node(2)
root.right.left = Node(3)


# preorderTraversal(root)
inorderTraversal(root)