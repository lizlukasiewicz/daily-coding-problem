"""
This problem was asked by Microsoft.

A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
"""

def perfection(num):
    if (num > 0 and num < 10):
        second_half = 10-num
        s_num = str(num)
        s_half = str(second_half)
        print(s_num + s_half)
    else:
        print("Idk what to do with this edge case")

perfection(1)