import Timer

endsAtOne = set([1])
endsAt89 = set([85, 145, 42, 20, 4, 16, 37, 89])

def GetDigitSquareSum(n):
    result = 0
    while(n != 0):
        result += (n % 10)**2
        n = n // 10
    return result

with (Timer.Timer()):
    for i in range(2, 10000000):
        if(i in endsAtOne or i in endsAt89):
            continue
        chain = [i]
        n = GetDigitSquareSum(i)
        while(True):
            if(n in endsAtOne):
                endsAtOne.update(chain)
                break
            elif(n in endsAt89):
                endsAt89.update(chain)
                break
            chain.append(n)
            n = GetDigitSquareSum(n)


    answer = len(endsAt89)
    print(answer)
    assert answer == 8581146

        
