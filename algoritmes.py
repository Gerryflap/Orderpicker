import math

from graphlib import Graph, distance


def getHeuristic(g, toDo, maxWeight, weight=0):
    length = 0
    if len(toDo) == 0:
        return 0
    for v in toDo:
        length += distance(v, g.root)
        weight += v.weight
    averageOrderWeight = weight/len(toDo)
    averagePerRound = math.floor(maxWeight/averageOrderWeight)
    return length/(math.ceil(weight/averagePerRound))


def getRoute(g :Graph, maxWeight):
    orders = g._vertices[:]
    location = g.root
    weight = 0
    dist = 0
    while orders or location != g.root:
        possible = [v for v in orders if weight + v.weight <= maxWeight and v != location]
        if location != g.root:
            possible.append(g.root)
        if not possible:
            nextV = g.root
        else:
            nextV = None
            bestScore = None
            for v in possible:
                estimate = getHeuristic(g, [vx for vx in orders if vx != v], maxWeight) + distance(location, v)
                if bestScore == None or estimate <= bestScore:
                    nextV = v
                    bestScore = estimate
        dist += distance(location, nextV)
        if nextV == g.root:
            weight = 0
        else:
            weight += nextV.weight
        g.addEdge(location, nextV)
        if location != g.root:
            orders.remove(location)
        location = nextV

    return dist


def printRoute(g: Graph):
    location = g.root
    print((g.root.x, g.root.y), 0)
    toDo = set(g.V())
    nbs = g.getNeigbourList()
    weight = 0
    while toDo:
        neighbours = [x for x in nbs[location] if x in toDo]
        if len(neighbours) == 0:
            location = g.root
        else:
            location = neighbours[0]
        if location == g.root:
            weight = 0
        else:
            weight += location.weight
        print((location.x, location.y), weight)
        if location != g.root:
            toDo.remove(location)
