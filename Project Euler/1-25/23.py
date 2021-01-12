import math

def IsAbundant(n):
    upperBound = int(math.sqrt(n))
    count = 0
    if(upperBound**2 == n): count -= upperBound
    for i in range(1, upperBound + 1):
        if(n % i == 0):
            count += i
            count += (n // i) if (i != 1) else 0
        if(count > n):
            return True
    return count > n

assert IsAbundant(12)
assert not IsAbundant(4)

upperlimit = 28123

abundantNumbers = list(filter(lambda x: IsAbundant(x), range(upperlimit)))
print(abundantNumbers)
assert 4 not in abundantNumbers
assert 12 in abundantNumbers

numbersThatCanBeSumOfAbundant = set()
sumOfAll = upperlimit * (upperlimit + 1) // 2

for i in range(len(abundantNumbers)):
    for j in range(i, len(abundantNumbers) - i):
        sum = abundantNumbers[i] + abundantNumbers[j]
        if(sum > upperlimit):
            break
        if(sum not in numbersThatCanBeSumOfAbundant):
            sumOfAll -= sum
            numbersThatCanBeSumOfAbundant.add(sum)

print(sumOfAll)

assert sumOfAll == 4179871