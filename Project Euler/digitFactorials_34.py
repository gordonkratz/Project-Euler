import math, functools, Utilities, itertools

def LowerBoundForNDigits(n):
    for i in range(10):
        if math.factorial(i)*n > 10**(n-1):
            return 10**(n-1) + i

def UpperBoundForNDigits(n):
    for i in range(10):
        if math.factorial(i) >= 10**n:
            return 10**(n-1) * i
    return 0

def IsSumOfFactorialOfDigits(n):
    return functools.reduce(lambda acc, x: acc + math.factorial(int(x)), str(n), 0) == n

upperBound = 0
for i in itertools.count(1):
    if(UpperBoundForNDigits(i) == 0):
        upperBound = UpperBoundForNDigits(i-1)
        break

answer = functools.reduce(Utilities.Sum, filter(IsSumOfFactorialOfDigits, range(3, upperBound)))

print(answer)
assert answer == 40730