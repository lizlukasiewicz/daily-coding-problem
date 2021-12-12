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
    startRow = 0  # k
    startCol = 0  # l
    endRow = len(matrix) # m
    endCol = len(matrix[0]) # n
    while (startRow < endRow and startCol < endCol):
        #print first row from remaining row
        for i in range(startCol, endCol):
            print(matrix[startRow][i], end=" ")
        
        startRow+=1
        #print last column from remaining columns
        for i in range(startRow, endRow):
            print(matrix[i][endCol - 1], end=" ")
        endCol-=1
        #print last row from remaining rows
        if (startRow < endRow):
            for i in range(endCol - 1, (startCol - 1), -1):
                print(matrix[endRow - 1][i], end=" ")
            endRow-=1
        #print first col from remaining columns
        if (startCol < endCol):
            for i in range(endRow - 1, startRow - 1, -1):
                print(matrix[i][startCol], end=" ")
            startCol+=1

    

test = [[1, 2, 3, 4], 
        [5, 6, 7, 8], 
        [9, 10, 11, 12], 
        [13, 14, 15, 16]]
spiral(test)