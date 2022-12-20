"""
This problem was asked by Amazon.

Given a pivot x, and a list lst, partition the list into three parts.

The first part contains all elements in lst that are less than x
The second part contains all elements in lst that are equal to x
The third part contains all elements in lst that are larger than x
Ordering within a part can be arbitrary.

For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may be [9, 3, 5, 10, 10, 12, 14].
"""
def partition_pivot1(x, lst):
    pivot=[]
    less=[num for num in lst if num < x]
    eq=[n for n in lst if n==x]
    great=[g for g in lst if g>x]
    print(f'{less} | {eq} | {great}')



testx = 10
testlst = [9, 12, 3, 5, 14, 10, 10]
partition_pivot1(testx, testlst)