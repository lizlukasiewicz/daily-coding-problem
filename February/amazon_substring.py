"""
This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".


"""

def substring(k:int, s:str):
    char={}
    longest={}
    left=0
    for right in range(len(s)):
        char[s[right]]=char.get(s[right], 0)+1
        
        while len(char) > k:
            char[s[left]]-=1

            if char[s[left]]==0:
                del char[s[left]]
            
            left+=1
        longest[right-left+1]=s[left:right+1]
    length=max(longest.keys())
    return longest[length]
    
testk=2
tests='abcba'
substring(k=testk, s=tests)