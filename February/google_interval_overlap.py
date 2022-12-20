"""
This problem was asked by Google.

Given a set of closed intervals, 
find the smallest set of numbers that covers all the intervals. 
If there are multiple smallest sets, return any of them.

For example, 
given the intervals [0, 3], [2, 6], [3, 4], [6, 9], 
one set of numbers that covers all these intervals is {3, 6}.
"""
def solution(list):
    new = set((list[0][0], list[0][1]))
    for item in list[1:]:
        item[0]
    #     for num in set:
    #         new.append(num)
    # #print(new)
    # ans = max(new, key=new.count())
    # print(ans)

test = [[0, 3], [2, 6], [3, 4], [6, 9]]
solution(test)