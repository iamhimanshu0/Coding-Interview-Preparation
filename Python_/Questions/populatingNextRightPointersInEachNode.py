"""
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root):
        self.root = Node(root)

t1 = Tree(1)
t1.root.left = Node(3)
t1.root.right = Node(2)
t1.root.left.left = Node(5)

t2 = Tree(2)
t2.root.left = Node(1)
t2.root.right = Node(3)
t2.root.left.right =  Node(4)
t2.root.right.right = Node(7)

def connect(root):
    if not root:
        return root

    leftNode = Node(root)
    while leftNode:
        head = Node(leftNode)
        while head:
            head.left.next = head.right
            if head.next != None:
                head.right.next = head.next.left
            head = head.next 
        leftNode = leftNode.left 

    return leftNode