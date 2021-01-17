import math, functools, Utilities

answer = functools.reduce(lambda acc, x: acc + x**x, range(1, 1000), 0) % 10**10
print(answer)
assert answer == 9110846700