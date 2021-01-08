# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    s = []
    current = tree
    get_next = False
    while True:
        if current is not None:
            s.append(current)
            current = current.left
        elif len(s) > 0:
            current = s.pop()
            if get_next is True:
                return current
            if current == node:
                get_next = True

            current = current.right
        else:
            break
    return None





