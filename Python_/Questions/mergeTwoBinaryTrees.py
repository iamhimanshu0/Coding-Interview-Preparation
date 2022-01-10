"""
# https://leetcode.com/problems/merge-two-binary-trees/

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

root1 = [1,3,5,7]
root2 = [2,1,3, None, 4, None, 7]
def mergeTree(t1, t2):
    if not t1 and not t2:
        return None
    
    v1 = t1.value if t1 else 0
    v2 = t2.value if t2 else 0

    root = Node(v1+v2)

    root.left = mergeTree(t1.left if t1 else None,
                            t2.left if t2 else None    
                        )
    
    root.right = mergeTree(t1.right if t1 else None,
                            t2.right if t2 else None    
                        )

    return root


print(
    mergeTree(t1.root, t2.root)      
)

# print(t1.root.value, t1.root.left.value, t1.root.right.value, t1.root.left.left.value)
# print(t2.root.value, t2.root.left.value,
#         t2.root.right.value, t2.root.left.right.value, t2.root.right.right.value)



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def mergeTrees(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> Optional[TreeNode]:
#         """
#         """
#         if t1 is None:
#             return t2
						
#         stack = []
#         stack.append((t1,t2))
#         while stack:
#             t = stack.pop()
#             if t[1] is None:
#                 continue
#             t[0].val += t[1].val
            
#             if t[0].left is None:
#                 t[0].left = t[1].left
#             else:
#                 stack.append((t[0].left,t[1].left))
            
#             if t[0].right is None:
#                 t[0].right = t[1].right
#             else:
#                 stack.append((t[0].right,t[1].right))
#         return t1
# """