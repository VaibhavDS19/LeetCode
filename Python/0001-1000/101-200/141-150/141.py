# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head and head.next:
            n1 = head
            n2 = head.next
            while n1 and n2 and n2.next:
                if n1 == n2:
                    return True
                n1 = n1.next
                n2 = n2.next.next
        return False
