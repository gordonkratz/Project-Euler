import networkx as nx, functools

testInput = [
        [131, 201, 630, 537, 805],
        [673, 96, 803, 699, 732], 
        [234, 342, 746, 497, 524],
        [103, 965, 422, 121, 37], 
        [18, 150, 111, 956, 331]
    ]

def FindShortestPathSum(input):
    gr = nx.MultiDiGraph()
    for x in range(len(input)):
        for y in range(len(input)):
            node = (x, y)
            #add right
            if(x < len(input)-1):
                gr.add_edge(node, (x+1, y), weight=input[x+1][y])
            #add left
            if(x > 0):
                gr.add_edge(node, (x-1, y), weight=input[x-1][y])
            #add down
            if(y < len(input)-1):
                gr.add_edge(node, (x, y+1), weight=input[x][y+1])
            #add up
            if(y > 0):
                gr.add_edge(node, (x, y-1), weight=input[x][y-1])
    path = nx.algorithms.shortest_paths.weighted.dijkstra_path(gr, (0,0), (len(input)-1, len(input)-1))
    return functools.reduce(lambda acc, node: acc + input[node[0]][node[1]], path, 0)

assert FindShortestPathSum(testInput) == 2297


file = open("p083_matrix.txt", "r")
input = list()
for line in file.readlines():
    nums = line.strip().split(",")
    for i in range(len(nums)):
        n = int(nums[i])
        if(len(input) <= i):
            input.append([n])
        else:
           input[i].append(n)

answer = FindShortestPathSum(input)
print(answer)
assert answer == 425185