class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        m = 0
        sum = 0
        for i in gain:
            sum += i
            m = max(m, sum)
        return m
