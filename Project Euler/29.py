
def GetValues():
    for a in range(2, 101):
        for b in range(2, 101):
            yield a**b

answer = len(set(GetValues()))
print(answer)
