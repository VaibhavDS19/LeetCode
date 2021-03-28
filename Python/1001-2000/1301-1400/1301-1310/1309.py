class Solution:
    def freqAlphabets(self, s: str) -> str:
        n = len(s)
        l = [''] * n
        n -= 1
        lang = 'abcdefghijklmnopqrstuvwxyz'
        i = 0
        o = ord('0')
        while n >= 0:
            i = 0
            if s[n] == '#':
                i = ord(s[n-1]) - o + 10 * (ord(s[n-2]) - o)
                l[n] = lang[i-1]
                n -= 3
            else:
                i = ord(s[n]) - o
                l[n] = lang[i-1]
                n -= 1
        return ''.join(l)
