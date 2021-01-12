def concat(s1, s2, spacer):
    return (s1 + spacer + s2) if s2 != "" else s1

def lessThan20(n):
    if(n == 0):
        return ""
    if (n == 1):
        return "one"
    elif (n == 2):
        return "two"
    elif (n == 3):
        return "three"
    elif (n == 4):
        return "four"
    elif (n == 5):
        return "five"
    elif (n == 6):
        return "six"
    elif (n == 7):
        return "seven"
    elif (n == 8):
        return "eight"
    elif (n == 9):
        return "nine"
    elif (n == 10):
        return "ten"
    elif (n == 11):
        return "eleven"
    elif (n == 12):
        return "twelve"
    elif (n == 13):
        return "thirteen"
    elif (n == 14):
        return "fourteen"
    elif (n == 15):
        return "fifteen"
    elif (n == 16):
        return "sixteen"
    elif (n == 17):
        return "seventeen"
    elif (n == 18):
        return "eighteen"
    elif (n == 19):
        return "nineteen"

def lessThan100(n):
    tensdigit = n // 10
    onesdigit = n % 10
    if(tensdigit <= 1):
        return lessThan20(n)
    if(tensdigit == 2):
        return "twenty "+lessThan20(onesdigit)
    if(tensdigit == 3):
        return "thirty "+lessThan20(onesdigit)
    if(tensdigit == 4):
        return "forty "+ lessThan20(onesdigit)
    if(tensdigit == 5):
        return "fifty "+lessThan20(onesdigit)
    if(tensdigit == 6):
        return "sixty "+ lessThan20(onesdigit)
    if(tensdigit == 7):
        return "seventy "+ lessThan20(onesdigit)
    if(tensdigit == 8):
        return "eighty "+lessThan20(onesdigit)
    if(tensdigit == 9):
        return "ninety "+lessThan20(onesdigit)

def lessThan1000(n):
    hundredsdigit = n // 100
    if(hundredsdigit == 0):
        return lessThan100(n)
    return concat(lessThan20(hundredsdigit) + " hundred ", lessThan100(n % 100), " and ")
    
totalLength = len("onethousand")
for i in range(1,1000):
    string = lessThan1000(i)
    length = len(string.replace(" ",""))
    totalLength += length
    #print(i, string, length, totalLength)
    
print(totalLength)

assert totalLength == 21124