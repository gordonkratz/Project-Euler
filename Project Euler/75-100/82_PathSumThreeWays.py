import functools, MatrixTools as mx

testInput = [
        [131, 201, 630, 537, 805],
        [673, 96, 803, 699, 732], 
        [234, 342, 746, 497, 524],
        [103, 965, 422, 121, 37], 
        [18, 150, 111, 956, 331]
    ]

answer = mx.FindShortestHorizontalPath(mx.ReadMatrix("p082_matrix.txt"))
print(answer)
assert answer == 260324