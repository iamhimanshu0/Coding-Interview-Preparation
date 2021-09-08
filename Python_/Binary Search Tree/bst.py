class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Average:: O(log(n)) time | O(1) space
    # worst :: O(n) time | O(1) space
    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                # get left subtree
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left

            else:
                # get right subtree
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right

        return self

    # Average:: O(log(n)) time | O(1) space
    # worst :: O(n) time | O(1) space
    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True

    def remove(self, value, parentNode=None):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                # node to deleted if 2 child
                if currentNode.left is not None and currentNode.right is not None:
                    # currentNode.value = smallest value of right subtree
                    currentNode.value = currentNode.right.getMinValue()
                    # delete that node 
                    currentNode.right.remove(currentNode.value, currentNode)
                # if current node is none
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left  = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right  = currentNode.right.right
                    else:
                        currentNode.value = None
                # if we don't have 2 child node
                elif parentNode.left == currentNode:
                    parentNode.left = (
                        currentNode.left
                        if currentNode.left is not None
                        else currentNode.right
                    )
                elif parentNode.right == currentNode:
                    parentNode.right = (
                        currentNode.left 
                        if currentNode.len is not None 
                        else currentNode.right
                    )
                break
        return self

    def getMinValue(self):
        currentNode = self 
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value