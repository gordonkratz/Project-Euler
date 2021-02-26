import math

file = open("p099_base_exp.txt", "r")
numbers = []
for line in file:
    line = line.strip().split(",")
    numbers.append((int(line[0]), int(line[1])))


def FindAnswer(iter: list):
    temp = max(map(lambda x: (math.log2(x[0]) * x[1], x), iter), key=lambda x: x[0])
    return iter.index(temp[1]) + 1

assert(FindAnswer([(632382,518061), (519432,525806)]) == 1)
assert(FindAnswer([(2,11), (3,7)]) == 2)

answer = FindAnswer(numbers)
print(answer)
assert answer == 709
