import Utilities, itertools, networkx as nx, functools
from enum import IntFlag

triangles = set(map(Utilities.Triangle, range(45, 141)))
squares = set(map(Utilities.Square, range(32, 100)))
pentagons = set(map(Utilities.Pentagonal, range(26, 82)))
hexagons = set(map(Utilities.Hexagonal, range(23, 71)))
heptagons = set(map(Utilities.Heptagonal, range(21, 64)))
octagons = set(map(Utilities.Octagonal, range(19, 59)))

class PFlag(IntFlag):
    Unknown = 0
    Triangle = 1
    Square = 1 << 1
    Pentagon = 1<<2
    Hexagon = 1<<3
    Heptagon = 1<<4
    Octagon = 1<<5
    All = Triangle | Square | Pentagon | Hexagon | Heptagon | Octagon

def GetFlags(n):
    flag = PFlag.Unknown
    if(n in triangles):
        flag |= PFlag.Triangle
    if(n in squares):
        flag |= PFlag.Square
    if(n in pentagons):
        flag |= PFlag.Pentagon
    if(n in hexagons):
        flag |= PFlag.Hexagon
    if(n in heptagons):
        flag |= PFlag.Heptagon
    if(n in octagons):
        flag |= PFlag.Octagon
    return flag

def GetCycles(graph, length):
    possibleCycles = [[n] for n in graph.nodes()]
    k = 1
    while (k < length):
        nextCycles = list()
        for c in possibleCycles:
            last = c[-1]
            tails = []
            for e in graph.out_edges(last):
                if(len(c) > 1 and last == e[1] and c[-2] == last):
                    continue
                tails.append(e[1])
            for t in tails:
                nextCycles.append(c + [t])
        possibleCycles = nextCycles
        k += 1
    for c in possibleCycles:
        if((c[-1], c[0]) in graph.out_edges(c[-1])):
            yield c

def GetSumOfRepresentativeCycle(flagCheck, *pSets):
    graph = nx.DiGraph()
    for n in itertools.chain(*pSets):
        flags = GetFlags(n)
        nstr = str(n)
        graph.add_edge(int(nstr[:2]), int(nstr[2:]), types=flags)
    for c in GetCycles(graph, len(pSets)):
        representedP = set()
        for i in range(len(c)-1):
            edgeData = graph[c[i]][c[i+1]]["types"]
            representedP.add(edgeData)
        representedP.add(graph[c[-1]][c[0]]["types"])
        if(len(representedP) != len(pSets) or 
           functools.reduce(lambda acc, x: acc | x, representedP) & flagCheck != flagCheck): 
            continue
        sum = 0
        for i in range(len(c)-1):
            sum += c[i]*100 + c[i+1]
        sum += c[-1]*100 + c[0]
        return sum

assert GetSumOfRepresentativeCycle(PFlag.Triangle | PFlag.Square | PFlag.Pentagon, triangles, squares, pentagons) == 19291
answer = GetSumOfRepresentativeCycle(PFlag.All, triangles, squares, pentagons, hexagons, heptagons, octagons)
print (answer)
assert answer == 28684