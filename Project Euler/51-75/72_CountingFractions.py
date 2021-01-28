import functools, Utilities

def GenerateTotients(nMax):
    phi = list(i for i in range(0, nMax+1))
    phi[0] = 0
    phi[1] = 0
    for i in range(2, len(phi)):
        if(phi[i] == i):
            for j in range(i, nMax+1, i):
                phi[j] -= phi[j] / i
    return phi

def GetNumberOfFractionsLessThan(n):
    return functools.reduce(Utilities.Sum, GenerateTotients(n))

assert GetNumberOfFractionsLessThan(8) == 21

answer = GetNumberOfFractionsLessThan(1000000)
print(answer)
assert answer == 303963552391
