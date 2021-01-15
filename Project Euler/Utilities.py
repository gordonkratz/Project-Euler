import math, functools

def GeneratePrimesUpTo(n):
    #if n == 2: return [2]
    #if n == 3: return [2,3]
    #""" Input n>=6, Returns a list of primes, 2 <= p < n """
    #n, correction = n-n%6+6, 2-(n%6>1)
    #sieve = [True] * (n//3)
    #for i in range(1,int(n**0.5)//3+1):
    #  if sieve[i]:
    #    k=3*i+1|1
    #    sieve[      k*k//3      ::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
    #    sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((n//6-k*(k-2*(i&1)+4)//6-1)//k+1)
    #return [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]
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

def Sum(a, b): return a + b


def GreatestCommonFactor(x, y):
    if(y > x):
        return GreatestCommonFactor(y, x)

    while y != 0:
        (x, y) = (y, x % y)
    return x

def ListOfPermutations(allowedDigits, disallowedDigitsInPosition=dict()):
    if(len(allowedDigits) == 1):
        if(0 in disallowedDigitsInPosition 
           and allowedDigits[0] in disallowedDigitsInPosition[0]):
            yield None
        else:
            yield(allowedDigits[0])
        return
    for digit in allowedDigits:
        if(digit in disallowedDigitsInPosition
           and len(allowedDigits) - 1 in disallowedDigitsInPosition[digit]):
            continue
        for subResult in ListOfPermutations(list(filter(lambda x: x != digit, allowedDigits))):
            yield(digit*10**(len(allowedDigits)-1) + subResult)


def IsPalindrome(n):
    stringN = str(n)
    return stringN == stringN[::-1]

def FileSplit(f, delim=',', bufsize=1024):
    prev = ''
    while True:
        s = f.read(bufsize)
        if not s:
            break
        split = s.split(delim)
        if len(split) > 1:
            yield prev + split[0]
            prev = split[-1]
            for x in split[1:-1]:
                yield x
        else:
            prev += s
    if prev:
        yield prev

def NumericScore(word):
    return functools.reduce(lambda acc, letter: acc + ord(letter) - 64, word, 0)

def Pentagonal(i):
    return (3*i**2 - i)/2

def IsPentagonal(p):
    x = (1 + 2*math.sqrt(.25 + 6*p))/6
    return x.is_integer() and x > 0

def Triangle(i):
    return (i**2 + i)/2

def IsTriangular(p):
    return (math.sqrt(.25+2*p)-.5).is_integer()

def Hexagonal(i):
    return 2*i**2 - i

def IsHexagonal(p):
    return (1 + math.sqrt(1+8*p)) % 4 == 0