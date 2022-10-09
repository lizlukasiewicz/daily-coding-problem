"""
This problem was asked by Apple.

Given a tree, find the largest tree/subtree that is a BST.

Given a tree, return the size of the largest tree/subtree that is a BST.
"""
class Node :
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return f'{self.data}'

class BinaryTree:
    def __init__(self):
        self.rooot = None
    def insert(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            return
        current_node = self.root
        while current_node:
            if new_node.data < current_node.data:
                if not current_node.left:
                    current_node.left = new_node
                    return
                else: current_node = current_node.left
            elif new_node.data > current_node.data:
                if not current_node.right:
                    current_node.right = new_node
                    return
                else: current_node = current_node.right
    def height(self, node = None):
        if not node:
            node = self.root
        max_height = 0
        def recursive_height(node, height=1):
            nonlocal max_height
            if node:
                if height > max_height:
                    max_height = height
                recursive_height(node.left, height +1)
                recursive_height(node.right, height+1)
            recursive_height(node)
            return max_height
        