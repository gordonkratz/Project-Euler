import functools, Utilities, itertools

def AssignRating(hand):
    isFlush = True
    isStraight = True
    groups = dict()
    trailing = None

    keyFunc = lambda c: c[0]
    shand = sorted(hand, key=keyFunc)
    for card in shand:
        if(card[0] not in groups):
            groups[card[0]] = 1
        else :
            groups[card[0]] += 1

        if(trailing == None):
            trailing = card
            continue

        if(card[1] != trailing[1]):
            isFlush = False
        if(card[0] != trailing[0] + 1):
            isStraight = False
        trailing = card
    
    sets = list(sorted(map(lambda g: (g[0], g[1]), 
                           groups.items()), key=lambda g: g[1], reverse=True))

    values = list(map(lambda c: c[0], hand))

    if(isStraight and isFlush):
        return (8, max(values), 1)
    if(isFlush):
        return (5, max(values), 1)
    if(isStraight):
        return (4, max(values), 1)

    nSets = len(sets)
    if(nSets == 2):
        return (6, sets[0][0], sets[1][0])
    if(nSets == 3):
        if(sets[0][1] == 3):
            return (3, sets[0][0], 1)
        else:
            return (2, sets[0][0], sets[1][0])
    if(nSets == 4):
       return (1, sets[0][0], 1)
    return (0, 1, 1)

def ConvertValue(digit):
    if(digit.isdigit()):
        return int(digit)
    if(digit == 'A'):
        return 14
    if(digit == 'K'):
        return 13
    if(digit == 'Q'):
        return 12
    if(digit == 'J'):
        return 11
    if(digit == 'T'):
        return 10

def ReadLine(input):
    split = list(map(lambda c: (ConvertValue(c[0]), c[1]), input.split()))
    hand1 = split[:5]
    hand2 = split[5:]
    return (hand1, hand2)

def AnalyzeLine(input):
    (hand1, hand2) = ReadLine(input)
    result1 = AssignRating(hand1)
    result2 = AssignRating(hand2)
    comparison = Utilities.SequentialCompare(result1, result2)
    if(comparison == 0):
        sHand1 = sorted(hand1, key=lambda c: c[0], reverse=True)
        sHand2 = sorted(hand2, key=lambda c: c[0], reverse=True)
        comparison = Utilities.SequentialCompare(sHand1, sHand2)
    return comparison

def TestCase(input, expectedWinner):
    comparison = AnalyzeLine(input)
    return comparison == -1 if expectedWinner == 1 else 1

assert TestCase("5H 5C 6S 7S KD 2C 3S 8S 8D TD", 2)
assert TestCase("5D 8C 9S JS AC 2C 5C 7D 8S QH", 1)
assert TestCase("2D 9C AS AH AC	3D 6D 7D TD QD", 2)
assert TestCase("4D 6S 9H QH QC	3D 6D 7H QD QS", 1)
assert TestCase("2H 2D 4C 4D 4S 3C 3D 3S 9S 9D", 1)
assert TestCase("5S AD 9C 8C 7C 8D 5H 9D 8S 2S", 2)
assert TestCase("AD 6C 6S 7D TH 6H 2H 8H KH 4H", 2)
assert TestCase("AH QC JC 4C TC 8C 2H TS 2C 7D", 2)
assert TestCase("9D 8D 4C JH 2C 2S QD KD TS 4H", 2)
assert TestCase("5C AD 5D AC 9C 7C 5H 8D TD KS", 1)

input = open("p054_poker.txt", "r")
iWinCount = 0
for line in input.readlines():
    if(AnalyzeLine(line) == -1):
        iWinCount += 1

print(iWinCount)
assert iWinCount == 376
