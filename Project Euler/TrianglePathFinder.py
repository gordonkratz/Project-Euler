import functools


class Node:
    def __init__(self, value):
        self.Value = value
        self.Weight = 0

    def __str__(self):
        return str(self.Value) + "(" + str(self.Weight) + ")"

def ProcessInput(lines):
    nodeList = []
    for line in lines:
        nodeArray = []
        for num in line.split(" "):
            nodeArray.append(Node(int(num)))
        nodeList.append(nodeArray)
    return nodeList

def FindMaxWeight(nodeList):
    #traverse to find max weight
    maxWeight = 0
    for i in range(len(nodeList)):
        for j in range(len(nodeList[i])):
            currentNode = nodeList[i][j]
            leftWeight = nodeList[i-1][j-1].Weight if i > 0 and j > 0 else 0
            rightWeight = nodeList[i-1][j].Weight if i > 0 and j < len(nodeList[i-1]) else 0
            currentNode.Weight = max(leftWeight, rightWeight) + currentNode.Value
            maxWeight = max(maxWeight, currentNode.Weight)
    return maxWeight

def TraverseTriangle(lines):
    return FindMaxWeight(ProcessInput(lines))
