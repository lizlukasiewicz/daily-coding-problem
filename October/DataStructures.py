# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#     def __str__(self):
#         return f'{self.data}'
    
# class BinaryTree:
#     def __init__(self):
#         self.root = None
#     def insert(self, data):
#         new_node = Node(data)
#         if not self.root:
#             self.root = new_node
#             return
#         current_node = self.root
#         while current_node:
#             if new_node.data < current_node.data:
#                 if not current_node.left:
#                     current_node.left = new_node
#                     return
#                 else: current_node = current_node.left
#             elif new_node.data > current_node.data:
#                 if not current_node.right:
#                     current_node.right = new_node
#                     return
#                 else: current_node = current_node.right
#     def print(self, node = None):
#         if not node: node = self.root
#         print(node)
#         if node.left:
#             self.print(node.left, "↙️")
#         if node.right:
#             self.print(node.right, "↘️")

# class NodeL:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.mid = None
#         self.right = None
#     def __str__(self):
#         return f'{self.data}'

# class Tree:
#     def __init__(self):
#         self.root = None
#     def insert(self, data):
#         new_node = NodeL(data)
#         if not self.root:
#             self.root = new_node
#             return
#         current_node = self.root
#     def print(self, node = None):
#         if not node: node = self.root
#         print(node)
#         if node.left:
#             self.print(node.left, "↙️")
#         if node.mid:
#             self.print(node.mid, "⬇️")
#         if node.right:
#             self.print(node.right, "↘️")

class ListNode: # CLASS NAME
    def __init__(self, data): # PROPERTIES
        self.data = data
        self.next = None
    # passing __str__ in a class asks "what do you want me to do if im printed"
    def __str__(self):
        return f'{self.data}'

class LinkedList: # CLASS NAME
    def __init__(self): # PROPERTIES
        self.head = None

    def __str__(self):
        result = []
        temp = self.head
        while temp is not None:
            result.append(temp.data)
            temp = temp.next
        return f'{result}'
    
    def get_node_at_index(self, index): # METHOD
        counter = 0 
        temp = self.head
        while counter < index:
            if temp.next is None:
                return "out of bounds my maaaannnnn" 
            temp = temp.next
            counter +=1
        return temp
    
    def append(self, new_data):
        # Check if the list is empty
        if self.head is None:
            new_node = ListNode(new_data)
            self.head = new_node
            return
        
        temp = self.head
        new_node = ListNode(new_data)
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
    
    def prepend(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node



class DoubleNode:
    def __init__(self, data):
        self.val = data
        self.next = None
        self.prev = None
    def __str__(self):
        return f'{self.data}'
# Class for doubly Linked List
class DoublyLinkedList:
    def __init__(self):
        self.current = None


    # Insert Element to Empty list
    def insert_into_empty_list(self, data):
        if self.current is None:
            new_node = DoubleNode(data)
            self.current = new_node
            print(f'adding:{new_node.val}')
        else:
            print("The list is empty")


    # Insert element at the end
    def append(self, data):
        # Check if the list is empty
        if self.current is None:
            new_node = DoubleNode(data)
            self.current = new_node
            return


        n = self.current
        new_node = DoubleNode(data)
        # Iterate till the next reaches NULL
        while n.next is not None:
            n = n.next
            
        n.next = new_node
        new_node.prev = n


    # Delete the elements from the start
    def delete_first(self):
        if self.current is None:
            print("The Linked list is empty, no element to delete")
            return 
        if self.current.next is None:
            self.current = None
            return
        self.current = self.current.next
        self.current.prev = None
    


    # Delete the elements from the end
    def delete_at_end(self):
        # Check if the List is empty
        if self.current is None:
            print("The Linked list is empty, no element to delete")
            return 
        if self.current.next is None:
            self.current = None
            return
        n = self.current
        while n.next is not None:
            n = n.next
        n.prev.next = None



    # Traversing and Displaying each element of the list
    def display(self):
        if self.current is None:
            print("The list is empty")
            return
        else:
            n = self.current
            print(f"self.current: {n.val}")
            while n is not None:
                n = n.next
        print("\n")