"""
This problem was asked by Microsoft.

Suppose an arithmetic expression is given as a binary tree. 
Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).
"""

#node constructor
class Node:
    def __init__(self, data): # override method
        self.data = data
        self.left = None
        self.right = None
  # ⬇️  method overried of the string method for the node 
    def __str__(self):
        return f'{self.data}'
#tree constructor
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data) 
        if not self.root: 
            self.root = new_node
            return

        current_node = self.root 
        while current_node:
            if new_node.data < current_node.data: # if data is less than node
                if not current_node.left: # if there is no left
                    current_node.left = new_node #set the left to be the new node
                    return 
                else: current_node = current_node.left # else move to the left
            elif new_node.data > current_node.data: # if the new node data is bigger than the current node
                if not current_node.right: #check if there is no right
                    current_node.right = new_node  #insert to the right
                    return
                else: current_node = current_node.right #otherwise we need to move to the right
    def print(self, node=None):
        if not node: node = self.root
        print(node)
        if node.left: 
            self.print(node.left)
        if node.right: 
            self.print(node.right)

BinaryTree().insert(6)
BinaryTree().print()


# RECURSTION-ish more like callback functions

# root = global variable middle (function later return (branch)middle(branch))

# if a node has a branch, set value of current node to global variable branch = (left middle right)
