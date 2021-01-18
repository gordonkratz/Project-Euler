import functools 

def GetCenterOfNthPascalRow(line):
    return functools.reduce(lambda acc, x : acc * (line - x) / x, 
                            range(1, (line + 1) // 2),
                            1)

def NumberOfPathsThroughGrid(dimension):
    pascalRow = dimension * 2 + 1
    return GetCenterOfNthPascalRow(pascalRow)

print(NumberOfPathsThroughGrid(20))

assert NumberOfPathsThroughGrid(2) == 6
assert NumberOfPathsThroughGrid(20) == 137846528820


