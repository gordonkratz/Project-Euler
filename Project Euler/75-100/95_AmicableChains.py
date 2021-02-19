import Timer, functools, operator

def GenerateSumOfDivisors(nMax):
    divisors = {i:[1] for i in range(nMax+1)}
    for i in range(2, nMax+1):
        for mul in range(i*2, nMax+1, i):
            divisors[mul].append(i)
    return {k:functools.reduce(operator.add, v) for k, v in divisors.items()}

def FindAnswer():
    nMax = 1000000
    divisors = GenerateSumOfDivisors(nMax)
    longestChain = 0
    startMin = nMax
    checked = set()
    for i in range(2, nMax):
        if(i in checked):
             continue
        currentChain = [i]
        next = divisors[i]
        broken = False
        while(next not in currentChain):
            if(next <= 0 or next > nMax):
                broken = True
                break
            currentChain.append(next)
            next = divisors[next]
        checked.update(currentChain)
        if(not broken):
            chainStartIndex = currentChain.index(next)
            chainLength = len(currentChain) - chainStartIndex
            if(chainLength > longestChain):
                longestChain = chainLength
                startMin = min(currentChain[chainStartIndex:])
    return startMin

with Timer.Timer():
    answer = FindAnswer()
    print(answer)
