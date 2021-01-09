# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        s = [(self, 0)]
        out = []

        while len(s) > 0:
            current_node, level = s.pop(0)

            for child in current_node.children:
                s.append((child, level + 1))

            out.append(current_node.name)

        return out
