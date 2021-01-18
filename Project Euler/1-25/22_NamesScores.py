import functools, itertools, Utilities

input = open("names.txt", "r")
names = []

for name in Utilities.FileSplit(input):
    names.append(name.replace("\"", ""))



sum = functools.reduce(lambda acc, name: acc + Utilities.NumericScore(name[0]) * name[1],
                zip(sorted(names), itertools.count(1, 1)), 0)

print(sum)

assert sum == 871198282

