"""

This problem was asked by Facebook.

Write a function that rotates a list by k elements. 
                For example, [1, 2, 3, 4, 5, 6] 
      rotated by two becomes [3, 4, 5, 6, 1, 2]. 
      
Try solving this without creating a copy of the list. 
How many swap or move operations do you need?


"""

def rotate_list(k: int, array: list):
  print(array)
  for n in range(k):
    array.append(array.pop(0))
  return array

if __name__=='__main__':
  list1=[1, 2, 3, 4, 5, 6]
  k1=2
  print(f'{rotate_list(k1, list1)}')