import functools, Utilities, itertools

def IsRelevant(n, m):
    return n == functools.reduce(Utilities.Sum, [int(i)**m for i in str(n)])

assert IsRelevant(1634, 4)
assert IsRelevant(8208, 4)
assert IsRelevant(9474, 4)
assert IsRelevant(92727, 5)

def FindMax(power):
    for i in itertools.count(1):
        if(int("9"*i) > 9**power*i):
            return 9**power*i

def FindPowerSums(power):
    max = FindMax(power)
    l = list(filter(lambda x: IsRelevant(x, power), range(2, max)))
    return functools.reduce(Utilities.Sum, filter(lambda x: IsRelevant(x, power), range(2, FindMax(power))))

assert FindPowerSums(4) == 19316

answer = FindPowerSums(5)
print(answer)
assert answer == 443839