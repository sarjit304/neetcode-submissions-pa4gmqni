class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0
        while right < len(prices):
            buy_price = prices[left]
            sell_price = prices[right]

            profit = sell_price - buy_price
            max_profit = max(max_profit, profit)

            if sell_price > buy_price:
                pass
            else:
                left = right
            right += 1

        return max_profit