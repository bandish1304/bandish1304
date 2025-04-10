class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        lo = prices[0]
        high = prices[0]
        n = len(prices)
        profit = 0

        while i < n-1:
            # where to buy
            while i < n-1 and prices[i] >= prices[i+1]:
                i += 1
            lo = prices[i]

            # where to sell
            while i < n-1 and prices[i] <= prices[i+1]:
                i += 1
            high = prices[i]

            profit += high - lo

        return profit
        