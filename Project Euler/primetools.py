

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
    for i in range(1, upperBound + 1):
        if(n % i == 0): count += 1
    count *= 2
    if(upperBound**2 == n): count -= 1
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

def GetPrimesFromFile(nMax):
    primes = []
    with open("primes.txt", "r") as fp:
        while True: 
            line = fp.readline() 
            if not line: 
                break
            value = int(line)
            if(value > nMax):
                break
            primes.append(value)
    return primes
        
class PrimeFactorizer:
    primes = list()
    knownFactors = dict()

    def __init__(self, seed: int):
        self.primes = sorted(GeneratePrimesUpTo(seed))

    def GetFactors(self, n: int) -> list:
        if(n == 1): return []
        if(n in self.knownFactors):
            return self.knownFactors[n]
        if(self.primes[-1] < n // 2):
            self.primes = sorted(GeneratePrimesUpTo(n))
        result = []
        next = n
        for p in self.primes:
            if(next == 1):
                break
            while(next % p == 0):
                next = next // p
                result.append(p)
                if(next in self.knownFactors):
                    result.extend(self.knownFactors[next])
                    next = 1
                    break
        self.knownFactors[n] = result
        return result
