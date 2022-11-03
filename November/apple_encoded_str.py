"""
This problem was asked by Apple.

You are given a hexadecimal-encoded string that has been XOR'd against a single char.

Decrypt the message. For example, given the string:

7a575e5e5d12455d405e561254405d5f1276535b5e4b12715d565b5c551262405d505e575f
You should be able to decrypt it and get:

Hello world from Daily Coding Problem


"""


example_string='7a575e5e5d12455d405e561254405d5f1276535b5e4b12715d565b5c551262405d505e575f'
n=2
string_list=[example_string[i:i+n] for i in range(0, len(example_string), n)]
print(string_list)