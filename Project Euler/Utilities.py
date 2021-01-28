import math, functools, itertools, networkx as nx

def Sum(a, b): return a + b
def Product(a, b): return a * b


def LeastCommonMultiple(x, y):
    return x*y / GreatestCommonFactor(x, y)

def GreatestCommonFactor(x, y):
    if(y > x):
        return GreatestCommonFactor(y, x)

    while y != 0:
        (x, y) = (y, x % y)
    return x

def ListOfPermutations(allowedDigits, disallowedDigitsInPosition=dict()):
    if(len(allowedDigits) == 1):
        if(0 in disallowedDigitsInPosition 
           and allowedDigits[0] in disallowedDigitsInPosition[0]):
            yield None
        else:
            yield(allowedDigits[0])
        return
    for digit in allowedDigits:
        if(digit in disallowedDigitsInPosition
           and len(allowedDigits) - 1 in disallowedDigitsInPosition[digit]):
            continue
        for subResult in ListOfPermutations(list(filter(lambda x: x != digit, allowedDigits))):
            yield(digit*10**(len(allowedDigits)-1) + subResult)


def IsPalindrome(n):
    stringN = str(n)
    return stringN == stringN[::-1]

def FileSplit(f, delim=',', bufsize=1024):
    prev = ''
    while True:
        s = f.read(bufsize)
        if not s:
            break
        split = s.split(delim)
        if len(split) > 1:
            yield prev + split[0]
            prev = split[-1]
            for x in split[1:-1]:
                yield x
        else:
            prev += s
    if prev:
        yield prev

def NumericScore(word):
    return functools.reduce(lambda acc, letter: acc + ord(letter) - 64, word, 0)

def Pentagonal(i):
    return (3*i**2 - i)//2

def IsPentagonal(p):
    x = (1 + 2*math.sqrt(.25 + 6*p))/6
    return x.is_integer() and x > 0

def Triangle(i):
    return (i**2 + i)//2

def IsTriangular(p):
    return (math.sqrt(.25+2*p)-.5).is_integer()

def Hexagonal(i):
    return 2*i**2 - i

def IsHexagonal(p):
    return (1 + math.sqrt(1+8*p)) % 4 == 0

def Square(i):
    return i**2

def IsSquare(i):
    return math.sqrt(i).is_integer()

def Heptagonal(i):
    return (5*i**2-3*i)//2


def Octagonal(i):
    return 3*i**2-2*i

def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    # Recipe credited to George Sakkis
    pending = len(iterables)
    nexts = itertools.cycle(iter(it).__next__ for it in iterables)
    while pending:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            pending -= 1
            nexts = itertools.cycle(itertools.islice(nexts, pending))

def allEqual(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == rest for rest in iterator)

def SequentialCompare(iterLeft, iterRight):
    for pair in zip(iterLeft, iterRight):
        if(pair[0] != pair[1]):
            return -1 if pair[0] > pair[1] else 1
    return 0

def GetOrAdd(dict, key, createFunc):
    if(key not in dict):
        dict[key] = createFunc()
    return dict[key]

def GetKCliques(graph, tarketK):
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
                toAdd = tuple(c.union({e}))
                cliques_1.add(toAdd)
        # remove duplicates
        cliques = list(map(set, cliques_1))
        k += 1
    return cliques

def countSetBits(n): 
    count = 0
    while (n): 
        n &= (n-1)  
        count+= 1
    return count 

def GenerateTotientValues(nMax):
    phi = list(i for i in range(0, nMax+1))
    for i in range(2, len(phi)):
        if(phi[i] == i):
            for j in range(i, nMax+1, i):
                phi[j] -= phi[j] // i
    return phi