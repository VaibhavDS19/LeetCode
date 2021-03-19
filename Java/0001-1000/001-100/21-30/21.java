/**
 * Definition for singly-linked list. public class ListNode { int val; ListNode
 * next; ListNode() {} ListNode(int val) { this.val = val; } ListNode(int val,
 * ListNode next) { this.val = val; this.next = next; } }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode l3 = new ListNode(), l4 = l1, l5 = l2, l6 = new ListNode(), cur = l3;
        while (l4 != null && l5 != null) {
            if (l4.val < l5.val) {
                l6 = new ListNode(l4.val);
                l4 = l4.next;
            } else {
                l6 = new ListNode(l5.val);
                l5 = l5.next;
            }
            cur.next = l6;
            cur = l6;
        }
        while (l4 != null) {
            l6 = new ListNode(l4.val);
            l4 = l4.next;
            cur.next = l6;
            cur = l6;
        }
        while (l5 != null) {
            l6 = new ListNode(l5.val);
            l5 = l5.next;
            cur.next = l6;
            cur = l6;
        }
        return l3.next;
    }
}