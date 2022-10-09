"""
This problem was asked by Two Sigma.

Using a function rand7() that returns an integer from 1 to 7 (inclusive) 
with uniform probability, 
implement a function rand5() that returns an integer from 1 to 5 (inclusive).
"""
import random

def rand7():
    print(random.randint(1, 7), "🎈")
rand7()
def rand5():
    print(random.randint(1, 5), "👹")
rand5()