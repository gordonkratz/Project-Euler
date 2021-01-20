import itertools

def GetCubePermutations(i, alreadyChecked):
    iCubed = i**3
    count = 0
    for p in itertools.permutations(str(iCubed)):
        pint = int("".join(p))
        if(pint in alreadyChecked): 
            break
        alreadyChecked.add(pint)
        if((round(pint**(1.0/3)))**3 == pint):
            yield pint

perm = set(GetCubePermutations(345, set()))
print(perm)
assert len(perm) == 3

alreadyChecked = set(map(lambda x: x**3, range(1000)))
for c in itertools.count(1000):
    if(len(set(GetCubePermutations(c, alreadyChecked))) == 5):
        print(c**3)
        break
    

