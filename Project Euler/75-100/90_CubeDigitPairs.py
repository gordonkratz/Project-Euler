import itertools, Utilities

def GenerateCubes():
    for i in range(1, 10):
        square = i**2
        a = square // 10
        b = square % 10
        a = a if a != 9 else 6
        b = b if b != 9 else 6
        yield (a, b)

cubes = list(GenerateCubes())

def GenerateDice():
    for die in itertools.combinations(range(10), 6):
        if(die[-1] == 9):
            yield (die[0], die[1], die[2], die[3], die[4], 6)
        else:
           yield die

def GenerateDicePairs():
    return itertools.combinations(GenerateDice(), 2)

def TestPair(diceA, diceB):
    for c in cubes:
        if(c[0] in diceA and c[1] in diceB):
            continue
        elif (c[0] in diceB and c[1] in diceA):
            continue
        else:
            return False
    return True

assert TestPair([0, 5, 6, 7, 8, 6], [1, 2, 3, 4, 8, 6])

def FindAnswer():
    count = 0
    for (diceA, diceB) in GenerateDicePairs():
        if(TestPair(diceA, diceB)):
            count += 1
    return count


answer = FindAnswer()
print(answer)
assert answer == 1217
