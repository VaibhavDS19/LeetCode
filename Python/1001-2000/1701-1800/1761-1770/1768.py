class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = len(word1)
        j = len(word2)
        s = ""
        n1 = 0
        n2 = 0
        while n1 < i and n2 < j:
            s += word1[n1] + word2[n2]
            n1 += 1
            n2 += 1
        if n1 < i:
            s += word1[n1:]
        if n2 < j:
            s += word2[n2:]
        return s
