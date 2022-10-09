"""
This problem was asked by Square.

Given a string and a set of characters, 
return the shortest substring containing all the characters in the set.

For example, given the string "figehaeci" 
and the set of characters {a, e, i}, you should return "aeci".

If there is no substring containing all the characters in the set, return null.


"""


t_string='figehaeci'
t_set={'a', 'e', 'i'}
def short_sub(string, characters):
    print(string, characters)
    sub=[]
    for letter in string:
        if letter in characters:
            n=string.index(letter)
            sub.append(string[n:])#sub.append(tuple([string[n:], len(string[n:])]))
    return min(sub)


short_sub(t_string, t_set)