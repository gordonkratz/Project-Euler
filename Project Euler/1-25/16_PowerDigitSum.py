import functools

print(functools.reduce(lambda acc, x: acc + int(x), str(2**1000), 0))
