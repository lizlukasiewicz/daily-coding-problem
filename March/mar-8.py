"""
Find an efficient algorithm to find the smallest distance 
(measured in number of words) between any two given words in a string.

For example, given words 
"hello", and "world" 
and a text content of 
"dog cat hello cat dog dog hello cat world", 
return 1 because there's only one word "cat" in between the two words.
"""
def textContent(string1, string2, context):
    clist = context.split()
    # find index of string2 
    index2 = clist.index(string2)
    # find closest occourance of string1 to string2
    for count, ele in enumerate(clist):
        if ele == string1:
            print(index2 - count, ele)
word1, word2 = "hello", "world"
test = "dog cat hello cat dog dog hello cat world"
textContent(word1, word2, test)