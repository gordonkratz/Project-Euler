import itertools

def listOfPermutations(allowedDigits):
    if(len(allowedDigits) == 1):
        yield(allowedDigits[0])
        return
    for digit in allowedDigits:
        for subResult in listOfPermutations(list(filter(lambda x: x != digit, allowedDigits))):
            yield(digit*10**(len(allowedDigits)-1) + subResult)

knowns = set()
sum = 0
for item in listOfPermutations([1, 2, 3, 4, 5, 6, 7, 8, 9]):
    st = str(item)
    first = int(st[0:2])
    second = int(st[2:5])
    product = int(st[5:])
    if(first*second == product and product not in knowns):
        knowns.add(product)
        sum += product

    first = int(st[0])
    second = int(st[1:5])
    if(first*second == product and product not in knowns):
        knowns.add(product)
        sum += product


print (sum)
assert sum == 45228