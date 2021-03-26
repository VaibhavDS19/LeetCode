class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        i = 0
        n = len(prices)
        while i < n:
            while i<n-1 and prices[i]>prices[i+1]:
                i += 1
            cur = prices[i]
            while i<n-1 and prices[i]<prices[i+1]:
                i += 1
            if prices[i] > cur:
                prof += prices[i] - cur
            i += 1
        return prof