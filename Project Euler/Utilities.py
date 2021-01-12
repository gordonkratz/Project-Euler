import math

def GeneratePrimesUpTo(n):
    if n == 2: return [2]
    if n == 3: return [2,3]
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n//3)
    for i in range(1,int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k//3      ::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
        sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((n//6-k*(k-2*(i&1)+4)//6-1)//k+1)
    return [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]

def GetNumberOfDivisors(n):
    upperBound = int(math.sqrt(n))
    count = 0
    for i in range(1, upperBound):
        if(n % i == 0): count += 1
    count *= 2
    if(upperBound**2 == n): count += 1
    return count

def IsPrime(n):
    return GetNumberOfDivisors(n) == 2

class PrimeFinder:
    def __init__(self, n):
        self.knownPrimes = set(GeneratePrimesUpTo(n))


    def IsPrime(self, n):
        if(n <= 1): return False
        if(n in self.knownPrimes): return True
        elif(IsPrime(n)):
            self.knownPrimes.add(n)
            return True
        return False

def Sum(a, b): return a + b


def GreatestCommonFactor(x, y):
    if(y > x):
        return GreatestCommonFactor(y, x)

    while y != 0:
        (x, y) = (y, x % y)
    return x

def ListOfPermutations(allowedDigits):
    if(len(allowedDigits) == 1):
        yield(allowedDigits[0])
        return
    for digit in allowedDigits:
        for subResult in ListOfPermutations(list(filter(lambda x: x != digit, allowedDigits))):
            yield(digit*10**(len(allowedDigits)-1) + subResult)


def IsPalindrome(n):
    stringN = str(n)
    return stringN == stringN[::-1]
