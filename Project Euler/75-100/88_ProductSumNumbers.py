import primetools, functools, Utilities, itertools, Timer

factorizer = primetools.PrimeFactorizer(12000)

def Sum(x: list):
    return functools.reduce(Utilities.Sum, x)

def Product(x: list):
    return functools.reduce(Utilities.Product, x)

knowns = dict()
def GenerateFactorizations(n):
    if(n == 1):
        return []
    if(n in knowns):
        return knowns[n]
    factors = [n]
    for i in range(n // 2 , 1, -1):
        if(n % i == 0):
            factors.append(i)
    factorizations = [[n]]
    for f in factors:
        for fa in GenerateFactorizations(n // f):
            factorizations.append([f] + fa)
    knowns[n] = factorizations
    return factorizations

#for g in GenerateFactorizations(200):
#    print(g)

def GetKValues(n):
    #factors = factorizer.GetFactors(n)
    #if(len(factors) == 1):
    #    return []
    #for i in range(1, len(factors)):
    #    rolledFactors = factors[:i]
    #    rolledFactors.append(Product(factors[i:]))
    #    s = Sum(rolledFactors)
    #    if(s <= n):
    #        yield len(rolledFactors) + n - s
    #    else:
    #        break
    kvalues = set()
    for factors in GenerateFactorizations(n):
        if(len(factors) == 1): continue
        s = Sum(factors)
        if(s <= n):
            kvalues.add(len(factors) + n - s)
    return kvalues

def GetMinimalKSums(kMax):
    needed = set(i for i in range(2, kMax + 1))
    acc = 0
    for i in itertools.count(4):
        added = False
        if(len(needed) == 0):
            break
        for k in GetKValues(i):
            if(k in needed):
                needed.discard(k)
                if(not added):
                    acc += i
                    added = True
    return acc

assert GetMinimalKSums(6) == 30
assert GetMinimalKSums(12) == 61

with (Timer.Timer()):
    answer = GetMinimalKSums(12000)
    print(answer)
    assert answer == 7587457
