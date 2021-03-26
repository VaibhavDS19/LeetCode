class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = max(nums)
        if m <= 0:
            return m
        s = 0
        for i in nums:
            s += i
            if s < 0:
                s = 0
            if s > m:
                m = s
        return m
