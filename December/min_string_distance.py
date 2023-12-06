"""

Find an efficient algorithm to find the smallest distance (measured in number of words) 
between any two given words in a string.

For example, 
                given words     "hello", and "world" 
      and a text content of     "dog cat hello cat dog dog hello cat world", 
return 1 because there's only one word "cat" in between the two words.

"""
def efficient_algo(w1: str, w2: str, content: str):
  # split text content to have count of words
  arr=content.split(" ")
  # highest distance length between words 
  distance=len(arr)
  # initiate zero for count 
  step=0
  # trigger boolean when first word has been found
  start=False

  # i hate stringing if statements but here it is
  for x in range(distance):
    if start:
      if arr[x]==w2:
        distance=min(distance, step)
        break
      step+=1

    if arr[x]==w1:
      if start:
        step=0
      start=True
      
  return step


if __name__== '__main__':
  word1="hello"
  word2="world"
  content1="dog cat hello cat dog dog hello cat world"
  print(f" should be 1: {efficient_algo(w1=word1, w2=word2, content=content1)}")