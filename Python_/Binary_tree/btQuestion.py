from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:

    def depthFirstSearch(self, root):
        result = []
        stack = [root]
        while len(stack) > 0:
            current = stack.pop()
            result.append(current.value)

            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

        return result

    def treeNodeAddition(self, root):
        return sum(self.depthFirstSearch(root))

    def recurrsiveNodeAddition(self, root):
        if root == None:
            return 0
        else:
            return root.value + self.recurrsiveNodeAddition(root.left) + self.recurrsiveNodeAddition(root.right)

    # searching using BFS

    def bfsSearch(self, root, target):
        if not root:
            return False

        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node.val == target:
                return True

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return False

    # Searching using DFS
    def treeSearchNode(self, root, node):
        isFind = 0
        stack = [root]
        while len(stack) > 0:
            current = stack.pop()
            if current.value == node:
                isFind = 1
            else:
                if current.left:
                    stack.append(current.left)
                if current.right:
                    stack.append(current.right)

        if isFind == 0:
            return False
        else:
            return True

    def recursiveSearch(self, root, target):
        if not root:
            return False

        if root.value == target:
            return True

        return self.recursiveSearch(root.left, target) or self.recursiveSearch(root.right, target)

    def findMaximum(self, root):
        if root == None:
            return "No root found"
        stack = [root]
        result = []
        while len(stack) > 0:
            val = stack.pop()
            result.append(val.value)

            if val.left:
                stack.append(val.left)
            if val.right:
                stack.append(val.right)

        return max(result)

    def recurrsiveFindMaximun(self, root):
        if root is None:
            return 0

        value = root.value
        left = self.recurrsiveFindMaximun(root.left)
        right = self.recurrsiveFindMaximun(root.right)

        if left > value:
            value = left
        if right > value:
            value = right

        return value

    # only if tree is BST
    def minValue(self, root):
        if root.left == None:
            return root.value
        return self.minValue(root.left)

    def printLeftSide(self, root):
        if root is None:
            return

        print(root.value)
        return self.printLeftSide(root.left)

    """
    Method 2: Another method to solve this problem is to do Level Order Traversal. 
    While doing the level order traversal, while adding Nodes at each level to Queue, 
    we have to add NULL Node so that whenever it is encountered, we can increment the 
    value of variable and that level get counted.
    """

    def heightOfTreeRecurssive(self, root):
        if not root:
            return 0

        dleft = self.heightOfTreeRecurssive(root.left)
        dright = self.heightOfTreeRecurssive(root.right)

        max_depth = max(dleft, dright) + 1

        return max_depth


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#     1
#    /  \
#    2  5
#  /  \  \
#  4  3   6

# print(BinaryTree().depthFirstSearch(a))
# print(BinaryTree().treeNodeAddition(a))
# print(BinaryTree().recurrsiveNodeAddition(a))
# print(BinaryTree().treeSearchNode(a, 2))
# print(BinaryTree().treeSearchNode(a, 5))
# print(BinaryTree().treeSearchNode(a, 6))
# print(BinaryTree().treeSearchNode(a, 1))
# print(BinaryTree().recursiveSearch(a, 10))
# print(BinaryTree().findMaximum(a))
# print(BinaryTree().recurrsiveFindMaximun(a))
# print(BinaryTree().printLeftSide(a))
# print(BinaryTree().heightOfTreeRecurssive(a))
# print(BinaryTree().heightOfTree(a))
print(BinaryTree().minValue(a))
