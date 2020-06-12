import timeit
from unittest import TestCase
from ATSelf.Aufgabe2 import *
import random
import matplotlib.pyplot as plt

def setup1():
    s1 = Node("S1")
    s2 = Node("S2", s1)
    s3 = Node("S3", s2)
    s4 = Node("S4", s2)

    return s1, [s1, s2, s3, s4]


def setup2():
    s1 = Node("S1")

    s2 = Node("S2", s1)

    s3 = Node("S3", s2)
    s4 = Node("S4", s2)
    s5 = Node("S5", s2)

    s6 = Node("S6", s3)
    s7 = Node("S7", s3)

    return s1, [s1, s2, s3, s4, s5, s6, s7]


def setup3():
    s5 = Node("S5")
    s1 = Node("S1", s5)
    s2 = Node("S2", s5)
    s3 = Node("S3", s5)
    s4 = Node("S4", s5)

    return s5, [s1, s2, s3, s4, s5]


def generateRandom(n: int):
    s0 = Node("0")

    nodes = [s0]
    for i in range(1, n):
        nodes.append(Node(str(i), random.choice(nodes)))

    return s0, nodes


def f0(node, i):
    return i


def f1(node, i):
    return i + 1


def f2(node, i):
    return (i + 1) ** 2


def f3(node, i):
    return int(getNodeID(node)) + i ** 2


class Test(TestCase):
    def test_solve(self):
        for idx, (setup, exp, f) in enumerate([(setup1, 2, f1),
                                               (setup2, 3, f1),
                                               (setup2, 0, f0),
                                               (setup2, 6, f2),
                                               (setup3, 4, f3)]):
            root, nodeList = setup()
            res = solve(nodeList, f)
            print(idx, res)
            if res != exp:
                print_tree(root, horizontal=False)

            self.assertEqual(res, exp, f"Case: {idx}")

    def test_solve_random_ntimes(self):
        n = np.arange(0, 10000, 1000)
        runtime = []
        for i in range(len(n)):

            print(n[i])
            start = timeit.default_timer()

            root, nodeList = generateRandom(n[i])

            stop = timeit.default_timer()
            delta = stop-start

            runtime.append((n[i], delta))

            res = solve(nodeList, f0)
            if res != 0:
                print_tree(root, horizontal=False)

            self.assertEqual(res, 0, f"Rand: {i}")



        plt.scatter(*zip(*runtime))
        plt.plot(*zip(*runtime))
        plt.savefig('plots/'+str(n[-1])+'.png')
        print(runtime)

        plt.xscale("log")
        plt.scatter(*zip(*runtime))
        plt.plot(*zip(*runtime))
        plt.savefig('plots/' + str(n[-1]) + '_log.png')
