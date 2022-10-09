"""
This question was asked by Google.

Given an integer n and a list of integers l, 
write a function that randomly generates a number 
from 0 to n-1 that isn't in l (uniform).
"""
import random
def generate_random(n, l):
    x = n-1
    num = random.randint(0, x)
    for val in l:
        if num == val:
            return generate_random(n, l)