import math, itertools

assert IsPentagonNumber(1)
assert IsPentagonNumber(5)
assert IsPentagonNumber(12)
assert IsPentagonNumber(70)
assert IsPentagonNumber(92)
assert not IsPentagonNumber(2)
assert not IsPentagonNumber(15)
assert not IsPentagonNumber(100)

def IsPentagonalPair(j, k):
    return (IsPentagonNumber(j)
            and IsPentagonNumber(k)
            and IsPentagonNumber(j + k)
            and IsPentagonNumber(k - j))

def GetA(j, n):
    squareRoot = math.sqrt(1 + (72*j*n) + (36*n**2) - 36*n)
    return (1+squareRoot) / 6

def GetB(j, n):
    squareRoot = math.sqrt(1 + (72*j**2) - (24*j) + (72*j*n) + (36*n**2) - (12*n))
    return (1+squareRoot) / 6

def FindSmallestPentagonalPair(index):
    pj = Pentagonal(index)
    pTrailing = pj
    for i in itertools.count(index+1):
        pk = Pentagonal(i)
        if(IsPentagonalPair(pj, pk)):
            return (pj, pk)
        if(pk - pTrailing > pj):
            return None
        pTrailing = pk

FindSmallestPentagonalPair(4)

#trailing = 1
#print("j = 5")
#for i in range(1, 9000):
#    a = GetA(5, i)
#    b = GetB(5, i)
#    print("n =", i, "a =", a, "k =", 5+i, "b =", b)
#    if(a.is_integer() and b.is_integer()): break

def TryGetSystem(r):
    for j in range(r):
        for n in itertools.count(1):
            a = GetA(j, n)
            b = GetB(j, n)
            k = j+n
            print("j =", j, "a =", a, "k =", k, "b =", b)
            if(k - a < 1): break
            if(b - k < 1): break
            if(a.is_integer() and b.is_integer()): return (j, a, k, b)

print(TryGetSystem(10000000000))

#for i in itertools.count():
#    result = FindSmallestPentagonalPair(i)
#    print(i, Pentagonal(i), result)
#    if(result is not None): break

#j = 5
#for n in itertools.count(1):
#    a = GetA(j, n)
#    b = GetB(j, n)
#    k = j+n
#    print("j =", j, "a =", a, "k =", k, "b =", b)
#    #if(k - a < 1): break
#    #if(b - k < 1): break
#    if(a.is_integer() or b.is_integer()): 
#        print("FOUND ONE:", Pentagonal(j), Pentagonal(a), Pentagonal(k), Pentagonal(b))
#        break