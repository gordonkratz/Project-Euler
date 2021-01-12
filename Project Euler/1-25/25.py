def FibonnaciWithNDigits(n):
    previous = 0
    current = 1
    index = 1

    while (len(str(current)) < n):
        current = current + previous
        previous = current - previous
        index += 1

    return index

    

assert(FibonnaciWithNDigits(3) == 12)

answer = FibonnaciWithNDigits(1000)
print(answer)

