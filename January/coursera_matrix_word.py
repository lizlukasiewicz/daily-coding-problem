"""
This problem was asked by Coursera.

Given a 2D board of characters and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

For example, given the following board:

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, exists(board, "ABCB") returns false.
"""
def exists(board, string):
  max_row=len(board)
  max_col=len(board[0])
  start_options=[]
  start_letter=string[0]
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j]==start_letter:
        start_options.append((i, j))
  print(start_options)

  def get_neighbours(row, col, next_letter):
    print(f'get_neighbors({next_letter}  , row:{row}, col:{col})')
    directions = [(-1, 0),(0, -1),(0, 1), (1, 0),]
    for row_diff, col_diff in directions:
      new_row=row+row_diff
      new_col=col+col_diff
      if (new_row>max_row or 0>new_row) and (new_col>max_col or 0>new_col):
          continue
      if board[new_row][new_col] != next_letter:
          continue
      print(f'new_row:{new_row}, new_col:{new_col}')
      yield (new_row, new_col)

  
  for start_row, start_col in start_options:
    next_row=start_row
    next_col=start_col

    for x in range(len(string)-1):
      current_letter=string[x]
      next_letter=string[x+1]
      print(f'current_letter:{current_letter} next_letter:{next_letter}')
      #neighbors=[]
      for neighbor_row, neighbor_col in get_neighbours(next_row, next_col, next_letter):
        #neighbors.append(board[neighbor_row][neighbor_col])
        if board[neighbor_row][neighbor_col]==next_letter:
          next_row, next_col=neighbor_row, neighbor_col
          continue
        
          # print('FALSE')
    return False
        
        #print(f'letter:{letter} neighbors:{board[neighbor_row][neighbor_col]}')


  

test_board=[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E'],
  ['Z','Z','Z','Z']
]
test_string="ABCCED"
test_string2="SEE"
test_string3="ABCB"
exists(test_board,test_string)
exists(test_board,test_string2)
exists(test_board,test_string3)