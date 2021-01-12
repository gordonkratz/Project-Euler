import math


def NthLexicographicPermutation(input, n):
    if(n == 0): return "".join(input)

    numOfSubpermutations = math.factorial(len(input) - 1)
    p = math.factorial(len(input))

    goesInto = n // numOfSubpermutations
    remainder = (n % numOfSubpermutations)

    leadingCharacter = input[goesInto]
    input.remove(leadingCharacter)

    return leadingCharacter + NthLexicographicPermutation(input, remainder)

assert (NthLexicographicPermutation(["0","1","2"], 4) == "201")

answer = (NthLexicographicPermutation(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], 999999))

print(answer)
assert answer == "2783915460"

