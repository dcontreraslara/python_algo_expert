import sys
def findClosestValueInBst(tree, target):
    if tree is None:
        return sys.maxsize

    current = abs(tree.value - target)
    left = findClosestValueInBst(tree.left, target)
    right = findClosestValueInBst(tree.right, target)

    if current < abs(left - target) and current < abs(right - target):
        return tree.value

    if abs(left - target) < abs(right - target):
        return left

    if abs(right - target) < abs(left - target):
        return right


import unittest


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)
        expected = 13
        actual = findClosestValueInBst(root, 12)
        self.assertEqual(expected, actual)
