"""
This problem was asked by Google.

Given an array of integers, 
return a new array where each element in the new array 
is the number of smaller elements to the right of that element 
in the original input array.

For example, given the array [3, 4, 9, 6, 1], 
return [1, 1, 2, 1, 0], since:

There is 1 smaller element to the right of 3
There is 1 smaller element to the right of 4
There are 2 smaller elements to the right of 9
There is 1 smaller element to the right of 6
There are no smaller elements to the right of 1

"""
def smallArray(list):
    new=[]
# loop through each array item except the last
    for num in list:
        diff = 0
        start=list.index(num)
        for compare in list[start:]:
            if num > compare:
                diff += 1
        new.append(diff)
    print(new)

    # starting from index of the item currently being looped
    #
    # comare that item to the rest of the values in the array
test1=[3, 4, 9, 6, 1]
smallArray(test1)