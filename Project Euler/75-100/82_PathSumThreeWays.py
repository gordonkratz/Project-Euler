import functools

testInput = [
        [131, 201, 630, 537, 805],
        [673, 96, 803, 699, 732], 
        [234, 342, 746, 497, 524],
        [103, 965, 422, 121, 37], 
        [18, 150, 111, 956, 331]
    ]

def Minimum(*ints):
    result = float('inf')
    for n in ints:
        if(n == None): continue
        else:
           result = min(result, n)
    return result
    

def FindWeight(x: int, y: int, result: list, input: list):
    if(y == len(input)-1):
        return input[x][y] + result[x-1][y]
    else:
        left = result[x-1][y]
        bottom = FindWeight(x, y+1, result, input)
        return min(left, bottom) + input[x][y]

def FindMinimalPath(input):
    results = [input[0]]
    for x in range(1, len(input)):
        results.append([])
        for y in range(len(input)):
            left = results[x-1][y]
            top = results[x][y-1] if y > 0 else None
            bottom = FindWeight(x, y+1, results, input) if y < len(input)-1 else None
            results[x].append(Minimum(left, top, bottom) + input[x][y])
    return functools.reduce(min, results[-1])

assert FindMinimalPath(testInput) == 994

file = open("p082_matrix.txt", "r")
input = list()
for line in file.readlines():
    nums = line.strip().split(",")
    for i in range(len(nums)):
        n = int(nums[i])
        if(len(input) <= i):
            input.append([n])
        else:
           input[i].append(n)

answer = FindMinimalPath(input)
print(answer)
assert answer == 260324