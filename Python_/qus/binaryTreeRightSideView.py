"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Input: root = [1,null,3]
Output: [1,3]

Input: root = []
Output: []
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root):
    if not root: return []

    stack = [root]
    result = []

    while stack:
        n = len(stack)
        for _ in range(len(stack)):
            n-=1
            node = stack.pop(0)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

            if n ==0:
                result.append(node.val)

    return result         

# o(n) space and time 
def rightView(root):
    if not root: return []

    ans = []
    queue = [root]

    while queue:
        lastNode = None
        for _ in range(len(queue)):
            cur = queue.pop(0)
            lastNode = cur

            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        ans.append(lastNode.val)

    return ans


root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(5)

root.right = TreeNode(3)
root.right.right = TreeNode(4)

print(rightView(root))