import Utilities, functools

sum = functools.reduce(Utilities.Sum, 
                       filter(lambda i: Utilities.IsPalindrome(i) 
                              and Utilities.IsPalindrome('{0:b}'.format(i)),
                              range(1000000)))

print(sum)
assert sum == 872187