class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        l = [0] * 26
        for i in text:
            l[ord(i) - 97] += 1
        return min(l[0], l[1], l[11]//2, l[13], l[14]//2)
