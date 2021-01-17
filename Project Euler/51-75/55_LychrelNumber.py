import Utilities

def IsLychrel(n):
    for i in range(51):
        n = n + int(str(n)[::-1])
        if Utilities.IsPalindrome(n):
            return False
    return True

assert not IsLychrel(47)
assert not IsLychrel(349)
assert IsLychrel(196)
assert IsLychrel(4994)

answer = len(list(filter(IsLychrel, range(10000))))
print(answer)
assert answer == 249