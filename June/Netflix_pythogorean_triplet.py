"""
This problem was asked by Netflix.

Given an array of integers, 
determine whether it contains a Pythagorean triplet. 
Recall that a Pythogorean triplet (a, b, c) is defined by the equation a2+ b2= c2.

"""

def pythogo(l:list):
    n=len(l)
    for i in range(n):
      l[i]= l[i]*l[i]
    l.sort()

    for i in range(n-1, 1, -1):
      s=set()
      for j in range(i - 1, -1, -1):
        if (l[i] - l[j]) in s:
          return True
        s.add(l[j])
    return False
      
arr = [10, 4, 6, 12, 5]

if (pythogo(arr)):
  print("True")
else:
  print("False")