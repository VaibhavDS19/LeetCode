class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        n1 = 2
        n2 = 3
        n3 = 3
        for i in range(3, n):
            n3 = n1 + n2
            n1 = n2
            n2 = n3
        return n3
