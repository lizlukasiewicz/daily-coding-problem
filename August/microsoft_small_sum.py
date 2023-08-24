"""
This problem was asked by Microsoft.

Given an array of positive integers, 
divide the array into two subsets 
such that the difference between 
the sum of the subsets is as small as possible.

For example, given [5, 10, 15, 20, 25], 
return the sets {10, 25} and {5, 15, 20}, 
which has a difference of 5, which is the smallest possible difference.
"""
# Partition list `l` into two subsets, `S1` and `S2`,
# def smallest_diff_sum(l:list, n:int, S1=0, S2=0):
#     print(f'\ninput:(n:{n}, S1:{S1}, S2:{S2})')
#     # BASE CASE: if the list becomes empty, 
#     if n<0:
#       # return the absolute difference between both sets
#       print(f'BASE: {abs(S1 - S2)} -- S1:{S1} S2:{S2}')
#       return abs(S1 - S2)
 
#     # Case 1. Include the current item in subset `S1` and recur
#     # for the remaining items `n-1`
#     print(f'✅ include = n:{n-1}, S1:{S1+l[n]}, S2:{S2}')
#     inc = smallest_diff_sum(l, n - 1, S1 + l[n], S2)
 
#     # Case 2. Exclude the current item from subset `S1` and recur for
#     # the remaining items `n-1`
#     print(f'❌ exclude = n:{n-1}, {S1}, S2:{S2+l[n]}')
#     exc = smallest_diff_sum(l, n - 1, S1, S2 + l[n])
#     print(f'output: (inc:{inc}, exc:{exc}) return {min(inc, exc)}')
#     return min(inc, exc)
    
# if __name__ == '__main__':
 
#     # Input: a set of items
#     S = [10, 20, 15, 5, 25]
#     print(f'LIST: {S}')
#     print('The minimum difference is', smallest_diff_sum(S, len(S) - 1))

############################################################################################

# Partition set `S` into two subsets, `S1` and `S2`, such that the
# difference between the sum of elements in `S1` and the sum
# of elements in `S2` is minimized
# def findMinAbsDiff(S, n, S1, S2, lookup):
#     print(f'\nLOOP [{S[n]}] ')
#     # Base case: if the list becomes empty, return the absolute
#     # difference between both sets
#     if n < 0:
#         print(f'RETURN {abs(S1 - S2)} -- abs({S1}-{S2})')
#         return abs(S1 - S2)
 
#     # Construct a unique key from dynamic elements of the input.
#     # Note that we can uniquely identify the subproblem with `n` and `S1` only,
#     # as `S2` is nothing but `S-S1`, where `S` is the sum of all elements

#     key = (n, S1)
#     print(f'KEY: (n:{n}, S1:{S1})')
 
#     # If the subproblem is seen for the first time, solve it and
#     # store its result in a dictionary
#     if key not in lookup:
 
#         # Case 1. Include the current item in subset `S1` and recur
#         # for the remaining items `n-1`
#         print(f'🦋 S1(include): [{S[n]}]  S1:{S1} == {S1+S[n]}\t 🍄 S2(exclude) [{S[n]}] S2:{S2} == {S2 + S[n]}')
#         inc = findMinAbsDiff(S, n - 1, S1 + S[n], S2, lookup)
 
#         # Case 2. Exclude the current item from subset `S1` and recur for
#         # the remaining items `n-1`
#         exc = findMinAbsDiff(S, n - 1, S1, S2 + S[n], lookup)
 
#         lookup[key] = min(inc, exc)
#     else:
#         print(f'\t🪐🪐🪐🪐🪐🪐🪐 key {key} in lookup {lookup[key]}')
#     return lookup[key]
 
 
# if __name__ == '__main__':
 
#     # Input: a set of items
#     S = [10, 20, 15, 5, 25]
#     print(f'{S}')
#     # create a dictionary to store solutions to subproblems
#     lookup = {}
 
#     print('The minimum difference is', findMinAbsDiff(S, len(S) - 1, 0, 0, lookup))

############################################################################################
############################################################################################
def findMinAbsDiff(S):
 
    # Find the sum of all elements
    total = sum(S)
 
    # Create a boolean table to store solutions to subproblems
    T = [[False] * (total + 1) for _ in range(len(S) + 1)]
    print(f'TOTAL: {total} \n')
 
    # Fill the lookup table in a bottom-up manner
    for i in range(len(S) + 1):
        print(f'\n\t[{i}] LOOP ')
 
        # elements with zero-sum are always true
        print(f'\tT[{i}][0] == True')
        T[i][0] = True
 
        j = 1
        while i > 0 and j <= total:
            print(f'\t\t 🐚 T[{i}][{j}] == T[{i-1}][{j}]')
            # exclude the i'th element
            T[i][j] = T[i - 1][j]
 
            # include the i'th element
            if S[i - 1] <= j:
                print(f'\t\t\t {S[i - 1]} <= j[{j}]\n\t\t\t T[{i}][{j}] |= T[{i-1}][{j} - {S[i-1]}]')
                T[i][j] |= T[i - 1][j - S[i - 1]]
                print(f'\t\t\t{T[i][j]}')
 
            j = j + 1
 
    # Find the maximum value of `j` between 0 and `sum/2` for which the
    # last row is true
    j = total // 2
    while j >= 0 and not T[len(S)][j]:
        j = j - 1
 
    return total - 2*j

if __name__ == '__main__':
 
    # Input: a set of items
    S = [10, 20, 15, 5, 25]
    print(f'{S}')
 
    print('The minimum difference is', findMinAbsDiff(S))