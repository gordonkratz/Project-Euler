
def MinimizedQuotientOfPermutedTotient(nMax):
    phi = list(i for i in range(0, nMax+1))
    minN = 0
    quotientMin = nMax
    for i in range(2, len(phi)):
        if(phi[i] == i):
            for j in range(i, nMax+1, i):
                phi[j] -= phi[j] // i
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