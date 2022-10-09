"""
This problem was asked by Facebook.

Given an array of integers, write a function to determine 
whether the array could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], 
you should return true, since we can modify the 10 into a 1 
to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, 
since we can't modify any one element to get a non-decreasing array.


"""
def increasing(array):
    #determine if the first value is more than the second value
    ans = 0
    i = 0
    while i < len(array):
        if array[i] > array[i+1]:
            ans +=1
        else:
            continue
        i+=1
    if ans > 1:
        return False
    else:
        return True