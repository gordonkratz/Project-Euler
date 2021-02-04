testInput = [
        [131, 201, 630, 537, 805],
        [673, 96, 803, 699, 732], 
        [234, 342, 746, 497, 524],
        [103, 965, 422, 121, 37], 
        [18, 150, 111, 956, 331]
    ]

def FindMinimalPath(input):
    results = [[0 for i in range(len(input))] for i in range(len(input))]
    for i in range(len(input)):
        for j in range(len(input[0])):
            weight = input[i][j]
            if(j > 0):
                if(i > 0):
                    weight += min(results[i][j-1], results[i-1][j])
                else:
                    weight += results[i][j-1]
            else:
                weight += results[i-1][j]
            results[i][j] = weight
    return results[-1][-1]

assert FindMinimalPath(testInput) == 2427

file = open("p081_matrix.txt", "r")
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
assert answer == 427337