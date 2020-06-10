from pptree import *
import numpy as np


def setup():
    s0 = Node("S0")

    s1 = Node("S1", s0)

    s2 = Node("S2", s1)
    s3 = Node("S3", s1)
    s4 = Node("S4", s1)

    s5 = Node("S5", s2)
    s6 = Node("S6", s2)

    return s0, [s0, s1, s2, s3, s4, s5, s6]


def sortNodes(nodeList):
    nodeDict = {}
    for node in nodeList:
        nodeDict[node] = len(node.children)
    nodes = sorted(nodeDict.items(), key=lambda x: x[1], reverse=True)

    return nodes


def getNodeID(node):
    return int(node.name[-1])


def f(node, i):
    return (i + 1) ** 2


def hit(node, i):
    if i == 0:
        return 1
    count = 1
    for child in node.children:
        count += hit(child, i - 1)
    return count


if __name__ == '__main__':
    root, nodeList = setup()
    print_tree(root, horizontal=False)
    nodeListSorted = sortNodes(nodeList)
