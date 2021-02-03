changeValues = [200, 100, 50, 20, 10, 5, 2, 1]

def FindChange(value, coins):
    combos = [0]*(value+1)
    coins.sort()
    combos[0] = 1
    for i in range(len(coins)):
        for j in range(coins[i], value + 1):
            diff = j - coins[i]
            if(diff < 0):
                continue
            combos[j] += combos[diff]
    return combos[-1] 


assert FindChange(0, changeValues) == 1       
assert FindChange(10, [1]) == 1
assert FindChange(9, [2]) == 0
assert FindChange(10, changeValues) == 11


answer = FindChange(200, changeValues)
print(answer)
assert answer == 73682

