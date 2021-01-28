from fractions import Fraction
import Utilities, functools, math

threeSevenths = Fraction(3, 7)


def GetNumeratorOfFractionLessThanThreeSevenths(dMax):
    c = 3
    d = 7
    b = ((c*dMax - 1) // d)
    a = (1 - c*b) // (0-d)
    
    b = (dMax // lowerBound.denominator) * lowerBound.denominator + lowerBound.numerator
    a = (lowerBound.numerator - b) // (0-lowerBound.denominator)
    return a

def GenerateFractionList(dMax):
    lowerBound = Fraction(0, 1)
    for d in range(dMax, (dMax//2), -1):
        lower = math.floor(lowerBound.numerator*d/lowerBound.denominator)
        for n in range(lower, d):
            f = Fraction(n, d)
            if(f < lowerBound):
                continue
            if(f >= threeSevenths):
                break
            lowerBound = f
    return lowerBound.numerator


assert GetNumeratorOfFractionLessThanThreeSevenths(8) == 2

answer = GetNumeratorOfFractionLessThanThreeSevenths(1000000)
print(answer)
assert answer == 428570