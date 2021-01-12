import functools, itertools

def FileSplit(f, delim=',', bufsize=1024):
    prev = ''
    while True:
        s = f.read(bufsize)
        if not s:
            break
        split = s.split(delim)
        if len(split) > 1:
            yield prev + split[0]
            prev = split[-1]
            for x in split[1:-1]:
                yield x
        else:
            prev += s
    if prev:
        yield prev


input = open("names.txt", "r")


names = []

for name in FileSplit(input):
    names.append(name.replace("\"", ""))

def NumericScore(name):
    return functools.reduce(lambda acc, letter: acc + ord(letter) - 64,
                           name, 0)

sum = functools.reduce(lambda acc, name: acc + NumericScore(name[0]) * name[1],
                zip(sorted(names), itertools.count(1, 1)), 0)

print(sum)

assert sum == 871198282

