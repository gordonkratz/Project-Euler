import Utilities, functools

primes = set(Utilities.GeneratePrimesUpTo(1000000))

def Truncatable(p, listOfPrimes):
    iterations = len(str(p)) - 1
    if(iterations == 0): return False
    for i in range(iterations):
        leftTrunc = p // 10 ** (i+1)
        rightTrunc = p % 10 ** (iterations-i)
        if(leftTrunc not in primes or rightTrunc not in primes):
            return False
    return True

assert Truncatable(3797, primes)
assert not Truncatable(5, primes)
assert not Truncatable(29, primes)

sum = functools.reduce(Utilities.Sum, filter(lambda x: Truncatable(x, primes), primes))

print(sum)
assert sum == 748317