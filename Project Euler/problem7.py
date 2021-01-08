
def FindNthPrime(n):
    if(n == 1): return 2
    primes = [2]

    num = 3
    while len(primes) < n:
        for p in primes:
            if(num % p == 0):
                break
        else: 
            primes.append(num)

        num += 2
    return num - 2

print(FindNthPrime(10001))

assert FindNthPrime(6) == 13
assert FindNthPrime(10001) == 104743