

def FindCollatzLength(n, dict):
    if(n == 1): return 1
    if n in dict:
        return dict[n]
    n = n/2 if n % 2 == 0 else 3*n + 1 
    return 1 + FindCollatzLength(n, dict)

def FindLongestCollatzLengthUpTo(n):
    longestChain = 0
    number = 0
    knownCollatzLengths = {}
    for i in range(1, n):
        chainLength = FindCollatzLength(i, knownCollatzLengths)
        if(chainLength > longestChain):
            longestChain = chainLength
            number = i
        knownCollatzLengths[i] = chainLength
    return number

print(FindLongestCollatzLengthUpTo(1000000))

assert FindLongestCollatzLengthUpTo(1000000) == 837799
