# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#     def __str__(self):## __str__ in class == what do you want Class to do if Class is printed
#         return f'{self.data}'
from DataStructures import ListNode, LinkedList, DoubleNode, DoublyLinkedList


"""

This problem was asked by Google.

Given the head of a singly linked list, 
swap every two nodes and return its head.

For example, 
given 1 -> 2 -> 3 -> 4, 
return 2 -> 1 -> 4 -> 3

"""
class SingleSwap(LinkedList):
    def __init__(self):
       super().__init__(self)
       self.second_node=True
       
    # still workin on this
    # def swap(self):
    #    curr=self.head
    #    next=curr.next
    #    while next is not None:
    #       if self.second_node:
    #         first=curr
    #         second=curr.next
    #         curr=second
    #         next=first
    #         self.second_node=False
          
        
          
       #if self.second_node:

    def display(self):
      if self.head is None:
        print("The list is empty")
        return
      else:
        n = self.head
        while n is not None:
          print(f"self.head: {n.data}")
          n = n.next
      print("\n")
  
ll=SingleSwap()
no=[1,2,3,4]
for n in no:
    ll.append(n)

ll.display()











"""

This problem was asked by Google.

Determine whether a doubly linked list is a palindrome. 
What if it’s singly linked?

For example, 1 -> 4 -> 3 -> 4 -> 1 
  returns True 

while 1 -> 4 
  returns False.


"""
# class Solution:
#     def isPalindrome(self, head:ListNode) -> bool:
#   ## COPY LIST INTO ARRAY, CHECK BACKWARDS
#         vals = []
#         curr = head
#         while curr is not None:
#             vals.append(curr.val)
#             curr = curr.next
        
#         return vals == vals[::-1]
        
        ## how do i explain how much slower this runs with smaller data
    #     if head is None:
    #         return True
        
    #     # find end of first half and reverse second half
    #     first_half_end = self.end_first(head)
    #     second_half_start = self.reverse_l(first_half_end.next)

    #     # Check palindrome
    #     result = True
    #     first_position = head 
    #     second_position = second_half_start
    #     while result and second_position is not None:
    #         if first_position.val != second_position.val:
    #             result = False
    #         first_position = first_position.next
    #         second_position = second_position.next
        
    #     first_half_end.next = self.reverse_l(second_half_start)
    #     return result


    # # FINDING END OF FIRST HALF
    # def end_first(self, head):
    #     fast = head
    #     slow = head
    #     while fast.next is not None and fast.next.next is not None:
    #         p_str=f'fast:{fast.val} slow:{slow.val}'
    #         fast = fast.next.next
    #         slow = slow.next
    #         print(f'{p_str} fast.next.next:{fast.val} slow.next: {slow.val}')
    #     return slow

    # # REVERSING SECOND HALF
    # def reverse_l(self, head):
    #     previous = None
    #     current = head
    #     while current is not None:
    #         cur=f'curr:{current.val}'

    #         next_node = current.next
    #         # next_n=f'next_node: {next_node.val}'
        
    #         current.next = previous
            
    #         previous = current
    #         # new_previous=f'previous=current: {previous.val}'

    #         current = next_node
    #         # current_val=f'curr:{current.val} = next_node:{next_node.val}'
    #         print(f'🍄{cur}')# | {next_n} | {new_previous} | {current_val}
    #     return previous




        ## RECURSIVE
        # self.front_pointer = head

        # def recursive_check(current = head):
        #     if current is not None:
        #         if not recursive_check(current.next):
        #             return False
        #         if self.front_pointer.val != current.val:
        #             return False
        #         self.front_pointer = self.front_pointer.next
        #     return True

        # return recursive_check()







"""
An XOR linked list is a more memory efficient doubly linked list. 

Instead of each node holding next and prev fields, it holds a field named both, 
which is an XOR of the next node and the previous node. 

Implement an XOR linked list; 
it has an add(element) which adds the element to the end, 
and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), 
you can assume you have access to get_pointer and dereference_pointer 
functions that converts between nodes and memory addresses.
"""














"""
This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. 
The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, 
return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""