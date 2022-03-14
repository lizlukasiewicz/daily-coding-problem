"""
This problem was asked by Amazon.

Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, 
since it can be rearranged to form racecar, which is a palindrome. 
daily should return false, since there's no rearrangement that can form a palindrome.

"""
from collections import Counter

def is_palindrome(phrase):
    counter = Counter(phrase.replace(" ", "").lower())
    print(sum(val % 2 for val in counter.values()) <= 1)

test1, test2 = "carrace", "daily"

is_palindrome(test1)
is_palindrome(test2)