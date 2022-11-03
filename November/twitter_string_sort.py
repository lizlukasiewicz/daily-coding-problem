"""

This problem was asked by Twitter.

Given a string, sort it in decreasing order based on the frequency of characters. 
If there are multiple possible solutions, return any of them.

For example, given the string tweet, return tteew. eettw would also be acceptable.

"""
def desc_string(str):
    new_string=''
    characters={}
    for letter in str:
        if letter not in characters: characters[letter]=str.count(letter)
    for char in sorted(characters.items()):
        new_string+=char[0]*char[1]
    print(new_string)

ex_string='tweet'
desc_string(ex_string)