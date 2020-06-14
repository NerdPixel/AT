import timeit
from unittest import TestCase
from ATSelf.Aufgabe2 import *
import random
import matplotlib.pyplot as plt


def setup1():
    s0 = Node("0")
    s1 = Node("1", s0)
    s2 = Node("2", s1)
    s3 = Node("3", s1)

    return s0, [s0, s1, s2, s3]


def setup2():
    s0 = Node("0")

    s1 = Node("1", s0)

    s2 = Node("2", s1)
    s3 = Node("3", s1)
    s4 = Node("4", s1)

    s5 = Node("5", s2)
    s6 = Node("6", s2)

    return s0, [s0, s1, s2, s3, s4, s5, s6]


def setup3():
    s4 = Node("4")
    s0 = Node("0", s4)
    s1 = Node("1", s4)
    s2 = Node("2", s4)
    s3 = Node("3", s4)

    return s4, [s0, s1, s2, s3, s4]


def setup4():
    s0 = Node("0")
    s1 = Node("1", s0)
    s2 = Node("2", s1)
    s3 = Node("3", s2)

    return s0, [s0, s1, s2, s3]


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
    return int(node.name) + i ** 2


test_cases = [
    (setup1, 2, f1),
    (setup2, 3, f1),
    (setup2, 0, f0),
    (setup2, 6, f2),
    (setup3, 4, f3),
    (setup4, 3, f1),
    (setup4, 4, f2),
    (setup4, 3, f3),
]


class Test(TestCase):
    def test_solve(self):
        for idx, (setup, exp, f) in enumerate(test_cases):
            root, nodeList = setup()
            res = solve(nodeList, f)
            print(idx, res)
            if res != exp:
                print_tree(root, horizontal=False)

            self.assertEqual(res, exp, f"Case: {idx}")

    def test_solve_random_ntimes(self):
        maxValue = 100000
        step = 5000
        n = np.arange(0, int(maxValue), step)
        runtime = []
        for i in range(len(n)):

            start = timeit.default_timer()

            root, nodeList = generateRandom(n[i])

            stop = timeit.default_timer()
            delta = stop - start

            print(str(n[i]) + "\t", "\t\tdelta: " + str(delta / 60) + "\t\tin minutes")
            runtime.append((n[i], delta))

            res = solve(nodeList, f0)
            if res != 0:
                print_tree(root, horizontal=False)

            self.assertEqual(res, 0, f"Rand: {i}")

        plt.scatter(*zip(*runtime))
        plt.plot(*zip(*runtime))
        plt.savefig('plots/' + str(n[-1]) + '.png')
        print(runtime)

        plt.xscale("log")
        plt.scatter(*zip(*runtime))
        plt.plot(*zip(*runtime))
        plt.savefig('plots/' + str(n[-1]) + '_log.png')


if __name__ == '__main__':
    n = Test()
    n.test_solve_random_ntimes()
