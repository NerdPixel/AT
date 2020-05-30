import numpy as np

class Tree:
    def __init__(self, val):
        self.node = val
        self.left = None
        self.right = None


def setup(arr, root, i, n):
    if i < n:
        temp = Tree(arr[i])
        root = temp
        root.left = setup(arr, root.left, 2 * i + 1, n)
        root.right = setup(arr, root.right, 2 * i + 2, n)
    return root


def calcnodes(k):
    return _calcNodes(2 ** k)


def _calcNodes(k):
    if k == 1:
        return 1
    return k + _calcNodes(int(k / 2))


def traverse(root):
    currentLevel = [root]
    while currentLevel:
        for node in currentLevel:
            print(node.node, "\t", end='')
        print()
        nextLevel = list()
        for n in currentLevel:
            if n.left:
                nextLevel.append(n.left)
            if n.right:
                nextLevel.append(n.right)
        currentLevel = nextLevel


def calcHight(root):
    if root is None:
        return 0
    return 1 + calcHight(root.left)


def generateNodeList(nLeaf: int):
    nNodes = calcnodes(nLeaf)
    return np.arange(0, nNodes)


if __name__ == '__main__':
    nLeaf = 3

    nodeList = generateNodeList(nLeaf)
    t = setup(nodeList, None, 0, len(nodeList))
    traverse(t)

    relevantNodes = [(7, 8), (9, 10), (11, 12), (13, 14)]
    #relevantNodes = [(7, 14), (8, 9), (10, 13), (11, 12)]
