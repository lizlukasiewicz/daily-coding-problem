"""

This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, 
return whether the brackets are balanced (well-formed).

For example, 
      given the string "([])[]({})", 
      you should return true.

Given the string "([)]" or "((()", 
    you should return false.

"""
def is_balanced(string: str):
  char_comp={
    '}':'{',
    ']': '[',
    ')': '('
  }
  stack=[]
  for char in string:
    if char in char_comp:
      if stack[-1] != char_comp[char]:
        return False
        
      stack.pop(-1)
      
    else:
      stack.append(char)
  
  if len(stack) > 0:
    return False

  return True


if __name__ == '__main__':
  ex1="([])[]({})"
  ex2="([)]"
  ex3="((()"
  print(f"should be true:{is_balanced(string=ex1)}")
  print(f"should be false:{is_balanced(string=ex2)}")
  print(f"should be false:{is_balanced(string=ex3)}")