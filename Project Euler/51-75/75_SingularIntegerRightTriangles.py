import Utilities, math

def GenerateTriangles(perimeterMax):
    mMax = math.ceil(math.sqrt(perimeterMax))
    for (n, m) in Utilities.FareySequence(mMax):
        if(n%2 ==1 and m %2 == 1): 
            continue
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2
        if(a+b+c) > perimeterMax: 
            continue
        for k in range(1, (perimeterMax // (a+b+c)) + 1):
            yield (a*k, b*k, c*k)


def CountSingleTriangles(pMax):
    counts = [0 for i in range(pMax+1)]
    for (a, b, c) in GenerateTriangles(pMax):
        counts[a+b+c] += 1
    result = 0
    for c in counts:
        if c == 1:
            result += 1
    return result

assert CountSingleTriangles(48) == 6

answer = CountSingleTriangles(1500000)
print(answer)
assert answer == 161667