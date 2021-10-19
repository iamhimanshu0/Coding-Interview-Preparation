class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def DepthFirstSearch(root):
    # if root is empty
    if root == None:
        return []
    else:
        # for storing result
        result = []
        # for doing DFs
        stack = [root]
        # loop through until the stack is empty
        while len(stack) > 0:
            # pop current item
            current = stack.pop()
            # append it to result
            result.append(current.value)

            # check if right not exist if yes then append
            if current.right:
                stack.append(current.right)
            # check if left not exist if yes then append
            if current.left:
                stack.append(current.left)

    return result


def recurssiveDFS(root):
    if root == None:
        return []

    leftValues = recurssiveDFS(root.left)
    rightValues = recurssiveDFS(root.right)

    return [root.value, *leftValues, *rightValues]


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#     a
#    /  \
#    b  c
#  /  \  \
#  d  e   f
# print(DepthFirstSearch(a))
print(recurssiveDFS(a))
