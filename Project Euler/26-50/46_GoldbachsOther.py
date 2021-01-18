import Utilities, math

def TryGetNonGolbachNumberBelow(upperLimit):
    primeFinder = Utilities.PrimeFinder(upperLimit)
    for n in range(33, upperLimit, 2):
        if(primeFinder.IsPrime(n)): continue
        if(not IsConjectureCompliant(n, primeFinder)):
            return n


def IsConjectureCompliant(n, primeFinder):
    for s in range(1, int(math.sqrt(n//2) // 1) + 1):
        p = n - 2*s**2
        if(primeFinder.IsPrime(p)):
            return True
    return False

answer = TryGetNonGolbachNumberBelow(1000000)
print(answer)