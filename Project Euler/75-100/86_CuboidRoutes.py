import math, Utilities, itertools

def GenerateAllCubes(nMax):
    fareymax = 2*nMax + 1
    for (n, m) in Utilities.FareySequence(fareymax):
        if(n%2 ==1 and m %2 == 1): 
            continue
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2
        if a > b:
            temp = a
            a = b
            b = temp
        ak = a
        bk = b
        ck = c
        while ak <= nMax and bk <= 2*nMax:
            yield (ak, bk, ck)
            ak += a
            bk += b
            ck += c

#for cube in GenerateAllCubes(10):
#    print(cube)

def Validate(x, y, z, expectedShortLength):
    route = min((y+z)**2 + x**2, (x+z)**2+y**2, (x+y)**2 + z**2)
    return route == expectedShortLength**2

def GenerateCubesWithIntegerPath(nMax):
    for (a, b, c) in GenerateAllCubes(nMax):
        for i in range(1, b // 2 + 1 ):
            if(Validate(a, i, b-i, c)):
                yield(a, b-i, i)
        if(b <= nMax):
            for i in range(1, a //2 + 1):
                if(Validate(b, i, a-i, c)):
                    yield(b, a-i, i)

def BruteForceKnowns(nMax):    
    knowns = set()
    x = 0
    while(x < nMax):
        x += 1
        for y in range(1, x+1):
            for z in range(1, y+1):
                route = min((y+z)**2 + x**2, (x+z)**2+y**2, (x+y)**2 + z**2)
                if(math.sqrt(route).is_integer()):
                    knowns.add((x, y, z))
    return knowns

assert len(list(GenerateCubesWithIntegerPath(100))) == 2060

def FilteredCount(list, m):
    return Utilities.Count(filter(lambda cube: cube[0] <= m and cube[1] <= m and cube[2] <= m, list))

def Hunt(target):
    upper = 2* math.ceil(math.sqrt(target))
    cubes = list(GenerateCubesWithIntegerPath(upper))
    while(len(cubes) < target):
        upper *= 2
        cubes = list(GenerateCubesWithIntegerPath(upper))

    lower = upper // 2
    while(FilteredCount(cubes, lower) > target):
        lower = lower // 2

    while(lower + 1 < upper):
        middle = (lower + upper) // 2
        count = FilteredCount(cubes, middle)
        if(count >= target):
            upper = middle
        else:
             lower = middle
    return upper

def HuntAnswer(target, start, step, last):
    for i in itertools.count(start, step):
        count = Count(GenerateCubesWithIntegerPath(i))
        if(count > target):
            if(step == 1 or last + 1 == i):
                return i
            return HuntAnswer(target, i - step + 1, step // 2, i - step)

assert Hunt(2000) == 100

answer = Hunt(1000000)
print(answer)
assert answer == 1818



