class Solution:
    def defangIPaddr(self, address: str) -> str:
        l = []
        for ch in address:
            if ch != '.':
                l.append(ch)
            else:
                l.append('[')
                l.append('.')
                l.append(']')
        return "".join(l)
