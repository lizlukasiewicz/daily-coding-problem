"""
This problem was asked by Bloomberg.

There are N prisoners standing in a circle, waiting to be executed. 
The executions are carried out starting with the kth person, 
and removing every successive kth person going clockwise until there is no one left.

Given N and k, write an algorithm to determine where a prisoner should stand in order to be the last survivor.

For example, if N = 5 and k = 2, the order of executions would be [2, 4, 1, 5, 3], so you should return 3.

Bonus: Find an O(log N) solution if k = 2.

"""
def execution(K:int, N:int):
    pris=[i for i in range(1, N+1)]*K
    print(f'pris: {pris}')
    pop={}
    # for num in pris:

    #     while len(pris)>K:
        


    #while len(pris) > 1:
          #if i%K !=0
    #     pris.pop(K)

        # for num in step:
        #     pris.pop(num)
        # print(f'after:{pris}')

testN=5
testk=2
execution(K=testk, N=testN)
