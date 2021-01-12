import itertools

def NthDigit(n):
    for i in itertools.count(1):
        string = str(i)
        length = len(string)
        if(n <= length):
            return int(string[n-1])
        n -= length

assert(NthDigit(12) == 1)
assert(NthDigit(1) == 1)

prod = 1
for i in range(6):
    prod *= NthDigit(10**i)

print(prod)