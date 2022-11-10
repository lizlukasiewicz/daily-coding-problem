"""

This problem was asked by Facebook.

We have some historical clickstream data gathered from our site anonymously using cookies. 
The histories contain URLs that users have visited in chronological order.

Write a function that takes two users' browsing histories as input 
and returns the longest contiguous sequence of URLs that appear in both.

For example, given the following two users' histories:

user1 = ['/home', '/register', '/login', '/user', '/one', '/two']
user2 = ['/home', '/red', '/login', '/user', '/one', '/pink']
You should return the following:

['/login', '/user', '/one']


"""
def browsing_his(u1, u2):
    tbl=[[0 for _ in range(len(u2)+1)] for _ in range(len(u1)+1)]
    for i, x in enumerate(u1):
        print(f'🐲 ({x}){tbl[i]} ')
        for j, y in enumerate(u2):
            print(f'({y}) 🌺 {tbl[i+1][j+1]} = {tbl[i][j]+1} if ({x}) == ({y}) else: 0')#max({tbl[i+1][j]}, {tbl[i][j+1]})')#+1)
            tbl[i+1][j+1] = tbl[i][j]+1 if x == y and u1[i-1]==u2[j-1] else max(tbl[i+1][j], tbl[i][j+1])
            # print(tbl[i+1][j+1])
    res=[]
    i, j = len(u1), len(u2)
    # while i and j:
    #     if tbl[i][j] == tbl[i - 1][j]:
    #         print(f'🪺 [i][j]:{tbl[i][j]} == [i-1][j]:{tbl[i - 1][j]}')
    #         i -= 1
    #     elif tbl[i][j] == tbl[i][j - 1]:
    #         print(f'🍗 [i][j]:{tbl[i][j]} == [i][j-1]:{tbl[i][j - 1]}')
    #         j -= 1
    #     else:
    #         print(f'💎 {u1[i - 1]}')
    #         res.append(u1[i - 1])
    #         i -= 1
    #         j -= 1
    # print(res[::-1])

user1 = ['/home', '/register', '/login', '/user', '/one', '/two']
user2 = ['/home', '/red', '/login', '/user', '/one', '/pink']

browsing_his(user1, user2)