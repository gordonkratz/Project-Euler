
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import functools, Utilities
from Utilities import GreatestCommonFactor



def LeastCommonMultipleInRange(n):
    return functools.reduce(Utilities.LeastCommonMultiple, range(1, n))

print(LeastCommonMultipleInRange(20))

assert(LeastCommonMultipleInRange(10) == 2520)
assert(LeastCommonMultipleInRange(20) == 232792560)