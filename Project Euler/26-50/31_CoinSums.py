import functools

def ComboCount(desiredValue, coins):
    if(desiredValue == 0 or len(coins) == 0): return 0
    currentCoin = coins[0]
    maxForLargest = desiredValue // currentCoin

    count = 1 if maxForLargest * currentCoin == desiredValue else 0 
    for i in range(maxForLargest, 0, -1):
        count += ComboCount(desiredValue - currentCoin * i, coins[1:])
    count += ComboCount(desiredValue, coins [1:])
    return count


changeValues = [200, 100, 50, 20, 10, 5, 2, 1]

assert ComboCount(0, changeValues) == 0       
assert ComboCount(10, [1]) == 1
assert ComboCount(9, [2]) == 0
assert ComboCount(10, changeValues) == 11


answer = ComboCount(200, changeValues)
print(answer)
assert answer == 73682

