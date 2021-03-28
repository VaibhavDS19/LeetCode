# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        n = None
        if head:
            while head.next:
                n = head.next
                head.next = prev
                prev = head
                head = n
            if head:
                head.next = prev
        return head
