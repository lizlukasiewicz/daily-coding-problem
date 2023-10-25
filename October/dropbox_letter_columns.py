"""

This problem was asked by Dropbox.

Spreadsheets often use this alphabetical encoding 
for its columns: "A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....

Given a column number, 
return its alphabetical column id. 

For example, given 1, return "A". Given 27, return "AA".

"""

def excel_columns(num):
  # make it better
  ords=[num for num in range(65, 91)]
  letter=num-1 if num < 27 else (num%26)-1
  div=int(num/26)-1
  if div>0:
    return f'{chr(ords[div])}{chr(ords[letter])}'
  return f'{chr(ords[letter])}'


if __name__ =='__main__':
  ex1=1
  ex2=27
  print(f' should be A:{excel_columns(ex1)}')
  print(f'should be AA:{excel_columns(ex2)}')