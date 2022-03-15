"""
uber::
given an tree where each edge has a length, 
compute the lengeth of the longet path in the tree
 for example given the following tree:
    a
b   c   d
       e   f
      g  h
and the weights::
a-b:3,
a-c: 5,
a-d: 8,
d-e: 2,
d-f: 4,
e-g:1,
e-h:1

the longest path would be:
    c -> a -> d -> f === with a length of 17
the path does not have to pass through the root, 
and each node can have any amount of children
"""