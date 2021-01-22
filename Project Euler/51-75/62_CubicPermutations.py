import itertools, math, Utilities


def GetCubePermutationsOfLength(n):
    for digitCount in itertools.count(2):
        lower = math.ceil((10**(digitCount-1))**(1./3))
        upper = math.ceil((10**digitCount)**(1./3))
        values = dict()
        for i in range(lower, upper):
            cube = i**3
            key = int("".join(sorted([d for d in str(cube)])))
            Utilities.GetOrAdd(values, key, lambda: list()).append(cube)
        for k, v in values.items():
            if(len(v) == n):
                return min(v)

assert GetCubePermutationsOfLength(3) == 41063625
answer = GetCubePermutationsOfLength(5)
print(answer)
assert answer == 127035954683
    

