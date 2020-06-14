from pptree import *
import numpy as np


class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []
        self.ID = int(name[-1])

        if parent:
            self.parent.children.append(self)

    def adj(self):
        c = []
        if self.parent is not None:
            c += [self.parent]
        c += self.children
        return c

    def __delitem__(self, key):
        self.__delattr__(self.ID)

    def __getitem__(self, item):
        return self.__getattribute__(self.item)

    def __setitem__(self, key, value):
        self.__setattr__(key, value)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __add__(self, other):
        return self.name + other

    def __radd__(self, other):
        return other + self.name


def sortNodes(nodeList):
    nodeDict = {}
    for node in nodeList:
        nodeDict[node] = len(node.children)
    nodes = sorted(nodeDict.items(), key=lambda x: x[1], reverse=True)

    return nodes


def solve(root, nodelist):
    # TODO Implement
    return 0
