
def HighestTotientQuotientOverRange(nMax):
    phi = list(i for i in range(0, nMax+1))
    for i in range(2, len(phi)):
        if(phi[i] == i):
            for j in range(i, nMax+1, i):
                phi[j] -= phi[j] / i
    maxN = 0
    quotientMax = 0
    for i in range(1, len(phi)):
        if(i / phi[i] > quotientMax):
            quotientMax = i / phi[i]
            maxN = i
    return maxN

assert HighestTotientQuotientOverRange(10) == 6

answer = HighestTotientQuotientOverRange(1000000)
print(answer)
assert answer == 510510


