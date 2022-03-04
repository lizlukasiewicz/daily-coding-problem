"""
Given a list, sort it using this method: 
reverse(lst, i, j), which reverses lst from i to j.


"""

def reverseList(lst, i, j):
    print(lst[i:j:-1])

testLst = [1, 2, 3, 4, 5]
testi, testj = 5, 0

reverseList(testLst, testi, testj)