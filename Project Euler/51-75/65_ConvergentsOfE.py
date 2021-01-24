from fractions import Fraction
import functools

def GenerateConvergentSeries(n):
    yield 2
    for i in range(2, n+1):
        if i % 3 == 0:
            yield i * 2 // 3
        else: 
            yield 1

def ConvergentOfE(n):
    fractionalTerm = 0
    series = list(GenerateConvergentSeries(n))
    for i in range(len(series)-1, 0, -1):
        fractionalTerm = Fraction(1, series[i] + fractionalTerm)
    fractionalTerm += series[0]
    return functools.reduce(lambda acc, x: acc + int(x), str(fractionalTerm.numerator), 0)

assert ConvergentOfE(10) == 17

answer = ConvergentOfE(100)
print(answer)
assert answer == 272
