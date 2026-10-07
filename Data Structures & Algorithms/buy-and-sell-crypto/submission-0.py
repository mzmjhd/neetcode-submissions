class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buyPrice = prices[0]
        for i in range (len(prices)):
            if i == 0:
                continue
            else:
                profit = max(profit, prices[i]-buyPrice)
                buyPrice = min(buyPrice, prices[i])
        return profit