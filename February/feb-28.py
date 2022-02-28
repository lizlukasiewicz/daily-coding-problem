"""
This problem was asked by Google.

Given the head of a singly linked list, swap every two nodes and return its head.

For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.

"""
class Node:
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
    def swapTwo(self, index):
        counter = 0



llist = LinkedList()
n1 = Node(1)
n2 = Node(2)
n3, n4 = Node(3), Node(4)
llist.append(n2)
llist.prepend(n1)
llist.append(n3)
llist.append(n4)

print(llist)