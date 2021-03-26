class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        i = 1
        now = 0
        for i in range(1, n):
            if nums[i] != nums[now]:
                now += 1
                nums[now] = nums[i]
        return now + 1
