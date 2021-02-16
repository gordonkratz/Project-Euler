import itertools, operator, Utilities

def Eval(arg1, arg2, op):
    if(arg1 == None or arg2 == None or (op == operator.truediv and arg2 == 0)):
        return None
    return op(arg1, arg2)

def Op(arg1, arg2, op):
    for (a, b) in itertools.product(arg1, arg2):
        yield Eval(a, b, op)
        if(op == operator.truediv or op == operator.sub):
            yield Eval(b, a, op)
            
def StaticInt(x):
    yield x

def GetMaximumIntSequence(digitSet):
    resultsList = []
    for combo in itertools.permutations(digitSet):
        for ops in itertools.product([operator.add, operator.sub, operator.truediv, operator.mul], repeat=3):
            for r in Op(Op(Op(StaticInt(combo[0]), StaticInt(combo[1]), ops[0]), StaticInt(combo[2]), ops[1]), StaticInt(combo[3]), ops[2]):
                if(r is not None and r > 0):
                    if(isinstance(r, int)):
                        resultsList.append(r)
                    elif(isinstance(r, float) and r.is_integer()):
                        resultsList.append(int(r))
    i = 1
    resultsList = list(sorted(set(resultsList)))
    for n in resultsList:
        if(n != i):
            return i - 1
        i += 1
    return i

assert GetMaximumIntSequence([1, 2, 3, 4]) == 28

def FindAnswer():
    currentHighest = 0
    answerSet = []
    for combo in itertools.combinations(range(1, 10), 4):
        maxInt = GetMaximumIntSequence(combo)
        if(maxInt > currentHighest):
            currentHighest = maxInt
            answerSet = combo
    answer = ""
    for i in answerSet:
        answer += str(i)
    return answer

answer = FindAnswer()
print(answer)
assert answer == '1258'