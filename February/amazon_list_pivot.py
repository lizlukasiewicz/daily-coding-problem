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
    print(x, lst)
    #initialize empty array
    # loop through array if item is less than x pop it out and append to new array
    # loop through array if item is equal to x pop it out and append to new array
    # append last items to new array

def partition_pivot2(x, lst):
    # enumerate through array 
    print(x)

testx = 10
testlst = [9, 12, 3, 5, 14, 10, 10]