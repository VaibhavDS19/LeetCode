class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = 0
        if nums:
            beg = 0
            end = len(nums) - 1
            while end >= 0 and nums[end] == val:
                c += 1
                end -= 1
            while beg <= end:
                if nums[beg] != val:
                    beg += 1
                else:
                    nums[beg], nums[end] = nums[end], nums[beg]
                    beg += 1
                    while end >= 0 and nums[end] == val:
                        c += 1
                        end -= 1
        return len(nums) - c
