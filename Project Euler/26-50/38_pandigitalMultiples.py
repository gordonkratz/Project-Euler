import itertools, functools, Utilities

def ConcatenatedProduct(number, n):
    return int(functools.reduce(Utilities.Sum, map(lambda x: str(x*number), range(1, n+1))))

def IsRelevant(pandigital):
    originalString = str(pandigital)
    for i in range(1, len(originalString)):
        baseNumber = int(originalString[0:i])
        for j in itertools.count(1):
            conProd = ConcatenatedProduct(baseNumber, j)
            if(conProd == pandigital): 
                return True
            if(conProd > pandigital): 
                break

assert IsRelevant(192384576)
assert ConcatenatedProduct(192, 3) == 192384576

for num in sorted(Utilities.ListOfPermutations([1, 2, 3, 4, 5, 6, 7, 8, 9]), reverse=True):
    if(IsRelevant(num)):
        print(num)
        break
    