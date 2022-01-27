"""
This problem was asked by Pinterest.

Given an integer list where each number represents the number of hops you can make,
 determine whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.


"""
def hops(array):
    # evaluate each value of the array with enumerate
    hop = 0
    end = len(array) - 1
    for i, val in enumerate(array):
        print(i, val)
    # 
    print(array)

test = [2, 0, 1, 0]