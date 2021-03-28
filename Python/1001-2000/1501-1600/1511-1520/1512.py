class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = [0] * 100
        count = 0
        for i in nums:
            count += n[i-1]
            n[i-1] += 1
        return count
