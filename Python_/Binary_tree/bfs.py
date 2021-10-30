from collections import deque


class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def breadth_first_values(root):
    if not root:
        return []

    queue = deque([root])
    values = []

    while queue:
        node = queue.popleft()

        values.append(node.val)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return values


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)


#     1
#    / \
#   2   3
#  / \ / \
# 4  5 6  7

print(breadth_first_values(root))
