"""
cons(a, b) constructs a pair, 
and 
car(pair) and cdr(pair) returns the first and last element of that pair. 

For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr.
"""

def cons(a, b):
    def pair(f):
        #print("in pair:", a, b)
        return f(a, b)
    #print("in cons:", a, b)
    return pair

def car(variable):
    x = locals
    print("in car", variable(x))

car(cons(3, 4))