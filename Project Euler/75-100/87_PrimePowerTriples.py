import math, primetools, itertools, Utilities

def GeneratePrimePowerSets(totalMax):
    fourthMax = math.ceil(math.pow(totalMax - 12, .25))
    thirdMax = math.ceil(math.pow(totalMax - 20, 1/3))
    squareMax = math.ceil(math.sqrt(totalMax - 24))
    primes = primetools.GeneratePrimesUpTo(max(fourthMax, thirdMax, squareMax))

    for square, third, fourth in itertools.product(filter(lambda p : p < squareMax, primes),
                                                  filter(lambda p : p < thirdMax, primes),
                                                  filter(lambda p : p < fourthMax, primes)):
        n = square**2 + third**3 + fourth**4
        if(n < totalMax):
            yield n

def FindAnswer(totalMax):
    return len(set(GeneratePrimePowerSets(totalMax)))

assert FindAnswer(50) == 4

answer = FindAnswer(50000000)
print(answer)
assert answer == 1097343

