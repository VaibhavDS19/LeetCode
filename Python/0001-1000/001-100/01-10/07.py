class Solution:
    def reverse(self, x: int) -> int:
        count = 0
        rev = 0
        l = 1
        if x < 0:
            l = -1
            x = x * - 1

        while x > 0:
            rev = rev*10 + x % 10
            x = x//10
            count += 1
            if count == 9:
                if rev > 214748364:
                    if x > 0:
                        return 0
                    return rev * l
                if rev == 214748364:
                    if x > 7:
                        return 0
        return rev * l
