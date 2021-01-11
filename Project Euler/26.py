import functools

def findCycle(div):
    num = 1
    results = dict()
    index = 0
    while(True):
        result = num // div
        remainder = num % div
        if(num in results):
            return index - results[num][1]
        else:
            results[num] = (remainder, index)
            index += 1
            num = remainder * 10

assert findCycle(6) == 1
assert findCycle(7) == 6
assert findCycle(11) == 2

largestCycle = 0
indexOf = 0
for i in range(1, 1000):
    cycle = findCycle(i)
    if(cycle > largestCycle):
        indexOf = i
        largestCycle = cycle


print(indexOf)
assert indexOf == 983
