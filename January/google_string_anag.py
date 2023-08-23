"""
This problem was asked by Google.

Given a word W and a string S, find all starting indices in S which are anagrams of W.

For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.


"""

def anagram(W: str, S:str):
    window=len(W)
    left=0
    empty_array=[]
    char=set(W)
    # optimize? :: make it recursive
    while window <= len(S):
        y=char.symmetric_difference(set(S[left:window]))
        if y==set():
          empty_array.append(left)
        left+=1
        window+=1
    print(empty_array)
    return empty_array

anagram(W="ab", S="abxaba")