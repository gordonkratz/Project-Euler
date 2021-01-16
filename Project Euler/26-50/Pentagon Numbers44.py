import math, itertools, Utilities

assert Utilities.IsPentagonal(1)
assert Utilities.IsPentagonal(5)
assert Utilities.IsPentagonal(12)
assert Utilities.IsPentagonal(70)
assert Utilities.IsPentagonal(92)
assert not Utilities.IsPentagonal(2)
assert not Utilities.IsPentagonal(15)
assert not Utilities.IsPentagonal(100)

def TryFindPairLessThan(n):
    for k in range(n, 1, -1):
        pk = Utilities.Pentagonal(k)
        print(k)
        for j in range(k, 1, -1):
            pj = Utilities.Pentagonal(j)
            if(Utilities.IsPentagonal(pk-pj) and Utilities.IsPentagonal(pk+pj)):
                return pk-pj

answer = TryFindPairLessThan(2200)
print(answer)
assert answer == 5482660

        