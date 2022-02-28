"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Input: root = [1,null,3]
Output: [1,3]

Input: root = []
Output: []
"""
# Python3 program to print right


# A binary tree node
class Node:	
	# A constructor to create a new
	# Binary tree Node
	def __init__(self, val):
		self.data = val
		self.left = None
		self.right = None

def rightView(root):
    if not root: return None
    
    stack = [root]
    result = []

    while stack:
        n = len(stack)
        
        while n > 0:
            n-=1
            node = stack.pop(0)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            
            if n == 0:
                result.append(node.val)
        
    return result

# Driver code

# Let's construct the tree as
# shown in example
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)

print(
    rightView(root)
)


