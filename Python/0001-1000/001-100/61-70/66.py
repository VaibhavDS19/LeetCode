class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        l = []
        c = 1
        while i >= 0:
            s = digits[i] + c
            c = s//10
            s = s % 10
            l.append(s)
            i -= 1
        if c == 1:
            l.append(1)
        return l[::-1]
