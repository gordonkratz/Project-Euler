import math, itertools

count = 0
for i in itertools.count(1):
    min = math.ceil(round(math.pow(10**(i-1), 1.0/i), 10))
    if(min >= 10):
        break
    count += 10 - min

print(count)
assert count == 49