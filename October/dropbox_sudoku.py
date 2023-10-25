"""
This problem was asked by Dropbox.

Sudoku is a puzzle where you're given 
a partially-filled 9 by 9 grid with digits. 
The objective is to fill the grid with the constraint 
that every row, column, and box ('3' by 3 subgrid) must contain all of the digits from 1 to 9.

Implement an efficient sudoku solver.

"""
from collections import defaultdict
class Solution:
    def solveSudoku(self, board):

        def could_place(d, row, col):
            """
            Check if one could place a number d in (row, col) cell
            """
            # d in rows[row] or d in columns[col] or d in boxes[box_index(row, col)]
            return not (d in rows[row] or d in columns[col] or \
                    d in boxes[box_index(row, col)])
        
        def place_number(d, row, col):
            """
            Place a number d in (row, col) cell
            """
            rows[row][d] += 1
            columns[col][d] += 1
            boxes[box_index(row, col)][d] += 1
            # print(f'rows[{row}][{d}]=={rows[row][d]} \t columns:[{col}][{d}]=={columns[col][d]} \tboxes[{box_index(row, col)}][{d}]\t board[{row}][{col}]=={d}')
            board[row][col] = str(d)
            
        def remove_number(d, row, col):
            """
            Remove a number which didn't lead 
            to a solution
            """
            del rows[row][d]
            del columns[col][d]
            del boxes[box_index(row, col)][d]
            board[row][col] = '.'    
            
        def place_next_numbers(row, col):
            """
            Call backtrack function in recursion
            to continue to place numbers
            till the moment we have a solution
            """
            # if we're in the last cell
            # that means we have the solution
            if col == N - 1 and row == N - 1:
                nonlocal sudoku_solved
                sudoku_solved = True
            #if not yet    
            else:
                # if we're in the end of the row
                # go to the next row
                if col == N - 1:
                    backtrack(row + 1, 0)
                # go to the next column
                else:
                    backtrack(row, col + 1)
                
                
        def backtrack(row = 0, col = 0):
            """
            Backtracking
            """
            # if empty
            if board[row][col] == '.':
                # iterate over all numbers from 1 to 9
                for d in range(1, 10):
                    if could_place(d, row, col):
                        place_number(d, row, col)
                        place_next_numbers(row, col)
                        # if sudoku is solved, there is no need to backtrack
                        # since the single unique solution is promised
                        if not sudoku_solved:
                            remove_number(d, row, col)
            else:
                place_next_numbers(row, col)
                    
        # box size
        n = 3
        # row size
        N = n * n
        # lambda function to compute box index
        box_index = lambda row, col: (row // n ) * n + col // n
        
        # init rows, columns and boxes
        rows = [defaultdict(int) for i in range(N)]
        columns = [defaultdict(int) for i in range(N)]
        boxes = [defaultdict(int) for i in range(N)]

        for i in range(N):
            for j in range(N):
                if board[i][j] != '.': 
                    d = int(board[i][j])
                    place_number(d, i, j)
        
        sudoku_solved = False
        backtrack()
# def sudoku_solver(grid):
#   possible_nums={ x:'num' for x in range(1,10)}
#   # function that scans 3x3 grid

#     # function to loop through vertical rows
#   def vertical(x_start):
#     nums_needed=possible_nums
#     for y in range(9):
#       if grid[y][x_start] in possible_nums:
#         print(f'grid[{y}][{x}]=={grid[y][x_start]}')
#         del nums_needed[grid[y][x_start]]
#     return nums_needed
  
#   for x in range(9):
#     print(f'needed in column {x}: {vertical(x)}')


    # function to loop through horizontal rows


if __name__ == '__main__':

  easy_sudoku=[
    ['1','5','.', '.','2','3', '9','.','.'],
    ['.','.','2', '.','5','.', '.','.','6'],
    ['8','.','9', '.','.','4', '3','2','.'],
    
    ['5','4','1', '9','7','.', '6','3','8'],
    ['.','.','.', '1','8','.', '.','.','2'],
    ['7','2','8', '4','3','.', '1','5','.'],
    
    ['.','9','.', '5','.','8', '.','.','.'],
    ['.','8','.', '2','4','.', '5','9','.'],
    ['2','1','5', '3','.','.', '.','6','4'],
  ]
  hard_sudoku=[
    ['.','.','2', '.','.','.', '.','.','4'],
    ['.','7','9', '.','.','.', '6','8','.'],
    ['.','3','8', '.','.','.', '.','1','.'],
    
    ['.','1','3', '.','7','2', '.','.','8'],
    ['.','.','.', '9','.','1', '.','4','.'],
    ['2','.','.', '.','.','8', '1','.','7'],
    
    ['.','4','.', '.','.','.', '.','.','.'],
    ['7','.','.', '.','.','.', '.','.','.'],
    ['8','9','1', '.','6','5', '.','.','.'],
  ]
  game= Solution()
  game.solveSudoku(easy_sudoku)
  print(f'solution:\n')
  for row in easy_sudoku:
      print(row)
  # game.solveSudoku(hard_sudoku)
  # print(f'\n\n')
  # for r in hard_sudoku:
  #     print(r)
  # sudoku_solver(easy_sudoku)