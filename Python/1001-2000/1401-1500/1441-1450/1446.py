class Solution:
    def maxPower(self, s: str) -> int:
        m = 0
        n = 0
        c = ''
        for ch in s:
            if ch != c:
                c = ch
                m = max(m, n)
                n = 1
            else:
                n += 1
        return max(m, n)
