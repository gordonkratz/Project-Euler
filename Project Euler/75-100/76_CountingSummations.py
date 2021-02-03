import Utilities

def FindCountingSums(value):
    return Utilities.FindSums(value, [i for i in range(1, value)])


assert FindCountingSums(5) == 6

answer = FindCountingSums(100)
print (answer)
assert answer == 190569291