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

class Tree:
    def __init__(self):
        self.root = None