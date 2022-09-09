"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Input: p = [1,2,3], q = [1,2,3]
Output: true

Input: p = [1,2], q = [1,null,2]
Output: false

Input: p = [1,2,1], q = [1,1,2]
Output: false
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def traverse(p, q):
    stack = [(p, q)]
    while stack:
        n1, n2 = stack.pop()
        if n1 and n2 and n1.val == n2.val:
            stack.append((n1.right, n2.right))
            stack.append((n1.left, n2.left))
        elif n1 != n2:
            return False
    return True


def isSameTree(root1, root2):
    return traverse(root1, root2)
    # if not root1 and not root2:
    #     return True
    # if not root1 or not root2:
    #     return False

    # if root1.val != root2.val:
    #     return False

    # return isSameTree(root1.right, root2.right) and isSameTree(root1.left, root2.left)

    # return traverse(root1) == traverse(root2)


root1 = Node(1)
# root1.left = Node(2)
root1.right = Node(2)
# root1.right.left = Node(3)

root2 = Node(1)
root2.left = Node(2)
# root2.right = Node(2)
# root2.right.right = Node(3)


print(isSameTree(root1, root2))
