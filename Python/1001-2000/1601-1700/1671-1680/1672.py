class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        l = []
        for account in accounts:
            l.append(sum(account))
        return max(l)
