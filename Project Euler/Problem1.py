from functools import reduce

def SumOfThreesAndFivesUpTo(n):
    x = n // 15 # How many multiples of 15 are the in n
    highestMultiple15 = x*15
    additional = SumOfThreesAndFivesInRange(highestMultiple15, n)
    return 45*x + (105*(x**2) - 105*x)/2 + additional

def SumOfThreesAndFivesInRange(n, m):
    return reduce(lambda sum, x: sum + x 
                  if (x % 3 == 0 or x % 5 == 0)
                    else sum, 
                  range(n, m), 0)

assert SumOfThreesAndFivesUpTo(16) == 60
assert SumOfThreesAndFivesUpTo(10) == 23
assert SumOfThreesAndFivesUpTo(15) == 45
assert SumOfThreesAndFivesUpTo(30) == 195
assert SumOfThreesAndFivesUpTo(1000) == 233168

print(SumOfThreesAndFivesUpTo(1000))
