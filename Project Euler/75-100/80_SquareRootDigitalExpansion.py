import math

def SumSquareRootDigits(n):
    result = math.floor(math.sqrt(n))
    remain = n - result**2
    sum = result
    for count in range(1, 100):
        remain *= 100
        d = 9
        for i in range(1, 10):
            if(20*result + i)*i > remain:
                d = i - 1
                break
        remain -= d*(20*result+d)
        result *= 10
        result += d
        sum += d
        count += 1
    return sum

assert SumSquareRootDigits(2) == 475


answer = 0
for i in range(2, 100):
    if(math.sqrt(i).is_integer()): 
        continue
    answer += SumSquareRootDigits(i)

print(answer)
assert answer == 40886