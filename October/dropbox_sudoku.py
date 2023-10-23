"""
This problem was asked by Dropbox.

Sudoku is a puzzle where you're given 
a partially-filled 9 by 9 grid with digits. 
The objective is to fill the grid with the constraint 
that every row, column, and box (3 by 3 subgrid) must contain all of the digits from 1 to 9.

Implement an efficient sudoku solver.

"""
def sudoku_solver(grid):
  possible_nums={ x:'num' for x in range(1,10)}
  
  # function that scans 3x3 grid

    # function to loop through vertical rows

    # function to loop through horizontal rows

easy_sudoku=[
  [1,5,0, 0,2,3, 9,0,0],
  [0,0,2, 0,5,0, 0,0,6],
  [8,0,9, 0,0,4, 3,2,0],
  
  [5,4,1, 9,7,0, 6,3,8],
  [0,0,0, 1,8,0, 0,0,2],
  [7,2,8, 4,3,0, 1,5,0],
  
  [0,9,0, 5,0,8, 0,0,0],
  [0,8,0, 2,4,0, 5,9,0],
  [2,1,5, 3,0,0, 0,6,4],


]