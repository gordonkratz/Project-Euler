import Utilities

def GetDigits(n):
    while (n > 0):
        yield n % 10
        n = n // 10

def AllArePrime(numbers, primeSet):
    for num in numbers:
        if(num not in primeSet):
            return False
    return True

def GetRotations(n):
    length = len(str(n))
    exp = 10**(length-1)
    for i in range(length):
        toAdd = n // exp
        n = n % exp * 10 + toAdd
        yield n

primes = set(Utilities.GeneratePrimesUpTo(1000000))
circularPrimes = set()

assert AllArePrime(list(GetRotations(197)), primes)
assert AllArePrime(list(GetRotations(2)), primes)



for p in primes:
    if(p in circularPrimes):
        continue
    permutations = list(GetRotations(p))
    if(AllArePrime(permutations, primes)):
        for num in permutations:
            circularPrimes.add(num)

answer = len(circularPrimes)
print(answer)
assert answer == 55
