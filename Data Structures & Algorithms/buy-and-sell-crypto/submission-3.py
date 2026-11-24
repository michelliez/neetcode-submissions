class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_purchase = float('inf')
        best_profit = 0

        for price in prices:
            if price < lowest_purchase:
                lowest_purchase = price

            elif price - lowest_purchase > best_profit:
                best_profit = price - lowest_purchase

        return best_profit