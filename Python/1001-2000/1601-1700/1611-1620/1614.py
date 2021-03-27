class Solution:
    def maxDepth(self, s: str) -> int:
        m = 0
        n = 0
        for i in s:
            if i == '(':
                n += 1
                m = max(m, n)
            elif i == ')':
                n -= 1
        return m
