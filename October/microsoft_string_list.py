"""
This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), 
return the original sentence in a list. If there is more than one possible reconstruction, 
return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', 
and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', 
and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or 
['bedbath', 'and', 'beyond'].


"""

def sentence_list(dic: set, string: str):
  ans=[]
  sentence=string

  for word in dic:
   
    if sentence.__contains__(word):
      ans.append(word)
      part=sentence.partition(word)
      sentence=part[0]+part[-1]
    # fix for order of words in list
    # fix for returning null
    

  return ans


if __name__=='__main__':
  set1, st1 ={'quick', 'brown', 'the', 'fox'}, "thequickbrownfox"
  set2, st2 ={'bed', 'bath', 'bedbath', 'and', 'beyond'}, "bedbathandbeyond"

  print(f"should be ['the', 'quick', 'brown', 'fox'] {sentence_list(set1, st1)}")
  print(f"should be ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'] {sentence_list(set2, st2)}")
