# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a = headA
        b = headB
        nA = 0
        nB = 0
        while a:
            nA += 1
            a = a.next
        while b:
            nB += 1
            b = b.next
        ret = None
        a = headA
        b = headB
        if nA > nB:
            while nA-nB != 0:
                nA -= 1
                a = a.next
        elif nB > nA:
            while nB - nA != 0:
                nB -= 1
                b = b.next
        while a and b:
            if a == b:
                ret = a
                break
            a = a.next
            b = b.next
        return ret
