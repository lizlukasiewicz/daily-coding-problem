"""
Given a list of integers, write a function that returns 
the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. 
[5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""
# NOT ACCOUNTING FOR EDGE CASES:
def largestSum(array):
    even=[]
    odd=[]
    #reverse loop through the array
    for i, num in reversed(list(enumerate(array))):
# split into 2 arrays depending on even or odd indices
        if i % 2 == 0:
            even.append(num)
            array.pop(i)
        else:
            odd.append(num)
            array.pop(i)
    evenSum=0
    oddSum=0
    total=[]
# find the sum of each individual array 
    for n in even:
        evenSum = evenSum + n
    total.append(evenSum)
    for m in odd:
        oddSum = oddSum + m
    total.append(oddSum)
# the largest sum gets returned as the answer
    print(max(total))
largestSum([2, 4, 6, 2, 5])

# EDGE CASES
#def edgeLargeSum(array):
    # if length of array is less than 4
    #reverse loop through array
    # take every other index number
    # find sum
    #if length of array is 4 or more
    # 

#could it be done with binary tree??
# if the index of the num in the array is not == +1 or -1 current node
# add value as a leaf