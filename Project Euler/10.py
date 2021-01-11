"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import functools
from Utilities import *

def SumOfPrimesBelow(n):
    return functools.reduce(lambda acc, x: acc + x, GeneratePrimesUpTo(n))


assert(SumOfPrimesBelow(10) == 17)
assert(SumOfPrimesBelow(2000000) == 142913828922)

print(SumOfPrimesBelow(2000000))