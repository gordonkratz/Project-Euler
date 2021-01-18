import Utilities, itertools

def TryFindAnswer():
    primeFinder = Utilities.PrimeFinder(900000000)
    cornerCount = 1
    primeCount = 0
    for i in itertools.count(3, 2):
        cornerCount += 4
        if(primeFinder.IsPrime(i**2-3*i+3)):
            primeCount += 1
        if(primeFinder.IsPrime(i**2-2*i+2)):
            primeCount += 1
        if(primeFinder.IsPrime(i**2-i+1)):
            primeCount += 1
        if(primeCount / cornerCount < .1):
            return i

answer = TryFindAnswer()
print(answer)
assert answer == 26241
