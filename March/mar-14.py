"""
This problem was asked by Google.

Given a string, return the first recurring character in it, 
or null if there is no recurring character.

For example, given the string "acbbac", return "b". 
Given the string "abcdef", return null.

"""



def first_recurring(string):
    hash_table={ }
    for letter in string:
        if letter in hash_table:
            print(letter)
            return letter
        else: 
            hash_table[letter] ="potato"
    print("null")



test1, test2 = "acbbac", "abcdef"
first_recurring(test1)
first_recurring(test2)