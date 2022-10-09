"""
This problem was asked by Lyft.

Given a list of integers and a number K, 
return which contiguous elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, 
then it should return [2, 3, 4], since 2 + 3 + 4 = 9.
"""





def sumofK(array, k):
    longest_sub=list()#current_sub=longest_sub=[array[0]]
    for i in range(len(array)):
        current=[array[i]]
        for next in array[i+1:]:
            current.append(next)
            if sum(current)==k:
                s_current=[str(s) for s in current]
                longest_sub = s_current if len(s_current) > len(longest_sub) else longest_sub
    print([int(n) for n in longest_sub])

"""

"""



test = [1, 2, 3, 4, 5]
goal = 9
sumofK(test, goal)