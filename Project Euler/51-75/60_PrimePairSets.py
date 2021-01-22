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

def GetCliquesOfPrimes(nMax, primeMax, kLength):
    graph = nx.Graph()
    for a, b in GetPrimePairs(nMax, primeMax):
        graph.add_edge(a, b)
    return Utilities.GetKCliques(graph, kLength)

def GetMinSumOfCliques(nMax, primeMax, length):
    return min(map(lambda c: functools.reduce(Utilities.Sum, c), GetCliquesOfPrimes(nMax, primeMax, length)))

assert GetMinSumOfCliques(10000, 700000, 4) == 792

answer = GetMinSumOfCliques(10000, 100000000, 5)
assert answer == 26033
