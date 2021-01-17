import Utilities

def GetLongestConsecutivePrimeSum(max):
    primes = list(sorted(Utilities.GeneratePrimesUpTo(max)))
    primeSet = set(primes)
    maxChain = 0
    maxSum = 0
    for i in range(len(primes) - 1):
        runningSum = primes[i]
        for j in range(i + 1, len(primes) - i):
            runningSum += primes[j]
            if(runningSum > max):
                break
            if(runningSum in primeSet and j - i > maxChain):
                maxChain = j - i
                maxSum = runningSum
    return maxSum

assert GetLongestConsecutivePrimeSum(100) == 41
assert GetLongestConsecutivePrimeSum(1000) == 953

answer = GetLongestConsecutivePrimeSum(1000000)
print(answer)
assert answer == 997651