import math, Utilities, Timer

def TriangleArea(repeatedSides, oddball):
    h = math.sqrt(repeatedSides**2 - (oddball**2/4))
    return (h*oddball, repeatedSides*2+oddball)

def GenerateHalfTriangles(perimeterMax):
    cMax = (perimeterMax // 3) + 1
    fareyMax = math.ceil(math.sqrt(cMax // 2))
    for (n, m) in Utilities.FareySequence(fareyMax):
        if(n%2 ==1 and m %2 == 1): 
            continue
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2
        if(c > cMax):
            continue
        if a > b:
            temp = a
            a = b
            b = temp
        if not (c == 2*a+1 or c == 2*a-1):
            continue
        yield (a, b, c)

def FindAnswer(pMax):
    perimSum = 0
    for (a, b, c) in GenerateHalfTriangles(pMax):
        print(c, c, 2*a)
        perimSum += c + c + 2*a
    return perimSum


def BruteForce(pMax):
    perimSum = 0
    for i in range(3, (pMax // 3) + 2, 2):
        if(math.sqrt(i**2 - (i-1)**2 /4).is_integer()):
            print(i, i, i-1)
            perimSum += 3*i-1
        upper = TriangleArea(i, i+1)
        if(math.sqrt(i**2 - (i+1)**2 /4).is_integer()):
            perimSum += 3*i+1
            print(i, i, i+1)
    return perimSum

with Timer.Timer():
    answer = BruteForce(1000000000)
    print(answer)
    assert answer == 518408346