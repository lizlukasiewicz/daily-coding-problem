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
  answer=''
  while num:
    num-=1
    c=num%26
    answer+=f"{chr(c+ord('A'))}"
    num=num//26
  # ords=[num for num in range(65, 91)]
  # letter=num-1 if num <= 26 else (num%26)-1
  
  # answer+=f'{chr(ords[letter])}'

  # div=(num/26)-1
  # control=0
  # if div>0: #while div>0 and control<10:
  #   control+=1
  #   answer+=f'{chr(ords[int(div)])}'
  return answer[::-1]


if __name__ =='__main__':
  ex1=18
  ex2=27
  ex3=624
  ex4=676
  # ex5=677# should be AAA
  print(f'should be R:{excel_columns(ex1)}')
  print(f'should be AA:{excel_columns(ex2)}')
  print(f'should be XZ:{excel_columns(ex3)}')
  print(f'should be ZZ:{excel_columns(ex4)}')