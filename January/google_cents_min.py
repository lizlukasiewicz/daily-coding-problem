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

# import unittest

# class TestStringMethods(unittest.TestCase):

#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')

#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())

#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)

# if __name__ == '__main__':
#     unittest.main()