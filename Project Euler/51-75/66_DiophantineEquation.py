import itertools, math
from fractions import Fraction

def GetSquareRootSeries(n):
    sqrt = math.sqrt(n)
    a = math.floor(sqrt)
    d = 1.0
    v = a
    yield a

    while(True):
        a = math.floor(d / (sqrt - v))
        d = (n - v**2) / d
        v = d*a - v 
        yield a

def GetConvergentPairs(d):
    series = list()
    for i in GetSquareRootSeries(d):
        series.append(i)
        fractionalTerm = 0
        for item in reversed(series[1:]):
            fractionalTerm = Fraction(1, item + fractionalTerm)
        fractionalTerm += series[0]
        yield fractionalTerm

def FindMinimalx(d):
    for fraction in GetConvergentPairs(d):
        if(fraction.numerator**2 - d*fraction.denominator**2 == 1):
            return fraction.numerator


assert FindMinimalx(2) == 3
assert FindMinimalx(3) == 2
assert FindMinimalx(5) == 9
assert FindMinimalx(6) == 5
assert FindMinimalx(7) == 8

def FindMinimalXInRange(dMax):
    maxX = 0
    result = 0
    for d in filter(lambda x: not math.sqrt(x).is_integer(), range(1, dMax+1)):
        x = FindMinimalx(d)
        if(x > maxX):
            maxX = x
            result = d
    return result


assert FindMinimalXInRange(7) == 5

answer = FindMinimalXInRange(1000)
print(answer)
assert answer == 661
