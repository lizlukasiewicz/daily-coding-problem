"""
This problem was asked by Microsoft.

Given an unsorted array of integers, 
find the length of the longest consecutive elements sequence.

For example, given [100, 4, 200, 1, 3, 2], 
the longest consecutive element sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.


"""
from collections import defaultdict
import sys

def consecutiveElements(list):
    a = set(list)
    longest = 0
    for i in a:
        if i-1 not in a:
            #current = i
            streak = 0
            while i in a:
                i+=1
                streak+=1
                longest = max(longest, streak)
    print(longest)
#sort the array 
    #list.sort()
    #print(list)
    # enumerate the sorted list
    #count = 0
    #for i, val in enumerate(list):
        #print(f'value: {val}')
        #print(f'value:{val}, index:{i}, next val: {next}')
        

test = [100, 4, 200, 1, 3, 2]
consecutiveElements(test)