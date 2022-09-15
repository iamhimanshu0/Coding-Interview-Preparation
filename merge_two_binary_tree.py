"""
You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.

Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]

Input: root1 = [1], root2 = [1,2]
Output: [2,2]
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def mergeTrees(root1, root2):

    if not root1:
        return root2
    if not root2:
        return root1

    new_node = Node(root1.val + root2.val)
    # root1.val += root2.val

    new_node.left = mergeTrees(root1.left, root2.left)
    new_node.right = mergeTrees(root1.right, root2.right)

    return new_node


def dfs(p):
    if not p:
        return
    stack = [p]
    result = []
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return result


root1 = Node(1)
root1.left = Node(3)
root1.right = Node(2)
root1.left.left = Node(5)

root2 = Node(2)
root2.left = Node(1)
root2.right = Node(3)
root2.left.right = Node(4)
root2.right.right = Node(7)


m = mergeTrees(root1, root2)
print(dfs(m))
