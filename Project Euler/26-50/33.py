import functools, Utilities

def GetPairs():
    for numerator in range(10, 100):
        numeratorFirstDigit = numerator // 10
        numeratorSecondDigit = numerator % 10

        for j in range(0, 10):
            #check if first digit can be cancelled
            den = numeratorFirstDigit * 10 + j
            if(IsRelevant(numerator, den, numeratorSecondDigit, j)):
               yield (numerator, den)

            den = j*10 + numeratorFirstDigit
            if(IsRelevant(numerator, den, numeratorSecondDigit, j)):
                yield(numerator, den)

            #check if second digit can be canceled
            den = j*10 + numeratorSecondDigit
            if(IsRelevant(numerator, den, numeratorFirstDigit, j)):
                yield(numerator, den)

            den = numeratorSecondDigit*10 + j
            if(IsRelevant(numerator, den, numeratorFirstDigit, j)):
                yield(numerator, den)

def IsRelevant(numerator, denominator, simplifiedNumerator, expectedDenominator):
    return (denominator > 0 
            and (numerator % 10 != 0 and denominator % 10 != 0)
            and numerator / denominator < 1 
            and simplifiedNumerator * denominator / numerator == expectedDenominator)

result = set(GetPairs())

print(result)

def accumulate(tupleA, tupleB):
    return (tupleA[0]*tupleB[0], tupleA[1]*tupleB[1])

product = functools.reduce(accumulate, result)
reduction = Utilities.GreatestCommonFactor(product[0], product[1])
answer = product[1] / reduction
print(answer)
assert answer == 100