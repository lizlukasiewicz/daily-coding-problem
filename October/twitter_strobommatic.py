"""

This problem was asked by Twitter.

A strobogrammatic number is a positive number that appears the same after being rotated 180 degrees. 
For example, 16891 is strobogrammatic.

Create a program that finds all strobogrammatic numbers with N digits.

"""

def get_strobogrammatic(n):
    result=helper(n, n)
    return result

def helper(n, length):
    if n==0:
        return [""]
    if n==1:
        return ["1", "0", "8"]
    middles= helper(n-2, length)
    result=[]
    for middle in middles:
        if n != length:
            result.append('0'+middle+'0')
        result.append('8'+middle+'8')
        result.append('1'+middle+'1')
        result.append('9'+middle+'6')
        result.append('6'+middle+'9')
    return result

if __name__=='__main__':
    print(get_strobogrammatic(3))