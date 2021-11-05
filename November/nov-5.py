"""
The edit distance between two strings refers to the minimum number of character 
insertions, deletions, and substitutions required to change one string to the other. 
For example, the edit distance between “kitten” and “sitting” is three: 
substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.


"""
def distance(string1, string2):
    #split string by charachtr and create list
    list1= []
    for char in string1:
        list1.append(char)
    list2 = []
    for c in string2:
        list2.append(c)
    i=0
    while i < len(list2):
        if list1[i] != list2[i]:
            i+=1
            continue
        else:
            list1.remove(list1[i])
            list2.remove(list2[i])
            i+=1
    difference = max(len(list2), len(list1))
    print(difference)

distance("kitten", "sitting")

#loop through each indexed letter of both strings
# if the letters match, pop them out of the string 
# find the max length of both