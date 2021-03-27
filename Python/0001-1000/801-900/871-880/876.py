# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        c = 0
        l = head
        while l:
            c += 1
            l = l.next
        c = c//2
        l = head
        while c > 0:
            l = l.next
            c -= 1
        return l
