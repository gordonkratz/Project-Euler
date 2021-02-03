import primetools, Utilities

def FindSumsOfPrimes(n):
    return Utilities.FindSums(n, primetools.GeneratePrimesUpTo(n))

assert FindSumsOfPrimes(10) == 5

def HuntAnswer(targetSumCount):
    upper = targetSumCount
    lower = 1

    while(FindSumsOfPrimes(upper) < targetSumCount):
        upper *= upper

    while(lower + 1 != upper):
        mid = (upper + lower) // 2
        midSum = FindSumsOfPrimes(mid)
        if(midSum >= targetSumCount):
            upper = mid
        else:
            lower = mid
    return upper

assert HuntAnswer(5) == 10

answer = HuntAnswer(5000)
print(answer)
assert answer == 71



