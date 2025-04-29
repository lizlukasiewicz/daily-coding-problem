"""
This problem was asjed by Amazon.

Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome.
daily should return false, since there's no rearrangement that can form a palindrome



"""

def palindrome_check(s: str):
  letters={}
  single_letter=0
  for i in s:

    if i in letters:
      letters[i] += 1
      #print(f'🪲 {i} = {letters[i]}')
    else:
      letters[i] = 1
      #print(f'🐌 {i} = {letters[i]}')
  for l in letters:
    if letters[l]==1:
      single_letter+=1
  if single_letter > 1:
    #print("False")
    return False
  #print("True")
  return True


test1="carrace"
test2="daily"

palindrome_check(test1)
palindrome_check(test2)