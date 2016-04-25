def distance(v1, v2):
    return abs(v1.x - v2.x) + abs(v1.y - v2.y)

class Edge:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
        self.length = distance(head, tail)


class Vertex:
    def __init__(self, x, y, weight):
        self.x = x
        self.y = y
        self.weight = weight

    def __repr__(self):
        return "<(%i, %i) w: %i>"%(self.x, self.y, self.weight)


class NoRootException(Exception):
    pass


class Graph:
    def __init__(self, vertexPositions):
        self._vertices = []
        self._edges = []
        self.root = None
        for pos in vertexPositions:
            x, y, weight = pos
            v = Vertex(x, y, weight)
            if weight == -1:
                self.root = v
            else:
                self._vertices.append(v)

        if self.root is None:
            raise NoRootException

    def V(self):
        return self._vertices

    def E(self):
        return self._edges

    def addEdge(self, v1, v2):
        self._edges.append(Edge(v1, v2))

    def getNeigbourList(self):
        nbs = dict()
        for v in self._vertices + [self.root]:
            nbs[v] = set()
        for e in self._edges:
            nbs[e.tail].add(e.head)
        return nbs

    def remove(self, v):
        self._edges = [edge for edge in self._edges if edge.head != v and edge.tail != v]
        self._vertices.remove(v)

    def clearEdges(self):
        self._edges = []

