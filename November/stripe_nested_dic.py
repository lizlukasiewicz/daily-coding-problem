"""

This problem was asked by Stripe.

Write a function to flatten a nested dictionary. Namespace the keys with a period.

For example, given the following dictionary:

{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}
it should become:

{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
You can assume keys do not contain dots in them, i.e. no clobbering will occur.

"""
def flatten(d: dict):
  for key in d:
    
    print(f'key: {key} val:{d[key]}')
    

    if isinstance(d[key], dict):
      for sub in d[key]:
        print(f'subkey:{sub} subval: {d[key][sub]}')

  


if __name__=='__main__':
  ex_d={
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
  }
  flatten(ex_d)
  