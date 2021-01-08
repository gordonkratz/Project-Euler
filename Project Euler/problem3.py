"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

"""
By factoring all factors out in order, you know that successive factors are
definitely going to be prime. 
"""
def GetLargestPrimeFactor(n):
    largestPrime = currentPotentialFactor = 2
    while(n != 1):
        if(n % currentPotentialFactor == 0):
            n /= currentPotentialFactor
        else:
            currentPotentialFactor += 1
    return currentPotentialFactor

print(GetLargestPrimeFactor(600851475143))

assert(GetLargestPrimeFactor(600851475143) == 6857)
assert(GetLargestPrimeFactor(13195) == 29)
        