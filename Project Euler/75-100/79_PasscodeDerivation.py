

def TryInsert(working, source):
    for i in range(len(working) -1):
        left = working[i]
        right = working[i+1]
        for line in source:
            for j in range(len(line) - 2):
                if(line[j] == left and line[j+2] == right):
                    return working[0:i+1] + line[j+1] + working[i+1:]

def Merge(codes):
    subCodes = set()
    for line in codes:
        workingCode = line
        while(True):
            result = TryInsert(workingCode, codes)
            if(result == None):
                subCodes.add(workingCode)
                break
            workingCode = result
    toRemove = set()
    for sc in subCodes:
        for other in subCodes:
            if(sc in other and sc != other):
                toRemove.add(sc)
                break
    return subCodes.difference(toRemove)

def MergeAll(codes):
    while(len(codes) > 1):
        codes = Merge(codes)
    return codes.pop()


input = open("p079_keylog.txt", "r")

lines = input.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

answer = MergeAll(lines)
print(answer)
assert answer == '73162890'