"""
This problem was asked by Facebook.

Given a function f, and N return a debounced f of N milliseconds.

That is, as long as the debounced f continues to be invoked, 
f itself will not be called for N milliseconds.
"""
# Debouncing means to supress the call to a function within a given timeframe, 
# say you call a function 100 times within 1 second 
# but you only want to allow the function to run once every 10 seconds 
# a debounce decorated function would run the function once 10 seconds after 
# the last function call if no new function calls
from datetime import datetime
import threading

test_n=100
def test_funct(str):
    print(f'🦄 hell0 {str}')

def debounce(N):
    def decorator(f):
        def debounced(*args, **kwargs):
            def call_f():
                debounced._timer = None
                return function(*args, **kwargs)
            if debounced._timer is not None:
                debounced._timer.cancel()
            debounced._timer = threading.Timer(N, call_f)
            debounced._timer.start()
        debounced._timer = None
        return debounced
    return decorator(test_funct('world'))

debounce(test_n)