"""
This problem was asked by Google.

Given the root of a binary tree, 
return a deepest node. For example, in the following tree, return d.

    a
   / \
  b   c
 /
d

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return f'{self.data}'

class BinaryTree:
    def __init__(self):
        self.root = None

    def depth(self, node = None):
        def get_max(self):
            rightSide = 0
            leftSide = 0
            if not self.root:
                return False
            current_node = self.root
            while current_node.right:
                current_node = current_node.right
            return current_node.data