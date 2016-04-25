from algoritmes import getRoute, printRoute
from graphlib import Graph

l = [(0,0,-1), (5,5,1), (1, 10, 1), (10,7,7), (2,3,3), (2,4,7), (10, 13, 3), (10, 11, 3), (10, 12, 3)]
g = Graph(l)


for w in range(7, 200):
    print(w, getRoute(g, w))
    g.clearEdges()

l = [(0,0,-1), (1,3,7), (3,6,3), (5,5,3), (6,4,3), (5,1,7)]
g = Graph(l)


for w in range(7, 100):
    print(w, getRoute(g, w))
    printRoute(g)
    g.clearEdges()