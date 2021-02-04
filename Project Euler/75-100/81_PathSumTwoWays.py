import MatrixTools as mx

testInput = [
        [131, 201, 630, 537, 805],
        [673, 96, 803, 699, 732], 
        [234, 342, 746, 497, 524],
        [103, 965, 422, 121, 37], 
        [18, 150, 111, 956, 331]
    ]

assert mx.FindShortestPathSum(testInput, mx.Direction.Two) == 2427

answer = mx.FindShortestPathSum(mx.ReadMatrix("p081_matrix.txt"), mx.Direction.Two)
print(answer)
assert answer == 427337