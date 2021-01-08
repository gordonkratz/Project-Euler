
import functools as f

def SumOfSquares(n):
    return f.reduce(lambda x, y: x + y**2, range(1, n + 1))

def SquareOfSum(n):
    return (n * (n + 1) / 2) ** 2

def Difference(n):
    return SquareOfSum(n) - SumOfSquares(n)

print(Difference(100))

assert Difference(10) == 2640
assert Difference(100) == 25164150