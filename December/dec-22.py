"""
This problem was asked by google

Given k sorted singly linked lists, write a function to merge all the lists into one singly linked list
"""
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class merged:
    def margeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_node = ListNode()
        temp = new_node
        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        if l1 is not None:
            temp.next = l1
        else:
            temp.next = l2
        return new_node.next