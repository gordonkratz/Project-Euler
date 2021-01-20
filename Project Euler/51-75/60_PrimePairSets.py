import Utilities, functools, Timer, itertools, primetools
import networkx as nx

def GetPrimePairs(nMax, primeMax):
    primes = set(primetools.GetPrimesFromFile(primeMax))
    for p in primes:
        if(p < 10): continue
        digits = len(str(p))
        for i in range(1, digits):
            powerOfTen = 10**i
            left = p // powerOfTen
            right = p % powerOfTen
            if(left > nMax or right > nMax):
                continue
            if(i > 1 and (right // (powerOfTen//10)) == 0):
                continue
            new = right * 10**(digits-i) + left
            if(left in primes and right in primes and new in primes):
                yield (left, right)



def GetPrimeAssociations(nMax):
    paths = dict()
    for (a, b) in GetPrimePairs(nMax):
        Utilities.GetOrAdd(paths, a, lambda : set()).add(b)
        Utilities.GetOrAdd(paths, b, lambda : set()).add(a)
    return paths

def GetCliquesLength(nMax, length):
    paths = GetPrimeAssociations(nMax)
    return GetAllCliques(paths, length)



def k_cliques(graph, tarketK):
    # 2-cliques
    cliques = [{i, j} for i, j in graph.edges() if i != j]
    k = 2
    
    while k < tarketK:        
        # merge k-cliques into (k+1)-cliques
        cliques_1 = set()
        for c in cliques:
            edges = None
            for v in c:
                if(edges == None):
                    edges = set(map(lambda t: t[1], graph.edges(v)))
                else:
                    edges = edges.intersection(set(map(lambda t: t[1], graph.edges(v))))
            for e in edges:
                cliques_1.add(tuple(c.union({e})))
        #for u, v in itertools.combinations(cliques, 2):
        #    w = u ^ v
        #    if len(w) == 2 and graph.has_edge(*w):
        #        cliques_1.add(tuple(u | w))

        # remove duplicates
        cliques = list(map(set, cliques_1))
        k += 1
    return cliques

from networkx.algorithms.approximation import clique

def NetworkxMethod(nMax, primeMax, length):
    graph = nx.Graph()
    for a, b in GetPrimePairs(nMax, primeMax):
        graph.add_edge(a, b)
    return k_cliques(graph, length)

def GetMinSumOfCliques(nMax, primeMax, length):
    return min(map(lambda c: functools.reduce(Utilities.Sum, c), NetworkxMethod(nMax, primeMax, length)))

assert GetMinSumOfCliques(10000, 700000, 4) == 792

answer = GetMinSumOfCliques(10000, 100000000, 5)
assert answer == 26033
