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
        print(i,"index", val, "value")
        land = hop+val
        print(land, "landing")
        # ⬇️ infinite loop ⬇️ dont run this
        # while land < end:
        #     array[land] += val
        #     print(array[land], "next")
    
    #print(array)

test = [2, 0, 1, 0]
hops(test)