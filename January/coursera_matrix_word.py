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
# loop through the arrays for the first character of the string, return the index # for 

# then 
x = 10
y = 2
#print(x<<y)
# 👾 print(x*(2**y))

#print(x>>y)
# 👾 print(x//(2**y))

#print(y<<x)
# 👾 print(y*(2**x))

#print(y>>x)
# 👾 print(y//(2**x))

print(x&y, " = 10 & 2")
print(x|y, " = 10 | 2")
print(~x, "= ~10  same as -10 - 1")
print(x^y, " = 10 ^ 2")

print(2**10)