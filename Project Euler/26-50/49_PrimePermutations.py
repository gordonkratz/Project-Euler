import Utilities

def GetPrimePermutations():
    primes = list(filter(lambda x: x > 999, Utilities.GeneratePrimesUpTo(10000)))
    grouped = dict()
    for p in primes:
        key = ''.join(sorted(str(p)))
        if(key not in grouped):
            grouped[key] = [p]
        else:
            grouped[key].append(p)
    
    for l in filter(lambda x: len(x) > 3, grouped.values()):
        for i in range(len(l) - 2):
            first = l[i]
            second = l[i+1]
            third = l[i+2]
    
            if(second-first == third-second and first != 1487):
                return str(first) + str(second) + str(third)

answer = GetPrimePermutations()
print(answer)
assert answer == "296962999629"
