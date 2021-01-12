import Utilities, functools, time

startTime = time.perf_counter()
primes = set(Utilities.GeneratePrimesUpTo(1000000000))
endTime= time.perf_counter()
print("Elapsed to find Primes: ", endTime - startTime)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
startTime = time.perf_counter()
domain = []
for i in range(6, len(digits)):
    domain += Utilities.ListOfPermutations(digits[:i+1])
answer = max(filter(lambda x: x in primes, domain))
endTime= time.perf_counter()
print("Elapsed to iterate over pandigitals: ", endTime - startTime)
print(answer)
assert answer == 7652413