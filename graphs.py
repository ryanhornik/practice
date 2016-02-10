import random
from math import pow, sqrt
import sys


class Graph(object):
    class Node(object):
        def __init__(self, location=None):
            self.neighbors = []
            if location is None:
                self.location = (random.randrange(0, 10), random.randrange(0, 10))
            else:
                if type(location) is not tuple or len(location) != 2:
                    raise ValueError("Location must be tuple of length 2")
                self.location = location

        def add_neighbor(self, other):
            if other not in self.neighbors:
                self.neighbors.append(other)
            if self not in other.neighbors:
                other.add_neighbor(self)

        def estimate_distance(self, goal):
            x1, y1 = self.location
            x2, y2 = goal.location

            return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

        def __str__(self):
            return "Node ({}, {})".format(self.location[0], self.location[1])

    def __init__(self, root):
        self.root = root

    @staticmethod
    def path_cost(path):
        cost = 0
        for i in range(1, len(path)):
            cost += path[i - 1].estimate_distance(path[i])
        return cost

    def __str__(self):
        return str(self.root)


def setup_graph(start, end):
    A = Graph.Node((3, 0))
    B = Graph.Node((9, 0))
    C = Graph.Node((3, 3))
    D = Graph.Node((4, 3))
    E = Graph.Node((6, 3))
    F = Graph.Node((0, 4))
    G = Graph.Node((4, 4))
    N = Graph.Node((7, 6))
    H = Graph.Node((9, 6))
    I = Graph.Node((0, 8))
    J = Graph.Node((1, 8))
    K = Graph.Node((0, 9))
    O = Graph.Node((1, 9))
    L = Graph.Node((4, 9))
    M = Graph.Node((7, 9))
    P = Graph.Node((6, 4))
    Q = Graph.Node((7, 4))

    start.add_neighbor(A)
    start.add_neighbor(F)

    A.add_neighbor(B)
    A.add_neighbor(C)

    B.add_neighbor(H)

    C.add_neighbor(D)

    D.add_neighbor(E)
    D.add_neighbor(G)

    E.add_neighbor(P)
    P.add_neighbor(Q)
    Q.add_neighbor(N)

    F.add_neighbor(G)
    F.add_neighbor(I)

    G.add_neighbor(L)

    H.add_neighbor(end)
    H.add_neighbor(N)

    I.add_neighbor(J)
    I.add_neighbor(K)

    J.add_neighbor(O)

    K.add_neighbor(O)

    O.add_neighbor(L)

    L.add_neighbor(M)

    M.add_neighbor(N)

    N.add_neighbor(H)
    return Graph(start)


def find_a_star(start, goal, path=None):
    if path is None:
        path = {}
    closed_set = set()
    open_set = {start}
    g_scores = {start: 0}
    f_scores = {start: start.estimate_distance(goal)}

    while len(open_set) > 0:
        current = min(open_set, key=lambda x: f_scores[x])
        print(current)
        if current is goal:
            return reconstruct_path(path, goal)
        open_set.remove(current)
        closed_set.add(current)
        for neighbor in current.neighbors:
            if neighbor in closed_set:
                continue
            tentative_g_score = g_scores.get(current, sys.maxsize) + Graph.path_cost([current, neighbor])
            if neighbor not in open_set:
                open_set.add(neighbor)
            elif tentative_g_score >= g_scores.get(neighbor, sys.maxsize):
                continue

            path[neighbor] = current
            g_scores[neighbor] = tentative_g_score
            f_scores[neighbor] = g_scores[neighbor] + neighbor.estimate_distance(goal)
    return None


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

s = Graph.Node((0, 0))
e = Graph.Node((9, 9))
graph = setup_graph(s, e)

path = find_a_star(s, e)

if path:
    for n in path:
        print(n.location)
