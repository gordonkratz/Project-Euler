import math

count = 0
for n in range(2, 101):
    for r in range(n-1, 1, -1):
        if(math.factorial(n)//(math.factorial(r)*math.factorial(n-r)) >= 1000000):
            count += 1

print(count)
assert count == 4075