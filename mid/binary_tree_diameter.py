# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def depth(tree, level):
    if tree is None:
        return level

    return max(depth(tree.left, level + 1), depth(tree.right, level + 1))


def binaryTreeDiameter(tree):
    if tree is None:
        return 0

    left = depth(tree.left, 0)
    right = depth(tree.right, 0)

    maxL = binaryTreeDiameter(tree.left)
    maxR = binaryTreeDiameter(tree.right)

    return max(left + right, maxL, maxR)





