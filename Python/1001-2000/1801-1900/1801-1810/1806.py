class Solution:
    def reinitializePermutation(self, n: int) -> int:
        m = 0
        c = 1
        j = 0
        for i in range(n):
            if i % 2 == 0:
                j = i//2
            else:
                j = n//2 + (i-1)//2
            while j != i:
                c += 1
                if j % 2 == 0:
                    j = j//2
                else:
                    j = n//2 + (j-1)//2
            m = max(m, c)
            c = 1
        return m
