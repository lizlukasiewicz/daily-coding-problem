"""
This problem was asked by Facebook.

Given a multiset of integers, 
return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, 
it would return true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, 
it would return false, since we can't split it up into two subsets that add up to the same sum.

"""
# n = len(thisSet) 

def isSubset(arr, n, sum):
    if sum ==0:
        return True
    if n == 0 and sum !=0:
        return False
    if arr[n-1]> sum:
        return isSubset(arr, n-1, sum)
    return isSubset(arr, n-1, sum) or isSubset(arr, n-1, sum-arr[n-1])

def findPartition(arr, n):
    sum = 0
    for num in arr:
        sum += num
    if sum % 2 != 0:
        return False
    return isSubset(arr, n, sum // 2)

arr = ((15, 5, 20, 10, 35))
n = len(arr)

if findPartition(arr, n) ==True:
    print("can be divided into two subsets of equal sum")
else:
    print("cannot be divided into two subsets of equal sum")