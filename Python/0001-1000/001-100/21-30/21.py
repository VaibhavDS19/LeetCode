# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ret = ListNode()
        now = ret
        while (not l1 is None) and (not l2 is None):
            if l1.val < l2.val:
                x = ListNode(l1.val)
                l1 = l1.next
            else:
                x = ListNode(l2.val)
                l2 = l2.next
            now.next = x
            now = now.next

        while not l1 is None:
            x = ListNode(l1.val)
            l1 = l1.next
            now.next = x
            now = now.next

        while not l2 is None:
            x = ListNode(l2.val)
            l2 = l2.next
            now.next = x
            now = now.next

        return ret.next
