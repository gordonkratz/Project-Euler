import Utilities

def MinimizedQuotientOfPermutedTotient(nMax):
    phi = Utilities.GenerateTotientValues(nMax)
    minN = 0
    quotientMin = nMax
    for i in range(2, len(phi)):
        if(i/phi[i] < quotientMin):
            input = sorted(str(i))
            output = sorted(str(phi[i]))
            if(input == output):
                quotientMin = i/phi[i]
                minN = i
    return minN

answer = MinimizedQuotientOfPermutedTotient(10**7)
print(answer)
assert answer == 8319823