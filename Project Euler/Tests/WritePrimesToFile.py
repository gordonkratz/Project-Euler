import primetools

f = open("primes.txt", "w")

for p in primetools.GeneratePrimesUpTo(500000000):
    f.write(str(p))
    f.write('\n')

f.close()