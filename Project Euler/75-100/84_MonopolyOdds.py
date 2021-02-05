import random


board = ['GO', 'A1', 'CC2', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3',
         'JAIL', 'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3',
         'FP', 'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3', 
         'G2J', 'G1', 'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2']

rand = random.Random()

def DiceRoll(diceSize):
    return(rand.randint(1, diceSize), rand.randint(1, diceSize))

def AddToIndex(start, amount):
    next = start + amount
    if(next >= len(board)):
        next %= len(board)
    while(next < 0):
        next += len(board) 
    return next

def GetNext(startIndex, squareType):
    next = AddToIndex(startIndex, 1)
    square = board[next]
    while(squareType not in square):
        next = AddToIndex(next, 1)
        square = board[next]
    return next

def SpecialMoves(space):
    if(space == 30):
        return (10, True)
    elif('CC' in board[space]):
        roll = rand.randint(1, 16)
        if(roll == 1):
            return (0, False)
        elif(roll == 2):
            return (10, True)
    elif('CH' in board[space]):
        roll = rand.randint(1, 16)
        if(roll == 1):
            return (0, False)
        if(roll == 2):
            return (10, True)
        if(roll == 3):
            return (11, False)
        if(roll == 4):
            return (24, False)
        if(roll == 5):
            return (39, False)
        if(roll == 6):
            return (5, False)
        if(roll == 7 or roll == 8):
            return (GetNext(space, 'R'), False)
        if(roll == 9):
            return (GetNext(space, 'U'), False)
        if(roll == 10):
            return (AddToIndex(space, -3), False)
    return (space, False)

def DoMove(diceSize, current):
    (a, b) = DiceRoll(diceSize)
    temp = AddToIndex(current, a+b)
    (next, isOver) = SpecialMoves(temp)
    return (next, isOver or a != b)

def DoTurn(diceSize, current):
    count = 1
    (next, isOver) = DoMove(diceSize, current)
    while not isOver:
        if(count == 3): return 10
        (next, isOver) = DoMove(diceSize, next)
        count += 1
    return next

def DoSimulation(diceSize, iterations):
    currentIndex = 0
    counts = [0 for i in range(len(board))]
    for i in range(iterations):
        currentIndex = DoTurn(diceSize, currentIndex)
        counts[currentIndex] += 1
    return counts

results = DoSimulation(4, 3000000)
joined = dict()
for i in range(len(results)):
    joined[board[i]] = results[i]/30000

results = list(sorted(joined.items(), key=lambda x: x[1]))
for key, value in results:
    print(key, value)
