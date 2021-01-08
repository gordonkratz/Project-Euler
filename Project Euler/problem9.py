import math as m

def GetTriplets(b, n):
    if(b == n): pass
    a = (n**2 - 2*b*n)/(2*n - 2*b)
    c = m.sqrt(a**2 + b**2)
    if(a.is_integer() and c.is_integer()
       and a > 0 and c > 0):
        return a*b*c

    pass

def FindTripletSummingTo(n):
    for i in range(1, n//2):
        product = GetTriplets(i, n)
        if(product != None):
            return product
    pass

print(FindTripletSummingTo(1000))

assert(FindTripletSummingTo(1000) == 31875000)
assert(FindTripletSummingTo(12) == 60)