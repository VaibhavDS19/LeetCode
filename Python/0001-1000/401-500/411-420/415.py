class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ret = ""
        c = 0
        i = len(num1) - 1
        j = len(num2) - 1
        while i >= 0 and j >= 0:
            s = c + ord(num1[i]) + ord(num2[j]) - 2*ord("0")
            c = s//10
            s = s % 10
            ret = str(s) + ret
            i -= 1
            j -= 1
        while i >= 0:
            s = c + ord(num1[i]) - ord("0")
            c = s//10
            s = s % 10
            ret = str(s) + ret
            i -= 1
        while j >= 0:
            s = c + ord(num2[j]) - ord("0")
            c = s//10
            s = s % 10
            ret = str(s) + ret
            j -= 1
        if c > 0:
            return str(c) + ret
        return ret
