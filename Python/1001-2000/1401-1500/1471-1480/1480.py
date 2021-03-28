class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        l = []
        for i in nums:
            l.append(sum + i)
            sum += i
        return l
