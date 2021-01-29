import math

def GetNextNumber(n):
    result = 0
    digit = 0
    while(n != 0):
        digit = n % 10
        n = n // 10
        result += math.factorial(digit)
    return result

assert GetNextNumber(145) == 145
assert GetNextNumber(363600) == 1454

def GetChainLengthAugment(n):
    if(n == 169 or n == 363601 or n == 1454):
        return 3
    if(n == 871 or n == 45361 or n == 872 or n == 45362):
        return 2
    if(n == 145):
        return 1
    return 0

def FindChains(nMax):
    knowns = {1: 0, 2: 0, 169: 2, 363601: 2, 1454: 2, 871: 1, 45361: 1, 872: 1, 45362: 1, 145: 0}
    count = 0
    for i in range(1, nMax+1):
        if(i in knowns): continue

        chain = [i]
        previous = i
        while(True):
            next = GetNextNumber(previous)
            chain.append(next)
            if(next == previous):
                knowns[next] = 0
            if(next in knowns):
                augment = knowns[next]
                for j in range(len(chain)):
                    length = len(chain) - j + augment - 1
                    knowns[chain[j]] = length
                    if(length == 59):
                        count += 1
                break
            previous = next
    return count

answer = FindChains(1000000)
print(answer)
assert answer == 402