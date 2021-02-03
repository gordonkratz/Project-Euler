import Utilities, itertools, math, functools

def PentagonalSequence(k: int):
    i = 1
    r = Utilities.Pentagonal(i)
    while(r <= k):
        yield k - r
        i *= -1
        if(i > 0):
            i += 1
        r = Utilities.Pentagonal(i)

def FindAnswer():
    values = [1]
    for k in itertools.count(1):
        sum = 0
        i = 0
        for p in PentagonalSequence(k):
            v = values[p]
            sign = 1 if i % 4 < 2 else -1
            sum += sign*v
            i += 1
        sum %= 1000000
        if(sum == 0):
            return k
        values.append(sum)


answer = FindAnswer()
print(answer)
assert answer == 55374