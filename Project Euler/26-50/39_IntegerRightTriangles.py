import math

def MaybeGenerateTriplet(b, n):
    a = (n**2 - 2*b*n)/(2*n - 2*b)
    c = math.sqrt(a**2 + b**2)
    if(a.is_integer() and c.is_integer()
       and a > 0 and c > 0):
        return (a, b, c)
    pass

def CountAllTripletsSummingTo(p):
    count = 0
    for i in range(1, (p // 4) + 1):
        trip = MaybeGenerateTriplet(i, p)
        if(trip != None): 
            count += 1
    return count

assert CountAllTripletsSummingTo(120) == 3

maxCount = 0
pMax = 0
for p in range(1, 1001):
    count = CountAllTripletsSummingTo(p)
    if(count> maxCount):
        maxCount = count
        pMax = p

print(pMax)