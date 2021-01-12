import functools

#This is the most brute force way. Create the grid and then just sum up the relevant cells
#O(n) for time
#O(n^2) for space << not great!!
def getSumOfDiagonals(dimension):
    grid = [[0 for y in range(dimension)] for x in range(dimension)]

    x = dimension // 2
    y = dimension // 2 
    add = 1
    prevAdd = 0
    count = 1
    
    for i in range(1, dimension**2 + 1):
        grid[x][y] = i
        if(add != prevAdd):
            y += (1 if add % 2 != 0 else -1)
        else:
            x += (1 if add % 2 != 0 else -1)
        count -= 1
        if(count == 0):
            if(add != prevAdd):
                prevAdd = add
            else: 
                add += 1
            count = add
    result = 0
    for i in range(dimension):
        result += grid[i][i]
        result += grid[dimension - i - 1][i] if (dimension - i - 1 != i) else 0 
    return result

#I noticed you could write a formula to generate each corner of the grid. 
#These all derive from the fact that the top right corner series is the square of odd integers series. You can
#figure out the other corners in relation to the top right. Here they are simplified as much as reasonable. 
#where n is the length of one side of the grid
#top right corner = n^3
#top left corner = n^2-n+1
#bottom left corner = n^2-2n+2
#bottom right corner = n^2-3n+3
#Add the terms for each corner together and simplify to get this accumulation function.
#O(n) for time and space << better
def arithmatically(n):
    if(n % 2 == 0): raise
    # note that this relies on the fact that the reduce function doesn't apply the lambda to the first argument of the sequence.
    # It uses the first argument as default value. If it applied the lambda initially and used a default of 0, this function would
    # be off by 3 becuase it would count the center cell (which contains a 1) four times - once as each of the four corners
    # of a 1x1 grid
    return functools.reduce(lambda acc, x: acc + 4*x**2 - 6*x + 6, range(1, n+1, 2)) 

#The solution can also be expressed as the sum of the two right corner series times 2, which simplifies into the programmed function
#sum from 1 to n (2(top right corner + bottom right corner)) - 3 <-- again subtract for misleading 1 cell grid
#O(1) for time and space << BEST
def formula(n):
    return (4*n**3 + 3*n**2 + 8*n -9) / 6

a = getSumOfDiagonals(5)
b = arithmatically(5)
c = formula(5)

assert a == 101
assert b == 101
assert c == 101

answer = formula(1001)
assert answer == 669171001
print(answer)
