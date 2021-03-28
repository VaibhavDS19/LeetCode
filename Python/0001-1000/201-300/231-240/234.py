# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        n = 0
        h1 = head
        while h1:
            n += 1
            h1 = h1.next
        b = n % 2 == 1
        h1 = head
        rev = None
        prev = None
        n //= 2
        while n != 0:
            rev = h1.next
            h1.next = prev
            prev = h1
            h1 = rev
            n -= 1
        if b:
            h1 = h1.next
        while prev and h1:
            if prev.val != h1.val:
                return False
            prev = prev.next
            h1 = h1.next
        return True