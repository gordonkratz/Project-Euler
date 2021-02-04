from enum import IntFlag
import functools, networkx as nx, itertools

def ReadMatrix(fileName):
    file = open(fileName, "r")
    input = list()
    for line in file.readlines():
        nums = line.strip().split(",")
        for i in range(len(nums)):
            n = int(nums[i])
            if(len(input) <= i):
                input.append([n])
            else:
               input[i].append(n)
    return input

class Direction(IntFlag):
    Unknown = 0
    Right = 1
    Left = 1 << 1
    Up = 1<<2
    Down = 1<<3
    Two = Right | Down
    Three = Right | Up | Down
    All = Right | Left | Up | Down

def CreateGraph(input, directions: Direction):
    gr = nx.MultiDiGraph()
    for x in range(len(input)):
        for y in range(len(input)):
            node = (x, y)
            #add right
            if(directions & Direction.Right and x < len(input)-1):
                gr.add_edge(node, (x+1, y), weight=input[x+1][y])
            #add left
            if(directions & Direction.Left and x > 0):
                gr.add_edge(node, (x-1, y), weight=input[x-1][y])
            #add down
            if(directions & Direction.Down and y < len(input)-1):
                gr.add_edge(node, (x, y+1), weight=input[x][y+1])
            #add up
            if(directions & Direction.Up and y > 0):
                gr.add_edge(node, (x, y-1), weight=input[x][y-1])
    return gr

def Accumulate(path, input):
    return functools.reduce(lambda acc, node: acc + input[node[0]][node[1]], path, 0)

def FindShortestPathSum(input, directions: Direction):
    gr = CreateGraph(input, directions)
    path = nx.algorithms.shortest_paths.weighted.dijkstra_path(gr, (0,0), (len(input)-1, len(input)-1))
    return Accumulate(path, input)

def ShortestPathMulti(graph, input, yTarget):
    path = nx.algorithms.shortest_paths.weighted.multi_source_dijkstra(graph, [(0, i) for i in range(len(input))], (len(input)-1, yTarget))
    return Accumulate(path[1], input)

def FindShortestHorizontalPath(input):
    gr = CreateGraph(input, Direction.Three)
    return min(map(lambda i: ShortestPathMulti(gr, input, i), range(len(input))))