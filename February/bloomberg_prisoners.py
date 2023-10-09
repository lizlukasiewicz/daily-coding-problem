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
    order=[]
    circle=[i for i in range(1, N+1)]
    print(f'circle:{circle}')
    count=K
    ## CONDITION 1: while len(circle)> 1:
    while len(circle) > 1:
      to_remove=[]
    
      ## CONDITION 2: while count > 0
      for i, pris in enumerate(circle):
        count-=1
        print(f'({count}) prisoner:{pris}')
        if count < 1:
            order.append(pris)
            to_remove.append(i)
            count=K
      
      for ind in reversed(to_remove):
         circle.pop(ind)

    return circle[0]

if __name__ == '__main__':
  testN=5
  testk=2
  print(execution(K=testk, N=testN))
