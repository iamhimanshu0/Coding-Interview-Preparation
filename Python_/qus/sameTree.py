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

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p,q):
    if not p and not q: return True
   
    def bfs(root):
        if not root: return []
        stack = [root]
        result = []

        while stack:
            curNode = stack.pop()
            result.append(curNode.val)

            if curNode.left:
                stack.append(curNode.left)
            else:
                result.append("left")

            if curNode.right:
                stack.append(curNode.right)
            else:
                result.append("right")


        return result

    print(bfs(p))
    print(bfs(q))

    return bfs(p) == bfs(q)

    
def isSameTree2(p,q):
    if not p and not q: return True
        
    stack =  [[p,q]]
    result = []

    while stack:
        pValue, qValue = stack.pop(0)
        
        if not pValue or not qValue:
            return False

        if pValue.val == qValue.val:
            result.append(True)
        else:
            result.append(False)
        
        if pValue.left or qValue.left:
            stack.append([pValue.left, qValue.left])
        # else:
        #     return False
        
        if pValue.right or qValue.right:
            stack.append([pValue.right, qValue.right])
        # else:
        #     return False
    # print(result)
    return all(result)


p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

print(isSameTree2(p,q))