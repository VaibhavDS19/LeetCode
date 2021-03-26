class Solution:
    def mySqrt(self, x: int) -> int:
        b = 1
        e = x
        while b <= e:
            mid = (b + e) // 2
            if mid * mid <= x:
                b = mid + 1
            else:
                e = mid - 1

        return b - 1
