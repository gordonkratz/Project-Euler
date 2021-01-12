import math

def GeneratePrimesUpTo(n):
    primes = list()
    # In general Sieve of Sundaram,  
    # produces primes smaller 
    # than (2*x + 2) for a number  
    # given number x. Since we want 
    # primes smaller than n, we  
    # reduce n to half 
    nNew = int((n - 1) / 2); 
  
    # This array is used to separate  
    # numbers of the form i+j+2ij 
    # from others where 1 <= i <= j 
    # Initialize all elements as not marked 
    marked = [0] * (nNew + 1); 
  
    # Main logic of Sundaram. Mark all  
    # numbers of the form i + j + 2ij  
    # as true where 1 <= i <= j 
    for i in range(1, nNew + 1): 
        j = i; 
        while((i + j + 2 * i * j) <= nNew): 
            marked[i + j + 2 * i * j] = 1; 
            j += 1; 
  
    # Since 2 is a prime number 
    if (n > 2): 
        primes.append(2) 
  
    # Print other primes. Remaining  
    # primes are of the form 2*i + 1  
    # such that marked[i] is false. 
    for i in range(1, nNew + 1): 
        if (marked[i] == 0): 
            primes.append(2 * i + 1)
    return primes

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
