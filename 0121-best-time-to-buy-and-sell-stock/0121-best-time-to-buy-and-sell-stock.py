class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        smallest_num = 0

        for p in range(1, len(prices)):
            if prices[p] < prices[smallest_num]:
                smallest_num = p
            elif profit < prices[p] - prices[smallest_num]:
                profit = prices[p] - prices[smallest_num]
            
        return profit
        