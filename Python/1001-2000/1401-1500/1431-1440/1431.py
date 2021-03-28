class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ret = []
        m = max(candies)
        for i in candies:
            ret.append((i+extraCandies) >= m)
        return ret
