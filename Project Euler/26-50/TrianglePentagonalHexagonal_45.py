import itertools, Utilities

def FindNextTriagularPentagonalHexagonal(hexagonalIndexLowerBound):
    for i in itertools.count(hexagonalIndexLowerBound):
        h = Utilities.Hexagonal(i)
        if(Utilities.IsPentagonal(h) and Utilities.IsTriangular(h)):
            return h

answer = FindNextTriagularPentagonalHexagonal(144)
print(answer)
assert answer == 1533776805