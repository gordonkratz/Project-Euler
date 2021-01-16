import itertools, Utilities, math

knownFactors = dict()
def GetPrimeFactors(n, sortedListOfPrimes):
    if(n in knownFactors):
        return knownFactors[n]
    if(n == 1):
        return set()
    for p in sortedListOfPrimes:
        if(n % p == 0):
            result = GetPrimeFactors(n // p, sortedListOfPrimes).union(set([p]))
            knownFactors[n] = result
            return result

def RisingFactorial(i, m):
    result = i
    for j in range(i+1, i+m):
        result *= j
    return result
        

def TryGetSequenceLessThan(n, mFactors):
    primes = list(Utilities.GeneratePrimesUpTo(n))
    primes.sort()
    iCandidate = 2
    consecutiveCount = 0

    for i in range(iCandidate, n):
        primeFactors = GetPrimeFactors(i, primes)
        if(len(primeFactors) == mFactors):
            consecutiveCount += 1
            if(consecutiveCount == mFactors):
                return iCandidate
            continue
       #reset
        consecutiveCount = 0
        iCandidate = i + 1
       

assert TryGetSequenceLessThan(100, 2) == 14
assert TryGetSequenceLessThan(1000, 3) == 644

answer = TryGetSequenceLessThan(1000000, 4)
print(answer)


