"""

This problem was asked by Amazon.

Consider the following scenario: 
there are N mice and N holes placed at integer points along a line. 
Given this, find a method that maps mice to holes such that the largest number of steps any mouse takes is minimized.

Each move consists of moving one mouse one unit to the left or right, 
and only one mouse can fit inside each hole.

For example, 
suppose the mice are positioned at  -5  -4 -3 -2 -1 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16
    [1, 4, 9, 15],                  [🕳,0, 0, 0, 0,🕳, 🐭,0,0, 🐭, 0, 0, 0, 0,🐭, 🕳, 0, 0, 0, 0, 🐭,🕳]
and the holes are located at 
    [10, -5, 0, 16]. 

In this case, the best pairing would require us 
to send the mouse at 1 to the hole at -5, 
so our function should return 6.


"""

#finding the least greatest difference in values between 2 lists
def map_mice(mice: list, holes:list):
  distance=0
  for i in range(len(mice)):
    left_hole=min(holes) 
    left_mouse=min(mice)
    distance=max(distance, abs(left_hole-left_mouse))
    mice.remove(left_mouse)
    holes.remove(left_hole)
  return distance

if __name__ == '__main__':
  mice=[1, 4, 9, 15]
  holes=[10, -5, 0, 16]
  print(f' should be 6: {map_mice(mice=mice, holes=holes)}')