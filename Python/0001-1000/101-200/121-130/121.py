class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        high = prices[0]
        profit = 0

        for price in prices[1:]:
            if price < low:
                low = price
                high = price
            elif price > high:
                high = price
                profit = max(high - low, profit)

        return profit
