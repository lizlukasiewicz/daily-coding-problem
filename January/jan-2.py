"""
This problem was asked by LinkedIn.

Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right, 
and satisfies the constraint that the key in the left child must be 
less than or equal to the root and the key in the right child must be 
dgreater than or equal to the root.
"""
 
def isValid(tree, val):
    if not tree.root:
        return False
    current_node = tree.root
    while current_node:
        if val < current_node.data:
            current_node = current_node.left
        elif val > current_node.data:
            current_node