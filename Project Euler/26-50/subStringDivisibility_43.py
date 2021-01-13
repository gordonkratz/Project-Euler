import functools, Utilities

def RelevantThree(n):
    firstDigit = n % 10
    secondDigit = n // 10 % 10
    thirdDigit = n // 100 % 100
    return (secondDigit % 2 == 0
        and firstDigit != secondDigit
        and secondDigit != thirdDigit
        and thirdDigit != firstDigit) 
multiplesOfThree = list(map(lambda x: str(x).zfill(3), 
                            filter(RelevantThree, [3*i for i in range (1000//3)])))

def IsRelevant(n):
    return (n // 1000000 % 2 == 0
        and n // 100000 % 1000 % 3 == 0
        and n // 10000 % 5 == 0
        and n // 1000 % 1000 % 7 == 0
        and n // 100 % 1000 % 11 == 0
        and n // 10 % 1000 % 13 == 0
        and n % 1000 % 17 == 0)

assert IsRelevant(1406357289)

def AppendToMakeMultiple(base, multipleOf):
    for digit in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        if (digit in base
            or int(base[-2:] + digit) % multipleOf != 0):
            continue
        yield base + digit
        

def GetPermutations():
    for base in multiplesOfThree:
        for p in AppendToMakeMultiple(base, 5):
            for p2 in AppendToMakeMultiple(p, 7):
                for p3 in AppendToMakeMultiple(p2, 11):
                    for p4 in AppendToMakeMultiple(p3, 13):
                        for p5 in AppendToMakeMultiple(p4, 17):
                            for p6 in Prepend(p5, ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
                                for p7 in Prepend(p6, ['1', '2', '3', '4', '5', '6', '7', '8', '9']):
                                    if(len(p7)) == 10:
                                        yield int(p7)
                

def Prepend(base, listOfAdditions):
    for item in listOfAdditions:
        if(item not in base):
            yield item + base 


answer = functools.reduce(Utilities.Sum, GetPermutations())
print(answer)
assert answer == 16695334890