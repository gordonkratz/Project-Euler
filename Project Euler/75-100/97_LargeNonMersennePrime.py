import Timer

def FindNumber():
    answer = 1
    pow = 7830457
    while(pow > 0):
        answer *= 2**(40 if pow > 40 else pow)
        answer %= 10**10
        pow -= 40
    answer *= 28433
    answer += 1
    answer %= 10**10
    return answer

with Timer.Timer():
    answer = FindNumber()
    print(answer)
    assert answer == 8739992577