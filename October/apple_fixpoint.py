"""
This problem was asked by Apple.

A fixed point in an array is an element whose value is equal to its index. 
Given a sorted array of distinct elements, return a fixed point, if one exists. 
Otherwise, return False.

For example, given [-6, 0, 2, 40], 
you should return 2. 

Given [1, 5, 7, 8], 
you should return False
"""
def fixpoint(arr: list):
  for i, num in enumerate(arr):
    if i == num:
      return num
  
  return False

if __name__ == '__main__':
  ex1=[-6, 0, 2, 40]
  ex2=[1, 5, 7, 8]

  print(f'should be 2: {fixpoint(ex1)}')
  print(f'should be False: {fixpoint(ex2)}')