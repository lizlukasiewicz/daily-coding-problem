"""
This problem was asked by LinkedIn.

Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right, 
and satisfies the constraint that the key in the left child must be 
less than or equal to the root and the key in the right child must be 
dgreater than or equal to the root.
"""
 
def isValid(self, data):
    if not self.root:
        return False
    current_node = self.root
    while current_node:
        if current_node.right <= current_node.data:
            print("not valid")
        elif current_node.left >= current_node.data:
            print("not valid")
        else:
            print("valid")