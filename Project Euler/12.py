import math

def GetNumberOfDivisors(n):
    upperBound = int(math.sqrt(n))
    count = 0
    for i in range(1, upperBound):
        if(n % i == 0): count += 1
    count *= 2
    if(upperBound**2 == n): count += 1
    return count
    
def NthTriangle(n):
    return n*(n+1) // 2

def TriangleNumberWithMinimumFactors(n):
    i = 1
    while True:
        triangle = NthTriangle(i)
        factors = GetNumberOfDivisors(triangle)
        if(factors >= n): return triangle
        i += 1

assert TriangleNumberWithMinimumFactors(5) == 28
assert TriangleNumberWithMinimumFactors(500) == 76576500

print(TriangleNumberWithMinimumFactors(500))