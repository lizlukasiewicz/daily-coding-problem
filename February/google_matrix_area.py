"""
This question was asked by Google.

Given an N by M matrix consisting only of 1's and 0's, 
find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

[[1, 0, 0, 0],
 [1, 0, 1, 1],
 [1, 0, 1, 1],
 [0, 1, 0, 0]]
Return 4.
"""
def max_area(m: list):
    highest=0
    track=[0*len(m)]

test_matrix=[[1, 0, 0, 0],
            [1, 0, 1, 1],
            [1, 0, 1, 1],
            [0, 1, 0, 0]]