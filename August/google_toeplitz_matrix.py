"""
This problem was asked by Google.

In linear algebra, a toeplitz matrix is one in which the elements 
on any given diagonal from top left to bottom right are identical.

Here is an example:

[
[1, 2, 3, 4, 8],
[5, 1, 2, 3, 4],
[4, 5, 1, 2, 3],
[7, 4, 5, 1, 2]
]
Write a program to determine whether a given input is a Toeplitz matrix.

"""
def toeplitz(matrix):
    # conditional checking length of each list is equal
    it = iter(matrix)
    the_len=len(next(it))
    if not all(len(l) == the_len for l in it):
        print('false')
        return False
    # loop through length of lists and length of each list
    for i in range(len(matrix[0])):
        print(f'[0][{i}]  {matrix[0][i]}')
        
        for j in range(1, len(matrix)):
            if (i+j) < len(matrix[0]):
              print(f'[{j}][{i+j}] == {matrix[j][i+j]}')


if __name__ == '__main__':
    example=[
            [1, 2, 3, 4, 8],
            [5, 1, 2, 3, 4],
            [4, 5, 1, 2, 3],
            [7, 4, 5, 1, 2]
            ]
    print(toeplitz(matrix=example))