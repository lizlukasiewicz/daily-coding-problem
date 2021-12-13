"""
Given an array of integers, find the first missing positive integer in linear time 
and constant space. 

In other words, find the lowest positive integer that does not exist in the array. 

The array can contain duplicates and negative numbers as well.

For example, 
the input [3, 4, -1, 1] should give 2. 
The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""
def missing(array):
#sort array in ascending order
    array.sort()
    print(array)
    #loop through array
    #comparing each comapring item to the next
    current=0
    next=1
    while next < len(array):
        last = len(array)-1
        #If the current item +1 is equal to the next
        if array[current]+1 == array[next] or array[current]+1 ==0:
        #continue
            pass
        elif array[current]+1 != array[next] and array[current]+1 != 0:
            print(array[current]+1)
            return array[current]+1
        elif next == last:
            print(array[next]+1)
            #return array[last]+1
        current+=1
        next+=1

missing([3, 4, -1, 1])
missing([1, 2, 0])