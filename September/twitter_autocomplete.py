"""

This problem was asked by Twitter.

Implement an autocomplete system. 
That is, given a query string s 
and a set of all possible query strings, 
return all strings in the set that have s as a prefix.

For example, 
given the query string de 
and the set of strings [dog, deer, deal], 
return [deer, deal].

Hint: Try preprocessing the dictionary 
 into a more efficient data structure to speed up queries.

"""
def autocomplete(q: str, set: list):
  match=[]
  for s in set:
    if q == s[:len(q)]:
      match.append(s)
  return match

if __name__ == '__main__':
  ex1=['dog', 'deer', 'deal']
  query1='de'
  print(f'{autocomplete(q=query1, set=ex1)}')