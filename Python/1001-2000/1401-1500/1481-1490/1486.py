class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ret = 0
        for i in range(n):
            ret ^= start
            start += 2
        return ret
