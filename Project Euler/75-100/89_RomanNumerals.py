
numeralValues = {'I' : 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
subtractivePairs = {'M':'C', 'D':'C', 'C': 'X', 'L':'X', 'X':'I', 'V':'I'}
numerics = {value:key for key, value in numeralValues.items()}
orderedNumerics = list(sorted(numeralValues.values(), reverse=True))

def CalculateValue(numerals: str):
    total = 0
    i = 0
    while i < len(numerals):
        current = numeralValues[numerals[i]]
        i += 1
        if(i < len(numerals)):
            next = numeralValues[numerals[i]]
            if(next > current):
                current = next - current
                i += 1
        total += current
    return total

assert CalculateValue("MDCVI") == 1606
assert CalculateValue("MCCCCCCVI") == 1606
assert CalculateValue("XLVIIII") == 49
assert CalculateValue("XLIX") == 49
assert CalculateValue("XVI") == 16

def GenerateRomanNumerals(n: int):
    i = 0
    result = ""
    currentVal = orderedNumerics[i]
    currentChar = numerics[currentVal]
    subtractive = numeralValues[subtractivePairs[currentChar]] if currentChar in subtractivePairs else 0
    while(n > 0):
        if(n >= currentVal):
            result += currentChar
            n -= currentVal
        elif(n >= currentVal-subtractive):
            result += numerics[subtractive]
            result += currentChar
            n -= currentVal - subtractive
        else:
            i += 1
            currentVal = orderedNumerics[i]
            currentChar = numerics[currentVal]
            subtractive = numeralValues[subtractivePairs[currentChar]] if currentChar in subtractivePairs else 0
    return result

assert GenerateRomanNumerals(10) == "X"
assert GenerateRomanNumerals(1) == "I"
assert GenerateRomanNumerals(5) == "V"
assert GenerateRomanNumerals(50) == "L"
assert GenerateRomanNumerals(100) == "C"
assert GenerateRomanNumerals(500) == "D"
assert GenerateRomanNumerals(1000) == "M"
assert GenerateRomanNumerals(16) == "XVI"
assert GenerateRomanNumerals(55) == "LV"
assert GenerateRomanNumerals(750) == "DCCL"
assert GenerateRomanNumerals(19) == "XIX"
assert GenerateRomanNumerals(49) == "XLIX"
assert GenerateRomanNumerals(1606) == "MDCVI"


file = open("p089_roman.txt", "r")
savings = 0
for line in file:
    line = line.strip()
    converted = GenerateRomanNumerals(CalculateValue(line))
    savings += len(line) - len(converted)

print(savings)
assert savings == 743



