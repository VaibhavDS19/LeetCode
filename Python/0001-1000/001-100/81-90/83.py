# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head:
            n = head
            it = head.next
            cur = n.val
            while it:
                if it.val != cur:
                    cur = it.val
                    n.next = it
                    n = n.next
                it = it.next
            n.next = None
        return head
