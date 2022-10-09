"""
This problem was asked by Facebook.

You have a large array with most of the elements as zero.

Use a more space-efficient data structure, 
SparseArray, that implements the same interface:

init(arr, size): initialize with the original large array and size.
set(i, val): updates index at i with val.
get(i): gets the value at index i.


"""
class SparseArray:
    def init(arr, size):
    #loop thrugh array with enumerate?
        print(arr, size)
        def set(i , val):
            print(val, i)
        def get(i):
            print(arr.index(i))