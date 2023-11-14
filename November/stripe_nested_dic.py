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
def flatten(d: dict, path=None):
  if path is None:
    # path=''
    path=[]
  for key, val in iter(d.values()) and iter(d.items()):
    print(f'\t\t\t🔮 key:{key} \tval: {val}')
    newpath= path+[key]
    if isinstance(val, dict):
      for u in flatten(val, newpath):
        yield u
    else:
      yield newpath, val
  

  


if __name__=='__main__':
  ex_d={
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        },
        "car":9,
    },
    "hello": {
        "world": {
            "why":1,
            "baz": 8
        },
        "girl":{
          "cherry":0,
          "gone":8
        }
    },
  }
  new_dict={}
  print('original dict:\n{')
  for i in ex_d:
    print(f'\t{i}: {ex_d[i]}')
  print('}\n\n')

  for path, val in flatten(ex_d):
    new_keys='.'.join(path)
    print(f"🐝{new_keys}: {val}")
    # ex_d.pop(path[0], '')
    new_dict[new_keys]=val
  print('\nupdated dict:')

  for k, v in new_dict.values() and new_dict.items():
    print(f'\t{k}: {v}, ')
  