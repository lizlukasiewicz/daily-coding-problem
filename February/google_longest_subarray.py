"""

This problem was asked by Google.

Given an array of elements, 
return the length of the longest subarray 
where all its elements are distinct.

For example, 
    given the array [5, 1, 3, 5, 2, 3, 4, 1], 
    return 5 as the longest subarray of distinct elements 
    is [5, 2, 3, 4, 1].

"""
def destinct_subarray(arr: list):
    dis={}
    m_count=0
    left=0
    for right in range(len(arr)):
        

        while arr[right] in dis:
            left+=1
        dis[arr[right]]



        m_count=max(m_count, right-left+1)