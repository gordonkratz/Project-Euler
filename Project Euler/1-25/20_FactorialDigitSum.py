import math, functools

sum = functools.reduce(lambda acc, x: acc + int(x), str(math.factorial(100)), 0)

print (sum)