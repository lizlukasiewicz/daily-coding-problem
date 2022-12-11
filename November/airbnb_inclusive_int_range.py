"""

This problem was asked by Airbnb.

Given an array of integers, return the largest range, inclusive, 
of integers that are all included in the array.

For example, given the array [9, 6, 1, 3, 8, 10, 12, 11], 
return (8, 12) since 8, 9, 10, 11, and 12 are all in the array.

"""

def largest_inclusive(arr):
    #ans=list()
    inclusive=[]
    stk=[]
    for i, num in enumerate(sorted(arr)[::-1]):
        if stk and int(stk[-1]-num)==1:
            inclusive.append(stk[-1])
            stk.pop()
            inclusive.append(num)
        stk.append(num)
        print(f'i:{i} num:{num} stk:{stk}')
    #ans=tuple(ans)
    print(f'ans::{min(inclusive), max(inclusive)}')

nums=[9, 6, 1, 3, 8, 10, 12, 11]
largest_inclusive(nums)