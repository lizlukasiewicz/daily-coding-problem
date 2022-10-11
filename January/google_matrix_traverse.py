"""
This problem was asked by Google.

You are in an infinite 2D grid where you can move in any of the 8 directions:

 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)
You are given a sequence of points and the order in which you need to cover the points. 
Give the minimum number of steps in which you can achieve it. You start from the first point.

Example:

Input: [(0, 0), (1, 1), (1, 2)]
Output: 2
It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).
"""


def matrix_steps(steps):
    #step= (column, row)
    first=steps[0]
    last=steps[-1]
    m_count=max(abs(first[0]-last[0]), abs(first[1]-last[1]))

    print(f'min steps:{m_count}')


#calculate 

test = [(0, 0), (1, 1), (1, 2)]
test2=[(0, 0), (0, 1), (0, 2), (1, 2)]
test3=[(5, 5), (4, 4), (3, 4), (3, 3), (3, 5)]
test4=[(3, 3), (3, 4), (2, 4), (1, 4), (0, 5)]
matrix_steps(test)
matrix_steps(test2)
matrix_steps(test3)
matrix_steps(test4)