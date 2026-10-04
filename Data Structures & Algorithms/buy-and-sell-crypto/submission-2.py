class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        low_price = float('inf')
        for price in prices:
            low_price = min(low_price, price)
            profit = price - low_price
            max_profit = max(max_profit, profit)
        return max_profit
        