import Utilities

def HighestTotientQuotientOverRange(nMax):
    phi = Utilities.GenerateTotientValues(nMax)
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


