from Utilities import *

def Quadratic(a, b, n):
    return n**2 + a*n + b

primeFinder = PrimeFinder(10**6)
currentLongestChain = 0
answer = 0
for b in range(-1000, 1000):
    for a in range(-999, 1000):
        currentN = 0
        while(primeFinder.IsPrime(Quadratic(a, b, currentN))):
            currentN += 1
        if(currentN > currentLongestChain):
            currentLongestChain = currentN
            answer = a * b

print(answer)

assert answer == -59231