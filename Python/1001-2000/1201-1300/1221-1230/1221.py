class Solution:
    def balancedStringSplit(self, s: str) -> int:
        n = 0
        c = 0
        for ch in s:
            if ch == 'R':
                c += 1
            else:
                c -= 1
            if c == 0:
                n += 1
        return n
