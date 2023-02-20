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
    # print(f'arr: {arr}')
    dis={}
    m_count=0
    left=0
    for right in range(len(arr)):
        # print(f'current:({right}){arr[right]}')
        while arr[right] in dis:
            # print(f'({left}){arr[left]}--({right}){arr[right]} in {dis}')
            dis[arr[left]]-=1
            if dis[arr[left]]==0:
                del dis[arr[left]]
            left+=1
        
        dis[arr[right]]= dis.get(arr[right], 0)+1

        m_count=max(m_count, right-left+1)
    # print(f'max count:{m_count}')
    return m_count

testarr=[5, 1, 3, 5, 2, 3, 4, 1]
destinct_subarray(testarr)