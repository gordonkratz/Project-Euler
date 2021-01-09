import math

def GetSumOfDivisors(n):
    upperBound = int(math.sqrt(n))
    count = 0-n
    for i in range(1, upperBound + 1):
        if(n % i == 0):
            count += i
            count += n // i
    if(upperBound**2 == n): count -= upperBound
    return count

assert(GetSumOfDivisors(2)) == 1
assert GetSumOfDivisors(220) == 284
assert GetSumOfDivisors(284) == 220

checked = set()
sum = 0

for i in range(10000):
    if i in checked: continue
    sumDiv = GetSumOfDivisors(i)
    other = GetSumOfDivisors(sumDiv)
    if(i == other and i != sumDiv and sumDiv < 10000):
        sum += i + sumDiv
    checked.add(i)
    checked.add(sumDiv)

print(sum)
    
