import itertools, math

def CountSubrectangles(x, y):
    return x*(x+1)*y*(y+1) // 4

assert CountSubrectangles(2, 3) == 18

def HuntAnswer(target):
    x = math.floor(math.sqrt(target))
    y = x
    while(CountSubrectangles(x, y) < target):
        x *= 2
        y = x
    bestX = x
    bestY = y
    bestDelta = abs(target - CountSubrectangles(x, y))
    while(x > 2):
        subcount = CountSubrectangles(x, y)
        delta = abs(target - subcount)
        if(delta == 0):
            bestX = x
            bestY = y
            break
        if(delta < bestDelta):
            bestDelta = delta
            bestX = x
            bestY = y
        if(subcount < target):
            x -= 1
            y = x
        else:
            y -= 1  
    return bestX*bestY

assert HuntAnswer(18) == 6

answer = HuntAnswer(2000000)
print(answer)
assert answer == 2772