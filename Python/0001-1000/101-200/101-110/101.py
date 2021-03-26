# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root:
            return self.cmp(root.left, root.right)
        return root

    def cmp(self, left, right):
        if left and right:
            if left.val != right.val:
                return False
        if (not left) and (not right):
            return True
        if (not left) or (not right):
            return False
        return self.cmp(left.left, right.right) and self.cmp(left.right, right.left)
