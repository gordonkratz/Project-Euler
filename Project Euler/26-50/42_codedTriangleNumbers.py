import Utilities, itertools

triangleNumbers = set()
for i in itertools.count(1):
    t = 0.5*i*(i+1)
    triangleNumbers.add(t)
    if(t > 364): break

input = open("p042_words.txt", "r")
names = list(filter(lambda i: i in triangleNumbers, 
    map(lambda name: Utilities.NumericScore(name.replace("\"", "")),
                Utilities.FileSplit(input))))

print(len(names))