# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def helper(topAncestor, descendantOne, descendantTwo, res, level=0):
    if descendantOne is None or descendantTwo is None:
        return None

    if descendantOne == descendantTwo:
        res.append([level, descendantOne])
        return descendantOne

    l = helper(topAncestor, descendantOne.ancestor, descendantTwo, res, level + 1)
    r = helper(topAncestor, descendantOne, descendantTwo.ancestor, res, level + 1)

    if l is not None:
        return l

    if r is not None:
        return r


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    res = []
    helper(topAncestor, descendantOne, descendantTwo, res, 0)
    if len(res) == 0:
        return None

    res = sorted(res, key=lambda x: x[0])
    return res[0][1]




print(ord('a'))