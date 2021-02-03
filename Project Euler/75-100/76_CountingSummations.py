def FindSums(value):
    combos = [0]*(value+1)
    combos[0] = 1
    for i in range(1, value):
        for j in range(i, value+1):
            diff = j - i
            combos[j] += combos[diff]
    return combos[-1] 


assert FindSums(5) == 6

answer = FindSums(100)
print (answer)
assert asnswer == 190569291