class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        smallest = 0

        for p in range(1, len(prices)):
            if prices[p] < prices[smallest]:
                smallest = p
            elif profit < prices[p] - prices[smallest]:
                profit = prices[p] - prices[smallest]
            
        return profit
