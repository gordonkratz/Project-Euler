import functools
largest = 0
for a in range(100):
    for b in range(100):
        largest = max(functools.reduce(lambda acc, x: acc + int(x), str(a**b), 0), largest)

print(largest)
assert largest == 972
