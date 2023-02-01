"""
This problem was asked by Google.

Find the minimum number of coins required to make n cents.

You can use standard American denominations, 
that is, 1¢, 5¢, 10¢, and 25¢.

For example, given n = 16, 
return 3 since we can make it with a 10¢, a 5¢, and a 1¢.

"""

def change(n: int):
    denominations=[25, 10, 5, 1]
    number=n
    count=0
    for cent in denominations:

        while number-cent > -1:
            count+=1
            number-=cent
            
        
    print(f'count:: {count}')
    return count

ex_n=116
change(ex_n)