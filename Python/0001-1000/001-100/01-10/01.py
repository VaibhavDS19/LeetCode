# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ret = []
        d = {}
        for i, j in enumerate(nums, 0):
            if j in d.keys():
                ret.append(i)
                ret.append(d[j])
                return ret
            else:
                d[target - j] = i
        return ret
