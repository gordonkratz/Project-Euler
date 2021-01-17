
import itertools

def HasPermutedMultiples(n, multiples):
    nSorted = sorted(str(n))
    for j in range(2, multiples+1):
        m = n*j
        if(sorted(str(m)) != nSorted):
           return False
    return True

assert HasPermutedMultiples(125874, 2)

def GetAnswer():
    for i in itertools.count(1):
        if(HasPermutedMultiples(i, 6)):
            return i

answer = GetAnswer()
print(answer)
assert answer == 142857
