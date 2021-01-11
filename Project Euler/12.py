import math
from Utilities import *

    
def NthTriangle(n):
    return n*(n+1) // 2

def TriangleNumberWithMinimumFactors(n):
    i = 1
    while True:
        triangle = NthTriangle(i)
        factors = GetNumberOfDivisors(triangle)
        if(factors >= n): return triangle
        i += 1


print(TriangleNumberWithMinimumFactors(500))

assert TriangleNumberWithMinimumFactors(5) == 28
assert TriangleNumberWithMinimumFactors(500) == 76576500
