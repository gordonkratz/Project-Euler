import itertools, math

def GenerateCoordinates(nMax):
    return itertools.combinations(itertools.product(range(nMax+1), repeat=2), 2)

def GetHypoteneuse(x, y):
    return x**2 + y**2

def CheckForRightTriangle(a, b):
    one = GetHypoteneuse(b[0], b[1])
    three = GetHypoteneuse(a[0], a[1])
    two = GetHypoteneuse(abs(a[0]-b[0]), abs(a[1]-b[1]))
    if(one > three and one > two):
        return two + three == one
    elif(two > three and two > one):
        return one + three == two
    else:
        return one + two == three

def FindAnswer(nMax):
    count = 0
    for a, b in GenerateCoordinates(nMax):
        if(a == (0,0) or b == (0,0)):
            continue
        if(CheckForRightTriangle(a, b)):
            count += 1
    return count

assert(FindAnswer(2) == 14)

answer = FindAnswer(50)
print(answer)
assert answer == 14234