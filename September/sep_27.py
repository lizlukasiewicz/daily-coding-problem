"""
This problem was asked by Palantir.

A typical American-style crossword puzzle grid is an N x N matrix with black and white squares, 
which obeys the following rules:

Every white square must be part of an "across" word and a "down" word.
No word can be fewer than three letters long.
Every white square must be reachable from every other white square.
The grid is rotationally symmetric 
(for example, the colors of the top left and bottom right squares must match).
Write a program to determine whether a given matrix qualifies as a crossword grid.

"""

def crossword_check(crossword):
    # valid=False
    # if len(crossword) == len([w_row for w_row in crossword]):
    #     # forward=[row for row in crossword]
    #     # backward=[r_row[::-1] for r_row in crossword[::-1]]
    #     for thing, rev in zip([row for row in crossword], [r_row[::-1] for r_row in crossword[::-1]]):
    #         rev=list(reversed(rev))
    #         for x, y in zip(thing, rev):
    #             valid=True if x==y else False
    #     print(f'rotational results: {valid}')
        # if valid:
    i=0
    current_whitespace=0
    next_zero=lambda cross: cross.index(0)
    while i < len(crossword):
        print(f'({len(crossword[i:])})current:{crossword[i:]}')#[i][current_whitespace:]}')
        current_whitespace=len(crossword[:next_zero(crossword[i:])])#[i][:next_zero(crossword[i:])])
        print(f'current_whitespace: {current_whitespace} length of:{crossword[i:next_zero(crossword[i:])+i]}')
        current_whitespace+=1
        i+=current_whitespace
        print(f'(i={i}, ws={current_whitespace}) next: {crossword[i:]}')#[i][:current_whitespace]}')
                
                # print(f'lambda1:: {crossword[i][:zero(crossword[i])]}')
                # middle=crossword[i][zero(crossword[i])+1:]
                # print(f'middle:{middle} ')
                # print(f'lambda3: {crossword[i][zero(middle):]}')
                
            #print(f'whitespace result: {valid}')
        # divide=len(crossword)//2
        # top_l=[row[:divide] for row in crossword[:divide]]
        # bottom_r=[b_row[-divide:] for b_row in crossword[-divide:]]
        # for top, bottom in zip([row[:divide] for row in crossword[:divide]], [b_row[-divide:] for b_row in crossword[-divide:]]):
        #     bottom=list(reversed(bottom))
        #     #print(f'{top} == {bottom}')
        #     for t, b in zip(top, bottom):
        #         valid=True if t==b else False

        # if [row[:divide] for row in crossword[:divide]] == [b_row[-divide:] for b_row in crossword[-divide:]]:
        #     valid=True
        # for item in top_l:
        #     print(f'top left:{item}')
        # for y in bottom_r:
        #     print(f'bottom right:{list(reversed(y))}')
    # print(valid)
loop_ex=[1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1]
crossword_check(loop_ex)
# ex_cross_odd=[
#         [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
#         [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
#         [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0],
#         [0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
#         [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
#         [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0],
#         [0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
#         [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
#         [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1]
#         ]
# ex_cross_even=[
#         [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
#         [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0],
#         [0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
#         [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
#         [1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0],
#         [0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
#         [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1]
# ]
# print('odd crossword: ')
# crossword_check(ex_cross_odd)
# print('even crossword: ')
# crossword_check(ex_cross_even)