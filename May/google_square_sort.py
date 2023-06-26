"""

This problem was asked by Google.

Given a sorted list of integers, square the elements and give the output in sorted order.

for example, given:
                [-9, -2, 0, 2, 3]
            return:
                [0, 4, 4, 9, 81]

"""

test1=[-9, -2, 0, 2, 3]

def sort_square(list: list):
  o_list=list
  print(f'original list: {o_list}')

  # dumb and slow::
  l=[num**2 for num in list]
  print(f'dumb and slow: {sorted(l)}')
  return l

sort_square(test1)