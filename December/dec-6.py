"""
This problem was asked by Facebook.

There is an N by M matrix of zeroes. 
Given N and M, write a function to count the number of ways of 
starting at the top-left corner and getting to the bottom-right corner. 
You can only move right or down.

For example, given a 2 by 2 matrix, 
you should return 2, since there are two ways to get to the bottom-right:
Right, then down
Down, then right

Given a 5 by 5 matrix, 
there are 70 ways to get to the bottom-right. (8 moves needed to get from top right to bottom left)
x x x x x
x x x x x
x x x x x
x x x x x
x x x x x
"""
import math
# math.comb (n, k) # of possible combinations of k things from n items
# math.comb( of 8 things, from 25 items)
print('2x2 combo is ', math.comb(2, 1))
print('5x5 combo is', math.comb(8, 4))
# 
# moves = n * m -2 (2 because the first and last move)
# 
# math.comb(2 things from 4 items) 