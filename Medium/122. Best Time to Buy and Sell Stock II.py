class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += (prices[i] - prices[i - 1])
            
        return profit
        
# Algorithm Technique
# Greedy → take profit whenever you see an increasing sequence.

# Time Complexity:  O(n) (one pass through prices)
# Space Complexity: O(1) (only profit variable)
