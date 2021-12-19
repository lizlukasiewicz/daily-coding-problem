"""
This problem was asked by Google.

Given the head of a singly linked list, reverse it in-place.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Reverse:
    def reverseList(self, head: ListNode)-> ListNode:
        curr = head
        prev = None
        while curr is not None:
            print(f'❗️ current: {curr.val}')
            print(f'🔜 next: {curr.next.val}')
            print(f'🔙 previous: {prev}')
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
        return prev