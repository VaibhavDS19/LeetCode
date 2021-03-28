class Solution:
    def numberOfSteps(self, num: int) -> int:
        c = -1
        while num:
            c += 2 if num & 1 else 1
            num >>= 1

        return c if c != -1 else 0
