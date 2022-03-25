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
    def print(self, node = None):
        if not node: node = self.root
        print(node)
        if node.left:
            self.print(node.left, "↙️")
        if node.right:
            self.print(node.right, "↘️")

class NodeL:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.mid = None
        self.right = None
    def __str__(self):
        return f'{self.data}'

class Tree:
    def __init__(self):
        self.root = None
    def insert(self, data):
        new_node = NodeL(data)
        if not self.root:
            self.root = new_node
            return
        current_node = self.root
    def print(self, node = None):
        if not node: node = self.root
        print(node)
        if node.left:
            self.print(node.left, "↙️")
        if node.mid:
            self.print(node.mid, "⬇️")
        if node.right:
            self.print(node.right, "↘️")

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    #passing __str__ in a class asks "what do you want me to do if im printed"
    def __str__(self):
        return f'{self.data}'

class LinkedList:
    def __init__(self):
        self.head = None
    def __str__(self):
        result = []
        temp = self.head
        while temp is not None:
            result.append(temp.data)
            temp = temp.next
        return f'{result}'
    def get_node_at_index(self, index):
        counter = 0 
        temp = self.head
        while counter < index:
            if temp.next is None:
                return "out of bounds my maaaannnnn" 
            temp = temp.next
            counter +=1
        return temp
    def append(self, new_data):
        temp = self.head
        new_node = Node(new_data)
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
    def prepend(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node