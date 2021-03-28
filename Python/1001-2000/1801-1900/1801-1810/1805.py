class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s = set()
        n = -1
        o = ord('0')
        for c in word:
            if c >= '0' and c <= '9':
                if n != -1:
                    n = n*10 + ord(c) - o
                else:
                    n = ord(c) - o
            else:
                s.add(n)
                n = -1
        if n != -1:
            s.add(n)
            n = -1
        s.discard(-1)
        return len(s)
