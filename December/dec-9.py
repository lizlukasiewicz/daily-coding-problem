"""
Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
You should print out the following:

1
2
3
4
5
"""
def spiral(matrix):
    ans = []
    if(len(matrix)==0):
        return ans
    row = len(matrix)
    column = len(matrix[0])
    seen = [[0 for i in range(column)] for j in range(row)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r = 0
    c = 0
    direction = 0
    # iterate from 0 to row * column - 1
    for i in range(row * column):
        ans.append(matrix[r])
        seen[r]=True
        cr =r + dr[direction]
        cc = c + dc[direction]
        if (0 <= cr and cr < row and 0 <= cc and cc < column and not(seen[cr][cc])):
            row = cr
            column = cc
        else:
            direction = (direction + 1) % 4
            row += dr[direction]
            column += dc[direction]
    return ans

test = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

for x in spiral(test):
    print(x, end=" ")
print()
