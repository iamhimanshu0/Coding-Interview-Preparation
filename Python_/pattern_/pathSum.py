"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.

"""


class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def pathSum(root, targetSum):
    if root == []:
        return False

    stack = [(root, targetSum)]

    while stack:
        curNode, curSum = stack.pop()

        if curNode.left is curNode.right is None and curNode.val == curSum:
            return True

        if curNode.left:
            stack.append([curNode.left, curSum-curNode.val])
        if curNode.right:
            stack.append([curNode.right, curSum-curNode.val])

    return False


def recursive(root, targetSum):
    if not root:
        return False
    elif not root.left and not root.right:
        if root.val == targetSum:
            return True
        else:
            return False

    return recursive(root.left, targetSum - root.val) or recursive(root.right, targetSum - root.val)


root = Node(5)
root.left = Node(4)
root.left.left = Node(11)
root.left.left.left = Node(7)
root.left.left.right = Node(2)

root.right = Node(8)
root.right.left = Node(13)
root.right.right = Node(4)
root.right.right.right = Node(1)


print(recursive(root, 22))
