"""
This problem was asked by Microsoft.

Given an array of numbers, 
find the length of the longest increasing subsequence in the array. 
The subsequence does not necessarily have to be contiguous.

For example, 
given the array 
                [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], 

the longest increasing subsequence 
has length 6: it is 0, 2, 6, 9, 11, 15.
"""
def long_increase(arr: list):
  print(f'{arr}')
  stack=[]
  # # PREVIOUS LESSER
  # for i, num in enumerate(arr):
  #   print(f'[{i}] {num}')
  #   while stack and num < stack[-1]:
  #     print(f'{stack}\n{num} < {stack[-1]}')
  #     stack.pop()
  #   if stack:
  #     print(f'{stack}')
  #   stack.append(num)
  
  # # NEXT GREATER
  # stack2=[]
  # for j, n in enumerate(reversed(arr)):
  #   print(f'[{j}] {n}')
  #   while stack2 and n > stack2[-1]:
  #     print(f'{stack2}\n{n} < {stack2[-1]}')
  #     stack2.pop()
  #   if stack2:
  #     print(f'{stack2}')
  #   stack2.append(n)

  # # PREVIOUS GREATER 
  # for i, num in enumerate(arr):
  #   print(f'[{i}] {num}')
  #   while stack and num > stack[-1]:
  #     print(f'{stack}\n{num} > {stack[-1]}')
  #     stack.pop()
  #   if stack:
  #     print(f'{stack}')
  #   stack.append(num)

  # # NEXT LESSER
  # for i, num in enumerate(reversed(arr)):
  #   print(f'[{i}] {num}')
  #   while stack and num < stack[-1]:
  #     print(f'{stack}\n{num} < {stack[-1]}')
  #     stack.pop()
  #   if stack:
  #     print(f'{stack}')
  #   stack.append(num)


  return "done!"

    


if __name__ == '__main__':
  arr=[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
  print(long_increase(arr=arr))