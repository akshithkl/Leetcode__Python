class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prices = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < min_prices:
                min_prices = prices[i]

            max_profit = max(max_profit,prices[i] - min_prices)

        return max_profit        
