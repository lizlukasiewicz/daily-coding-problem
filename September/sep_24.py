"""
This problem was asked by Yahoo.

You are given a string of length N and a parameter k. 
The string can be manipulated by taking one of 
the first k letters and moving it to the end.

Write a program to determine the lexicographically smallest string 
that can be created after an unlimited number of moves.

For example, suppose we are given the string 'daily' and k = 1. 
The best we can create in this case is ailyd.

"""
# def algo_string(n, k):
#     lex=[]


# ex_string='daily'
# ex_k=1

"""
Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
 
"""
arr1 = [1,2,3,4,5]
k1 = 4 
x1 = 3
arr2 = [1,2,3,4,5] 
k2 = 4 
x2 = -1
def findClosestElements(arr, k, x):
        sorted_arr= sorted(arr, key = lambda num: abs(num-x))
        result=[]
        for i in range(k+1):
            print(f'🎺 x:{x}  - i:{i}) i after sorted_arr:{sorted_arr[i]}')
            result.append(sorted_arr[i])
        print(f'🎯 {result}')
        return sorted(result)

# findClosestElements(arr1, k1, x1)
# findClosestElements(arr2, k2, x2)



def maxSubArray(nums):
    current_subarray = max_subarray = nums[0]
    print(f'🏁  start: cur:{current_subarray} max:{max_subarray} nums:{nums[0]}')
    for num in nums[1:]:
        print(f'✅ cur:{current_subarray} max:{max_subarray} currentval:{num}')
        current_subarray=max(num, current_subarray + num)
        print(f'🌞 cur:{current_subarray} max:{max_subarray}')
        max_subarray=max(max_subarray, current_subarray)
        print(f'🍄 cur:{current_subarray} max:{max_subarray}')
    return max_subarray

ex1=[-2,1,-3,4,-1,2,1,-5,4]
maxSubArray(ex1)
