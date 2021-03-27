class Solution:
    def toLowerCase(self, s: str) -> str:
        ret = ""
        A = ord("A")
        Z = ord("Z")
        l = []
        for ch in s:
            x = ord(ch)
            if x >= A and x <= Z:
                l.append(chr(x + 32))
            else:
                l.append(chr(x))
        return ret.join(l)
