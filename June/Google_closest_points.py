"""
This problem was asked by Google.

Given a set of points (x, y) on a 2D cartesian plane, 
find the two closest points. 
For example, given the points 

  [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)], 

return [(-1, -1), (1, 1)].

"""
ex=[(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)]
def dumb_and_slow(list: list):
  vals={}
  # first loop - for each set
  for x in range(len(list)):
      
      # second loop - compare to other values
      for y in range(len(list)):
          if x==y:
              continue
          d1=abs(list[x][0] - list[y][0])
          d2=abs(list[x][1] - list[y][1])

          diff=d1+d2
          vals[diff] = [list[x], list[y]]
  m=min(vals.keys())
  print(vals[m])


dumb_and_slow(ex)        
