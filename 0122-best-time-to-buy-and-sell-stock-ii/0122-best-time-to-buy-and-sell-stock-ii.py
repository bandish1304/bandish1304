class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        low = 0
        high = 0
        profit = 0
        n = len(prices)

        while i < n-1:
            # find the lowest point
            while i < n-1 and prices[i] >= prices [i + 1]:
                i += 1
            low = prices[i]
            # find the highest point
            while i < n-1 and prices[i] <= prices[i+1]:
                i += 1
            high = prices[i]

            profit = profit + high - low

        return profit

        