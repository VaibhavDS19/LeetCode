class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n1 = len(a)
        n2 = len(b)
        if n1 > n2:
            b = "0"*(n1-n2) + b
        elif n2 > n1:
            a = "0"*(n2-n1) + a
            n1 = n2

        c = ""
        i = n1 - 1
        ch = 0
        while i >= 0:
            s = ord(a[i]) + ord(b[i]) + ch - 96
            ch = s//2
            s = s % 2
            c += str(s)
            i -= 1
        if ch == 1:
            c = c + str(ch)
        return c[::-1]
