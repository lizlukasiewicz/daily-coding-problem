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


def matrix_steps(steps, board):
    #step= (column, row)
    
    # def get_neighbors(row, col):
    #     for row_diff, col_diff in steps:
    #         new_row=row+row_diff
    #         new_col=col+col_diff
    #         if not (0 <= new_row <= max_row and 0 <= new_col <= max_col):
    #             continue
    #         yield (new_row, new_col)
    for i in range(len(steps)-1):
        next_step=steps[i+1]
        current=steps[i]
        # if abs(next_step[0]-current[0])<=1 or abs(next_step[1]-current[1])<=1:
        board[current[0]][current[1]]=1
        board[next_step[0]][next_step[1]]=1
        # else:
        #     print(f'cannot step more than 1')
        # next_s=steps[i+1]# (1, 1)
        # step= 1 if abs(next_s[0]-current[0])==1 or abs(next_s[1]-current[1])==1 else 0
        # if step>0:
    print('new board:')
    for row in board:
        print(row)


#calculate 
t_board=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
test = [(0, 0), (1, 1), (1, 2)]
test2=[(0, 0), (0, 1), (0, 2), (1, 2)]
matrix_steps(test, t_board)
matrix_steps(test2, t_board)