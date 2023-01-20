"""
This problem was asked by Google.

Given an array of strictly the characters 'R', 'G', and 'B', 
segregate the values of the array so that all the 
Rs come first, 
Gs come second, 
Bs come last. 
You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array 
['G', 'B', 'R', 'R', 'B', 'R', 'G'], 
it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

"""
def swap_linear(arr:list):
    #print(f'start::{arr}')
    count=0
    mid=arr.count('R')+1
    i=0
    while count < len(arr):
        #print(f'count:{count} i:{i} arr:{arr}')
        count+=1
        if arr[i]=='B':
            b=arr.pop(i)
            arr.append(b)
        elif arr[i]=='G':
            g=arr.pop(i)
            arr.insert(mid, g)
        else:
            i+=1
        



test_lst=['G', 'B', 'R', 'R', 'B', 'R', 'G']
swap_linear(test_lst)