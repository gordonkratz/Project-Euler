"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def IntIsPalindrome(n):
    stringN = str(n)
    return stringN == stringN[::-1]


def LargestPalindromeProductOfNumbersLessThan(n):
    currentLargest = 1
    for i in range(n, 1, -1):
        for j in range(i, 1, -1):
            product = i*j
            if(IntIsPalindrome(product) and product > currentLargest):
                currentLargest = product
            elif(product < currentLargest):
                break
    return currentLargest

print(LargestPalindromeProductOfNumbersLessThan(1000))

assert(LargestPalindromeProductOfNumbersLessThan(100) == 9009)
assert(LargestPalindromeProductOfNumbersLessThan(1000) == 906609)