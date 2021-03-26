class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        b = 0
        e = len(nums) - 1
        if target < nums[0]:
            return 0
        if target > nums[len(nums)-1]:
            return len(nums)
        while b <= e:
            mid = (e+b)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                if nums[mid-1] < target:
                    return mid
                e = mid - 1
            else:
                if nums[mid+1] > target:
                    return mid + 1
                b = mid + 1
        return mid
