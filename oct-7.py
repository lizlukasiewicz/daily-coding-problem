"""
Given an array of integers, return a new array such that each element at index i 
of the new array is the product of all the numbers in the original array except the one at i.

For example, 
if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""
def product(array):
#first initialize an empty array for the values to be appended to
    new_array = []
    i=0
#then loop through the input array with a while loop to keep track of current index
    while i < len(array):
        prod_array = array.copy()
        prod_array.pop(i)
        result=1
        for x in prod_array:
            result = result * x
        i+=1
        new_array.append(result)
    print(new_array)
    

product([1, 2, 3, 4, 5])
    # else, push every other value of array into a new array
        # find the sum of all the values in the new array
         #append the sum to the empty array