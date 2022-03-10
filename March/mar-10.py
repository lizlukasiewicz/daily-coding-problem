"""
This problem was asked by MongoDB.

Given a list of elements, 
find the majority element, which appears more than half the time 
(> floor(len(lst) / 2.0)).

You can assume that such element exists.

For example, given [1, 2, 1, 1, 3, 4, 0], return 1.


"""
def majorityElem(lst):
    print(len(lst)//2)
    for num in lst:
        if lst.count(num) >= len(lst)//2:
            print(num)
            return num

test =[1, 2, 1, 1, 3, 4, 0]

majorityElem(test)