class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #so first we create min and max
        buy = prices[0]
        max_price = 0

        for price in prices:
            buy = min(buy, price)
            max_price = max(max_price, price-buy)
        return max_price
        
        