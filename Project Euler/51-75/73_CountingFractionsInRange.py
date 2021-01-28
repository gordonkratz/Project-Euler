from fractions import Fraction

def GenerateFractionalSequence(dMax, lowerBound):
    b = (dMax // lowerBound.denominator) * lowerBound.denominator + lowerBound.numerator
    a = (lowerBound.numerator - b) // (0-lowerBound.denominator)
    c = lowerBound.numerator
    d = lowerBound.denominator
    while (c <= dMax):
        k = (dMax + b) // d
        (a, b, c, d) = (c, d, k * c - a, k * d - b)
        yield Fraction(a, b)

def CountFractionsInRange(dMax):
    lowerBound = Fraction(1, 3)
    upperBound = Fraction(1, 2)
    count = 0
    for fraction in GenerateFractionalSequence(dMax, lowerBound):
        if(fraction <= lowerBound):
            continue
        if(fraction >= upperBound):
            break
        count += 1
    return count

assert CountFractionsInRange(8) == 3

answer = CountFractionsInRange(12000)
print(answer)
assert asnwer == 7295372