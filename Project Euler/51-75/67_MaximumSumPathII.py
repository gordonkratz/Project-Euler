import TrianglePathFinder

f = open("p067_triangle.txt", "r")

answer = TrianglePathFinder.TraverseTriangle(f.readlines())
print(answer)
assert answer == 7273