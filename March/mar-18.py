"""
This problem was asked by Jane Street.

Given an arithmetic expression in Reverse Polish Notation, write a program to evaluate it.

The expression is given as a list of numbers and operands. 
For example: [5, 3, '+'] should return 5 + 3 = 8.

For example, 
[15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] 
should return 5, since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.

You can assume the given expression is always valid.

"""
from math import trunc


def łukasiewicz(list):
    stack=[]
    for i in list:
        if i not in {"+", "-", "*", "/"}:
            stack.append(int(i))
            print(stack, "👁‍🗨")
        else:
            b, a = stack.pop(), stack.pop()
            if i =="+":
                stack.append(a + b)
                print(stack, "🦋") 
            elif i == "-": 
                stack.append(a-b)
                print(stack, "🍄")
            elif i == "*":
                stack.append(a * b)
                print(stack, "🌚") 
            else:
                stack.append(trunc(a /b))
                print(stack, "🥑")
    print(stack[0])



test1=[5, 3, '+']
test2=[15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']
łukasiewicz(test2)