import Utilities, itertools

def generatePossibleMasks(n):
    charSet = set(str(n))
    for char in charSet:
        for m in GenerateMasksForDigit(char, str(n)):
            yield m

def GenerateMasksForDigit(digit, strN):
    substrings = strN.split(digit)
    max = 2**(len(substrings) - 1)
    padding = len('{0:b}'.format(max - 1))
    for i in range(1, max):

        binary = '{0:b}'.format(i).zfill(padding)
        binary = binary.replace('1', 'X').replace('0', digit)
        yield ''.join(Utilities.roundrobin(substrings, binary))


def TryGetSmallestPrimeWithFamilySize(familySize, upperBound):
    primes = Utilities.GeneratePrimesUpTo(upperBound)
    masks = dict()
    for p in primes:
        for m in generatePossibleMasks(p):
            if(m in masks):
                masks[m].append(p)
            else:
               masks[m] = [p]
    return min(itertools.chain(*filter(lambda x: len(x) == familySize, masks.values())))

assert TryGetSmallestPrimeWithFamilySize(6, 100) == 13
assert TryGetSmallestPrimeWithFamilySize(7, 100000) == 56003

answer = TryGetSmallestPrimeWithFamilySize(8, 1000000)
print(answer)
assert answer == 121313