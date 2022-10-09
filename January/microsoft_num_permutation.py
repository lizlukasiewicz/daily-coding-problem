"""

Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Given a number in the form of a list of digits, return all possible permutations.

For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
import itertools
def possibilities(array):
    poss = itertools.permutations(array)
    ans = list(poss)
    print(ans)
#     answer = []
#     if len(array)== 0:
#         return answer
#     if len(array) == 1:
#         return [array]
#     # loop through each index of the array
#     for i in range(len(array)):
#         # at each index, initialize a new array to push 
#         round = []
#         round.append(array[i])
#         # first push the index were currently on
#         # followed by a loop through the next two 
#         # if index
# data = list('123')
# for p in possibilities(data):
#     print(p)
test = [1, 2, 3]
possibilities(test)

def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i]==0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return
# permutations(test)