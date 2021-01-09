input = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
import functools


class Node:
    def __init__(self, value):
        self.Value = value
        self.Weight = 0

    def __str__(self):
        return str(self.Value) + "(" + str(self.Weight) + ")"

graph = []

#process input
for line in input.splitlines():
    nodeArray = []
    for num in line.split(" "):
        nodeArray.append(Node(int(num)))
    graph.append(nodeArray)

#traverse to find max weight
maxWeight = 0
for i in range(len(graph)):
    for j in range(len(graph[i])):
        currentNode = graph[i][j]
        leftWeight = graph[i-1][j-1].Weight if i > 0 and j > 0 else 0
        rightWeight = graph[i-1][j].Weight if i > 0 and j < len(graph[i-1]) else 0
        currentNode.Weight = max(leftWeight, rightWeight) + currentNode.Value
        maxWeight = max(maxWeight, currentNode.Weight)
    print()

print(maxWeight)

assert(maxWeight == 1074)