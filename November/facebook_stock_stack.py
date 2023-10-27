"""
This problem was asked by Facebook.

Given a array of numbers representing the stock prices of a company in chronological order, 
write a function that calculates the maximum profit you could have made from 
buying and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, 
since you could buy the stock at 5 dollars and sell it at 10 dollars.
"""
# is monotonic stack timeee
def bitcoin_bro(stocks: list):
  stack=[]
  diff=0
  for s in reversed(stocks):
    if stack:
      diff=max(diff, abs(stack[0]-s))

    while stack and s > stack[-1]:
      stack.pop()
    

    
    stack.append(s)
  return diff


if __name__=='__main__':
  stock=[9, 11, 8, 5, 7, 10]
  print(f'should be 5: {bitcoin_bro(stocks=stock)}')