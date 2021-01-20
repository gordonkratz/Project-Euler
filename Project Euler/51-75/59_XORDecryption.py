import Utilities, itertools, functools

input = open("p059_cipher.txt", "r")

def decrypt(bytes, key):
    keys = itertools.cycle(key)
    for b, k in zip(bytes, itertools.cycle(keys)):
        yield(b^k)

def ToString(decryptedBytes):
    return ''.join(map(chr, decryptedBytes))

assert ToString(decrypt([107, 65], [42])) == 'Ak'

def TestKey(key, input):
    result = ToString(decrypt(input, key))
    if("the" in result):
        print(key, result[:30])

text = list(map(int, input.readline().split(",")))
#for key in itertools.product(range(ord('a'), ord('z') + 1), repeat=3):
#    TestKey(key, text)

result = ToString(decrypt(text, [101, 120, 112]))
print(result)
answer = functools.reduce(lambda acc, c: acc + ord(c), result, 0)
print(answer)
assert answer == 129448