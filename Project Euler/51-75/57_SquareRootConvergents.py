from fractions import Fraction

def SquareRootOfTwoDenominator(iterations):
    if(iterations == 1):
        return 2
    return 2 + Fraction(1, SquareRootOfTwoDenominator(iterations - 1))

def SqrtTwoApproximation(iterations):
    return 1 + Fraction(1, SquareRootOfTwoDenominator(iterations))

oneIter = SqrtTwoApproximation(1)
print(oneIter)

assert SqrtTwoApproximation(1) == Fraction(3, 2)
assert SqrtTwoApproximation(2) == Fraction(7, 5)
assert SqrtTwoApproximation(3) == Fraction(17, 12)

count = 0
fractionalTerm = Fraction(1, 2)

for i in range(2, 1001):
    fractionalTerm = Fraction(1, 2 + fractionalTerm)
    a = 1 + fractionalTerm
    if(len(str(a.numerator)) > len(str(a.denominator))):
        count += 1

print(count)
assert count == 153

