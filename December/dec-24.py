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
        if not node:
            node = self.root
        max_height = 0 
        def recursive_height(node, height=1):
            nonlocal max_height
            if node: 
                if height> max_height:
                    max_height = height
                recursive_height(node.left, height +1)
                recursive_height(node.right, height+1)
            recursive_height(node)
            return max_height