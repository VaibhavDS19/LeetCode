class Solution:
    def toGoatLatin(self, S: str) -> str:
        l = S.split(' ')
        n = len(l)
        for i in range(n):
            if l[i][0] not in "aeiouAEIOU":
                l[i] = l[i][1:] + l[i][0]
            l[i] = l[i] + "ma" + 'a'*(i+1)
        return " ".join(l)
