


def CheckValidation(puzzle, index):
    currentNumber = puzzle[index]

    # check row
    start = index // 9 * 9
    for r in range(9):
        i = start + r
        if(i == index):
            continue
        if(puzzle[i] == currentNumber):
            return False

    # check column
    start = index % 9
    for r in range(9):
        i = 9 * r + start
        if(i == index):
            continue
        if(puzzle[i] == currentNumber):
            return False

    # check box
    leftMost = index // 3 * 3
    topCorner = (leftMost % 9) + (leftMost // 27 * 27)
    for a in range(3):
        for b in range(3):
            i = 9*a + b + topCorner
            if(i == index):
                continue
            if(puzzle[i] == currentNumber):
                return False
    return True

testPuzzle = [0 for i in range(81)]
testPuzzle[36] = 9
testPuzzle[45] = 9
assert not CheckValidation(testPuzzle, 45)

testPuzzle[25] = 8
assert CheckValidation(testPuzzle, 25)

sampleValidPuzzle = [4,8,3,9,2,1,6,5,7,9,6,7,3,4,5,8,2,1,2,5,1,8,7,6,4,9,3,5,4,8,1,3,2,9,7,6,7,2,9,5,6,4,1,3,8,1,3,6,7,9,8,2,4,5,3,7,2,6,8,9,5,1,4,8,1,4,2,5,3,7,6,9,6,9,5,4,1,7,3,8,2]
for i in range(81):
    assert CheckValidation(sampleValidPuzzle, i)

def SolveSudoku(puzzle: list):
    fixed = [True if x != 0 else False for x in puzzle]
    copy = [p for p in puzzle]
    index = 0
    while(index < 81):
        if(fixed[index]):
            index += 1
        else:
            copy[index] += 1
            while(not CheckValidation(copy, index)):
                copy[index] += 1

            if(copy[index] > 9):
                copy[index] = 0
                index -= 1
                while(fixed[index]):
                    index -= 1
            else: 
                index += 1
    return copy

file = open("p096_sudoku.txt", "r")
file.readline()
bigGrid = []
currentGrid = []
for line in file:
    if("Grid" in line):
        bigGrid.append(currentGrid)
        currentGrid = []
    else:
        currentGrid.extend(int(x) for x in line.strip())
bigGrid.append(currentGrid)


assert SolveSudoku(bigGrid[0]) == sampleValidPuzzle

i = 0
for p in bigGrid:
    print("Grid ", i)
    i += 1
    for x in range(0, 81, 9):
        print(p[x:x+9])


answer = 0
for i in range(len(bigGrid)):
    solved = SolveSudoku(bigGrid[i])
    for i in range(len(solved)):
        if(not CheckValidation(solved, i)):
            print("problem: ", i)
            for x in range(0, 81, 9):
                print(solved[x:x+9])
            
    answer += solved[0] * 100
    answer += solved[1] * 10
    answer += solved[2]
print(answer)
