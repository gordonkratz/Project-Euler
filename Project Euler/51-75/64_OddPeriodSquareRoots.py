import math

def GetSqrtPeriodLength(n):
    sqrt = math.sqrt(n)
    if(sqrt.is_integer()):
        return 0

    a = math.floor(sqrt)
    d = 1.0
    v = a
    aValues = [(a,d,v)]

    while(True):
        a = math.floor(d / (sqrt - v))
        d = (n - v**2) / d
        v = d*a - v 
        if (a,d,v) in aValues:
            return len(aValues) - aValues.index((a,d,v))
        aValues.append((a,d,v))

assert GetSqrtPeriodLength(2) == 1
assert GetSqrtPeriodLength(5) == 1
assert GetSqrtPeriodLength(6) == 2
assert GetSqrtPeriodLength(7) == 4
assert GetSqrtPeriodLength(8) == 2
assert GetSqrtPeriodLength(10) == 1
assert GetSqrtPeriodLength(11) == 2
assert GetSqrtPeriodLength(12) == 2
assert GetSqrtPeriodLength(13) == 5
assert GetSqrtPeriodLength(3) == 2

def GetNumberWithOddPeriod(nMax):
    count = 0
    for i in range(1, nMax):
        period = GetSqrtPeriodLength(i)
        if(period % 2 != 0):
            count += 1
    return count

assert GetNumberWithOddPeriod(14) == 4

answer = GetNumberWithOddPeriod(10001)
print(answer)
assert answer == 1322