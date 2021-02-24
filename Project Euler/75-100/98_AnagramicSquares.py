import Utilities, math, itertools

def ConvertKey(s: str):
    newKey = []
    digit = 0
    for key, group in itertools.groupby(sorted(s)):
        for g in group:
            newKey.append(str(digit))
        digit += 1
    return "".join(newKey)

def Convertible():
    pass


file = open("p098_words.txt", "r")
anagrams = dict()
for word in Utilities.FileSplit(file):
    stripped = word.strip("\"")
    key = "".join(sorted(stripped))
    Utilities.GetOrAdd(anagrams, key, lambda: []).append(stripped)

anagrams = {key: value for key, value in filter(lambda item: len(item[1]) > 1, anagrams.items())}

maxDigits = max(map(lambda k: len(k), anagrams.keys()))
iMax = math.ceil(math.sqrt(maxDigits))

squareAnagrams = dict()
i = 1
square = str(i**2)
while(len(square) < maxDigits):
    key = "".join(sorted(square))
    Utilities.GetOrAdd(squareAnagrams, key, lambda: []).append(square)
    i += 1
    square = str(i**2)

squareAnagrams = {key: value for key, value in filter(lambda item: len(item[1]) > 1, squareAnagrams.items())}

wordPatterns = dict()
for key in anagrams.keys():
    newKey = ConvertKey(key)
    Utilities.GetOrAdd(wordPatterns, newKey, lambda: []).append(key)

def Translate(word:str , key:dict):
    for k, v in key.items():
        word = word.replace(k, v)
    return word

def CheckForAnagramicSquares(words: list, numbers: list):
    for n in numbers:
        cKey = dict()
        for i in range(len(words[0])):
            cKey[words[0][i]] = n[i]
        for word in words[1:]:
            translated = Translate(word, cKey)
            if(translated in numbers):
                yield max(int(n), int(translated))

CheckForAnagramicSquares(['ATE', 'TEA'], ['256', '625'])

maxSquare = 0
for key, value in squareAnagrams.items():
    newKey = ConvertKey(key)
    if(newKey in wordPatterns):
        #print(newKey)
        #print(wordPatterns[newKey])
        #for p in wordPatterns[newKey]:
        #    print(anagrams[p])
        #print(squareAnagrams[key])
        #print()
        for p in wordPatterns[newKey]:
            for square in CheckForAnagramicSquares(anagrams[p], squareAnagrams[key]):
                maxSquare = max(maxSquare, square)

print(maxSquare)
assert maxSquare == 18769