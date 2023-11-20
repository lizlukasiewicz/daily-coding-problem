"""

This problem was asked by Amazon.

Given a string, find the longest palindromic contiguous substring. 
If there are more than one with the maximum length, return any one.

For example, 
the longest palindromic substring of 
                "aabcdcb" 
               is "bcdcb". 

The longest palindromic substring of 
                "bananas" 
              is "anana".


"""
def longest_palindrome(s: str):
  ans=[]



if __name__ == '__main__':
  ex1="aabcdcb"
  ex2="bananas"

  print(f'should be bcdcb: {longest_palindrome(ex1)}')
  print(f'should be anana: {longest_palindrome(ex2)}')